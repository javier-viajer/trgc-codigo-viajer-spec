# CANONICAL REPRODUCIBILITY

Version: 1.0.0
Date: 2026-11-27
Status: Computational reproduction documented.

---

## 1. Purpose

This document records the computational reproduction of the canonical stability and equivariant bifurcation campaigns of the Pyramid-Parabola relational operator.

Its purpose is to establish the reproducibility of the reported numerical results using the published audit algorithms, without modifying their mathematical definitions, parameters or acceptance tolerances.

Computational reproducibility does not constitute exhaustive mathematical certification.

## 2. Repository Reference

Repository:

https://github.com/javier-viajer/trgc-codigo-viajer-spec

Audited commit:

6d8a99c74f45a6518cd892d6b633ca8362e853df

Directory:

convergence/

The audited commit provides a fixed reference for subsequent comparisons and independent reproduction attempts.

## 3. Audited Programs

### 3.1. Stability audit

File:

canonical_stability_audit.py

Git blob SHA:

c1e9e2a4aaeea1ff4652d886ce55124abe9065c6

### 3.2. Bifurcation audit

File:

canonical_bifurcation_audit.py

Git blob SHA:

02d67cdb40638d5504457dfd5a63a880a34aff12

No algorithmic modifications were reported during the reproduction.

## 4. Computational Environment

Reported reproduction environment:

- Python: 3.13.5.
- NumPy: 2.3.5.
- SciPy: 1.17.0.

These versions provide a reference environment.

Exact byte-level reproducibility across different software versions, numerical libraries and hardware architectures is not guaranteed.

## 5. Reproduction Procedure

From the convergence directory:

```bash
python canonical_stability_audit.py
```

The first program generates:

canonical_stability_results.json

The second program can be executed using:

```bash
python canonical_bifurcation_audit.py \
  --stability-input canonical_stability_results.json \
  --output canonical_bifurcation_results_full.json
```

The explicit output argument prevents accidental replacement of the consolidated summary stored in the repository.

The complete critical search must be executed without supplying a previously generated critical-input file when reproducing the campaign from scratch.

## 6. Preserved Campaign Parameters

The reproduction retains:

- 24 canonical nodes.
- Six strata.
- Four nodes per stratum.
- 56 triangular compositions.
- 126 four-node compositions.
- 182 total stratified compositions.
- Fixed undirected relational mass C0 = 1.
- Update parameter mu = 0.2.

The stability campaign uses:

- Epsilon: 0.05 and 0.15.
- Gamma: 1.5 and 2.5.

The critical campaign uses 12 equally spaced epsilon values between 0.001 and 0.165.

## 7. Stability Campaign Results

| Quantity | Reported | Reproduced |
|---|---:|---:|
| Parameter-composition cases | 728 | 728 |
| Located equilibria | 3278 | 3278 |
| Stable equilibria | 145 | 145 |
| Unstable equilibria | 3133 | 3133 |

Detailed classification:

| Support | Epsilon | Gamma | Stable | Unstable |
|---|---:|---:|---:|---:|
| 3 | 0.05 | 1.5 | 56 | 168 |
| 3 | 0.05 | 2.5 | 6 | 118 |
| 3 | 0.15 | 1.5 | 20 | 132 |
| 3 | 0.15 | 2.5 | 6 | 118 |
| 4 | 0.05 | 1.5 | 46 | 1150 |
| 4 | 0.05 | 2.5 | 0 | 422 |
| 4 | 0.15 | 1.5 | 11 | 605 |
| 4 | 0.15 | 2.5 | 0 | 420 |
| Total | | | 145 | 3133 |

Maximum matrix equilibrium residual:

4.718447854656915e-14

The accumulated equilibrium counts refer to different parameter-composition cases and must not be interpreted as simultaneous attractor counts.

## 8. Critical Campaign Results

| Quantity | Reported | Reproduced |
|---|---:|---:|
| Total examined cases | 2184 | 2184 |
| Located critical points | 2022 | 2022 |
| Missing critical points | 162 | 162 |

Classification:

| Critical family | Count |
|---|---:|
| Fold candidates | 1120 |
| Simple symmetry candidates | 578 |
| Heterogeneous multiple candidates | 180 |
| Homogeneous multiple points | 144 |
| Total located | 2022 |

Maximum critical equation residual:

9.715907189900008e-9

Missing numerical roots remain unresolved cases.

They do not establish mathematical nonexistence.

## 9. Cubic and Multiple-Point Results

The regenerated numerical artifact contains:

- 578 subcritical pitchfork classifications.
- 180 heterogeneous multiple candidates.
- 180 multiple candidates satisfying the numerical normal-form hypothesis checks.

Maximum multiple-point refinement residual:

5.204170427930421e-16

The numerical classifications remain conditional on the corresponding local reduction hypotheses and numerical acceptance criteria.

No interval-certified bifurcation classification is claimed.

## 10. Artifact Integrity

### 10.1. Complete bifurcation artifact

Original output filename:

canonical_bifurcation_results.json

Artifact size:

2874010 bytes

SHA-256:

607b6f246d18529fe847d112fdb063b9bca975e488385e595c745971db91386f

### 10.2. Intermediate stability artifact

Filename:

canonical_stability_results.json

Artifact size:

623610 bytes

SHA-256:

7e399f265e2972f79ba818517fd2b9eea56b1038daa92eb7bab1dec1c379266d

The SHA-256 values identify the retained complete reproduction artifacts.

The previous reproduction report records byte-for-byte agreement between the original complete bifurcation artifact and the regenerated artifact.

The retained reproduction artifacts have been inspected again during preparation of this document, confirming their hashes, aggregate counts and maximum residuals.

## 11. Repository Summary Distinction

The repository currently contains a compact summary under the filename:

canonical_bifurcation_results.json

This summary is not the complete numerical artifact.

Its SHA-256 is therefore not expected to match the complete artifact hash recorded in Section 10.

The reproduction scripts generate individual numerical records that are omitted from the repository summary.

Preserving the complete artifacts separately is recommended.

## 12. Reproducibility Classification

| Verification component | Status |
|---|---|
| Published program identification | Recorded |
| Same-algorithm reproduction | Reported successful |
| Retained artifact integrity | Verified |
| Stability aggregate counts | Verified from retained artifact |
| Critical aggregate counts | Verified from retained artifact |
| Cubic classification counts | Verified from retained artifact |
| Multiple-point counts | Verified from retained artifact |
| Maximum numerical residuals | Verified from retained artifact |
| Original-versus-regenerated byte identity | Previously reported |
| Independent alternative algorithm | Pending |
| Cross-platform reproducibility | Pending |
| Exhaustive root certification | Pending |
| Global branch continuation | Pending |
| Global basin classification | Pending |

## 13. Scientific Interpretation

The retained numerical artifacts support the reported computational consistency of the canonical stability and bifurcation campaigns.

This strengthens the reproducibility framework of the project.

However, agreement between executions of the same algorithms cannot exclude systematic errors shared by those algorithms.

The numerical campaigns do not establish:

- Exhaustive enumeration of equilibria.
- Exhaustive classification of bifurcations.
- Global branch connectivity.
- Global attraction basin boundaries.
- Universal apical attraction.
- Global strict contractivity.
- Equivalence with TRGC.
- Validation of the hybrid operator.

## 14. Next Verification Objectives

The next research phase should address:

1. Independent equilibrium search algorithms.
2. Independent Jacobian and spectral verification.
3. Pseudo-arclength continuation.
4. Detection of additional critical branches.
5. Interval-certified root searches.
6. Global attraction basin classification.
7. Symmetry-induced basin correspondence.
8. Independent TRGC operator comparison.

## 15. Related Documents

- CANONICAL_STABILITY_MAP.md
- CANONICAL_BIFURCATIONS.md
- EQUIVARIANT_NORMAL_FORMS.md
- HIGHER_SUPPORT_EQUILIBRIA.md
- REDUCED_SUPPORT_STABILITY.md
- CANONICAL_OPERATOR_CORRESPONDENCE.md
- RELATIONAL_QUOTIENT_METRIC.md
- EQUILIBRIUM_CLASSIFICATION.md
- canonical_reproducibility_results.json
- README.md

## 16. Governance

The established governance framework remains unchanged:

- Level II retained.
- Level III open.
- No automatic promotion.
- Lambda reserved exclusively for the Fourth Factor.
- Versions v1.6 and v1.7 remain isolated.
- No post hoc rescaling.
- Episode 44 remains frozen.
- No automatic hybrid operator validation.
- No automatic equivalence between TRGC and Codigo Viajer.

Computational reproducibility strengthens the evidence.

Only mathematical demonstrations can establish equivalence.

---

TRCG — CODIGO VIAJER — PYRAMID-PARABOLA

END OF DOCUMENT
