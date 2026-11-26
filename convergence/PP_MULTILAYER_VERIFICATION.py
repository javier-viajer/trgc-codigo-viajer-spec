"""Independent verification of the partial PP multilayer model.
Run: python PP_MULTILAYER_VERIFICATION.py --output pp_verification.json
Requires Python 3.9+ and NumPy. No canonical hybrid operator is assumed.
"""
import argparse
import json
from pathlib import Path
import numpy as np

N = 24

def require(condition, message):
    if not condition:
        raise AssertionError(message)

def edges(step):
    return {tuple(sorted((i, (i + step) % N))) for i in range(N)}

def transform(E, p):
    return {tuple(sorted((p[i], p[j]))) for i, j in E}

def matrix(E):
    A = np.zeros((N, N), dtype=np.int64)
    for i, j in E:
        A[i, j] = A[j, i] = 1
    return A

def orbits(group):
    return sorted({tuple(sorted({p[i] for p in group})) for i in range(N)})

def compose(p, q):
    return tuple(p[q[i]] for i in range(N))

def check_group(group):
    S = set(group)
    require(tuple(range(N)) in S, 'Identity missing')
    require(all(sorted(p) == list(range(N)) for p in S), 'Invalid permutation')
    require(all(compose(p,q) in S for p in S for q in S), 'Closure failed')

def canonical(x, group):
    return min(tuple(x[i] for i in np.argsort(p)) for p in group)

def check_equivariance(F, states, group, action, atol=1e-12):
    """Test a supplied deterministic operator and explicit state action.
    F and action must be pure functions; action(p, x) returns numeric state.
    This finite test is not a proof of universal equivariance.
    """
    errors = []
    for x in states:
        for p in group:
            lhs = np.asarray(F(action(p, x)), dtype=float)
            rhs = np.asarray(action(p, F(x)), dtype=float)
            require(lhs.shape == rhs.shape and lhs.size > 0, 'Invalid output shape')
            require(np.isfinite(lhs).all() and np.isfinite(rhs).all(), 'Nonfinite output')
            errors.append(float(np.max(np.abs(lhs-rhs))))
    require(bool(errors), 'No equivariance cases supplied')
    return {'cases': len(errors), 'max_error': max(errors), 'passed': all(e <= atol for e in errors), 'atol': atol}

def verify():
    layers = [edges(1), edges(8), edges(6), {tuple(sorted((i,23-i))) for i in range(N)}]
    D = [tuple((a+e*i)%N for i in range(N)) for e in (1,-1) for a in range(N)]
    require(len(set(D)) == 48, 'Dihedral enumeration failed')
    groups = [ [p for p in D if all(transform(E,p)==E for E in layers[:k])] for k in range(1,5)]
    G = groups[-1]
    H = [p for p in G if all(p[i]%6 == i%6 for i in range(N))]
    require([len(g) for g in groups]+[len(H)] == [48,48,48,4,2], 'Unexpected group orders')
    r = tuple((i+12)%N for i in range(N))
    require(set(H)=={tuple(range(N)),r}, 'Unexpected stratified group')
    for g in (D,G,H): check_group(g)
    require(all(len(o)==4 for o in orbits(G)) and len(orbits(G))==6, 'Klein orbits')
    require(all(len(o)==2 for o in orbits(H)) and len(orbits(H))==12, 'Stratified orbits')
    A = [matrix(E) for E in layers]
    require([len(E) for E in layers]==[24,24,24,12], 'Edge counts')
    require(all(np.array_equal(a,a.T) and not np.diag(a).any() for a in A), 'Matrix structure')
    gram = [[int(np.trace(a@b)) for b in A] for a in A]
    require(gram==[[48,0,0,4],[0,48,0,0],[0,0,48,0],[4,0,0,24]], 'Gram matrix')
    det = gram[1][1]*gram[2][2]*(gram[0][0]*gram[3][3]-gram[0][3]*gram[3][0])
    require(det==2617344, 'Gram determinant')
    expected = [sorted(2*np.cos(2*np.pi*np.arange(N)/N)), [-1]*16+[2]*8, [-2]*6+[0]*12+[2]*6, [-1]*12+[1]*12]
    errors = [float(np.max(np.abs(np.linalg.eigvalsh(a)-b))) for a,b in zip(A,expected)]
    require(max(errors)<1e-12, 'Spectrum mismatch')
    rotations = []
    # Illustrative integer weights constant within each stratum; not canonical weights.
    w = np.arange(N)%6+1
    x = np.arange(N)**2
    for a in (0,6,12,18):
        p = tuple((i+a)%N for i in range(N))
        modular = all(w[p[i]]==w[i] for i in range(N))
        require(modular, 'Stratified weights not invariant')
        rotations.append({'degrees': a*15, 'all_four_layers': p in G, 'strata': all(p[i]%6==i%6 for i in range(N)), 'stratified_weights_invariant': modular})
    require([v['all_four_layers'] for v in rotations]==[True,False,True,False], 'Rotation mismatch')
    rng = np.random.default_rng(42)
    for _ in range(100):
        x = rng.integers(0, 2, N)
        require(all(canonical(x,H)==canonical(x[np.argsort(p)],H) for p in H), 'Canonical representative')
    def cycles(p):
        unseen = set(range(N)); count = 0
        while unseen:
            i = min(unseen); count += 1
            while i in unseen:
                unseen.remove(i); i = p[i]
        return count
    def burnside(g,q):
        total = sum(q**cycles(p) for p in g)
        require(total%len(g)==0, 'Nonintegral Burnside count')
        return total//len(g)
    require(burnside(G,2)==4197376 and burnside(H,2)==8390656, 'Burnside counts')
    return {'status':'PASS', 'scope':'partial four-layer model, fixed strata', 'group_orders':[len(g) for g in groups]+[len(H)], 'rotations':rotations, 'gram':gram, 'gram_determinant':det, 'gram_rank':4, 'spectral_max_errors':errors, 'orbits_klein':orbits(G), 'orbits_stratified':orbits(H), 'binary_orbits_klein':burnside(G,2), 'binary_orbits_stratified':burnside(H,2), 'canonical_trials':100, 'seed':42, 'canonical_full_architecture':'NOT VERIFIED', 'hybrid_equivariance':'NOT TESTED', '44A_44B':'NOT TESTED', 'governance':'Level II retained; Level III open; lambda reserved for fourth factor'}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = json.dumps(verify(), indent=2, allow_nan=False)
    if args.output:
        args.output.write_text(result+'\n', encoding='utf-8')
    print(result)
