Canonical bifurcations
Version 1.0.0. Scope: canonical relational operator only.
Critical locus
Write alpha=(gamma-1)/(gamma+1), h_i=2 gamma log(g_i)/(gamma+1)+alpha log(p_i)+log(1-p_i). Solve h_i=h_m, sum p_i=1, ell_2+alpha=0. The grid contains 12 equally spaced epsilon values from 0.001 to 0.165 and all 182 compositions. Warm starts and finite multistart root searches are not pseudo-arclength continuation. At most one critical root is retained per case.
2184 cases: 2022 located, 162 missing (not proof of absence). Classification: 1120 fold candidates, 758 symmetry candidates, 144 homogeneous multiple points. The original critical search accepts residual <1e-8. Symmetry screening uses repeated same-stratum components within 0.003 of p_c=(gamma-1)/(2 gamma); it is heuristic and followed by refinement.
Simple folds
For Q orthonormal tangent basis, H=Q^T diag(h') Q. For a simple null direction v, A=sum v_i partial_gamma h_i, B=sum h''_i v_i^3. If the complement is invertible and A B !=0, gamma-gamma_c= -B/(2A) s^2+O(s^3). All 1120 candidates have negative estimated ratio. This is a numerical candidate classification, not interval-certified nondegeneracy. Stability of a branch additionally requires stable complementary modes.
Symmetry refinement
578 two-node cases refined with a positive crossing coefficient and positive effective cubic coefficient, negative definite complement; consistent with subcritical pitchforks. 180 three-node blocks on four-node supports were separately refined: all 180 meet numerical hypotheses of the S3 normal form (negative complementary eigenvalue, nonzero crossing, negative quadratic coefficient). Crossing coefficient range 1.2293857049228194 to 18.59805222385123; maximum equilibrium-system residual 5.204170427930421e-16. These are sampled points, not distinct bifurcations.
144 homogeneous points have exact critical multiplicity m-1. See EQUIVARIANT_NORMAL_FORMS.md for analytical branches and stability. The 180 heterogeneous points are now checked numerically, not algebraically certified.
Reproduction
python canonical_stability_audit.py
python canonical_bifurcation_audit.py --stability-input canonical_stability_results.json
Optional --critical-input critical_curves.json reuses an existing critical grid. The consolidated JSON contains stability, critical, cubic and multiple records. The consolidation was executed using the existing critical and stability records; the full grid search was not rerun during consolidation. No global continuation, exhaustive bifurcation count, basin probabilities or hybrid claims.
Governance: Level II retained; Level III open; lambda reserved for Factor 4; Episode 44 unchanged.
