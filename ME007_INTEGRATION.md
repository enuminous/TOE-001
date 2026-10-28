# ME-007 / TOE-001 — A conserved-source candidate, its ambiguity, and its consequences

**Version:** 2026-10-28 / v0.2  
**Research:** Matthew Chenoweth Wright / Monolithic LLC, with AI-assisted mathematical and software construction.  
**Status:** **A valid conditional classical realization of the *form* of ME-007, NOT a derivation of its original undefined informational tensor, NOT quantum gravity, and NOT a Theory of Everything.**

> **ME-006 cross-reference correction (28 October 2026):** This earlier note correctly states that the isolated **ME-007 entry** does not define the information tensor, but the wider canonical **ME-006** equation immediately preceding it *does* supply the symbolic ansatz `I_{μν}=T^φ_{μν}+R_{μν}`. Its `R_{μν}` is designated recursive informational structure but has no independent constitutive law, physical observable, or unambiguous variational dynamics in the cited entry. Accordingly, the precise gap is not a complete absence of an information-tensor formula: it is the lack of a **physically identifiable recursive remainder**. The [new F01 source and operational-information audit](F01_ME007_INFORMATION_IDENTIFICATION.md) gives the corrected source reading, an explicit compatible remainder, the alpha/kappa-invariant total source, and a measurable *conditional* mutual-information scalar. It does not identify a unique gravitational information tensor.

## 1. Source provenance is a hard constraint

The preserved [ME-007 canonical Lean entry](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/01f51acb0b0e564105dcf7f14cc55998d41b91ce/Monolithic102/ME007.lean) gives:

\[
\boxed{G_{\mu\nu}+\Lambda g_{\mu\nu}=8\pi G(T_{\mu\nu}+\kappa I_{\mu\nu}).}
\tag{ME-007, historical form}
\]

Its accompanying description calls \(I_{\mu\nu}\) a *proposed informational tensor*. **There is no tensor definition, independent information action, normalization, or constitutive equation in that canonical entry.** The frozen [EFMW open-obligations register](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md) correctly lists ME-007-BIANCHI as unresolved. This document does not silently overwrite or revise the canonical source. We label each new definition **TOE001–ME007–r1**.

We take the previously disclosed [TOE-001 action](PAPER.md), with one explicitly added constant cosmological term, and ask whether that **specific** theory can be expressed in ME-007 form. *It can.* This is not yet an equivalence to Wright's original unknown informational dynamics.

## 2. Chosen action and equations, with all assumptions declared

Signature \((-+++)\), \(c=\hbar=1\), \(M_{\rm Pl}^2=(8\pi G)^{-1}>0\), constant \(\Lambda\), positive scalar kinetic signs, minimal coupling, and a separately generally covariant Standard Model action (or a perfect-fluid effective approximation for the numerical test). No direct scalar–SM portal is assumed. Write the scalar mixing as **\(\gamma\)** to distinguish it from the metric.

\[
S=\int d^4x\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}(R-2\Lambda)+\mathcal L_{\rm SM}
-\frac12(\nabla\phi)^2-\frac12(\nabla\chi)^2
-\frac12m^2\phi^2-\frac12M^2\chi^2-\gamma\phi\chi\right]+S_{\rm GHY}.
\]

The variations give:

\[
\Box_g\phi-m^2\phi-\gamma\chi=0,\qquad
\Box_g\chi-M^2\chi-\gamma\phi=0,
\]
\[
M_{\rm Pl}^2(G_{\mu\nu}+\Lambda g_{\mu\nu})
=T^{\rm SM}_{\mu\nu}+T^{\phi,0}_{\mu\nu}+T^{\chi,0}_{\mu\nu}+T^{\rm mix}_{\mu\nu},
\]

where for \(q=\phi\) or \(\chi\),

\[
T^{q,0}_{\mu\nu}=\nabla_\mu q\nabla_\nu q-g_{\mu\nu}
\left[\frac12(\nabla q)^2+\frac12m_q^2q^2\right],
\qquad T^{\rm mix}_{\mu\nu}=-g_{\mu\nu}\gamma\phi\chi.
\]

These formulae are conventional two-scalar Einstein–matter field theory. They are not reconstructed from the original EFMW 102 equations, Base888 or an information-theoretic axiom.

## 3. Explicit ME-007 tensor *candidate* and conservation

Choose *any* allocation \(0\le\alpha\le1\) and nonzero dimensionless \(\kappa\). Define **new**, model-specific tensors

\[
\boxed{T^{(\alpha)}_{\mu\nu}:=T^{\rm SM}_{\mu\nu}+T^{\phi,0}_{\mu\nu}
+\alpha T^{\rm mix}_{\mu\nu}},
\]

\[
\boxed{I^{(\alpha)}_{\mu\nu}:=\kappa^{-1}\left[T^{\chi,0}_{\mu\nu}
+(1-\alpha)T^{\rm mix}_{\mu\nu}\right]}. \tag{R1}
\]

Substitution proves \(T^{(\alpha)}+\kappa I^{(\alpha)}=T^{\rm total}\) identically, so the field equation has exactly the *historical ME-007 shape*. But **this construction is a freely chosen allocation of an ordinary scalar stress tensor, not an identification of the historical physical meaning of information**.

The scalar equations and \(\nabla^\mu T^{\rm SM}_{\mu\nu}=0\) give

\[
\nabla^\mu T^{\phi,0}_{\mu\nu}=\gamma\chi\nabla_\nu\phi,
\quad\nabla^\mu T^{\chi,0}_{\mu\nu}=\gamma\phi\nabla_\nu\chi,
\quad\nabla^\mu T^{\rm mix}_{\mu\nu}=-\gamma(\chi\nabla_\nu\phi+\phi\nabla_\nu\chi).
\]

Consequently

\[
\boxed{\nabla^\mu T^{(\alpha)}_{\mu\nu}
=J^{(\alpha)}_{\nu}
=\gamma[(1-\alpha)\chi\nabla_\nu\phi-\alpha\phi\nabla_\nu\chi]},
\]

\[
\boxed{\kappa\nabla^\mu I^{(\alpha)}_{\mu\nu}=-J^{(\alpha)}_{\nu},
\quad\nabla^\mu(T^{(\alpha)}_{\mu\nu}+\kappa I^{(\alpha)}_{\mu\nu})=0.} \tag{R2}
\]

**The individual sectors are not conserved in general.** Only their sum is. If the historical intended ordinary tensor is instead **just the SM stress** then a different equally consistent choice is \(I=\kappa^{-1}T_{\rm scal,total}\); the field equation cannot determine which split was intended. Noether conservation is contingent on the new action and on shell; it does not make \(I\) independently observable.

### A genuine underdetermination result

For two choices \(\alpha,\beta\), \(T^{(\alpha)}-T^{(\beta)}=(\alpha-\beta)T^{\rm mix}\) and \(\kappa(I^{(\alpha)}-I^{(\beta)})=-(\alpha-\beta)T^{\rm mix}\). Thus the **same gravitational field and conservation law** correspond to infinitely many assignments of ordinary versus information stress. Additionally, the normalization \(\kappa\) can be rescaled inversely with \(I\). **Without an independently defined EFMW information observable or constitutive law, ME-007 cannot be uniquely closed from Einstein's equation and Bianchi alone.** This is not a failure of general relativity; it is a missing physical definition in the historical candidate.

## 4. Consequences in the explicit spatially-flat FLRW test

Assume \(ds^2=-dt^2+a(t)^2d\mathbf x^2\), \(H=\dot a/a\), homogeneous scalars, and independently conserved matter approximated as \(p_m=w\rho_m\) with \(-1\le w\le1\). These are **extra symmetry assumptions**: this subsection is a cosmological reduction, not arbitrary curved spacetime or a quantum-gravity simulation.

\[
\rho_{\rm sc}=\frac12(\dot\phi^2+\dot\chi^2)+V,\quad
p_{\rm sc}=\frac12(\dot\phi^2+\dot\chi^2)-V,
\]
\[
3M_{\rm Pl}^2H^2=\rho_m+\rho_{\rm sc}+M_{\rm Pl}^2\Lambda,\quad
\dot H=-\frac{(1+w)\rho_m+\dot\phi^2+\dot\chi^2}{2M_{\rm Pl}^2},
\]
\[
\ddot\phi+3H\dot\phi+m^2\phi+\gamma\chi=0,\quad
\ddot\chi+3H\dot\chi+M^2\chi+\gamma\phi=0,
\]
\[
\dot\rho_m+3H(1+w)\rho_m=0.
\]

The sector continuity equations in this split are

\[
\dot\rho_{\rm ord}+3H(\rho_{\rm ord}+p_{\rm ord})=Q_{\rm ord},
\quad
\dot\rho_I+3H(\rho_I+p_I)=Q_I,
\]

\[
Q_{\rm ord}=-\gamma[(1-\alpha)\chi\dot\phi-\alpha\phi\dot\chi],
\qquad \kappa Q_I=-Q_{\rm ord}.
\]

The total conservation identity is \(\dot\rho_{\rm total}+3H(\rho_{\rm total}+p_{\rm total})=0\); it propagates the Friedmann constraint once it is imposed initially. These identities were also checked by symbolic cancellation with SymPy, and independently by numerical evolution using a fourth-order Runge–Kutta integrator; these are not general-purpose formal proof certificates.

### Two nontrivial restrictions imposed by this candidate

1. **No nonsingular flat-space bounce under the assumed null energy condition:** for canonical scalars and ordinary matter with \(\rho_m\ge0,w\ge-1\), \(\dot H\le0\). A contracting universe cannot change to expansion through a smooth \(H=0\) bounce within this spatially flat model, regardless of constant \(\Lambda\). A claimed EFMW bounce needs additional degrees of freedom, modified gravity, positive spatial curvature, or explicit violations of at least one assumption; no such mechanism was derived here.
2. **No global preferred rotation from this ansatz:** FLRW imposes exact homogeneity and isotropy. It cannot generate or represent a universal preferred rotation axis; any EFMW anisotropic cosmology requires a different metric and dynamics.

Positive quadratic stability, \(m^2>0,M^2>0,\gamma^2<m^2M^2\), removes tachyonic flat-space scalar modes but does **not** establish full gravitational/quantum stability. Both scalar fields still contribute to stress-energy even when mixing vanishes; \(\gamma=0\) is **not** the full SM+GR theory.

## 5. Reproducibility, comparisons and limitations

The program [toe001/me007.py](toe001/me007.py) implements the selected \(I^{(\alpha)}\) and the flat-FLRW reduction without external runtime dependencies. [tests/test_me007.py](tests/test_me007.py) exercises alternative allocations and κ values (the total gravity source is unchanged), expected sector non-conservation, decoupling, positivity, constraint propagation and fourth-order convergence. The optional independent [symbolic verifier](scripts/check_me007_symbolic.py) uses SymPy, and its JSON output is [results/me007_symbolic_checks.json](results/me007_symbolic_checks.json).

Run:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/check_me007_symbolic.py  # optional: requires sympy
python3 - <<'PY'
from toe001.me007 import simulate_flrw
print(simulate_flrw()['max_relative_friedmann_residual'])
PY
```

**Numerical control:** default dimensionless values \(m^2=1,M^2=4,\gamma=0.25,M_{\rm Pl}^2=1,\Lambda=0,\kappa=1,\alpha=0.5,w=0\), with initial \((\phi,\chi,\dot\phi,\dot\chi,a,\rho_m)=(0.7,-0.3,0.2,-0.1,1,0.2)\), expanding \(H\) from the Friedmann constraint; 2,400 RK4 steps with \(\Delta t=10^{-3}\). The saved [results/me007_flrw_reference.json](results/me007_flrw_reference.json) reports maximum normalized Friedmann constraint residual approximately \(6.61\times 10^{-14}\) and numerical exchange mismatch of order \(10^{-16}\). This is a **self-consistency test of explicitly supplied classical equations**, not empirical corroboration.

**Comparison baselines and counterfactuals:** \(\gamma=0\); alternate \(\alpha\) and \(\kappa\) (same total source by construction); a conventional two-scalar model (identical dynamics); independently specified observational matter couplings (currently absent). The label “information” does not produce a distinctive measurable quantity.

## 6. Closure ledger — what can and cannot be claimed

| Gate | Result | What the result actually means |
|---|---|---|
| Einstein equation can be written in ME-007 form | **PASS (constructed)** | New \(I^{(\alpha)}\) defined as a chosen slice of ordinary scalar stress |
| Total on-shell Bianchi/source consistency | **PASS (conditional)** | Derived for this action, not the historical undefined tensor |
| Individual-sector exchange and FLRW conservation | **PASS (conditional)** | Correct opposing transfer terms; no false assumption of separate conservation |
| Classical numerical/symbolic checks | **PASS** | Local homogeneous model and polynomial identities only |
| Unique original EFMW informational tensor | **UNRESOLVED** | Infinitely many valid splits; needs independent constitutive definition |
| Full 102-equation EFMW compatibility | **UNRESOLVED** | Current model contains only two fields, not the source corpus |
| Curved-space quantum field theory and UV-complete quantum gravity | **UNRESOLVED** | Classical Einstein metric is an assumption |
| Derivation of observed SM fields, chiral content and parameters | **UNRESOLVED** | SM inserted as input |
| New physical prediction beyond conventional two-scalar EFT | **UNRESOLVED** | No independently calibrated observable or portal |
| Independent physical reproduction | **UNRESOLVED** | No external measurements or independent physics review |
| **Theory of Everything closure** | **FAIL AS A CLAIM / NOT DEMONSTRATED** | No theory-wide closure follows from these checks |

**Conclusion:** A careful partial ME-007 *realization* is possible, and its consequences reveal a real obstruction to claiming uniqueness or a new physical law. Neither recursion nor repeated numerical iteration can repair missing observational input or manufacture an independent physical definition for the canonical \(I_{\mu\nu}\). The next rigorous step is to supply that tensor and its observable meaning before asserting that TOE-001 describes EFMW rather than an ordinary two-scalar gravity model.