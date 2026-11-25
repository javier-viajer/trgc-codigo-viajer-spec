"""Audit of explicitly specified strata and rotation; not the full PP model."""
import itertools
import json
import math

N = 24

def rotation(a):
    return tuple((i+6*a)%N for i in range(N))

def compose(p,q):
    return tuple(p[q[i]] for i in range(N))

def cycles(p):
    seen=set(); lengths=[]
    for i in range(N):
        if i in seen: continue
        j=i; n=0
        while j not in seen:
            seen.add(j); n+=1; j=p[j]
        lengths.append(n)
    return sorted(lengths)

def preserves_weights(p,w,m=None):
    return all((w[p[i]]-w[i]) % m == 0 if m else w[p[i]]==w[i] for i in range(N))

def orbit_counts(q):
    if not isinstance(q,int) or q<1: raise ValueError('q must be positive integer')
    a=q**6; b=(q**12-a)//2; c=(q**24-q**12)//4
    return {1:a,2:b,4:c,'total':a+b+c}

def audit():
    group=[rotation(a) for a in range(4)]
    strata=[i%6 for i in range(N)]
    auxiliary=[tuple((sign*i+k)%N for i in range(N)) for sign,k in [(1,0),(1,12),(-1,11),(-1,23)]]
    edges=list(itertools.combinations(range(N),2))
    unseen=set(edges); edge_orbits=[]
    while unseen:
        i,j=min(unseen); orbit={tuple(sorted((p[i],p[j]))) for p in group}
        unseen-=orbit; edge_orbits.append(len(orbit))
    return {'scope':'strata and declared rotation only; no full canonical automorphism claim',
            'rotation_order':len(set(group)), 'composition_verified':all(compose(group[a],group[b])==group[(a+b)%4] for a,b in itertools.product(range(4),repeat=2)),
            'cycle_lengths':[cycles(p) for p in group], 'binary_orbits':orbit_counts(2),
            'strata_preserved':all(preserves_weights(p,strata) for p in group),
            'strata_only_group_order':math.factorial(4)**6,
            'intersection_with_auxiliary_order':len(set(group)&set(auxiliary)),
            'edge_orbits_by_size':{str(k):edge_orbits.count(k) for k in set(edge_orbits)},
            'source':'DOCUMENTO_MAESTRO_PIRAMIDE_PARABOLA.md v1.2.0 sections 1,2,4.4; main branch, commit not pinned'}

if __name__=='__main__': print(json.dumps(audit(),indent=2))
