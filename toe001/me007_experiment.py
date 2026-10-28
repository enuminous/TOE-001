"""F03: coupled-oscillator classical Langevin analog and MI analysis.
Independent calibration is essential; code cannot establish informational gravity.
This is standard BAOAB and standard Gaussian information, not novel EFMW dynamics.
"""
from __future__ import annotations
from dataclasses import dataclass
import csv
import hashlib
import math
import random
from pathlib import Path

@dataclass(frozen=True)
class Calibration:
    m2: float = 1.0
    M2: float = 4.0
    gamma: float = 0.25
    beta: float = 1.0
    damping: float = 0.8
    dt: float = 0.04
    noise_phi: float = 0.0
    noise_chi: float = 0.0

    def __post_init__(self):
        vals=tuple(vars(self).values())
        if not all(math.isfinite(v) for v in vals):
            raise ValueError('Calibration must be finite')
        if min(self.m2,self.M2,self.beta,self.damping,self.dt)<=0 or self.dt>.2:
            raise ValueError('Mass stiffness, beta, damping, 0<dt<=.2 required')
        if self.gamma*self.gamma >= self.m2*self.M2:
            raise ValueError('Unstable quadratic potential')
        if self.noise_phi<0 or self.noise_chi<0:
            raise ValueError('Sensor noise sigma cannot be negative')

def expected_mi(cal:Calibration)->float:
    """Population MI of equilibrium position amplitudes in nats."""
    return -.5*math.log1p(-cal.gamma*cal.gamma/(cal.m2*cal.M2))

def expected_covariance(cal:Calibration)->tuple[float,float,float]:
    det=cal.m2*cal.M2-cal.gamma*cal.gamma
    return cal.M2/(cal.beta*det), -cal.gamma/(cal.beta*det), cal.m2/(cal.beta*det)

def coupled_langevin(cal:Calibration, *, steps:int=100000,
                     burn:int=10000, stride:int=8, seed:int=20261028):
    """Time-correlated SYNTHETIC sensor data from full Langevin ODE.
    qdot=p; pdot=-Kq-damping*p+sqrt(2*damping/beta)*white_noise.
    Standard BAOAB splitting, exactly integrated OU momentum kick.
    This is not independent instrument data or a new physical law.
    """
    if steps<10 or steps>5_000_000 or not 0<=burn<steps or not 1<=stride<=steps:
        raise ValueError('Invalid finite trajectory grid')
    r=random.Random(seed)
    a=math.exp(-cal.damping*cal.dt)
    sigma=math.sqrt((1-a*a)/cal.beta)
    phi=chi=u=v=0.0
    dt=cal.dt
    for i in range(steps):
        u-=.5*dt*(cal.m2*phi+cal.gamma*chi)
        v-=.5*dt*(cal.gamma*phi+cal.M2*chi)
        phi+=.5*dt*u;chi+=.5*dt*v
        u=a*u+sigma*r.gauss(0,1)
        v=a*v+sigma*r.gauss(0,1)
        phi+=.5*dt*u;chi+=.5*dt*v
        u-=.5*dt*(cal.m2*phi+cal.gamma*chi)
        v-=.5*dt*(cal.gamma*phi+cal.M2*chi)
        if i>=burn and (i-burn)%stride==0:
            measured_phi=phi+cal.noise_phi*r.gauss(0,1) if cal.noise_phi else phi
            measured_chi=chi+cal.noise_chi*r.gauss(0,1) if cal.noise_chi else chi
            yield ((i+1)*dt,measured_phi,measured_chi)

def csv_read(path:str|Path):
    """Requires time,phi,chi columns and monotonic timestamps."""
    with open(path,encoding='utf-8',newline='') as f:
        rd=csv.DictReader(f)
        if rd.fieldnames is None or not {'time','phi','chi'}.issubset(set(rd.fieldnames)):
            raise ValueError('CSV requires time,phi,chi headers')
        out=[];last=-float('inf')
        for j,row in enumerate(rd):
            if j>=2_000_000:raise ValueError('Too many observations')
            try:
                t,p,c=(float(row[x]) for x in ('time','phi','chi'))
            except (ValueError,TypeError,KeyError) as ex:raise ValueError(f'Bad row {j+2}') from ex
            if not all(math.isfinite(x) for x in (t,p,c)) or t<=last:
                raise ValueError('Nonfinite measurement or nonincreasing time')
            out.append((t,p,c));last=t
    if len(out)<100:raise ValueError('At least 100 paired samples required')
    return out

def csv_write(path:str|Path,records):
    with open(path,'w',encoding='utf-8',newline='') as f:
        wr=csv.writer(f);wr.writerow(('time','phi','chi'))
        for row in records:wr.writerow(tuple(format(v,'.16g') for v in row))

def file_sha256(path:str|Path)->str:
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(65536),b''):h.update(b)
    return h.hexdigest()

def _cov(x,y):
    if len(x)!=len(y) or len(x)<3:raise ValueError('Need paired observations')
    n=len(x);mx=sum(x)/n;my=sum(y)/n
    a=sum((v-mx)**2 for v in x)/(n-1)
    b=sum((v-mx)*(w-my) for v,w in zip(x,y))/(n-1)
    c=sum((v-my)**2 for v in y)/(n-1)
    return (a,b,c)

def _mi(cov,cal):
    a,b,c=cov
    a-=cal.noise_phi**2;c-=cal.noise_chi**2
    if a<=0 or c<=0 or b*b>=a*c:
        raise ValueError('Debiased covariance not positive definite; measurement invalid')
    return -.5*math.log1p(-b*b/(a*c)),b/math.sqrt(a*c),(a,b,c)

def summarize(records,cal:Calibration,*,bootstrap:int=150,seed:int=991)->dict:
    """Moving-block uncertainty and time-shift null; exploratory statistics only."""
    if not 1<=bootstrap<=2000:raise ValueError('bootstrap outside bounds')
    records=list(records)
    if len(records)<200:raise ValueError('Need >=200 paired samples')
    times,x,y=zip(*records)
    if not all(math.isfinite(t) for t in times) or any(b<=a for a,b in zip(times,times[1:])):
        raise ValueError('Times must increase')
    if not all(math.isfinite(z) for z in x+y):raise ValueError('Nonfinite observations')
    n=len(x)
    observed,rho,cov=_mi(_cov(x,y),cal)
    length=max(20,int(math.sqrt(n)))
    rng=random.Random(seed)
    replicates=[]
    for _ in range(bootstrap):
        indices=[]
        while len(indices)<n:
            begin=rng.randrange(n-length+1)
            indices.extend(range(begin,begin+length))
        inds=indices[:n]
        replicate,_,_=_mi(_cov([x[i] for i in inds],[y[i] for i in inds]),cal)
        replicates.append(replicate)
    replicates.sort()
    low=replicates[max(0,int(.025*bootstrap))]
    high=replicates[min(bootstrap-1,int(.975*bootstrap))]
    null=[]
    if n>20*length:
        for _ in range(min(80,bootstrap)):
            shift=rng.randrange(10*length,n-10*length)
            v,_,_=_mi(_cov(x,y[shift:]+y[:shift]),cal)
            null.append(v)
    first,_,_=_mi(_cov(x[:n//2],y[:n//2]),cal)
    second,_,_=_mi(_cov(x[n//2:],y[n//2:]),cal)
    expected=expected_mi(cal)
    return {
        'n_paired':n,'observed_MI_nats':observed,
        'estimated_correlation':rho,
        'theory_MI_nats_from_independently_specified_stiffness':expected,
        'MI_minus_theory_nats':observed-expected,
        'paired_block_bootstrap_95pct':[low,high],
        'bootstrap_block_length_samples':length,
        'half_sample_MI_nats':[first,second],
        'stationarity_screen':'REQUIRES_INDEPENDENT_VALIDATION',
        'sensor_noise_correction':'independent uncorrelated Gaussian variance only',
        'observed_debiased_covariance':list(cov),
        'ideal_Gibbs_covariance':list(expected_covariance(cal)),
        'shift_null_MI_median_nats':sorted(null)[len(null)//2] if null else None,
        'shift_null_max_nats':max(null) if null else None,
        'pass_physics':'UNRESOLVED',
        'distinguishes_EFMW_from_ordinary_oscillators':False,
        'q_field_identified_by_measurement':False,
        'gravitational_coupling_measured':False,
        'note':'Blocked uncertainty is exploratory; mixing, stationarity, sensor transfer and instrument calibration still require validation.'
    }
