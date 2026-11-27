import numpy as np,json
from scipy.optimize import root
from itertools import combinations_with_replacement
from pathlib import Path

def calc(js,e,x):
 m=len(js);p=np.r_[x[:-1],1-sum(x[:-1])];t=x[-1]
 if min(p)<=0 or max(p)>=1 or t<=1:return None
 a=(t-1)/(t+1);g=-.5*np.log1p(-e*np.array(js));h=2*t/(t+1)*g+a*np.log(p)+np.log1p(-p)
 b=np.sqrt(p/(1-p));ell=np.linalg.eigvalsh(np.outer(b,b)-np.diag(b*b))[-2]
 return np.r_[h[:-1]-h[-1],ell+a]

def critical_rows():
 rows=[];grid=np.linspace(.001,.165,12)
 for m in (3,4):
  for js in combinations_with_replacement(range(1,7),m):
   prev=None
   for e in grid:
    if len(set(js))==1:x=np.r_[np.full(m-1,1/m),m/(m-2)];err=0.
    else:
     seeds=([prev] if prev is not None else [])+[np.r_[np.full(m-1,1/m),t] for t in (1.15,1.5,2.,m/(m-2))]
     x=None
     for seed in seeds:
      def f(y):
       z=calc(js,e,y);return z if z is not None else np.full(m,100.)
      s=root(f,seed,tol=1e-10,options={"maxfev":100});z=calc(js,e,s.x)
      if z is not None and np.max(abs(z))<1e-8:
       x=s.x;err=float(np.max(abs(z)));break
    if x is not None:prev=x;rows.append(dict(strata=js,epsilon=float(e),gamma=float(x[-1]),p=np.r_[x[:-1],1-sum(x[:-1])].tolist(),residual=err))
    else:rows.append(dict(strata=js,epsilon=float(e),gamma=None))

 return rows

from collections import Counter
from scipy.linalg import null_space

def classify(rows):
 out=[]
 for r in rows:
  o=dict(r);out.append(o)
  if r['gamma'] is None:o['kind']='missing';continue
  p=np.array(r['p']);g=r['gamma'];j=np.array(r['strata']);e=r['epsilon'];a=(g-1)/(g+1);m=len(p)
  Q=null_space(np.ones((1,m)));d=a/p-1/(1-p);dd=-a/p**2-1/(1-p)**2
  H=Q.T@np.diag(d)@Q; ev,V=np.linalg.eigh(H);idx=np.argsort(abs(ev));v=Q@V[:,idx[0]]
  A=v@(2/(g+1)**2*(np.log(p)-.5*np.log1p(-e*j)));B=np.sum(dd*v**3)
  b=np.sqrt(p/(1-p));ell=np.linalg.eigvalsh(np.outer(b,b)-np.diag(b*b)); mult=int(sum(abs(ell[:-1]+a)<1e-6))
  # exact symmetric candidate: repeated equal weights at peak, approximate p may be split by ill-conditioned solver
  pc=(g-1)/(2*g);near=np.where(abs(p-pc)<.003)[0]; counts=Counter(j[near]);rep=max(counts.values(),default=0)
  if len(set(j))==1:kind='homogeneous_multiple'
  elif rep>=2:kind='symmetry_candidate'
  elif mult==1 and abs(A)>1e-5 and abs(B)>1e-3:kind='fold_candidate'
  else:kind='unresolved'
  o.update(kind=kind,A=float(A),B=float(B),unit_multiplicity=mult,peak_repeat=int(rep),hessian_eigenvalues=ev.tolist(),side=float(-B/(2*A)) if abs(A)>1e-10 else None)
 return out

def cubic(rows):
 out=[]
 for r in rows:
  if r['kind']!='symmetry_candidate':continue
  j=np.array(r['strata']);m=len(j);e=r['epsilon'];g=-.5*np.log1p(-e*j);p=np.array(r['p']);t=r['gamma'];pc=(t-1)/(2*t)
  ids=max([np.where((j==k)&(abs(p-pc)<.003))[0] for k in set(j)],key=len); k=len(ids)
  o=dict(strata=j.tolist(),epsilon=e,original_gamma=t,repeat=k);out.append(o)
  if k!=2:o['kind']='multiple_candidate';continue
  rest=np.array([i for i in range(m) if i not in ids]);
  def unpack(x):
   t=x[0];p=np.zeros(m);p[ids]=(t-1)/(2*t);p[rest]=x[1:];return t,p
  def fun(x):
   t,p=unpack(x)
   if t<=1 or np.any(p<=0) or np.any(p>=1):return np.ones(m-1)*100
   h=2*t/(t+1)*g+(t-1)/(t+1)*np.log(p)+np.log1p(-p);return np.r_[p.sum()-1,h[rest]-h[ids[0]]]
  sol=root(fun,np.r_[t,p[rest]],tol=1e-11);t,p=unpack(sol.x)
  if np.max(abs(fun(sol.x)))>1e-9 or abs(t-r['gamma'])>.02:o['kind']='unresolved';continue
  a=(t-1)/(t+1);d=a/p-1/(1-p);dd=-a/p**2-1/(1-p)**2;ddd=2*a/p**3-2/(1-p)**3
  v=np.zeros(m);v[ids]=[1/np.sqrt(2),-1/np.sqrt(2)];W=null_space(np.vstack([np.ones(m),v]));L=W.T@np.diag(d)@W;ev=np.linalg.eigvalsh(L)
  if min(abs(ev))<1e-7:o['kind']='multiple_candidate';continue
  ht=2*(g+np.log(p))/(t+1)**2;z=-W@np.linalg.solve(L,W.T@ht);w=-W@np.linalg.solve(L,W.T@(dd*v*v));
  A=np.sum(v*v*(2/(t+1)**2/p+dd*z));B=np.sum(ddd*v**4)/6+np.sum(dd*v*v*w)/2
  side=-B/A if abs(A)>1e-8 else None
  o.update(gamma=t,p=p.tolist(),linear=A,cubic=B,side=side,complement=ev.tolist(),kind=('subcritical' if B>0 and A>0 else 'supercritical' if B<0 and A>0 else 'other') if max(ev)<0 and abs(A)>1e-8 and abs(B)>1e-8 else 'other')
 return out

def multiple(rows):
 out=[]
 for r in rows:
  if r['kind']!='symmetry_candidate' or r['peak_repeat']<3:continue
  j=np.array(r['strata']); p=np.array(r['p']); t=r['gamma']; e=r['epsilon']; g=-.5*np.log1p(-e*j)
  ids=max([np.where((j==k)&(abs(p-(t-1)/(2*t))<.003))[0] for k in set(j)],key=len)
  rest=np.array([i for i in range(len(j)) if i not in ids],dtype=int)
  def unpack(x):
   q=np.zeros(len(j));q[ids]=(x[0]-1)/(2*x[0]);q[rest]=x[1:];return x[0],q
  def fun(x):
   t,q=unpack(x)
   if t<=1 or min(q)<=0 or max(q)>=1:return np.full(len(rest)+1,100.)
   h=2*t/(t+1)*g+(t-1)/(t+1)*np.log(q)+np.log1p(-q)
   return np.r_[sum(q)-1,h[rest]-h[ids[0]]]
  sol=root(fun,np.r_[t,p[rest]],tol=1e-11); T,q=unpack(sol.x);err=float(max(abs(fun(sol.x))))
  o=dict(strata=j.tolist(),epsilon=e,original_gamma=t,residual=err,status='unresolved');out.append(o)
  if err>1e-9 or abs(T-t)>.02:continue
  V=np.zeros((len(j),len(ids)-1));V[ids,:]=null_space(np.ones((1,len(ids))))
  W=null_space(np.vstack([np.ones(len(j)),V.T]));alpha=(T-1)/(T+1);d=alpha/q-1/(1-q);dd=-alpha/q**2-1/(1-q)**2
  L=W.T@np.diag(d)@W;ev=np.linalg.eigvalsh(L)
  if len(ev) and min(abs(ev))<1e-7:continue
  z=-W@np.linalg.solve(L,W.T@(2*(g+np.log(q))/(T+1)**2))
  a=float(2/(T+1)**2/q[ids[0]]+dd[ids[0]]*z[ids[0]])
  o.update(gamma=T,p=q.tolist(),linear=a,quadratic=float(dd[ids[0]]/2),complement=ev.tolist(),status='verified_hypotheses' if abs(a)>1e-7 and max(ev,default=-1)<0 else 'other')
 return out

if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('--critical-input',type=Path);parser.add_argument('--stability-input',type=Path,required=True);parser.add_argument('--output',type=Path,default=Path(__file__).with_name('canonical_bifurcation_results.json'));args=parser.parse_args()
 rows=json.loads(args.critical_input.read_text())['rows'] if args.critical_input else critical_rows()
 classified=classify(rows); cub=cubic(classified); mult=multiple(classified)
 stability=json.loads(args.stability_input.read_text())
 result=dict(scope='sampled numerical evidence; not exhaustive; no global continuation',stability=stability,critical=classified,cubic=cub,multiple=mult,summary=dict(critical=dict(Counter(r['kind'] for r in classified)),cubic=dict(Counter(r['kind'] for r in cub)),multiple=dict(Counter(r['status'] for r in mult))))
 args.output.write_text(json.dumps(result,allow_nan=False,indent=2));print(result['summary'])
