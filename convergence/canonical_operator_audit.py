"""Formula correspondence audit; not certification of upstream code."""
import json
from pathlib import Path
import numpy as np

SEED = 20261125
TOL = 1e-10
N = 24

def mass(r):
    return float(np.triu(r, 1).sum())

def perron(r):
    return np.abs(np.linalg.eigh(r)[1][:, -1])

def canonical(r, g, gamma, mu, c0):
    v = perron(r)
    b = np.outer(g*v, g*v)**gamma
    np.fill_diagonal(b, 0)
    return (1-mu)*r + mu*b*(c0/mass(b))

def reference(r, w, gamma, mu):
    u = w*perron(r)**gamma
    b = np.outer(u, u)
    np.fill_diagonal(b, 0)
    return (1-mu)*r + mu*b*(mass(r)/mass(b))

def error(a,b):
    return float(np.linalg.norm(a-b)/np.linalg.norm(b))

def run():
    rng = np.random.default_rng(SEED)
    p = (np.arange(N)+6)%N
    generators = []
    for j in range(6):
        for s in range(3):
            q = np.arange(N)
            a,b = j+6*s,j+6*(s+1)
            q[a],q[b] = q[b],q[a]
            generators.append(q)
    maxima = dict(correspondence=0., rotation=0., stratified=0., mass=0.)
    count=0
    negative=[]
    for ratio in (.01,.05,.10,.15):
        # Illustrative height convention, not a verified upstream indexing.
        z_over_h = np.tile(np.arange(6)*ratio,4)
        g = (1-z_over_h)**(-.5)
        for gamma in (.8,12/11,1.2,2.,3.):
            for mu in (0.,.2,1.):
                for _ in range(8):
                    a=rng.uniform(.1,1.,(N,N)); r=(a+a.T)/2
                    np.fill_diagonal(r,0); r/=mass(r)
                    f=canonical(r,g,gamma,mu,1.)
                    values=dict(correspondence=error(f,reference(r,g**gamma,gamma,mu)), rotation=error(canonical(r[np.ix_(p,p)],g,gamma,mu,1.),f[np.ix_(p,p)]), mass=abs(mass(f)-1), stratified=max(error(canonical(r[np.ix_(q,q)],g,gamma,mu,1.),f[np.ix_(q,q)]) for q in generators))
                    for k,v in values.items(): maxima[k]=max(maxima[k],v)
                    if mu>0:
                        q=np.arange(N); q[0],q[1]=q[1],q[0]
                        negative.append(error(canonical(r[np.ix_(q,q)],g,gamma,mu,1.),f[np.ix_(q,q)]))
                    count+=1
    passed=all(v<=TOL for v in maxima.values()) and min(negative)>TOL
    return dict(version='0.1.0',status='formula_audit_only',upstream_commit=None,seed=SEED,tolerance=TOL,comparisons=count,height_convention='z/H = j*ratio, j=0..5, illustrative',ratios=[.01,.05,.1,.15],gamma=[.8,12/11,1.2,2,3],mu=[0,.2,1],samples_per_combination=8,numpy_version=np.__version__,max_errors=maxima,negative_control_min=min(negative),passed=passed,episode_44_modified=False,level_II='retained',level_III='open',lambda_status='reserved_fourth_factor')

if __name__=='__main__':
    result=run()
    output=json.dumps(result,indent=2,allow_nan=False)
    Path(__file__).with_name('canonical_operator_results.json').write_text(output+'\n',encoding='utf-8')
    print(output)
    raise SystemExit(0 if result['passed'] else 1)
