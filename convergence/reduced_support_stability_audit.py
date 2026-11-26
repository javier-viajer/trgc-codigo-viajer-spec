"""Independent audit of the stated relational formula, not the hybrid system."""
import json
from itertools import combinations
from pathlib import Path
import numpy as np

N=24
A,B=np.triu_indices(N,1)
# Illustrative heights, not certified canonical parameters.
G=(1-np.tile(np.arange(6)*0.1,4))**(-0.5)

def step(x,gamma,mu):
    r=np.zeros((N,N)); r[A,B]=x; r[B,A]=x
    _,v=np.linalg.eigh(r)
    u=(G*np.abs(v[:,-1]))**gamma
    y=u[A]*u[B]; y/=y.sum()
    return (1-mu)*x+mu*y

def audit():
    rows=[]; tol=1e-10; eps=1e-8
    for gamma in (0.8,1.,1.2,2.):
        for mu in (0.2,1.):
            fixed=[]; ratios=[]; errors=[]; mass=[]; positive=[]
            for j,(a,b) in enumerate(zip(A,B)):
                x=np.zeros(len(A)); x[j]=1
                fixed.append(float(np.linalg.norm(step(x,gamma,mu)-x,1)))
                k=next(k for k in np.argsort(-G) if k not in (a,b))
                mask=((A==min(a,k))&(B==max(a,k)))|((A==min(b,k))&(B==max(b,k)))
                p=x*(1-eps); p[mask]=eps/2
                y=step(p,gamma,mu); ratio=float(y[np.arange(len(A))!=j].sum()/eps)
                ratios.append(ratio); mass.append(abs(float(y.sum())-1))
                if gamma==1:
                    errors.append(abs(ratio-(1-mu+mu*G[k]*(1/G[a]+1/G[b]))))
                if gamma>1:
                    errors.append(abs(ratio-(1-mu)))
                    q=x*(1-eps)+eps/len(A)
                    for _ in range(12): q=step(q,gamma,mu)
                    positive.append(float(q[np.arange(len(A))!=j].sum()))
            passed=max(fixed)<tol and max(mass)<tol and (min(ratios)>1 if gamma<=1 else max(ratios)<1 and max(positive)<eps)
            if gamma==1: passed=passed and max(errors)<1e-5
            rows.append(dict(gamma=gamma,mu=mu,edges=len(A),fixed_error_max=max(fixed),mass_error_max=max(mass),ratio_min=min(ratios),ratio_max=max(ratios),linear_prediction_error_max=max(errors) if errors else None,positive_trajectory_final_outside_mass_max=max(positive) if positive else None,passed=bool(passed)))
    return dict(scope='Independent formula; illustrative heights; unit edge mass',numpy_version=np.__version__,weights=G.tolist(),epsilon=eps,tolerance=tol,positive_trajectory_steps=12,rows=rows,all_passed=all(r['passed'] for r in rows))

if __name__=='__main__':
    result=audit(); path=Path(__file__).with_name('reduced_support_stability_results.json'); path.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n'); print(json.dumps(result,indent=2)); assert result['all_passed']
