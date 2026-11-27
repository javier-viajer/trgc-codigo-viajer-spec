Equivariant normal forms
Version 1.0.0 — analytical local results with explicit hypotheses.
Setup
Use the equilibrium functions h_i from CANONICAL_BIFURCATIONS.md. On a fixed positive support the equations are smooth. Let r equivalent nodes share p_c=(gamma_c-1)/(2 gamma_c). Assume the critical kernel is exactly E_r={x: sum x_i=0} on that block, the complementary tangent Hessian is invertible, and the symmetric branch crosses transversely (a !=0). For stability statements use the spectral criterion in CANONICAL_STABILITY_MAP.md. No smooth second derivative across a support boundary is assumed.
h'=alpha/p-1/(1-p), h''=-alpha/p^2-1/(1-p)^2, h'''=2alpha/p^3-2/(1-p)^3. Let Pi_r project onto E_r. The reduced equilibrium equation has leading terms a tau x+c Pi_r(x^2), c=h''(p_c)/2<0, tau=gamma-gamma_c. Higher terms include cubic equivariants and parameter corrections.
S2
For unit v=(e_a-e_b)/sqrt(2), let W span the noncritical tangent complement, L=W^T diag(h') W. The symmetric branch derivative is z=-W L^-1 W^T partial_gamma h. Define w=-W L^-1 W^T(h'' v^2), a=sum v_i^2(partial_gamma h'_i+h''_i z_i), b=sum h'''_i v_i^4/6+sum h''_i v_i^2 w_i/2. Reduced equation 0=s(a tau+b s^2+...). If a,b>0 and L negative definite, the pitchfork is subcritical and nearby broken branches unstable. Numerical evidence: 578 refined cases satisfy these signs.
S3
x=(2s,-s,-s) and permutations. Pi_3(x^2)=s x. Branch s=-a tau/c+O(tau^2). Reduced eigenvalues cs and -3cs to leading order: opposite signs, hence dynamically unstable. Applies to homogeneous triangles and the 180 refined heterogeneous three-node critical blocks under the stated hypotheses.
S4
1+3: x=(3s,-s,-s,-s), Pi_4(x^2)=2s x. Branch s=-a tau/(2c)+O(tau^2). Reduced eigenvalues 2cs,-4cs,-4cs to leading order: unstable.
2+2: x=(s,s,-s,-s), Pi_4(x^2)=0. Internal splitting eigenvalues +/-2cs+O(s^2) imply instability for nonzero small s. For homogeneous m=4, no internal noncritical complement, a=8/9, c=-32/9, d=h'''/6=512/81. Thus s^2=(9/64)(2-gamma)+O((2-gamma)^2), subcritical.
Homogeneous controls
For m homogeneous nodes, gamma_c=m/(m-2), a=2m/(gamma_c+1)^2, c=-m^3/[2(m-1)^2], d=m^4(m-2)/[3(m-1)^3]. For m=3: a=3/8,c=-27/8,d=27/8. For m=4: values above. Multiplicity m-1.
General two-group result
For multiplicities k,r-k and values u,v with ku+(r-k)v=0, the leading relation is a tau=-c(u+v). Internal eigenvalues c(u-v),c(v-u) have multiplicities k-1,r-k-1; the unbalanced radial eigenvalue is c(u+v). For r>=3, either both internal modes exist with opposite signs, or the radial mode and the larger group's internal mode have opposite signs. Balanced groups have both internal modes. Hence these local branches are unstable. This is not a claim about all global branches or arbitrary larger critical kernels.
At fixed gamma>1 the scalar equilibrium function is strictly concave in p, so within a common-weight block there are at most two distinct component values. This supports the two-group classification locally for the specified kernel. No global attractor selection follows.
Governance: Level II retained; Level III open; lambda reserved for Factor 4; Episode 44 unchanged.
