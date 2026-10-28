# F01 — ME-006/ME-007 informational-tensor identifiability and an operational information observable

**Date:** 28 October 2026  
**Research:** Matthew Chenoweth Wright / Monolithic LLC, with AI-assisted derivation and software tests.  
**Version:** F01-r1, source-lock anchored to the canonical 102 equations and TOE-001 ME-007 r1.  
**Scope:** Mathematical identifiability + synthetic equilibrium measurement demonstration; **no astrophysical or laboratory observations and no experimental evidence for informational gravity**.

## Executive result

1. **Source correction:** The canonical [ME-006](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/equations.json), directly preceding ME-007, *does* provide a symbolic tensor ansatz, `I_{μν}=T^{φ}_{μν}+R_{μν}`, in which `T^φ` is the standard scalar stress tensor. The remaining `R_{μν}` is described as *recursive informational structure* but has no independently specified constitutive law, dynamics or measurement prescription in the cited canonical entry. The earlier TOE-001 analysis focused on the ME-007 entry alone; that is too narrow to characterize the whole canonical corpus. The added ME-006 context narrows—but does not close—the gap.
2. **A truly partition-invariant dynamical quantity exists:** the *total* stress tensor `T^{(α)}+κ I^{(α)}`, its FLRW energy density and pressure, and the resulting `H` and `Ḣ` in the TOE-001 model are independent of arbitrary `α` and nonzero `κ`. Conversely, the individual labeled tensors generally vary.
3. **An independently operational information *scalar* can be derived under new, explicit statistical assumptions:** the Gaussian mutual information between two classically observable oscillator amplitudes in a stationary Gibbs state, obtained from measured covariance rather than from a gravitational field equation.
4. **Identifiability verdict:** the mutual information is `α,κ` invariant and could be measured in a coupled-oscillator or low-voltage circuit analogue. However, it is standard Gaussian correlation information; it does not uniquely define the original `R_{μν}`, a local informational stress tensor, a gravitational coupling, or an EFMW-specific physical effect. **F01 physical identification remains UNRESOLVED.**

## 1. What the historical source actually says

The preserved [canonical ME-006 / ME-007 / ME-008 sequence](https://github.com/enuminous/Monolithic_102_EFMW) records

\[
\begin{aligned}
\mathrm{ME\! -\! 006:}\quad I_{\mu\nu}&=\nabla_\mu\phi\nabla_\nu\phi-\tfrac12g_{\mu\nu}\nabla_\alpha\phi\nabla^\alpha\phi-g_{\mu\nu}V(\phi)+R_{\mu\nu}^{\rm rec},\\
\mathrm{ME\! -\! 007:}\quad G_{\mu\nu}+\Lambda g_{\mu\nu}&=8\pi G(T_{\mu\nu}+\kappa I_{\mu\nu}).
\end{aligned}
\]

The superscript `rec` in this analysis disambiguates **the original author's `R_{μν}` recursive symbol** from the Ricci tensor. It is *not* a silent change to the historical formula. The first three terms of ME-006 equal the conventional minimally coupled scalar stress `T^φ_{μν}` (also listed in ME-015). The source labels `R_{μν}` informational/recursive but does not specify its metric variation, dimensions, independent source fields, or local observables. The later ME-009/011 sketches are not an unambiguous independently varied construction of this tensor because their recursion variables/metric dependence and boundary definitions remain unspecified.

For the minimal scalar potential `V=m²φ²/2` and metric signature `(-+++)`,

\[
\nabla^\mu I_{\mu\nu}=(\Box_g\phi-m^2\phi)\nabla_\nu\phi+\nabla^\mu R^{\rm rec}_{\mu\nu}.
\]

Assuming constant nonzero `κ`, separate covariant conservation of the specified ordinary source, and an on-shell metric equation, ME-007 requires

\[
\nabla^\mu R^{\rm rec}_{\mu\nu}=-(\Box_g\phi-m^2\phi)\nabla_\nu\phi.
\tag{A}
\]

Equation (A) constrains the **divergence** of `R`; it does not determine all its tensor components. In the interacting TOE-001 scalar model `□φ−m²φ=γχ`, its right-hand side becomes `−γχ∇νφ`. This identity is a conditional consistency requirement, not evidence that an independently new physical information field has been derived.

## 2. Explicit non-uniqueness of the source accounts

With the unchanged two-scalar action in [TOE-001](ME007_INTEGRATION.md), let `T^mix_{μν}=−g_{μν}γφχ`. As before, for `0≤α≤1`, `κ≠0`, define

\[
T^{(\alpha)}=T^{SM}+T^{\phi,0}+\alpha T^{mix},\qquad
I^{(\alpha,\kappa)}=\kappa^{-1}[T^{\chi,0}+(1-\alpha)T^{mix}].
\]

Then identically `T^(α)+κI^(α,κ) = T^SM+T^φ+T^χ+T^mix`. Thus observables computed from the fully specified model, such as the metric response and total energy-momentum, are invariant under `α` and `κ`, while the named information tensor is not.

For one fixed **dimensionless illustrative state** `(φ,χ,φ̇,χ̇,ρ_m)=(0.7,−0.3,0.2,−0.1,0.2)` and `(m²,M²,γ)=(1,4,0.25)`, the exact energy-density account is:

| Allocation | Ordinary density | Labeled `I₀₀` | `ρ_ordinary+κρ_I` |
|---|---:|---:|---:|
| `α=0, κ=1` | 0.465000 | 0.132500 | **0.597500** |
| `α=0.5, κ=1` | 0.438750 | 0.158750 | **0.597500** |
| `α=1, κ=1` | 0.412500 | 0.185000 | **0.597500** |
| `α=0.5, κ=3` | 0.438750 | 0.0529167 | **0.597500** |

These are algebraic values, not cosmological density measurements. The labels change while the same modeled total does not. The same result applies to total pressure and (for the same physical state) the flat-FLRW `H²` inferred from it.

To connect **ME-006's exact ansatz** to the particular `T=T^SM` assignment and `κ=1`, one possible recursive remainder is

\[
\boxed{R^{rec}_{\mu\nu}:=T^{\chi,0}_{\mu\nu}+T^{mix}_{\mu\nu}}\tag{B}
\]

so that `I=T^φ+R^rec=T^φ+T^χ+T^mix`. On-shell, `(B)` has divergence `−γχ∇νφ` and meets (A). For general `κ`, another consistent definition is `R^{rec}=κ^{-1}T^{scalar,total}−T^φ`. **These are explicit mathematical completions, not noncircular identifications of the original recursive physics.** Infinitely many source allocations remain possible. Even with a fixed divergence, adding an admissible independently conserved symmetric tensor changes `R` without changing (A).

## 3. Independent operational *scalar* information: a conditional derivation

A quantity worth measuring independently of gravity is the **mutual information of physical readouts** of the two modes. To derive a closed formula, add assumptions *not contained in the historical EFMW equations*: a calibrated, stationary, classical thermal Gibbs ensemble of the **flat homogeneous** coupled oscillator, two separately accessible scalar-like coordinates `(φ,χ)`, and positive-definite stiffness

\[
K=\begin{pmatrix}m^2&\gamma\\\gamma&M^2\end{pmatrix},\qquad D=m^2M^2-\gamma^2>0.
\]

The measured position distribution is assumed Gaussian:

\[
p(\phi,\chi)\propto\exp\big[-\tfrac{\beta}{2}(\phi,\chi)K(\phi,\chi)^\top\big],\qquad
C\equiv\operatorname{Cov}(\phi,\chi)=\beta^{-1}K^{-1}=
\frac{1}{\beta D}\begin{pmatrix}M^2&-\gamma\\-\gamma&m^2\end{pmatrix}.
\]

Thus the Pearson correlation coefficient is `ρ=−γ/√(m²M²)`. The **ordinary Gaussian** mutual information is

\[
\boxed{\mathcal M=I_{\rm Shannon}(\phi;\chi)=-\frac12\ln(1-\rho^2)
=\frac12\ln\frac{m^2M^2}{m^2M^2-\gamma^2}.}\tag{C}
\]

The logarithm is natural, giving information in *nats*. Unlike `I_{μν}`, this `\mathcal M` is **not a rank-two tensor**. It can be determined solely from calibrated simultaneous mode readings, including an independent laboratory analogue, without using the gravitational field equation. `α` and `κ` do not appear in the probability model, so (C) is invariant under their reassignment. The information quantity is also independent of inverse temperature `β` **within this particular ideal classical Gibbs model**, although its raw covariances scale with temperature.

The independent *response check* obtained by varying the **physical coupling** at fixed `m²,M²,β` is

\[
\boxed{\frac{\partial\mathcal M}{\partial\gamma}=\frac{\gamma}{D}
=-\beta\operatorname{Cov}(\phi,\chi).}\tag{D}
\]

Equation (D) cross-checks a standard thermodynamic/statistical inference. It is a way to test the mutual-information model from mode measurements without interpreting `I_{μν}`. It is **not** a gravitational susceptibility or novel law. The MI also has a sign degeneracy: reversing `γ` changes cross-correlation sign but not `\mathcal M`. Its divergence as `D→0⁺` warns that the quadratic thermal model approaches loss of normalizability, not that cosmic informational energy becomes infinite.

## 4. Executed synthetic audit and null controls

Python 3 standard-library implementation: [toe001/me007_identity.py](toe001/me007_identity.py), [14 focused tests](tests/test_me007_identity.py), deterministic generator [scripts/run_me007_identity.py](scripts/run_me007_identity.py) and [archived result JSON](results/me007_identity_reference.json). The sample generator draws directly from the chosen equilibrium Gaussian: it is **not a simulation of real instruments, an autonomous cosmological measurement, or an independently sourced field observation**.

| Computation | Result |
|---|---:|
| `m²,M²,γ,β` | `1, 4, 0.25, 1` |
| Stiffness determinant `D` | `3.9375` |
| Analytic correlation `ρ` | `−0.125000` |
| Analytic mutual information | `0.007874178484` nats |
| Synthetic independent thermal draws | `80,000` (seed `20261028`) |
| Estimated Gaussian mutual information | `0.007626598092` nats |
| Zero-coupling population mutual information | `0` nats |
| Zero-coupling synthetic estimate | approximately `0.00000148984` nats |
| Information response `∂M/∂γ` | `0.06349206349` |
| Unit tests | **14/14 PASS** |
| SymPy identities checked separately | covariance, response, partition, ME-006 remainder: **zero residual** |

The small positive finite-sample null estimate reflects estimator/sample fluctuations; it does not imply real coupling. The analytic MI and synthetic estimator agree at the chosen sample count to an absolute difference of about `0.000248` nats. No significance or external replication is inferred from a pseudorandom sample constructed with the very covariance being tested.

## 5. An inexpensive real-world measurement protocol, NOT YET RUN

Use two distinguishable, weakly coupled classical oscillator modes (mechanical or low-voltage electronic) with known separately calibrated amplitudes. Establish equilibrium-like stationary stochastic forcing with independently measured noise properties, or separately test the precise nonequilibrium distribution rather than pretending it is Gibbs. Acquire paired amplitude trajectories; evaluate thermalization/stationarity, cross-talk, drift and autocorrelation. Estimate the covariance with independent sensor-noise correction, calculate `\hat\rho`, then `\hat{\mathcal M}=−\tfrac12\ln(1−\hat\rho^2)` **only after validating the Gaussian assumption**. For independent time-series samples use an effective sample size or blocked bootstrap; naïve iid uncertainties are inappropriate for autocorrelated trajectories.

Repeat for `γ=0`, positive and negative calibrated couplings and multiple temperatures. Predeclare the uncertainty and nuisance-treatment protocol, then test (C) and (D) on held-out runs. Comparison controls are ordinary coupled-harmonic-oscillator statistics and established stochastic thermodynamics. A successful measurement would validate the apparatus and statistical model **only**, not informational gravitation.

If the proposed astrophysical EFMW field components cannot be mapped to independently calibrated physical sensors or observables, this laboratory analogue cannot be promoted to a test of ME-006 as a universal law.

## 6. Why the scalar cannot by itself become a unique gravitational tensor

- The observable `\mathcal M` has units of **nats**, whereas a stress-energy source has units of **energy per volume** in conventional units. Conversion requires a physically justified normalization, coarse-graining volume or density, and a dynamical coupling—not merely a naming convention.
- Mutual information between two sets of readouts depends on what subsystems and readout variables are identified; it is not automatically a local covariant scalar field on a four-dimensional spacetime. Separate invertible transformations of the two variables preserve MI, but arbitrary mixing between their definitions need not.
- Even a hypothetical choice of local information density leaves open how its dependence on the metric and fields enters an independent generally covariant action `S_rec[g,fields]`, from which a rank-two tensor could be defined by `R^{rec}_{μν}=−2/√−g δS_rec/δg^{μν}`. **No such physically grounded action is derived here.**
- Equation (A) constrains only the divergence; many rank-two tensors have the same divergence. The effect of the new source must additionally be distinct from a reparameterization of conventional scalar stress, dark energy or other known matter.
- `\kappa I` is the combination entering ME-007. If `κ` is free, gravitational observables alone cannot determine an absolute normalization of `I` separately; a genuinely independent measurement/coupling convention is necessary.

Therefore finding a measured *information* scalar is **not equivalent** to determining the original *informational stress tensor*. This is the exact boundary between the present positive computational result and physical ME-007 closure.

## 7. Verdict and next decisional experiment

| Gate | Verdict |
|---|---|
| Canonical ME-006 recognized and related to ME-007 | **PASS — source-recovery correction** |
| `α,κ`-invariant gravitational total source | **PASS — model identity** |
| Nontrivial independently operational information scalar | **PASS — derived under extra Gaussian thermal assumptions; laboratory measurement not conducted** |
| `∂M/∂γ` covariance response / zero-coupling null | **PASS — analytic and synthetic check** |
| Original recursive `R_{μν}` uniquely fixed | **UNRESOLVED** |
| Local covariant stress tensor derived from independent information dynamics | **UNRESOLVED** |
| EFMW-specific physical prediction and actual measurement | **UNRESOLVED** |
| ME-007 as new experimentally established gravitational physics | **NOT ESTABLISHED** |

**Next experiment:** independently and noncircularly define the recursive sector's spacetime fields, metric dependence and observables; derive its action's metric variation; calculate a fixed, observable difference from an ordinary two-scalar control; and only then conduct a blinded/held-out physical test. Until then, the strongest defensible statement is: **the chosen scalar model has an operational correlation observable, but no unique EFMW gravitational information tensor has been physically identified.**

### Sources

- [Canonical 102 equation source, especially ME-006 through ME-015](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/equations.json).
- [TOE-001 original ME-007 classical candidate and source-partition audit](ME007_INTEGRATION.md).
- [EFMW frozen open obligations](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md).
- [Gaussian mutual information reference and derivation](https://d2l.smola.org/chapter_mdl-information-theory/mdl-mutual-information.html).
- [Gaussian covariance/mutual information information-theoretic background](https://pmc.ncbi.nlm.nih.gov/articles/PMC7062371/).

*This research note records a new focused audit and classical-statistical calculation in the EFMW research program, not a newly discovered fundamental physics theorem. Provenance of standard Gaussian identities is acknowledged.*
