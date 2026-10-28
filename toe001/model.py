"""TOE-001: a conditional two-scalar GR+SM effective-sector test bed.

Only the flat homogeneous scalar system is simulated here. The covariant
formulation and its geometric conservation identity are derived in PAPER.md.
Units are dimensionless, c=hbar=1; no physical parameter fit is claimed.
"""
from dataclasses import dataclass
import cmath
import math


@dataclass(frozen=True)
class Params:
    m2: float = 1.0
    M2: float = 4.0
    g: float = 0.25

    def __post_init__(self):
        if not all(math.isfinite(v) for v in (self.m2, self.M2, self.g)):
            raise ValueError("Parameters must be finite")
        if self.m2 <= 0 or self.M2 <= 0:
            raise ValueError("Both squared masses must be strictly positive")

    def stable(self) -> bool:
        return self.g * self.g < self.m2 * self.M2

    def eigenvalues(self):
        delta = math.hypot(self.m2 - self.M2, 2 * self.g)
        return ((self.m2 + self.M2 - delta) / 2,
                (self.m2 + self.M2 + delta) / 2)

    def eigenvectors(self):
        # Columns of orthonormal rotation diagonalize [[m2,g],[g,M2]].
        theta = math.atan2(2 * self.g, self.M2 - self.m2) / 2
        co, si = math.cos(theta), math.sin(theta)
        return ((co, -si), (si, co))


def force(q, p: Params):
    phi, chi = q
    return (-p.m2 * phi - p.g * chi, -p.g * phi - p.M2 * chi)


def energy(q, v, p: Params):
    phi, chi = q
    phidot, chidot = v
    return 0.5 * (phidot**2 + chidot**2 + p.m2 * phi**2 +
                  p.M2 * chi**2 + 2 * p.g * phi * chi)


def verlet_step(q, v, dt: float, p: Params):
    if not math.isfinite(dt) or dt <= 0:
        raise ValueError("time step must be positive and finite")
    a = force(q, p)
    nq = tuple(qi + vi * dt + 0.5 * ai * dt**2
               for qi, vi, ai in zip(q, v, a))
    na = force(nq, p)
    nv = tuple(vi + 0.5 * (ai + nai) * dt
               for vi, ai, nai in zip(v, a, na))
    return nq, nv


def exact_solution(t: float, q0, v0, p: Params):
    if not p.stable():
        raise ValueError("oscillatory exact solution requires positive definite mass matrix")
    vals = p.eigenvalues()
    vecs = p.eigenvectors()
    q, v = [0.0, 0.0], [0.0, 0.0]
    for mass2, eig in zip(vals, vecs):
        w = math.sqrt(mass2)
        amp = sum(e * a for e, a in zip(eig, q0))
        vel = sum(e * a for e, a in zip(eig, v0))
        x = amp * math.cos(w * t) + vel * math.sin(w * t) / w
        xd = -amp * w * math.sin(w * t) + vel * math.cos(w * t)
        for k in range(2):
            q[k] += eig[k] * x
            v[k] += eig[k] * xd
    return tuple(q), tuple(v)


def susceptibility(omega: float, p: Params, k: float = 0., eta: float = 0.005):
    """Linear phi response to an EXTERNAL test source J phi at frozen k.

    The test source is not a measured SM coupling. Nonzero eta is a
    numerical retarded prescription, not dissipation derived from EFMW.
    """
    if eta <= 0 or not all(math.isfinite(x) for x in (omega,k,eta)):
        raise ValueError("finite omega, k, and positive eta required")
    z = (omega + 1j*eta)**2
    a = p.m2 + k*k - z
    b = p.M2 + k*k - z
    return b / (a*b - p.g*p.g)


def response_residues(p: Params):
    """Weights of phi in normal modes. They are nonnegative and sum to 1."""
    return tuple(vec[0]**2 for vec in p.eigenvectors())


def simulate(p: Params, steps: int = 20000, dt: float = .001,
             q0=(1.0,0.0), v0=(0.0,0.0)):
    if not p.stable():
        raise ValueError("stable simulation requires g^2 < m2*M2")
    if steps < 0 or steps > 5_000_000:
        raise ValueError("steps outside declared range")
    q, v = tuple(q0), tuple(v0)
    e0 = energy(q, v, p)
    max_rel_energy = 0.0
    for _ in range(steps):
        q,v = verlet_step(q,v,dt,p)
        max_rel_energy = max(max_rel_energy, abs(energy(q,v,p)-e0)/max(1.,abs(e0)))
    target, target_v = exact_solution(steps*dt,q0,v0,p)
    max_position_error = max(abs(a-b) for a,b in zip(q,target))
    max_velocity_error = max(abs(a-b) for a,b in zip(v,target_v))
    return {"steps":steps,"dt":dt,"final_time":steps*dt,
            "initial_energy":e0,"final_energy":energy(q,v,p),
            "max_relative_energy_drift":max_rel_energy,
            "max_position_error_vs_exact":max_position_error,
            "max_velocity_error_vs_exact":max_velocity_error,
            "final_q":list(q),"exact_q":list(target)}
