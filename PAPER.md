# TOE-001 — A Covariant EFMW-Inspired Memory-Sector Candidate: Action, Conservation, Stability, and Correspondence

**Research program:** Monolithic LLC / Matthew Chenoweth Wright  
**Working model and software:** AI-assisted mathematical construction, 28 October 2026  
**Status:** **A conditional classical effective-field-theory test bed; not a Theory of Everything and not a derivation of EFMW's historical 102 equations.**  
**Primary technical predecessor:** [QST-002](https://github.com/enuminous/QST/blob/main/QST-002.md), especially the explicitly assumed covariant two-scalar memory sector.  
**Research constraints:** [EFMW frozen obligations](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md) and [EFMW Lagrangian audit](https://github.com/enuminous/EFMW-Lagrangian).

## 0. Claim boundary and scope

TOE-001 is the smallest internally consistent *candidate* joining an assumed Einstein–Hilbert gravitational action, an assumed experimentally successful Standard Model matter action, and an explicitly defined EFMW-inspired recursive/memory *toy sector*. It is **not** a quantum-gravitational theory, it does **not** derive the Standard Model, and it does **not** establish a uniquely EFMW physical effect. Its purpose is to make the central logical and mathematical obligations executable.

It is important not to overclaim that two coupled scalars are new: they are a conventional covariant field-theory construction. A retarded kernel obtained by eliminating a field is textbook effective dynamics and does not by itself prove a physical EFMW memory ontology. Results that close *internal* checks do not close the larger theory.

### Frozen convention and assumptions

- Four-dimensional, oriented Lorentzian spacetime, signature $(-,+,+,+)$; use $\hbar=c=1$.
- General covariance; smooth real scalar fields $\phi,\chi$ with positive conventional kinetic terms.
- Minimal coupling to gravity, no *direct* SM portal and no additional physical pressure postulate.
- $M_{\mathrm{Pl}}^2=(8\pi G)^{-1}$; usual metric boundary term when boundaries are present.
- $m^2>0$, $M^2>0$, real mixing $g$ with mass dimension two; labels $m$ and $M$ are **not** inferred particle masses.
- The observed gravitational and SM interactions are **inputs**; not derived from a finite Base888 register or the EFMW equations.

## 1. One candidate action

With $V(\phi,\chi)=\tfrac12m^2\phi^2+\tfrac12M^2\chi^2+g\phi\chi$, define

$$
\boxed{\begin{aligned}
S_\mathrm{TOE001}[g,\Psi_{\rm SM},\phi,\chi]
={}&\int_{\mathcal M} d^4x\,\sqrt{-g}\left[
\frac{M_{\rm Pl}^2}{2}R+\mathcal L_{\rm SM}(g,\Psi_{\rm SM})\\
&-\frac12 g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi
-\frac12 g^{\mu\nu}\partial_\mu\chi\partial_\nu\chi
-V(\phi,\chi)\right]+S_{\rm GHY}.
\end{aligned}}
$$

$g$ denotes both the metric (with indices) and the *separate scalar coupling constant* (without indices); for clarity implementation uses `g` for mixing and the metric appears only in the paper. Both must not be conflated. The gravitational surface term $S_{\rm GHY}$ is included for a well-posed Dirichlet metric variation on appropriate boundaries.

**Physical interpretation:** a mathematical extension of GR+SM with two additional canonical scalars. The name "TOE-001" is a *research-test identifier*, not a completed theory.

## 2. Euler–Lagrange equations

Varying the scalar fields, with compactly supported variations or compatible boundary data,

$$\delta_\phi S=\int\sqrt{-g}\,[\Box_g\phi-\partial_\phi V]\,\delta\phi,$$
$$\delta_\chi S=\int\sqrt{-g}\,[\Box_g\chi-\partial_\chi V]\,\delta\chi.$$

Hence, with $\Box_g=\nabla_\mu\nabla^\mu$,

$$\boxed{(\Box_g-m^2)\phi=g\chi,\qquad(\Box_g-M^2)\chi=g\phi.} \tag{1}$$

In Minkowski spacetime with signature $(-+++)$, these become

$$\ddot\phi-\nabla^2\phi+m^2\phi+g\chi=0,$$
$$\ddot\chi-\nabla^2\chi+M^2\chi+g\phi=0.\tag{2}$$

Varying the metric gives, under the usual variational assumptions,

$$\boxed{M_{\rm Pl}^2G_{\mu\nu}=T^{\rm SM}_{\mu\nu}+T^{\rm scal}_{\mu\nu},} \tag{3}$$

where

$$T^{\rm scal}_{\mu\nu}=\partial_\mu\phi\partial_\nu\phi+\partial_\mu\chi\partial_\nu\chi
-g_{\mu\nu}\left[\tfrac12(\nabla\phi)^2+\tfrac12(\nabla\chi)^2+V\right]. \tag{4}$$

The stress tensor includes the mixing potential; splitting its terms into separately conserved parts would generally be incorrect.

## 3. Conservation law and the precise boundary

By covariant differentiation of (4) and the commuting covariant second derivatives of scalars,

$$\boxed{\nabla^\mu T^{\rm scal}_{\mu\nu}
=(\Box_g\phi-\partial_\phi V)\nabla_\nu\phi
+(\Box_g\chi-\partial_\chi V)\nabla_\nu\chi.} \tag{5}$$

Equation (1) makes (5) zero *on shell*. Diffeomorphism invariance also supplies the corresponding SM stress identity under its field equations. Thus $\nabla^\mu T^{\rm total}_{\mu\nu}=0$, consistent with $\nabla^\mu G_{\mu\nu}=0$.

**Critical distinction:** This closes a conservation calculation **for the new two-scalar action only**. It does **not** discharge [ME-007-BIANCHI](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md) for the original EFMW informational tensor, which has not been uniquely defined or identified with (4). A full formal differential-geometric proof of all assumptions has not been checked by Lean here; (5) is a standard analytic identity, and the numerical package verifies its homogeneous energy consequence.

## 4. Classical stability and causality

The quadratic potential has Hessian

$$K=\begin{pmatrix}m^2&g\\g&M^2\end{pmatrix},\qquad
\lambda_\pm=\frac{m^2+M^2\pm\sqrt{(m^2-M^2)^2+4g^2}}2.$$

The strictly positive definite parameter domain is

$$\boxed{m^2>0,\quad M^2>0,\quad g^2<m^2M^2.} \tag{6}$$

This means no tachyonic homogeneous mass mode in the *linear quadratic sector*; it does not prove a generally well-posed nonlinear quantum-gravity theory. At equality a massless mode appears, and above it the quadratic potential has an unstable direction.

The equations retain the ordinary metric principal symbol $g^{\mu\nu}k_\mu k_\nu$ and local hyperbolic dynamics in a well-posed globally hyperbolic setting. This supports local light-cone propagation at the equation level under those assumptions; it is not a demonstration of a new faster-than-light mechanism.

In flat homogeneous spacetime the positive energy is

$$E=\tfrac12(\dot\phi^2+\dot\chi^2)+\tfrac12m^2\phi^2+\tfrac12M^2\chi^2+g\phi\chi,$$

with $dE/dt=0$ on solutions. The package checks this identity algebraically in the reduced ODE and with a symplectic numerical integrator.

## 5. Explicit memory from an eliminated field

On a specified globally hyperbolic background with retarded Green operator $G_R$ for $(\Box_g-M^2)$,

$$\chi(x)=\chi_{\rm hom}(x)+g\int d^4y\sqrt{-g(y)}\,G_R(x,y)\phi(y).$$

Substituting into the first equation yields

$$\boxed{(\Box_g-m^2)\phi(x)=g\chi_{\rm hom}(x)
+g^2\int d^4y\sqrt{-g(y)}\,G_R(x,y)\phi(y).} \tag{7}$$

This is a causal history-dependent *effective equation*, provided the retarded operator and initial data exist. The second field has not vanished physically: its influence and independent initial conditions survive in the kernel and $\chi_{\rm hom}$. It would be incorrect to claim that memory emerges from nothing or that this procedure uniquely identifies EFMW.

## 6. Correspondence with established physics

When $\phi=\chi=0$ the new field equations are solved, the scalar stress vanishes, and the Einstein+SM equations remain a consistent solution sector. When $g=0$, scalar mixing vanishes and two free scalars remain; **the full theory does not become strictly identical to GR+SM** because these additional modes still exist. A true low-energy decoupling claim requires a controlled heavy-mass/weak-excitation limit and an estimate of residual effects, without tuning away actual observations.

Neither this construction nor the Base888 model derives the observed quantum gauge fields, their chiral representations, or a UV-finite gravitational theory. The gravitational action is the *classical* Einstein–Hilbert input; there is no quantized spacetime in TOE-001.

## 7. Falsifiable *conditional* response structure, not yet an observable

To define a mathematical probe, add a small **external diagnostic source** $J\phi$ on fixed Minkowski background, then set $J=0$ for the closed system. At spatial wave number $k$ and frequency $\omega$ with retarded regulator $\eta>0$, let $z=(\omega+i\eta)^2$. The probe-to-$\phi$ susceptibility is

$$\boxed{\chi_{\phi\phi}(\omega,k)=
\frac{k^2+M^2-z}{(k^2+m^2-z)(k^2+M^2-z)-g^2}.} \tag{8}$$

For nonzero $g$, the response has two normal-mode poles at $\omega^2=k^2+\lambda_\pm$, with nonnegative spectral weights summing to one. For $g=0$ the $\phi$ response reduces to a single free-field pole. This distinction is testable in the *toy model*. It is **not** a new verified physical signal because no real laboratory source $J$ or detector coupling has been derived from EFMW, and ordinary two-scalar EFT predicts the same form. A matched conventional two-scalar model is an essential control, not merely the $g=0$ ablation.

A future physical test must specify a gauge-invariant portal, parameter values or bounded priors, calibration data, realistic experimental noise, and a preregistered new prediction. It must compare to GR+SM plus the strongest conventional alternative using the same data and parameter budget.

## 8. Reproduced reference run

The dimensionless illustrative parameters are $m^2=1$, $M^2=4$, $g=0.25$. The exact squared frequencies are

$$\lambda_-=\frac{5-\sqrt{9.25}}2\simeq0.9793093674,\quad
\lambda_+=\frac{5+\sqrt{9.25}}2\simeq4.0206906326.$$

A 20,000-step velocity-Verlet integration with $dt=0.001$, $\phi(0)=1$, $\chi(0)=\dot\phi(0)=\dot\chi(0)=0$ produced:

- **15/15** Python tests passing, including positivity, null decoupling, exact eigenmode checks, response pole checks, convergence, and energy.
- Maximum relative total-energy drift **$1.2302\times10^{-7}$**.
- Maximum coordinate error versus the exact two-mode solution **$6.7964\times10^{-7}$**.

These are numerical results for a well-known quadratic oscillator theory—not experimental measurements, not Einstein-equation integration, and not independent confirmation of EFMW. Tests are in `tests/test_model.py`; the freeze is in `results/reference.json` and generated by `run.py`.

## 9. Gates and disqualifiers

| Gate | Status in TOE-001 | What would close it |
|---|---|---|
| Defined covariant candidate action | **PASS (analytic construction)** | Independent source review of conventions, variation and boundary conditions |
| Scalar EOM and total conservation | **PASS (conditional analytic identity)** | External mathematical review; fully formal GR/SM assumptions remain inputs |
| Homogeneous scalar stability | **PASS (strict $g^2<m^2M^2$)** | Analyze nonlinear, quantum and curved-background stability |
| Numerical reproducibility | **PASS (local 15 tests)** | Independent environment reproduction |
| Recovery of GR+SM | **PARTIAL (exact zero-field solution sector)** | Controlled decoupling of additional degrees of freedom |
| EFMW 102 equation correspondence, ME-007 | **UNRESOLVED** | Exact definitions and derivation; not just analogy |
| GR quantum completion | **UNRESOLVED** | Consistent quantum gravitational observables/UV completion |
| SM gauge content emerging from first principles | **UNRESOLVED** | Non-circular chiral spectrum, dynamics and anomaly cancellation |
| Unique new physical effect of EFMW | **UNRESOLVED** | Physical portal, bounded prediction distinguishable from conventional EFT |
| Independent observational/experimental falsification | **UNRESOLVED** | Held-out data and adversarial independent replication |

**Automatic limiter:** No result is labeled `TOE_CLOSED` while *any* mandatory physical gate is unresolved. In particular, a clean numerical test or a correct on-shell conservation identity cannot upgrade a toy model to fundamental physics.

## 10. The next decisive theorem and experiment

1. **Derive** a *unique* EFMW informational stress tensor and field dynamics, including source dimensions, signs and its relationship to the historical canonical equations. Either identify these fields with $\phi,\chi$ by a noncircular map or declare that this model is only an analogy.
2. **Prove** the original ME-007 Bianchi obligation in its own notation, including all dependencies and conditions. If it cannot be closed, constrain or reject the claim.
3. **Specify** an actual coupling to an observational channel and compute a quantitative test that differs from *both* GR+SM and a generic coupled-two-scalar EFT. Pre-register the failure threshold, conventional controls and parameter count.
4. **Attempt** a quantum-complete, 3+1-dimensional continuum theory whose low-energy limit recovers known quantum fields and gravitational interactions. Base888 currently lacks that derivation.

## 11. Provenance and references

- Wright's EFMW mathematical program and historical candidate corpus: [EFMW canonical review](https://github.com/enuminous/EFMW), [open obligations](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md).
- Wright / AI-assisted predecessor to the current construction: [QST-002 — two-scalar memory sector](https://github.com/enuminous/QST/blob/main/QST-002.md). This work does **not** claim that its known scalar equations were uniquely discovered by EFMW.
- [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian) for the original source-sign, coupling and stress-energy gaps. The candidate action here is new and does not retroactively correct those files.
- [CFSG audit](https://github.com/enuminous/CFSG/blob/main/audit/CFSG_ZOO_2026-10-27.md) illustrates bounded theorem-inspection conventions; the CFSG team and their proofs are **unrelated** to a putative TOE derivation.
- Isidori, Wilsch, Wyler, *The Standard Model Effective Field Theory at Work*, Rev. Mod. Phys. 96, 015006 (2024), https://doi.org/10.1103/RevModPhys.96.015006 — modern EFT perspective and why beyond-SM operators require careful physical tests.
- Standard GR/scalar variation and Klein–Gordon constructions are textbook mathematics; the conservation identities herein are not claimed as an original scientific discovery.

**Authorship note:** TOE-001 was constructed for Matthew Chenoweth Wright and Monolithic LLC with AI assistance; historical EFMW concepts are attributed to Wright, conventional field-theory principles to the wider physics community. Nothing in this document claims authorship of the Standard Model, general relativity, or other researchers' results.
