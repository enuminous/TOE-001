"""ME-007/T0E-001 candidate: covariant total stress, FLRW demonstration.

This is an explicitly CHOSEN decomposition of a conventional two-scalar action.
It does NOT identify the historical EFMW informational stress tensor uniquely.
Signature (-,+,+,+); units are dimensionless, c=hbar=1.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
from toe001.model import Params


@dataclass(frozen=True)
class Gravity:
    mpl2: float = 1.0
    cosmological_constant: float = 0.0
    kappa: float = 1.0
    allocation: float = 0.5
    w: float = 0.0

    def __post_init__(self):
        values = (self.mpl2, self.cosmological_constant, self.kappa,
                  self.allocation, self.w)
        if not all(math.isfinite(x) for x in values):
            raise ValueError('Nonfinite gravitational parameter')
        if self.mpl2 <= 0 or self.kappa == 0:
            raise ValueError('M_Pl^2 > 0 and nonzero kappa are required')
        if not 0 <= self.allocation <= 1:
            raise ValueError('Mixing-stress allocation must be in [0,1]')
        if self.w < -1 or self.w > 1:
            raise ValueError('Use -1 <= w <= 1 in this classical test')


def potential(phi: float, chi: float, p: Params):
    return 0.5 * p.m2 * phi**2 + 0.5 * p.M2 * chi**2 + p.g * phi * chi


def stress(phi, chi, u, v, rho_m, p: Params, gr: Gravity):
    """Energy density, isotropic pressure and sector partition in flat FLRW.

    'ordinary' means chosen SM-fluid + phi + allocation*interaction.
    'information' is explicitly defined by the complementary scalar stress.
    Only (ordinary + kappa*information) is the invariant total here.
    """
    if rho_m < 0:
        raise ValueError('Matter rho must be nonnegative')
    mix = p.g * phi * chi
    kinetic = 0.5 * (u*u + v*v)
    rho_scalar = kinetic + potential(phi, chi, p)
    press_scalar = kinetic - potential(phi, chi, p)
    rho_ord = rho_m + 0.5*u*u + 0.5*p.m2*phi*phi + gr.allocation*mix
    press_ord = gr.w*rho_m + 0.5*u*u - 0.5*p.m2*phi*phi - gr.allocation*mix
    rho_info_source = 0.5*v*v + 0.5*p.M2*chi*chi + (1-gr.allocation)*mix
    press_info_source = 0.5*v*v - 0.5*p.M2*chi*chi - (1-gr.allocation)*mix
    rho_total = rho_m + rho_scalar
    press_total = gr.w*rho_m + press_scalar
    return {
        'rho_scalar': rho_scalar, 'p_scalar': press_scalar,
        'rho_ordinary': rho_ord, 'p_ordinary': press_ord,
        'rho_information': rho_info_source/gr.kappa,
        'p_information': press_info_source/gr.kappa,
        'rho_total': rho_total, 'p_total': press_total,
        'rho_assembled': rho_ord + gr.kappa*(rho_info_source/gr.kappa),
        'p_assembled': press_ord + gr.kappa*(press_info_source/gr.kappa),
        'rho_plus_p_scalar': u*u+v*v,
    }


def energy_exchange(phi, chi, u, v, p: Params, gr: Gravity):
    """Q such that dot(rho) + 3H(rho+p) = Q.

    Ordinary=SM+phi+alpha*interaction; information complement.
    Their exchanges exactly cancel; neither need be conserved alone.
    """
    q_ord = -p.g*((1-gr.allocation)*chi*u - gr.allocation*phi*v)
    return q_ord, -q_ord/gr.kappa


def hubble_constraint(state, p: Params, gr: Gravity):
    # State: (phi,chi,u,v,a,H,rho_m)
    rho = stress(*state[:4], state[6], p, gr)['rho_total']
    return 3*gr.mpl2*(state[5]*state[5] - gr.cosmological_constant/3) - rho


def initial_state(p: Params, gr: Gravity, phi=0.7, chi=-0.3,
                  u=0.2, v=-0.1, rho_m=0.2, scale=1.0):
    if not p.stable():
        raise ValueError('Positive-definite mass matrix required for this test')
    if scale <= 0 or rho_m < 0:
        raise ValueError('Scale positive and matter density nonnegative')
    st = stress(phi, chi, u, v, rho_m, p, gr)
    h2 = st['rho_total']/(3*gr.mpl2) + gr.cosmological_constant/3
    if h2 < 0:
        raise ValueError('No real flat-FLRW Hubble rate for these inputs')
    return (float(phi),float(chi),float(u),float(v),float(scale),
            math.sqrt(h2),float(rho_m))


def derivative(y, p: Params, gr: Gravity):
    phi,chi,u,v,a,H,rho_m = y
    return (
        u, v,
        -3*H*u-p.m2*phi-p.g*chi,
        -3*H*v-p.M2*chi-p.g*phi,
        H*a,
        -(u*u+v*v + (1+gr.w)*rho_m)/(2*gr.mpl2),
        -3*H*(1+gr.w)*rho_m,
    )


def derivative_sectors(y, p: Params, gr: Gravity):
    """Independently differentiate sector density polynomials along EOM."""
    phi,chi,u,v,a,H,rho_m=y
    dphi,dchi,du,dv,da,dH,dm=derivative(y,p,gr)
    alpha=gr.allocation
    drho_ord=(dm+u*du+p.m2*phi*dphi +
              alpha*p.g*(dphi*chi+phi*dchi))
    drho_info=(v*dv+p.M2*chi*dchi+
               (1-alpha)*p.g*(dphi*chi+phi*dchi))/gr.kappa
    s=stress(phi,chi,u,v,rho_m,p,gr)
    balance_ord=drho_ord+3*H*(s['rho_ordinary']+s['p_ordinary'])
    balance_info=drho_info+3*H*(s['rho_information']+s['p_information'])
    return balance_ord,balance_info


def rk4(y, dt: float, p: Params, gr: Gravity):
    if dt <= 0 or not math.isfinite(dt):
        raise ValueError('dt must be positive and finite')
    def add(x,k,f): return tuple(a+f*dt*b for a,b in zip(x,k))
    k1=derivative(y,p,gr)
    k2=derivative(add(y,k1,0.5),p,gr)
    k3=derivative(add(y,k2,0.5),p,gr)
    k4=derivative(add(y,k3,1),p,gr)
    return tuple(z+dt*(a+2*b+2*c+d)/6
                 for z,a,b,c,d in zip(y,k1,k2,k3,k4))


def simulate_flrw(p=None, gr=None, steps=2400, dt=0.001,
                  phi=0.7,chi=-0.3,u=0.2,v=-0.1,rho_m=0.2):
    p=Params() if p is None else p
    gr=Gravity() if gr is None else gr
    if not 0 <= steps <= 100000 or dt <= 0 or not math.isfinite(dt):
        raise ValueError('Invalid time grid')
    y=initial_state(p,gr,phi,chi,u,v,rho_m)
    max_constraint=0.0
    max_exchange=0.0
    max_total_source_mismatch=0.0
    min_hdot=0.0
    sample=[]
    for n in range(steps+1):
        s=stress(*y[:4],y[6],p,gr)
        c=abs(hubble_constraint(y,p,gr))/max(1.0,s['rho_total'])
        max_constraint=max(max_constraint,c)
        q1,q2=energy_exchange(*y[:4],p,gr)
        e1,e2=derivative_sectors(y,p,gr)
        max_exchange=max(max_exchange,abs(q1-e1),abs(q2-e2))
        max_total_source_mismatch=max(max_total_source_mismatch,
                                      abs(s['rho_assembled']-s['rho_total']),
                                      abs(s['p_assembled']-s['p_total']))
        if n%max(1,steps//24)==0:
            sample.append({'t':n*dt,'phi':y[0],'chi':y[1],
                           'H':y[5],'a':y[4],'rho_total':s['rho_total'],
                           'friedmann_residual':c})
        if n < steps:
            y=rk4(y,dt,p,gr)
    final_stress=stress(*y[:4],y[6],p,gr)
    return {
        'status':'CONDITIONAL_CLASSICAL_FLRW_ONLY',
        'steps':steps,'dt':dt,'final_t':steps*dt,
        'final_state':list(y), 'final_stress':final_stress,
        'max_relative_friedmann_residual':max_constraint,
        'max_partition_exchange_error':max_exchange,
        'max_total_source_mismatch':max_total_source_mismatch,
        'no_flat_bounce_under_nec':True,
        'quantum_gravity_derived':False,
        'historical_efmw_information_tensor_identified':False,
        'full_theory_of_everything':False,
        'trace':sample,
    }
