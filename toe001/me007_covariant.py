"""F02 conditional scalar--tensor extension of TOE-001 (NOT physical EFMW identification).

The field q is NEW and is not proven equal to local Gaussian mutual information.
This is ordinary Jordan-frame scalar--tensor EFT; units c=hbar=1, signature -+++.
All values in the FLRW demonstration are dimensionless illustrative values.
"""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class Model:
    m2: float = 1.0
    M2: float = 4.0
    gamma: float = 0.25
    mpl2: float = 1.0
    z: float = 1.2
    xi: float = 0.15
    mu2: float = 0.3
    w: float = 0.0

    def __post_init__(self):
        v=(self.m2,self.M2,self.gamma,self.mpl2,self.z,self.xi,self.mu2,self.w)
        if not all(math.isfinite(x) for x in v):
            raise ValueError('All parameters must be finite')
        if min(self.m2,self.M2,self.mpl2,self.z,self.mu2) <= 0:
            raise ValueError('Positive masses, Planck scale and scalar kinetic required')
        if self.gamma*self.gamma >= self.m2*self.M2:
            raise ValueError('Positive two-field stiffness determinant required')
        if not -1 <= self.w <= 1:
            raise ValueError('Fluid w outside specified range')

    def F(self, q: float) -> float:
        return self.mpl2*(1-self.xi*q*q)
    def Fq(self, q: float) -> float:
        return -2*self.mpl2*self.xi*q
    def Fqq(self) -> float:
        return -2*self.mpl2*self.xi
    def K(self) -> float:
        return self.mpl2*self.z
    def U(self,q:float) -> float:
        return 0.5*self.mpl2*self.mu2*q*q
    def Uq(self,q:float) -> float:
        return self.mpl2*self.mu2*q
    def MI(self) -> float:
        """A global equilibrium two-mode statistic, NOT the local q field."""
        return -0.5*math.log1p(-self.gamma*self.gamma/(self.m2*self.M2))


def densities(y:tuple[float,...], p: Model) -> dict:
    """State (phi,chi,phidot,chidot,q,qdot,a,H,rho_m)."""
    phi,chi,u,v,q,qdot,a,H,rho=y
    scalar_kin=0.5*(u*u+v*v)
    V=0.5*(p.m2*phi*phi + p.M2*chi*chi)+p.gamma*phi*chi
    base_rho=rho +scalar_kin+V
    base_p=p.w*rho+scalar_kin-V
    return {'rho_base':base_rho,'p_base':base_p, 'rho_q':0.5*p.K()*qdot*qdot+p.U(q),
            'p_q':0.5*p.K()*qdot*qdot-p.U(q)}


def constraint(y: tuple[float,...],p:Model) -> float:
    s=densities(y,p);q,qdot,H=y[4],y[5],y[7]
    return 3*p.F(q)*H*H +3*H*p.Fq(q)*qdot-s['rho_base']-s['rho_q']


def initial_state(p:Model,phi=.7,chi=-.3,u=.2,v=-.1,
                  q=.35,qdot=.02,a=1.0,rho_m=.2):
    if not all(math.isfinite(x) for x in (phi,chi,u,v,q,qdot,a,rho_m)):
        raise ValueError('Nonfinite initial conditions')
    if a<=0 or rho_m <0 or p.F(q)<=0:
        raise ValueError('Nonpositive scale/density/Planck factor')
    intermediate=(phi,chi,u,v,q,qdot,a,0.,rho_m)
    s=densities(intermediate,p)
    c=3*p.F(q); b=3*p.Fq(q)*qdot
    positive=s['rho_base']+s['rho_q']
    disc=b*b+4*c*positive
    if disc < 0:raise ValueError('No real Hubble root for this initial state')
    H=(-b+math.sqrt(disc))/(2*c)
    return (phi,chi,u,v,q,qdot,a,H,rho_m)


def derivative(y:tuple[float,...],p:Model) -> tuple[float,...]:
    phi,chi,u,v,q,qd,a,H,rho=y
    F=p.F(q);Fq=p.Fq(q);Fqq=p.Fqq();K=p.K()
    if F<=0 or a<=0 or rho<0:
        raise ValueError('Outside positive-EFT test region')
    s=densities(y,p)
    base_enthalpy=s['rho_base']+s['p_base']
    # K*qdd - 3*Fq*Hdot = -3*H*K*qd - Uq + 6*Fq*H^2.
    src=-3*H*K*qd-p.Uq(q)+6*Fq*H*H
    # -2*F*Hdot - Fq*qdd = base_enthalpy+(K+Fqq)*qd^2-H*Fq*qd.
    total=base_enthalpy+(K+Fqq)*qd*qd-H*Fq*qd+(Fq/K)*src
    Hdot=-total/(2*F+3*Fq*Fq/K)
    qdd=(src+3*Fq*Hdot)/K
    return (u,v,-3*H*u-p.m2*phi-p.gamma*chi,
            -3*H*v-p.M2*chi-p.gamma*phi,
            qd,qdd,a*H,Hdot,-3*H*(1+p.w)*rho)


def rk4(y:tuple[float,...],dt:float,p:Model):
    if dt<=0 or not math.isfinite(dt):raise ValueError('Positive finite timestep required')
    def advance(yy,k,weight):return tuple(x+dt*weight*dx for x,dx in zip(yy,k))
    k1=derivative(y,p)
    k2=derivative(advance(y,k1,.5),p)
    k3=derivative(advance(y,k2,.5),p)
    k4=derivative(advance(y,k3,1.),p)
    return tuple(x+dt*(d1+2*d2+2*d3+d4)/6 for x,d1,d2,d3,d4 in zip(y,k1,k2,k3,k4))


def identity_residuals(y:tuple[float,...],p:Model) -> dict:
    """Test Friedmann and scalar curvature dynamics independently of algebraic eliminations."""
    d=derivative(y,p);q,qd,H=y[4],y[5],y[7]
    F=p.F(q);Fp=p.Fq(q);Fpp=p.Fqq();K=p.K()
    Hdot=d[7];qdd=d[5];R=6*(2*H*H+Hdot)
    s=densities(y,p)
    return {
       'scalar_eom':K*(qdd+3*H*qd)+p.Uq(q)-0.5*Fp*R,
       'raychaudhuri':-2*F*Hdot-(s['rho_base']+s['p_base']+K*qd*qd+Fpp*qd*qd+Fp*qdd-H*Fp*qd),
       'friedmann':constraint(y,p),
       'effective_planck_factor':F,
       'ricci_scalar':R,
    }


def dL_gw_over_em(F_at_emission:float, F_at_observer:float)->float:
    """Geometric-optics tensor propagation in standard F(q)R, NO screening/extra portals."""
    if min(F_at_emission,F_at_observer)<=0 or not all(map(math.isfinite,(F_at_emission,F_at_observer))):
        raise ValueError('Planck factors must be finite and positive')
    return math.sqrt(F_at_observer/F_at_emission)


def frozen_thermal_identification_residual(p: Model, R:float) -> float:
    """q=constant MI is a solution of the q EOM iff this equals zero.

    This is an obstruction, not an inferred cosmological information value.
    """
    q=p.MI()
    return p.Uq(q)-.5*p.Fq(q)*R


def simulate(p:Model|None=None, steps:int=2000, dt:float=.001)->dict:
    p=Model() if p is None else p
    if not 0<=steps<=100000 or dt<=0:raise ValueError('Invalid grid')
    y=initial_state(p);init=list(y);max_c=0.;max_q=0.;max_r=0.;minimal_F=float('inf')
    path=[]
    for i in range(steps+1):
        res=identity_residuals(y,p)
        max_c=max(max_c,abs(res['friedmann'])/max(1,abs(densities(y,p)['rho_base'])))
        max_q=max(max_q,abs(res['scalar_eom']))
        max_r=max(max_r,abs(res['raychaudhuri']))
        minimal_F=min(minimal_F,res['effective_planck_factor'])
        if i % max(1,steps//10)==0:
            path.append({'time':i*dt,'q':y[4],'H':y[7],'F':res['effective_planck_factor']})
        if i<steps:y=rk4(y,dt,p)
    return {'kind':'F02_hypothetical_scalar_tensor_not_me006_identification',
            'model':'F(q)R standard scalar tensor; q is an independent hypothetical field',
            'parameters':vars(p),'steps':steps,'dt':dt,
            'initial_state':init,'final_state':list(y),
            'max_normalized_friedmann_residual':max_c,
            'max_q_eom_residual':max_q,
            'max_raychaudhuri_residual':max_r,
            'min_F':minimal_F,
            'toy_tensor_distance_ratio_observed_final_emitted_initial':dL_gw_over_em(p.F(init[4]),p.F(y[4])),
            'equilibrium_MI_nats':p.MI(),
            'constant_q_eq_MI_residual_at_initial_R':frozen_thermal_identification_residual(p,identity_residuals(init,p)['ricci_scalar']),
            'physical_information_field_identified':False,
            'new_EFMW_effect_established':False,
            'full_theory_of_everything':False,
            'trace':path}
