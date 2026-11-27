from pathlib import Path
import numpy as np,json
from scipy.optimize import brentq
from collections import Counter
rng=np.random.default_rng(49)
def step(r,g,gamma,mu,v=None):
 n=len(g); i,j=np.triu_indices(n,1); R=np.zeros((n,n));R[i,j]=R[j,i]=r
 if v is None: v=np.abs(np.linalg.eigh(R)[1][:,-1])
 h=(g[i]*g[j]*v[i]*v[j])**gamma;h/=h.sum();return (1-mu)*r+mu*h
def L(r,g,gamma):
 i,j=np.triu_indices(len(g),1);R=np.zeros((len(g),len(g)));R[i,j]=R[j,i]=r;q=1+1/gamma
 return np.linalg.eigvalsh(R)[-1]/np.sum(r**q/(g[i]*g[j]))**(1/q)
out={}; rows=[]
for n in [3,24]:
 for eps in ([0] if n==3 else [.01,.05,.15]):
  g=np.ones(n) if n==3 else (1-eps*np.tile(np.arange(1,7),4))**-.5
  for ga in [.5,1,1.5,2.5,3,4]:
   for mu in [.2,1]:
    ds=[]; moves=[]
    for k in range(30):
     r=rng.dirichlet(np.ones(n*(n-1)//2)*(.2 if k%2 else 1));s=step(r,g,ga,mu);ds.append(L(s,g,ga)-L(r,g,ga));moves.append(np.linalg.norm(s-r))
    rows.append(dict(n=n,eps=eps,gamma=ga,mu=mu,count=len(ds),minimum=min(ds),negative=sum(d< -1e-12 for d in ds)))
out['monotonicity']=rows
# critical coefficient along ordered directions
out['critical']=[]
for d in [np.array([2.,0.,-2.]),np.array([1.,.9,-1.9]),np.array([2.,-1.,-1.])]:
 for h in [1e-3,1e-4,1e-5]:
  r=1/3+h*d;s=step(r,np.ones(3),3,.2);out['critical'].append(dict(direction=d.tolist(),h=h,coefficient=float(((s[0]-s[1])/(r[0]-r[1])-1)/(.2*h*d[2]))))
out['saddles']=[]
for ga in [1.2,1.5,2,2.9,3.1,4,8]:
 tm=((ga-1)/2)**(1/(ga+1));t=brentq(lambda t:t*t+t**(1-ga)-2,1e-100,tm) if ga<3 else brentq(lambda t:t*t+t**(1-ga)-2,tm,2**.5)
 a=1/(1+2*t**ga);r=np.array([a,(1-a)/2,(1-a)/2]);D=np.array([[1,0],[0,1],[-1,-1]]);J=np.column_stack([(step(r+1e-6*d,np.ones(3),ga,.2)-step(r-1e-6*d,np.ones(3),ga,.2))[:2]/2e-6 for d in D.T]);out['saddles'].append(dict(gamma=ga,t=t,residual=float(np.max(abs(step(r,np.ones(3),ga,.2)-r))),eigenvalues=np.linalg.eigvals(J).tolist()))
out['multiple_perron']=[]
g=np.ones(24);i,j=np.triu_indices(24,1);r=np.zeros(len(i));r[(i==0)&(j==1)]=.5;r[(i==2)&(j==3)]=.5
for ga in [.5,1,3,4]:
 for theta in np.linspace(0,np.pi/2,11):
  v=np.zeros(24);v[:2]=np.cos(theta)/np.sqrt(2);v[2:4]=np.sin(theta)/np.sqrt(2);s=step(r,g,ga,.2,v);out['multiple_perron'].append(float(L(s,g,ga)-L(r,g,ga)))
# negative control: reverse update direction, small step from interior
r=np.array([.5,.3,.2]);h=step(r,np.ones(3),1.5,1);s=r-.1*(h-r);out['negative_control']=float(L(s,np.ones(3),1.5)-L(r,np.ones(3),1.5))
json.dump(out,open(Path(__file__).with_name('canonical_lyapunov_results.json'),'w'),indent=2,default=lambda x:x.item())
print('cases',sum(r['count'] for r in rows),'min',min(r['minimum'] for r in rows),'negative',sum(r['negative'] for r in rows));print('critical',out['critical']);print('saddles',out['saddles']);print('multiple min',min(out['multiple_perron']),'negative control',out['negative_control'])
