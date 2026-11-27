import numpy as np,json
from itertools import combinations_with_replacement,product
from scipy.optimize import brentq
from pathlib import Path

def scan(js,e,t):
 g=(1-e*np.array(js))**-.5;a=(t-1)/(t+1);c=a/(1+a);w=g**(2*t/(t+1));km=min(w)*c**a*(1-c)
 def at(k):
  target=np.asarray(k)[...,None]*km/w;lo=np.zeros_like(target);hi=np.full_like(target,c)
  for _ in range(48):
   mid=(lo+hi)/2;mask=mid**a*(1-mid)<target;lo=np.where(mask,mid,lo);hi=np.where(mask,hi,mid)
  low=(lo+hi)/2;lo=np.full_like(target,c);hi=np.ones_like(target)
  for _ in range(48):
   mid=(lo+hi)/2;mask=mid**a*(1-mid)>target;lo=np.where(mask,mid,lo);hi=np.where(mask,hi,mid)
  return np.stack([low,(lo+hi)/2],axis=-1)
 grid=np.unique(np.r_[np.geomspace(1e-5,.1,40),np.linspace(.1,1,201)]);vals=at(grid);ix=np.arange(len(g));sol=[]
 for bits in product(range(2),repeat=len(g)):
  y=vals[:,ix,bits].sum(axis=1)-1
  ks=[grid[i] for i in np.where(abs(y)<1e-13)[0]]
  for i in np.where(y[:-1]*y[1:]<0)[0]:ks.append(brentq(lambda k:at(k)[ix,bits].sum()-1,grid[i],grid[i+1],xtol=1e-14))
  for k in ks:
   p=at(k)[ix,bits]
   if min(p)<1e-8 or abs(sum(p)-1)>1e-9 or any(np.linalg.norm(p-q)<1e-7 for q in sol):continue
   sol.append(p)
 rows=[]
 for p in sol:
  b=np.sqrt(p/(1-p));A=np.outer(b,b)-np.diag(b*b);ell=np.linalg.eigvalsh(A)[-2];rad=.8+.2*t*(1+ell)/(1-ell)
  R=np.outer(b,b);np.fill_diagonal(R,0);R/=np.triu(R,1).sum();_,V=np.linalg.eigh(R);u=(g*abs(V[:,-1]))**t;M=np.outer(u,u);np.fill_diagonal(M,0);M/=np.triu(M,1).sum();res=float(np.max(abs(M-R)))
  if res<=1e-8:rows.append(dict(p=p.tolist(),radius=float(rad),residual=res,status='stable' if rad<1-1e-7 else 'unstable' if rad>1+1e-7 else 'critical'))
 return dict(strata=js,epsilon=e,gamma=t,roots=rows)
if __name__=='__main__':
 rows=[]
 for m in (3,4):
  for js in combinations_with_replacement(range(1,7),m):
   for e in (.05,.15):
    for t in (1.5,2.5):rows.append(scan(js,e,t))
  print(m,len(rows),flush=True)
  Path(__file__).with_name('canonical_stability_results.json').write_text(json.dumps(dict(scope='sampled branch scan; not exhaustive; no fold certification',mu=.2,mass=1,rows=rows),allow_nan=False))
