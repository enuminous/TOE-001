# TOE-001 — Covariant EFMW-inspired Unified Action and Correspondence Test

**Status: executable conditional classical model — NOT a Theory of Everything.**

[Read the technical paper](PAPER.md) · [Run the tests](tests/test_model.py) · [Frozen numerical results](results/reference.json) · [Model code](toe001/model.py) · [Source program](https://github.com/enuminous/EFMW) · [Historical QST-002](https://github.com/enuminous/QST/blob/main/QST-002.md)

This package implements a dimensionless **flat homogeneous two-scalar subsector** of a clearly defined *covariant* GR + Standard Model + two-scalar classical action. Its mathematical construction supports a local, retarded memory representation by eliminating one scalar, positive-definite linear stability, the standard GR+SM **zero-scalar solution sector**, and a response function with two poles for nonzero mixing.

The full curved-spacetime Einstein equations, SM quantum field equations, quantum gravity, and the historical EFMW informational tensor are **not** numerically solved here. The program is a baseline architecture for tests, not a successful claim of physical unification.

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
