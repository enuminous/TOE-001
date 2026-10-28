"""F01 / ME-006/007: operational correlation invariant and stress nonidentifiability.

A classical Gibbs ensemble of two coupled oscillators is an explicitly chosen
additional statistical model, not empirical evidence for a gravitational
information tensor. The canonical ME-006 recursive tensor R_{mu nu} remains
undefined at the constitutive/dynamical level.

Only the Python standard library is used. Units dimensionless, k_B T=1/beta.
"""
from __future__ import annotations
import math
import random
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Pair:
    m2: float = 1.0
    M2: float = 4.0
    gamma: float = 0.25
    beta: float = 1.0

    def __post_init__(self) -> None:
        if not all(map(math.isfinite, (self.m2, self.M2, self.gamma, self.beta))):
            raise ValueError('Finite pair parameters required')
        if self.m2 <= 0 or self.M2 <= 0 or self.beta <= 0:
            raise ValueError('Strictly positive masses and inverse temperature required')
        if self.det <= 0:
            raise ValueError('Unstable or singular oscillator stiffness matrix')

    @property
    def det(self) -> float:
        return self.m2*self.M2-self.gamma*self.gamma


def covariance(p: Pair) -> tuple[float, float, float]:
    """(var(phi),cov(phi,chi),var(chi)) = (beta*K)^(-1)."""
    return (p.M2/(p.beta*p.det), -p.gamma/(p.beta*p.det),
            p.m2/(p.beta*p.det))


def correlation(p: Pair) -> float:
    return -p.gamma/math.sqrt(p.m2*p.M2)


def mutual_information_nats(p: Pair) -> float:
    """Gaussian pair mutual information from an ASSUMED equilibrium ensemble."""
    return -0.5*math.log1p(-p.gamma*p.gamma/(p.m2*p.M2))


def information_susceptibility(p: Pair) -> float:
    """d mutual information / d mixing at fixed mass parameters.

    This equals -beta * equilibrium covariance(phi,chi), a standard
    Gibbs-ensemble identity. It is NOT a gravitational susceptibility.
    """
    return p.gamma/p.det


def mi_from_covariance(c11: float, c12: float, c22: float) -> float:
    vals=(c11,c12,c22)
    if not all(map(math.isfinite,vals)) or c11 <= 0 or c22 <= 0:
        raise ValueError('Positive finite variances required')
    rho2=(c12*c12)/(c11*c22)
    if rho2 >= 1:
        raise ValueError('Covariance must be strictly positive-definite')
    return -0.5*math.log1p(-rho2)


def gibbs_samples(p: Pair, n: int = 30000, seed: int = 20261028):
    """Independent classical Gibbs draws, NOT dynamical data from nature.

    Cholesky of exact equilibrium position covariance. A real laboratory
    requires both mode readouts, calibrated stationarity, and noise controls.
    """
    if not isinstance(n, int) or n < 2 or n > 2000000:
        raise ValueError('Sample count outside declared range')
    a,b,c = covariance(p)
    l11=math.sqrt(a)
    l21=b/l11
    l22=math.sqrt(c-l21*l21)
    rng=random.Random(seed)
    for _ in range(n):
        z1,z2 = rng.gauss(0,1),rng.gauss(0,1)
        yield l11*z1,l21*z1+l22*z2


def empirical_covariance(samples: Iterable[tuple[float,float]]):
    """Streaming sample covariance without keeping all the samples in memory."""
    n=0; mx=my=ssx=ssy=sxy=0.0
    for x,y in samples:
        n+=1
        dx=x-mx
        mx += dx/n
        dy=y-my
        my += dy/n
        ssx += dx*(x-mx)
        ssy += dy*(y-my)
        sxy += dx*(y-my)
    if n<3: raise ValueError('At least 3 samples required')
    return (ssx/(n-1),sxy/(n-1),ssy/(n-1))


def energy_sources(phi: float, chi: float, u: float, v: float,
                   rho_m: float, w: float, p: Pair,
                   alpha: float, kappa: float) -> dict:
    """Selected TOE001 ME007 source partition; alpha/kappa are NOT new physics."""
    if not math.isfinite(alpha) or not 0<=alpha<=1:
        raise ValueError('alpha in [0,1] required')
    if not math.isfinite(kappa) or kappa == 0:
        raise ValueError('nonzero kappa required')
    if rho_m<0 or not -1<=w<=1:
        raise ValueError('invalid matter density or equation of state')
    mix=p.gamma*phi*chi
    rho_phi=.5*(u*u+p.m2*phi*phi)
    rho_chi=.5*(v*v+p.M2*chi*chi)
    press_phi=.5*(u*u-p.m2*phi*phi)
    press_chi=.5*(v*v-p.M2*chi*chi)
    rho_t=rho_m+rho_phi+rho_chi+mix
    press_t=w*rho_m+press_phi+press_chi-mix
    rho_o=rho_m+rho_phi+alpha*mix
    press_o=w*rho_m+press_phi-alpha*mix
    rho_i=(rho_chi+(1-alpha)*mix)/kappa
    press_i=(press_chi-(1-alpha)*mix)/kappa
    return {'rho_total':rho_t, 'p_total':press_t,
            'rho_ordinary':rho_o,'p_ordinary':press_o,
            'rho_information':rho_i,'p_information':press_i,
            'rho_reconstructed':rho_o+kappa*rho_i,
            'p_reconstructed':press_o+kappa*press_i,
            'rho_scalar':rho_phi+rho_chi+mix,
            'rho_phi':rho_phi,
            'rho_chi_plus_mix':rho_chi+mix,
            'rho_R_for_SM_as_ordinary_kappa1':rho_chi+mix}


def operational_summary(p: Pair,n: int=50000,seed: int=20261028) -> dict:
    cov=covariance(p)
    sample_cov=empirical_covariance(gibbs_samples(p,n,seed))
    return {
        'model':'conditional classical thermal Gibbs two-mode oscillator',
        'units':'mutual information in nats (natural logarithm)',
        'parameters':{'m2':p.m2,'M2':p.M2,'gamma':p.gamma,'beta':p.beta},
        'n_samples':n,'seed':seed,
        'exact_covariance':[float(x) for x in cov],
        'exact_correlation':correlation(p),
        'exact_MI_nats':mutual_information_nats(p),
        'sample_covariance':[float(x) for x in sample_cov],
        'sample_MI_nats':mi_from_covariance(*sample_cov),
        'alpha_kappa_invariant':True,
        'is_ordinary_gaussian_mutual_information':True,
        'is_efmw_specific':False,
        'me006_recursive_tensor_physically_identified':False,
        'gravity_from_information_derived':False,
        'experiment_on_real_physical_data':False
    }
