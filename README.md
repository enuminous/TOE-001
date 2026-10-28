# TOE-001 — Covariant EFMW-inspired Unified Action and Correspondence Test

**Status: executable conditional classical model — NOT a Theory of Everything.**

[Read the technical paper](PAPER.md) · [Run the tests](tests/test_model.py) · [Frozen numerical results](results/reference.json) · [Model code](toe001/model.py) · [Source program](https://github.com/enuminous/EFMW) · [Historical QST-002](https://github.com/enuminous/QST/blob/main/QST-002.md)

This package implements a dimensionless **flat homogeneous two-scalar subsector** of a clearly defined *covariant* GR + Standard Model + two-scalar classical action. Its mathematical construction supports a local, retarded memory representation by eliminating one scalar, positive-definite linear stability, the standard GR+SM **zero-scalar solution sector**, and a response function with two poles for nonzero mixing.

The full curved-spacetime Einstein equations, SM quantum field equations, quantum gravity, and the historical EFMW informational tensor are **not** numerically solved here. The program is a baseline architecture for tests, not a successful claim of physical unification.

## Interactive browser laboratory

**[Open `index.html` source](index.html)** · **[Download the standalone HTML file](https://raw.githubusercontent.com/enuminous/TOE-001/main/index.html)**

The root `index.html` is a **self-contained, offline-capable laboratory** requiring no packages, network or build tooling. Download it, then open it in a web browser. To publish it as a GitHub Pages website, enable **Settings → Pages → Deploy from branch → `main` / `/ (root)`** and wait for GitHub to report a successful deployment. A public Pages deployment has not been independently confirmed.

The laboratory includes:

- Adjustable squared masses, mixing, wavenumber, response regulator, initial conditions and integration timestep.
- A velocity-Verlet integration of the same **flat homogeneous two-scalar model** as [`toe001/model.py`](toe001/model.py), alongside an independently calculated exact normal-mode trajectory.
- Oscillation graphs, field-space orbit, maximum energy drift and numerical error, and a conditional response spectrum compared with the **`g=0` null model**.
- A frozen 20,000-step benchmark button matching the reference inputs in [`results/reference.json`](results/reference.json), plus an evidence JSON export.
- A visible distinction between conditional classical checks and the **unresolved** EFMW ME-007 tensor, quantum-gravity, Standard Model emergence and empirical-prediction obligations.

**Browser validation:** A local Chromium test completed without JavaScript errors. The frozen benchmark returned maximum energy drift approximately `1.230188e-7` and final position error approximately `6.796413e-7`, matching the Python reference to floating-point precision. The null-model switch and unstable-mass-matrix blocking were also exercised.

**Scope:** This is a presentation and calculator for the specified classical subsector, **not** a complete gravitational/particle simulation, a novel physical signature or a Theory of Everything.

## ME-007 conserved-source candidate (TOE001–ME007–r1)

**[Read the complete ME-007 derivation](ME007_INTEGRATION.md)** · [Python implementation](toe001/me007.py) · [FLRW reference output](results/me007_flrw_reference.json) · [Symbolic identity checks](results/me007_symbolic_checks.json) · [GitHub Actions verification](.github/workflows/verify-me007.yml)

We preserved [the canonical ME-007 source](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/01f51acb0b0e564105dcf7f14cc55998d41b91ce/Monolithic102/ME007.lean) and constructed an **explicitly assumed** informational-tensor candidate from the TOE-001 two-scalar stress tensor. It reproduces ME-007's Einstein-equation **shape** and proves conditional on-shell conservation, including energy exchange between the chosen ordinary and information sectors. An expandable spatially flat FLRW laboratory is now available in [index.html](index.html#me007).

**Research finding:** the split is mathematically nonunique: changing the interaction allocation α and normalization κ changes the labels assigned to the two sources while leaving total gravity unchanged. Consequently this construction does **not** identify the historical EFMW tensor or close ME-007 as an EFMW-specific physical law.

The classical FLRW reduction also implies **no smooth flat-spacetime bounce** with positive canonical kinetic terms and ordinary matter satisfying the null energy condition, and it cannot produce universal rotation from an exactly isotropic metric. These are useful restrictions rather than proof of unification.

**Verification:** the expanded suite has **31 passing Python unit tests** and **8 passing SymPy identities** (flat-FLRW polynomial consequences); browser model exchange/constraint checks were also exercised. The [CI workflow](.github/workflows/verify-me007.yml) validates those operations at each relevant push. **No Lean proof of the full four-dimensional tensor equation, independent physics experiment, quantum gravity or full Theory of Everything has been achieved.**

## F01 — Identifying an alpha/kappa-invariant information observable

**[Read F01 ME-006/ME-007 identification study](F01_ME007_INFORMATION_IDENTIFICATION.md)** · [Operational model](toe001/me007_identity.py) · [14 dedicated tests](tests/test_me007_identity.py) · [Frozen synthetic dataset](results/me007_identity_reference.json) · [Reproduction script](scripts/run_me007_identity.py)

**Canonical-source clarification:** ME-006 actually provides `I_{μν}=T^φ_{μν}+R_{μν}`, where `R_{μν}` is the still-undefined recursive-information remainder. The previous ME-007 study is preserved with a correction note. A concrete choice `R=T^χ+T^mix` at `κ=1` and `T=T^SM` satisfies source conservation on shell but remains conventional two-scalar physics, not the unique original EFMW information tensor.

**A non-gravitational information observable:** under the newly assumed classical Gaussian thermal state, two calibrated mode amplitudes have mutual information `0.5*ln[m²*M²/(m²*M²−gamma²)]`, independent of the arbitrary partition parameters `alpha` and `kappa`. This can be estimated from jointly observed amplitude covariances without a gravitational field measurement; a second response identity connects its coupling derivative to the cross-covariance.

**Synthetic reference:** for the illustrative default parameters, the analytic result is `0.007874178484` nats; 80,000 seeded Gibbs draws produce `0.007626598092` nats; the zero-coupling synthetic estimate is about `1.49e-6` nats. **14 focused Python tests passed locally**, and four independent symbolic cancellations were checked. These are synthetic/calculation results, *not actual field observations*. Neither an independent recursive `R_{μν}` nor an EFMW-specific gravitational signature has been identified.

Reproduce from the repository root: `python3 -m unittest discover -s tests -v` and `python3 scripts/run_me007_identity.py`. The frozen JSON should be treated as an illustrative numerical record, not new empirical evidence.

## Reproduce with Python 3.10+

```bash
python3 -m unittest discover -s tests -v
python3 run.py
python3 run.py --g 0 --out results/null_g0.json
```

No pip dependencies. The standard output reports numerical solver error and energy drift. The JSON file includes the frozen status gates and measured *simulation* diagnostics. All masses and couplings are chosen illustrative numbers in arbitrary dimensionless units; there is no empirical parameter calibration.

## Key equation

With $V(\phi,\chi)=\frac12m^2\phi^2+\frac12M^2\chi^2+g\phi\chi$ and $(-+++)$ metric,

$$S=\int\sqrt{-g}\,[\tfrac12M_{\mathrm{Pl}}^2R+\mathcal L_{SM}-\tfrac12(\nabla\phi)^2-\tfrac12(\nabla\chi)^2-V]\,d^4x+S_{GHY}.$$

This is **standard multi-scalar effective field theory** supplied as a conservative working model, not a derivation of a new theory from EFMW. The memory construction and conservation identity are explained in [PAPER.md](PAPER.md).

## Project state

| Claim | Evidence |
|---|---|
| Covariant action + conditional conservation identity | Analytic derivation in PAPER.md |
| Stable parameter domain, $g^2<m^2M^2$ | Analytic eigenvalues + unit tests |
| Homogeneous numerical energy and exact solution | 15 Python unit tests + reference.json |
| Exact GR+SM as zero-scalar solution sector | Conditional analytic consequence; **not** full equivalence |
| Derivation of quantum gravity or observed SM | **UNRESOLVED** |
| Unique EFMW physical effect and independent experiment | **UNRESOLVED** |

The strongest scientific falsifier is **not** a failure of a toy oscillator—it is a failure to derive a novel testable observable beyond what conventional coupled-scalar physics already explains. All further claims must honor that distinction.

## Attribution

Prepared for Matthew Chenoweth Wright / Monolithic LLC with AI assistance, using established GR, the Standard Model, and well-known coupled-scalar mathematics. The EFMW motivation and provenance remain distinct from independent physical proof. Sources and constraints are in PAPER.md. No new repository license is assigned without explicit authorization.
