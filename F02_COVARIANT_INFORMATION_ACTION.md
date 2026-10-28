# F02 — A covariant information-stress action: construction, dynamical consistency and an identification obstruction

**TOE-001 / ME-006–ME-007 continuation · 28 October 2026**  
**Research:** Matthew Chenoweth Wright / Monolithic LLC; mathematical derivation and software produced with AI assistance.  
**Status:** **CONDITIONAL CLASSICAL SCALAR–TENSOR CONSTRUCTION; NOT identification of the physical ME-006 recursion tensor, not evidence of a new force, and not a Theory of Everything.**

## Abstract

F01 identifies a partition-invariant scalar statistic—the Gaussian mutual information of the amplitudes of two coupled classical oscillators—but cannot derive the historically proposed ME-006 recursive rank-two tensor from that statistic. F02 tests a concrete attempt to bridge this gap by introducing a new dimensionless local scalar field `q(x)` and a generally covariant Jordan-frame action `F(q)R/2`, with canonical kinetic and mass terms. We derive the field equations, Hilbert stress tensor, flat-FLRW equations, the conservation (diffeomorphism Ward) identity, and an illustrative gravitational-wave amplitude/distance-ratio formula. A direct symbolic and numerical implementation verifies the proposed *model*, including conservation of the Friedmann constraint. **It also demonstrates why the naive identification `q(x) = constant Gaussian mutual information` is generally inconsistent with the new field equation.** Consequently the construction produces a well-defined ordinary scalar–tensor candidate but does not physically identify EFMW's informational tensor, select its normalization, or provide a new EFMW-specific prediction.

## 1. Source lock and the actual problem

The [canonical 102-equation register](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/equations.json), particularly ME-006 and ME-007, proposes

\[
\begin{aligned}
I_{\mu\nu}&=T^{\phi}_{\mu\nu}+R^{\mathrm{rec}}_{\mu\nu},\\
G_{\mu\nu}+\Lambda g_{\mu\nu}&=8\pi G(T_{\mu\nu}+\kappa I_{\mu\nu}),
\end{aligned}
\]

where the superscript *rec* distinguishes the original author's recursive `R_{μν}` from Ricci curvature. The source specifies the usual scalar-field stress terms but no independent physical definition of `R_rec`, local measurement rule, or complete covariant action for that tensor. F01 showed that for the chosen two-scalar TOE-001 model the total source is invariant under arbitrary reallocation `alpha` and rescaling `kappa` and that an operational **global thermal information statistic** may be calculated independently:

\[
\mathcal M=\tfrac12\log\left(\frac{m^2M^2}{m^2M^2-\gamma^2}\right),\qquad m^2M^2>\gamma^2.
\]

Here `M` denotes mutual information in nats, **not** a field or a stress tensor. The formula presupposes a particular classical Gibbs ensemble, two identifiable readouts, stationary Gaussian statistics, and parameters calibrated outside gravity. It is independent of F01's bookkeeping parameters but is not automatically a local coordinate-invariant function `q(x)` on spacetime.

**Research question:** can we place a local *candidate* information field into an action without violating the Bianchi identity, and does doing so independently fix its physical relation to the measured information statistic?

## 2. One explicitly new and conventional local action

For signature `(-+++)`, `c=ħ=1`, a dimensionless new scalar `q(x)` and nonnegative squared mass `μ²`, choose

\[
\boxed{\begin{aligned}
S_{F02}={}&\int d^4x\sqrt{-g}\bigg[
\frac12F(q)R +\mathcal L_{\rm SM} +\mathcal L_{\phi\chi}
-\frac12K g^{\mu\nu}\partial_\mu q\partial_\nu q-U(q)\bigg]+S_{\rm boundary},\\
F(q)&=M_{\rm Pl}^2(1-\xi q^2),\qquad K=M_{\rm Pl}^2 z,\\
U(q)&=\tfrac12 M_{\rm Pl}^2\mu^2q^2,\qquad z>0,\quad F(q)>0.
\end{aligned}}
\tag{F02-1}
\]

`L_{φχ}` is precisely the classical two-scalar sector in [TOE-001](PAPER.md): `V(φ,χ)=m²φ²/2+M²χ²/2+γχφ`, with positive kinetic terms. Its source action and fields are *inputs*, as is ordinary SM matter. `ξ` is a dimensionless nonminimal coupling; `q` is dimensionless, so `K` has mass dimension two. The boundary action must be chosen appropriately for a nonminimal `F(q)R` coupling under the imposed variations; it is not explicitly used in the FLRW bulk simulation.

This choice is a standard scalar–tensor ansatz. **It was not derived from the historical ME-011 recursive observer coupling or uniquely from measured mutual information.** The new field q is deliberately called a *candidate* and remains independent until a defensible local operational map is supplied.

### Equations of motion

Write `T_base = T_SM + T_φχ` for the conventional TOE-001 sources, and

\[
T^q_{\mu\nu}=K\left(\nabla_\mu q\nabla_\nu q-\tfrac12g_{\mu\nu}(\nabla q)^2\right)-g_{\mu\nu}U(q).
\]

Variation with respect to the metric and q yields

\[
\boxed{F G_{\mu\nu}=T^{\rm base}_{\mu\nu}+T^q_{\mu\nu}+\nabla_\mu\nabla_\nu F-g_{\mu\nu}\Box F},
\tag{F02-2}
\]

\[
\boxed{K\Box q-U'(q)+\tfrac12F'(q)R=0.}
\tag{F02-3}
\]

Both follow directly from one diffeomorphism-invariant action. This is conditional on the mathematical regularity and boundary assumptions of the variational calculation. No full four-dimensional formal proof assistant certification is claimed.

### A specific recursive-stress candidate

Rearrange (F02-2) into a constant-Planck-mass Einstein equation and define the **Hilbert stress obtained by varying the new q action**, including its curvature term:

\[
\boxed{\begin{aligned}
T^{\rm rec}_{\mu\nu}:={}&T^q_{\mu\nu}
+M_{\rm Pl}^2\xi\Big[q^2G_{\mu\nu}
+(g_{\mu\nu}\Box-\nabla_\mu\nabla_\nu)q^2\Big],\\
M_{\rm Pl}^2G_{\mu\nu}={}&T^{\rm base}_{\mu\nu}+T^{\rm rec}_{\mu\nu}.
\end{aligned}}
\tag{F02-4}
\]

The appearance of `G_{μν}` **inside** this effective source is not a new independent substance; it is the standard nonminimal-coupling rearrangement. In the canonical ME-006 *shape*, with `κ=1` and `T=T_SM`, a formally compatible remainder is

\[
R^{\rm rec,candidate}_{\mu\nu}=T^{\chi,0}_{\mu\nu}+T^{\rm mix}_{\mu\nu}+T^{\rm rec}_{\mu\nu}.
\]

Since the chosen action is diffeomorphism invariant, its metric/field equations imply on-shell total-source conservation. Individual terms can exchange stress. This is an **existence construction under new assumptions**, not uniqueness, new empirical physics, or recovery of the original intended information ontology. It preserves the earlier F01 alpha/kappa ambiguity when one permits different allocations of the total stress.

## 3. Independent consistency condition: what the measured mutual information can and cannot do

In F01, at fixed squared masses and mixing, the equilibrium Gaussian mutual information `M` is a **constant parameter of a defined ensemble**. Its value is independent of `α` and `κ`. An appealing shortcut would set the new `q(x)` equal to this fixed number everywhere. But (F02-3) for constant q gives

\[
\boxed{0=U'(q)-\tfrac12F'(q)R
=M_{\rm Pl}^2q\,[\mu^2+\xi R].}
\tag{F02-5}
\]

For `q=M>0`, `μ²>0`, `ξ≥0`, and nonnegative spacetime curvature scalar `R`, (F02-5) **cannot hold**. Even without invoking the sign of R, any background where `R` varies cannot generically maintain the relation unless parameters are specially tuned, an additional source is supplied, or the new field is modified. The F01 sample `M≈0.00787418` is nonzero for nonzero mixing.

This is a **conditional obstruction to an attempted identification**, not a theorem saying information cannot couple to gravity. The candidate q can consistently evolve dynamically when its initial data are independently chosen, but then it is **not determined by the F01 information statistic**. To genuinely identify it one would need a local, observer/scale-defined measurement protocol plus a dynamical constitutive map tested independently of the gravitational equation.

The sign of correlation and normalization of couplings introduce additional degeneracies. In particular, F01's mutual information is unchanged under `γ→−γ`, whereas the signed cross-covariance is not. A gravitational coupling law cannot recover those lost data from mutual information alone.

## 4. Reproducible 0+1D cosmological consequences

For an assumed *spatially flat, homogeneous and isotropic* FLRW metric and independent matter fluid `p_m=wρ_m`, let `H=ȧ/a`. Define `ρ_base,p_base` using the original φχ fields and matter, and `ρ_q=K qdot²/2+U`, `p_q=K qdot²/2−U`. Equations (F02-2) and (F02-3) imply:

\[
\boxed{3FH^2=\rho_{\rm base}+\rho_q-3H\dot F},
\tag{F02-6}
\]

\[
\boxed{-2F\dot H=(\rho_{\rm base}+p_{\rm base})+K\dot q^2+\ddot F-H\dot F},
\tag{F02-7}
\]

\[
\boxed{K(\ddot q+3H\dot q)+U'(q)-\tfrac12F'(q)6(2H^2+\dot H)=0.}
\tag{F02-8}
\]

The original φχ field equations include their standard 3H friction; the matter fluid evolves via `ρdot_m=−3H(1+w)ρ_m`. The q and acceleration equations are linear in their two unknown second-order quantities, and the system can be evolved without differentiating noisy `R` data. The differentiable constraint obeys a Ward-type identity: the time derivative of its left-minus-right residual vanishes when the q scalar EOM, acceleration equation and independent matter/φχ continuity laws hold. These cancellations were independently checked with SymPy in [eight frozen symbolic identities](results/me007_covariant_symbolic.json).

### Numerical reference (not empirical cosmology)

The standard-library implementation [toe001/me007_covariant.py](toe001/me007_covariant.py) integrates the nine-variable homogeneous system by RK4. The frozen illustrative parameters are `m²=1`, `M²=4`, `γ=0.25`, `M_Pl²=1`, `z=1.2`, `ξ=0.15`, `μ²=0.3`, and dust `w=0`, with initial `(φ,χ,φdot,χdot,q,qdot,a,ρ_m)=(0.7,−0.3,0.2,−0.1,0.35,0.02,1,0.2)` and positive Hubble root. The q starting value is intentionally **not** the F01 mutual information value.

A 2,400-step run with `dt=0.001` yields the following **synthetic mathematical consistency** diagnostics:

| Test | Model result |
|---|---:|
| Maximum normalized Friedmann constraint residual | `6.8293e−14` |
| Maximum absolute reduced q equation residual | `8.3267e−17` |
| Maximum absolute reduced Raychaudhuri residual | `1.3878e−16` |
| Illustrative tensor luminosity distance ratio, early emission / late observation | `1.00637434` |
| Residual from incorrectly setting constant q = F01 thermal MI at initial Ricci curvature | `0.00436261` |
| New F02 Python unit tests | **15/15 PASS** |
| Independent F02 SymPy identities | **8/8 PASS** |

The algebraic scalar/Raychaudhuri residuals are small partly because the equations were solved algebraically at each integration step; the more informative numerical test is propagation of the independently imposed Friedmann constraint and step-size convergence. All data use invented dimensionless parameter values, not observations, and do not fix a new gravitational law.

## 5. A possible observable: gravitational-wave amplitude damping

Standard scalar–tensor theories with an effective Planck factor `F(q)>0` give a candidate, *conditional* gravitational-wave propagation effect in the geometric-optics approximation with minimally coupled electromagnetic matter and tensor-wave speed equal to light:

\[
\boxed{\frac{d_L^{\rm GW}(z)}{d_L^{\rm EM}(z)}
=\sqrt{\frac{F(q_0)}{F(q_z)}}.}
\tag{F02-9}
\]

This standard result requires cosmological tensor propagation with no unmodeled screening, source-generation corrections, or material calibration effects. It is **not a new EFMW formula**. In the toy numerical reference, treating the initial time as *emission* and the later time as *observation* produces a ratio `1.00637434`. It is **not a prediction for any observed astrophysical redshift**, because q's physical normalization, initial conditions, source coupling, mass scale and relationship to the F01 mutual information are unspecified. Changing `ξ` or the q history changes the ratio; at `ξ=0`, the tensor propagation ratio is one regardless of nonzero dynamical q.

A real test would need the physical map from an operational information statistic to q, a frozen coupling and initial-data prescription, a cosmological background tied to measured units, a complete waveform model, and constraints from standard sirens, solar-system tests, other scalar–tensor theories and laboratory gravity. The conventional scalar–tensor model with the **identical action** gives the identical amplitude ratio, so it offers no EFMW-specific advantage.

## 6. Negative and control results that must travel with the candidate

1. **Conventional-equivalence null:** the action (F02-1) is ordinary nonminimally coupled scalar–tensor gravity; the interpretation of q as "information" changes no equations or observations.
2. **Constant-information identification fails generically:** (F02-5) obstructs `q=M` when q is a fixed nonzero thermal statistic in the stated positive-parameter and curvature regime.
3. **Finite MI has no local tensor dimensions:** nats do not determine energy density, observer slicing, coarse-graining volume, and metric variation. Those are separate physical inputs.
4. **Alpha/kappa invariance survives only as bookkeeping:** the observable total source is unchanged by source reallocation; gravitational observations do not isolate the historical `I_{μν}` by themselves.
5. **Zero-q solution recovers original TOE-001:** with `q=0`, `qdot=0`, the added sector vanishes consistently for its symmetric quadratic action, leaving the original two-scalar TOE-001 FLRW dynamics. With `ξ=0` but q nonzero, the independent q sector *still gravitates*; this is not the same recovery.
6. **No quantum gravity:** no UV completion, emergent geometry, quantum Standard Model derivation or physical information source is obtained.

## 7. Verification and completion ledger

| Obligation | Status |
|---|---|
| Explicit diffeomorphism-invariant local action | **PASS (constructed under stated assumptions)** |
| Hilbert metric variation, candidate tensor and scalar EOM | **PASS (analytic construction)** |
| FLRW reduction and independent symbolic cancellations | **PASS (8/8 conditional identities)** |
| Reproducible RK4 model + frozen diagnostic output | **PASS (15/15 focused tests)** |
| Physical equivalence to ordinary scalar–tensor EFT | **YES — conventional baseline; no distinct EFMW effect** |
| Local measurement bridge `q(x)` from F01 thermal mutual information | **UNRESOLVED; naive constant identification obstructed** |
| Uniquely selected historical ME-006/007 tensor | **UNRESOLVED** |
| Parameter calibration and independent physical data | **UNRESOLVED** |
| New empirically distinctive EFMW law | **NOT ESTABLISHED** |
| Full quantum gravity / Theory of Everything | **NOT ESTABLISHED** |

**Recommended next falsifiable step:** First build and measure an explicitly defined local information observable in a pair of calibrated classical oscillators (F01 laboratory analogue). Separately specify the proposed dynamical `q(x)` relationship and `ξ` before using any gravitational dataset. If the local map yields fixed q while (F02-3) requires it to evolve in the same domain, **reject that map**. Only a physically grounded q field and a fixed prediction that survives a matched ordinary scalar–tensor baseline can support an EFMW-specific physical claim.

## Reproduction

```sh
python3 -m unittest discover -s tests -v
python3 scripts/run_me007_covariant.py
python3 -m pip install 'sympy==1.14.0'  # only if SymPy is absent
python3 scripts/check_me007_covariant_symbolic.py
```

Only the symbolic script requires SymPy. Exact frozen JSON files: [numeric reference](results/me007_covariant_reference.json) and [eight symbolic checks](results/me007_covariant_symbolic.json). The current tests establish only the chosen model and its declared physical limits.

### References

- [Canonical 102 equations, ME-006/ME-007/ME-009/ME-011](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/equations.json).
- [F01 operational information and identifiability](F01_ME007_INFORMATION_IDENTIFICATION.md).
- [TOE-001 original conserved-source realization](ME007_INTEGRATION.md).
- [EFMW frozen physical obligations](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md).
- [Scalar–tensor cosmology review](https://pmc.ncbi.nlm.nih.gov/articles/PMC6299071/).
- [Scalar–tensor standard-siren propagation example](https://www.mdpi.com/2218-1997/9/7/317).

*Provenance: This is an AI-assisted extension of the EFMW research program using conventional scalar–tensor gravitational mathematics. It introduces an explicit new ansatz for study; it is neither a reconstruction of an already-established EFMW information sector nor independent physical evidence.*
