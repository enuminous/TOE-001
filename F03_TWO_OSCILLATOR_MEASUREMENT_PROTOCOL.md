# F03 — From measured oscillator correlations to a gravitational-information hypothesis: a controlled bridge test

**Matthew Chenoweth Wright / Monolithic LLC; AI-assisted method and code**  
**28 October 2026 · Version 0.1 · SYNTHETIC DYNAMICAL VALIDATION ONLY — NO REAL INSTRUMENT DATA ANALYZED.**

## Abstract

F01 derived the partition-invariant Gaussian mutual information of amplitudes for two coupled equilibrium oscillators. F02 then demonstrated that this *global* statistic cannot in general be substituted unchanged for a dynamical gravitational scalar `q(x)` in a chosen standard scalar–tensor action. F03 develops an end-to-end *measurement pipeline*: instead of sampling directly from the target equilibrium covariance as in F01, it independently generates a stochastic trajectory with an explicit Langevin equation, analyzes time-correlated paired readings, estimates Gaussian mutual information with moving-block uncertainty, checks a time-shifted null, and accepts third-party or laboratory CSV data with separately documented calibration. It recovers the ordinary thermal prediction to within sampling uncertainty under illustrative dynamics. **No observation of informational gravity, novel force, distinctively EFMW physics, or physically identified ME-006 tensor follows.**

## 1. Hypotheses and experimental boundary

**H0, conventional:** Two mass-normalized damped classical oscillators with stiffness matrix `K=[[m²,γ],[γ,M²]]` and an independently calibrated inverse temperature `β` reach the conventional classical Gibbs distribution. Their stationary position mutual information is

\[
\mathcal M_{\rm Gibbs}=-\tfrac12\log(1-\rho^2),\qquad
\rho=-\gamma/\sqrt{m^2M^2};\qquad
m^2M^2>\gamma^2.
\]

This is the **null conventional physical theory**, not an EFMW-specific prediction. 

**H1, prospective EFMW:** A separately derived local information field `q(x)` must have an operational map from experimentally measurable degrees of freedom *and* satisfy the F02 dynamical equation, with a fixed metric coupling that leads to an independently discriminating observation. **No noncircular such map is established in F03. H1 cannot yet be tested here.**

The experiment therefore measures whether a classical dynamics-to-correlation calculation behaves as assumed, not whether information generates gravity. A successful H0 is a control, not a discovery.

## 2. Dynamics chosen independently of the information estimator

Define normalized position and velocity vectors `x=(φ,χ)` and `v=(u,v)`; use unit inertial masses and a fixed harmonic potential,

\[
V(\phi,\chi)=\tfrac12m^2\phi^2+\gamma\phi\chi+\tfrac12M^2\chi^2.
\]

Simulate the **standard underdamped Langevin** equations with independent Wiener processes,

\[
\dot x=v,\qquad
\mathrm dv=-Kx\,\mathrm dt-\zeta v\,\mathrm dt+
\sqrt{2\zeta/\beta}\,\mathrm dW_t.
\]

The noise amplitude follows the conventional fluctuation–dissipation relation, **introduced as an assumption**; no EFMW source law predicts it. We use BAOAB operator splitting, including an exactly integrated velocity Ornstein–Uhlenbeck substep, to generate time-correlated trajectories. Position measurements are optionally contaminated by *independently calibrated*, uncorrelated Gaussian sensor noise, and only those known noise variances are subtracted. Cross-talk, correlated noise and filtering must be measured separately before real-world conclusions.

At stationary equilibrium, independently of the solver,

\[
C=\operatorname{Cov}(\phi,\chi)=\beta^{-1}K^{-1}
=\frac{1}{\beta(m^2M^2-\gamma^2)}
\begin{pmatrix}M^2&-\gamma\\-\gamma&m^2\end{pmatrix}.
\]

Measured paired displacements determine a covariance and thus a **Gaussian-model estimator** of mutual information, `−0.5 log(1−corr²)`. This is the actual MI only if the joint distribution is Gaussian. A non-Gaussian driven or oscillating regime requires a different estimator and an independently derived distribution; a high Gaussian plug-in value alone must not be called information gravity.

**Independent calibration requirement:** Obtain stiffness parameters `(m²,M²,γ)` from known mechanical coupling constants, independently measured normal modes/static-force responses, or electrical circuit element values **before** using the holdout amplitude traces to estimate MI. Deriving `γ` by inverting the *same* observed covariance and then reporting agreement with its formula is circular. Damping, effective temperature and measurement noise also require calibration. The theory and estimator must never share tuned parameters from the evaluation record without disclosure.

## 3. Executed synthetic experiment and controls

The frozen demonstration uses `m²=1, M²=4, γ=0.25, β=1, damping=0.8`, timestep `0.04`, **200,000** BAOAB steps, **20,000** burn-in steps, and every sixth point thereafter: **30,000 correlated paired position samples**. It uses seed `20261028` and a moving-block bootstrap (block length `173`, 120 replicates). This is *not* a laboratory observation.

The independently predicted thermal mutual information is `0.007874178484` nats. The dynamically generated trajectory gives approximately `0.008250895642` nats and a descriptive blocked 95% interval `[0.00604917,0.01077456]`. Signed position correlation is approximately `−0.127931`, close to the analytic `−0.125`. Null time shifts that break simultaneity while preserving each stream's autocorrelation produce a lower descriptive MI distribution, with median approximately `2.36e−5` nats and maximum approximately `4.08e−4` nats across the frozen shift draws. The two halves give `0.0067499` and `0.0098909` nats, a reminder that time-series uncertainty and stationarity assessment are material.

These statistics **do not establish a formal frequentist rejection**, and the bootstrap interval is exploratory: block length has not been validated on actual experimental autocorrelation times. The conventional H0 predicts the observed result; the model contains no extra EFMW force. Earlier F01's i.i.d. generator would not be an independent dynamical simulation, and this experiment specifically avoids that shortcut.

The [frozen reference JSON](results/f03_oscillator_reference.json) saves the source type, seed, run controls, observed and predicted values, null summary, and *fail-closed* physical claim flags. The [Python implementation](toe001/me007_experiment.py), [runner](scripts/run_f03_oscillators.py), and [18 focused tests](tests/test_me007_experiment.py) use only the standard library. The full TOE-001 suite is run in CI.

## 4. Real laboratory data protocol: executable, NOT YET PERFORMED

1. Build or obtain **two physically separate, calibrated** weakly coupled pendulums, flexural resonators, or a low-voltage two-mode electrical analog. Avoid mains/high-voltage apparatus.
2. Independently calibrate inertia, uncoupled stiffness, coupling, damping, sensor transfer functions, sampling clock, noise covariance, and the effective forcing/noise statistics. Keep calibration runs separate from confirmatory amplitude traces.
3. If claiming *thermal* Gibbs statistics, establish stationary stochastic forcing and verify the noise–dissipation relation. For deterministic forced oscillations or driven nonlinear systems, **do not apply the thermal formula without deriving the relevant distribution**.
4. Record paired samples at monotone timestamps in a CSV with headers `time,phi,chi`. Do not independently resample the two streams. Keep the original raw sensor files and hash them.
5. Create `calibration.json` with independently established values. Record date, apparatus, units, firmware, handling of dropped samples, and authorship in a separate lab notebook. `noise_phi/noise_chi` mean independently measured additive *standard deviations* in the same units as position readouts.
6. Apply the predeclared quality screens: calibration stability, Gaussianity of the joint distribution, sensor cross-talk/null, absence of drift, appropriate effective independent sample size, and sensitivity to block length.
7. Compare the holdout inferred MI to the *independently calculated* standard Gibbs prediction and a null coupling trial. Use runs at `γ=0`, both signs of `γ` if practical, multiple coupling strengths, and independently reproduced sessions.
8. For a future *gravitational* interpretation, derive and pre-register `q`'s local measurement map and an observable scalar–tensor gravity difference beyond conventional alternatives. The oscillator experiment alone cannot do it.

From the TOE-001 repository root:

```sh
# Frozen dynamic simulation, generated locally, NOT measured:
python3 scripts/run_f03_oscillators.py

# Optional export of raw *synthetic* records (label retained):
python3 scripts/run_f03_oscillators.py --synthetic-csv /tmp/f03_synthetic.csv

# Independent physical-data analysis (CSV and calibration must be genuine):
python3 scripts/run_f03_oscillators.py \
  --input /path/to/paired_recordings.csv \
  --calibration /path/to/calibration.json \
  --out /path/to/observed_analysis.json
```

**The second command is a data-analysis capability, not a report of real measurements conducted in this session.** The runner records input and calibration SHA-256 and marks file provenance as *user-supplied, not independently authenticated*.

## 5. Physical datasets found but not claimed as confirmation

A real two-resonator measurement collection is available through the 2026 [Ved et al. coupled MEMS acoustic-sensor dataset, Zenodo 18336535](https://zenodo.org/records/18336535). It includes two-channel resonator time series and independent excitation/coupling metadata, but the archive is approximately **35 GB** and contains strongly *driven* sweeps, tunable feedback and nonlinear/bifurcation regimes. Those regimes do **not** satisfy F01's stationary Gibbs assumptions by default. No raw MEMS data were downloaded or analyzed in the present experiment. A later study could preselect a defensible subset and derive an appropriate nonequilibrium prediction, with full source attribution.

[MechanicsDSL's coupled-oscillator data](https://github.com/MechanicsDSL/mechanicsdsl-datasets) provide a smaller *synthetic* inverse-problem regression control, but likewise cannot count as real measurements. [Xu et al.'s Damped Pendulum Dataset](https://github.com/EnzeXu/Damped_Pendulum_Dataset) contains real single-pendulum measurements that can assist with damping/sensor calibration; they are **not** two coupled position channels.

## 6. Interpretation and stop rule

The central F01 partition invariants—total stress and the Gaussian MI under the specified statistical assumptions—remain invariant under arbitrary labels `α` and `κ`, because those bookkeeping parameters do not enter the physical dynamics. A physically measurable MI is not a locally conserved stress tensor, and an arbitrary conversion from nats to joules per volume is insufficient. Nor does this experiment identify the F02 scalar `q`: F02 already demonstrated that assigning it a fixed nonzero F01 ensemble MI generally violates its equation of motion. A genuine constitutive map must be independent of the target gravitational equation and predict an effect inaccessible to a standard oscillator/scalar–tensor explanation.

| Gate | F03 result |
|---|---|
| Independent dynamical generation (not direct equilibrium covariance draws) | **PASS — synthetic** |
| Conventional thermal correlation and MI reproduced | **PASS — within descriptive numerical uncertainty** |
| Correlated-time-series uncertainty and shift-null diagnostics | **IMPLEMENTED; exploratory only** |
| External real laboratory sensor measurements | **UNRESOLVED — not acquired/analyzed** |
| Independent physical ME-006 recursive tensor | **UNRESOLVED** |
| Physical q–MI constitutive relation and gravitational coupling | **UNRESOLVED** |
| Distinctive EFMW prediction vs conventional coupled oscillators | **NOT ESTABLISHED** |

**Verdict:** F03 closes a *reproducible laboratory-analysis protocol and synthetic dynamical check*, not F01/F02's physical-gravity gap. A positive real coupled-oscillator measurement would validate conventional oscillator physics until a separately grounded, quantitatively distinctive information–gravity prediction is available.

### Attribution

This research package is a new reproducibility exercise for the EFMW portfolio. All Gaussian and Langevin laws employed are conventional. No original scientific priority or independent experimental validation is claimed for these established laws. Software developed with AI assistance for the TOE-001 repository. Historical ME-006/007 attribution remains with Wright; third-party datasets remain credited to their original researchers.