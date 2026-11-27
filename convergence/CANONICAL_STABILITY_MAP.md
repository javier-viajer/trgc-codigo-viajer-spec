Canonical stability map
Version: 1.0.0 — exploratory numerical evidence and analytical results.
Scope
24 nodes, six strata of four nodes, canonical weights g_j=(1-j epsilon)^(-1/2), 0<epsilon<1/6. The operator is Phi(R)=(1-mu)R+mu N(M), M_ij=(g_i v_i g_j v_j)^gamma off diagonal, zero diagonal, v the nonnegative unit Perron vector and N preserving undirected mass C0. The source correspondence is conditional on the operator in CANONICAL_OPERATOR_CORRESPONDENCE.md; upstream commit not pinned. No hybrid or Episode 44 claim.
Reduction
For a positive active support of size m, p_i>0, sum p_i=1, the equilibrium equations are
$$g_i^{2\gamma/(\gamma+1)}p_i^{(\gamma-1)/(\gamma+1)}(1-p_i)=K.$$
Reconstruct b_i=sqrt(p_i/(1-p_i)), R_ij=C0 b_i b_j/sum_{k<l} b_k b_l. The matrix A=bb^T-diag(b_i^2) has largest eigenvalue 1. For its second eigenvalue ell_2, strict stability for gamma>1 and 0<mu<=1 is equivalent to ell_2<-(gamma-1)/(gamma+1); strict reverse implies instability. Remaining external modes have multiplier 1-mu. Equality requires nonlinear analysis.
Sampled campaign
56 triangular and 126 four-node stratum multisets; epsilon in {0.05,0.15}, gamma in {1.5,2.5}, mu=0.2, C0=1. Roots are labelled within each representative support, not quotient orbit counts. The branch inversion scan uses 48 bisection iterations, a finite K grid and sign-change bracketing, rejects p_i<1e-8, deduplicates at 1e-7, and accepts matrix residual <=1e-8. Tangencies and small roots can be missed.
m
epsilon
gamma
stable
unstable
3
0.05
1.5
56
168
3
0.05
2.5
6
118
3
0.15
1.5
20
132
3
0.15
2.5
6
118
4
0.05
1.5
46
1150
4
0.05
2.5
0
422
4
0.15
1.5
11
605
4
0.15
2.5
0
420
728 cases; 3278 roots, 145 stable, 3133 unstable. Maximum matrix residual 4.718447854656915e-14. Corrects the earlier aggregate 3298/3153. These are counts across different parameter settings, not simultaneous attractors.
Exact controls
Homogeneous support m>=3 has threshold gamma=m/(m-2); for 1<gamma below threshold it is locally stable. All 276 single edges are stable for gamma>1. Consequently at least 306 stable equilibria for 1<gamma<2, 300 for 2<gamma<3, 276 for gamma>3. No global apical attraction follows. At gamma=1 full support exists iff g_min sum_i 1/g_i>m-1; for one lower stratum a and m-1 upper b this is epsilon<(2m-3)/(b(m-1)^2-a(m-2)^2).
Reproduction
Run python canonical_stability_audit.py (NumPy, SciPy). The generated stability JSON is an intermediate input to the integrated bifurcation audit. The consolidated JSON includes the original stability records. No exhaustive root certification or basin estimation.
Governance: Level II retained; Level III open; lambda reserved for Factor 4; v1.6/v1.7 isolated; no post hoc rescaling; Episode 44 unchanged.
