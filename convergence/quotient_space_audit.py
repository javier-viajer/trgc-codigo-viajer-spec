"""Single-edge quotient audit, independent reference operator; not canonical certification."""
import json
import math
from itertools import combinations
from pathlib import Path
import numpy as np

N = 24
SEED = 20261126
TOL = 1e-10
EDGES = list(combinations(range(N), 2))
A, B = np.array(EDGES).T
STRATA = np.arange(N) % 6
G = np.tile(np.arange(1., 7.), 4)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def swap(a, b):
    p = np.arange(N); p[a], p[b] = p[b], p[a]
    return p


def partition(generators):
    unseen = set(EDGES); groups = []
    while unseen:
        e = min(unseen); orbit = {e}; queue = [e]
        while queue:
            a, b = queue.pop()
            for p in generators:
                f = tuple(sorted((int(p[a]), int(p[b]))))
                if f not in orbit:
                    orbit.add(f); queue.append(f)
        unseen -= orbit; groups.append(sorted(orbit))
    return groups


def matrix(x):
    r = np.zeros((N, N)); r[A, B] = r[B, A] = x
    return r


def step(r, weights, gamma=1.2, mu=.2):
    vals, vecs = np.linalg.eigh(r)
    require(vals[-1]-vals[-2] > 1e-12, 'Non-simple dominant eigenvalue')
    u = (weights*np.abs(vecs[:, -1]))**gamma
    m = np.outer(u, u); np.fill_diagonal(m, 0)
    return (1-mu)*r + mu*m*(r[A,B].sum()/m[A,B].sum())


def reconstruct(a, b):
    if not (a > 0 and a*a/2 <= b < a*a):
        raise ValueError('Invalid positive weight pair')
    d = math.sqrt(2*b-a*a)
    return ((a-d)/2, (a+d)/2)


def audit():
    rot = (np.arange(N)+6)%N
    strat = [swap(j+6*k,j+6*(k+1)) for j in range(6) for k in range(3)]
    generators = {'S24':[swap(i,i+1) for i in range(23)], 'Z4':[rot],
                  'Z2':[(np.arange(N)+12)%N], 'stratified':strat}
    expected = {'S24':1,'Z4':72,'Z2':144,'stratified':21}
    partitions = {k:partition(v) for k,v in generators.items()}
    counts = {}; distances = {}; apex = {}
    for k, groups in partitions.items():
        require(len(groups)==expected[k], k+' orbit count')
        require(sum(map(len,groups))==276, k+' coverage')
        counts[k] = {str(s):sum(len(o)==s for o in groups) for s in sorted(set(map(len,groups)))}
        labels = {e:i for i,o in enumerate(groups) for e in o}
        # Exact minimization over the complete generated orbit of each edge.
        # Unit mass basis vectors have squared distance 0 or 2.
        checks = 0
        for e in EDGES:
            for o in groups:
                d2 = min(0 if e==f else 2 for f in o)
                require(d2==(0 if labels[e]==labels[o[0]] else 2), 'Quotient metric')
                checks += 1
        distances[k] = {'checks':checks,'distinct_class_distance':math.sqrt(2) if len(groups)>1 else None}
        if k!='S24':
            require(all(len({sum(STRATA[i]==5 for i in e) for e in o})==1 for o in groups),'Apical invariance')
            apex[k] = {str(n):sum(sum(STRATA[i]==5 for i in o[0])==n for o in groups) for n in range(3)}
    require(apex['stratified']=={'0':15,'1':5,'2':1},'Apical classes')
    require(counts['Z4']=={'2':6,'4':66},'Rotation orbit sizes')
    require(counts['stratified']=={'6':6,'16':15},'Stratified orbit sizes')
    fixed_counts=[sum(tuple(sorted(((a+6*k)%N,(b+6*k)%N)))==(a,b) for a,b in EDGES) for k in range(4)]
    require(fixed_counts==[276,0,12,0],'Burnside')
    W=np.diag(G); signatures={}; spectral_error=0.; fixed_error=0.; reconstruction_error=0.
    for j,e in enumerate(EDGES):
        x=np.zeros(276); x[j]=1.; r=matrix(x); r2=r@r
        signature=(float(np.trace(W@r2)),float(np.trace(W@W@r2)))
        pair=tuple(sorted(G[list(e)])); recovered=reconstruct(*signature)
        reconstruction_error=max(reconstruction_error,max(abs(a-b) for a,b in zip(pair,recovered)))
        signatures.setdefault(signature,set()).add(pair)
        spectral_error=max(spectral_error,float(np.max(np.abs(np.linalg.eigvalsh(r)-np.array([-1]+[0]*22+[1])))))
        fixed_error=max(fixed_error,float(np.max(np.abs(step(r,G)-r))))
    require(len(signatures)==21 and all(len(v)==1 for v in signatures.values()),'Complete signatures')
    require(max(spectral_error,fixed_error,reconstruction_error)<TOL,'Edge checks')
    # Repeated weights merge distinct stratum pairs; rotations cannot recover angular orientation.
    require((G[0]+G[1],G[0]**2+G[1]**2)==(G[0]+G[7],G[0]**2+G[7]**2),'Rotation collision')
    require(not any((0,1) in o and (0,7) in o for o in partitions['Z4']),'Distinct rotation classes')
    repeated=G.copy(); repeated[STRATA==1]=1
    require(repeated[0]==repeated[1] and STRATA[0]!=STRATA[1],'Repeated weight collision')
    for a,b in [(0,0),(2,1),(2,4),(2,5)]:
        try: reconstruct(a,b)
        except ValueError: pass
        else: raise AssertionError('Invalid reconstruction accepted')
    rng=np.random.default_rng(SEED); max_errors={'Z4':0.,'Z2':0.,'stratified':0.}; negative=[]; mass_error=0.
    broken=G.copy(); broken[0]*=2
    for _ in range(32):
        x=rng.uniform(.1,1.,276); r=matrix(x/x.sum()); f=step(r,G)
        mass_error=max(mass_error,abs(float(f[A,B].sum())-1))
        for k in max_errors:
            for p in generators[k]:
                lhs=step(r[np.ix_(p,p)],G); rhs=f[np.ix_(p,p)]
                max_errors[k]=max(max_errors[k],float(np.linalg.norm(lhs-rhs)/np.linalg.norm(rhs)))
        lhs=step(r[np.ix_(rot,rot)],broken); rhs=step(r,broken)[np.ix_(rot,rot)]
        negative.append(float(np.linalg.norm(lhs-rhs)/np.linalg.norm(rhs)))
    require(max(max_errors.values())<TOL and mass_error<TOL,'Equivariance or mass')
    require(min(negative)>TOL,'Broken-weight control')
    # Distinct fixed classes retain their exact quotient distance.
    ratios={}
    for k in ('Z4','Z2','stratified'):
        e,f=(o[0] for o in partitions[k][:2]); x=np.zeros(276); y=x.copy()
        x[EDGES.index(e)]=1; y[EDGES.index(f)]=1
        require(np.max(np.abs(step(matrix(x),G)-matrix(x)))<TOL,'Fixed representative')
        require(np.max(np.abs(step(matrix(y),G)-matrix(y)))<TOL,'Fixed representative')
        ratios[k]=1.0 # exact analytical ratio, using verified fixed classes
    return {'status':'PASS','scope':'single-edge family; independent formula; unit edge mass; illustrative distinct weights',
            'seed':SEED,'tolerance':TOL,'numpy_version':np.__version__,'weights':G.tolist(),
            'edge_count':276,'orbit_counts':{k:len(v) for k,v in partitions.items()},'orbit_sizes':counts,
            'burnside_fixed_edges_Z4':fixed_counts,'apical_edges':{'0':190,'1':80,'2':6},'apical_classes':apex,
            'quotient_metric':distances,'spectral_error_max':spectral_error,'fixed_error_max':fixed_error,
            'signature_count':len(signatures),'reconstruction_error_max':reconstruction_error,
            'negative_controls':{'repeated_weights':'PASS','rotation_collision':'PASS','invalid_pairs':'PASS','broken_weight_error_min':min(negative)},
            'equivariance_samples':32,'equivariance_error_max':max_errors,'mass_error_max':mass_error,
            'fixed_class_distance_ratio_analytic':ratios,'canonical_certification':False,'episode_44_modified':False,
            'limitations':['No general stratified metric solver for dense matrices','No basin estimates','No canonical upstream commit verified','No hybrid or 44A/44B tests'],
            'governance':'Level II retained; Level III open; lambda reserved for fourth factor'}


if __name__=='__main__':
    result=audit(); data=json.dumps(result,indent=2,allow_nan=False,default=lambda v: v.item() if isinstance(v,np.generic) else (_ for _ in ()).throw(TypeError(type(v).__name__)))+'\n'
    Path(__file__).with_name('quotient_space_results.json').write_text(data,encoding='utf-8')
    print(data)
