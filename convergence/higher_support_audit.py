"""Reference operator audit; illustrative weights, not canonical certification."""
import json
from itertools import combinations, product
from pathlib import Path
import numpy as np
from scipy.optimize import brentq, root
import scipy

def branches(g,t):
    g=np.asarray(g); a=(t-1)/(t+1); pc=a/(1+a); w=g**(2*t/(t+1)); f=lambda p:p**a*(1-p); km=min(w)*f(pc)
    def at(k):
        return np.array([(pc,pc) if abs(f(pc)-k*km/wi)<1e-14 else (brentq(lambda p:f(p)-k*km/wi,0,pc,xtol=1e-15),brentq(lambda p:f(p)-k*km/wi,pc,1,xtol=1e-15)) for wi in w])
    grid=np.unique(np.r_[np.geomspace(.001,.1,80),np.linspace(.1,1,250)]); vals=np.array([at(k) for k in grid]); out=[]; ix=np.arange(len(g))
    for bits in product(range(2),repeat=len(g)):
        y=vals[:,ix,bits].sum(axis=1)-1
        for j in range(len(grid)-1):
            if y[j]*y[j+1]<0:
                k=brentq(lambda k:at(k)[ix,bits].sum()-1,grid[j],grid[j+1],xtol=1e-14); p=at(k)[ix,bits]
                if min(p)>1e-10 and not any(np.linalg.norm(p-q)<1e-7 for q in out):out.append(p)
    return out

def audit(p,g,t,mu=.2):
    m=len(p); b=np.sqrt(p/(1-p)); A=np.outer(b,b)-np.diag(b*b); ell=np.linalg.eigvalsh(A)[:-1]; pred=1-mu+mu*t*(1+ell)/(1-ell)
    pairs=list(combinations(range(m),2)); n=len(pairs); r=np.array([b[i]*b[j] for i,j in pairs]);r/=r.sum()
    def F(x,t=t):
        R=np.zeros((m,m))
        for z,(i,j) in zip(x,pairs):R[i,j]=R[j,i]=z
        _,V=np.linalg.eigh(R);u=(np.asarray(g)*abs(V[:,-1]))**t; y=np.array([u[i]*u[j] for i,j in pairs]);return (1-mu)*x+mu*y/y.sum()
    J=np.column_stack([((F(r+1e-6*(np.eye(n)[i]-np.eye(n)[-1]))-F(r-1e-6*(np.eye(n)[i]-np.eye(n)[-1])))/(2e-6))[:-1] for i in range(n-1)])
    actual=np.linalg.eigvals(J); expected=np.sort(np.r_[pred,np.full(n-m,1-mu)]); err=max(np.max(abs(np.sort(actual.real)-expected)),np.max(abs(actual.imag)))
    return dict(p=p.tolist(),edges=r.tolist(),radius=float(max(abs(expected))),spectral_error=float(err),fixed_residual=float(max(abs(F(r)-r)))),F,r

def critical():
    g=np.array([1.,1.1,1.2])
    def deriv(x):
        p=np.r_[x[:2],1-sum(x[:2])];t=x[2];a=(t-1)/(t+1);h=2*t/(t+1)*np.log(g)+a*np.log(p)+np.log1p(-p);d=a/p-1/(1-p);dd=-a/p**2-1/(1-p)**2;J=np.diag(d[:2])+d[2]*np.ones((2,2));ht=2/(t+1)**2*(np.log(g)+np.log(p));return h[:2]-h[2],J,ht[:2]-ht[2],dd
    s=root(lambda x:np.r_[deriv(x)[0],np.linalg.det(deriv(x)[1])],[.12457,.39612,1.56556],tol=1e-12);assert s.success
    f,J,ft,dd=deriv(s.x);ev,V=np.linalg.eigh(J);q=V[:,np.argmin(abs(ev))];q*=np.sign(q[0]);A=q@ft;B=q@(dd[:2]*q*q-dd[2]*sum(q)**2);p=np.r_[s.x[:2],1-sum(s.x[:2])];rec,F,r=audit(p,g,s.x[2]);x=r[:2];t=s.x[2]
    def G(x,t):return F(np.r_[x,1-sum(x)],t)[:2]-x
    h=1e-5;D=np.column_stack([(G(x+h*e,t)-G(x-h*e,t))/(2*h) for e in np.eye(2)]);U,S,Vh=np.linalg.svd(D);v=Vh[-1];v*=np.sign(v[0]);w=U[:,-1];w/=w@v
    checks=[]
    for h in [1e-4,3e-5,1e-5]:checks.append(dict(step=h,A=float(w@((G(x,t+h)-G(x,t-h))/(2*h))),B=float(w@((G(x+h*v,t)-2*G(x,t)+G(x-h*v,t))/h**2))))
    assert abs(A)>1e-3 and abs(B)>1e-3 and abs(ev[-1])<1e-8 and ev[0]<-1e-3 and all(abs(c['A'])>1e-3 and abs(c['B'])>1e-3 for c in checks)
    return dict(gamma=float(t),**rec,reduced_eigenvalues=ev.tolist(),A=float(A),B=float(B),orientation=float(-B/(2*A)),equation_residual=float(max(abs(f))),dynamic_eigenvalues=np.linalg.eigvals(D+np.eye(2)).tolist(),dynamic_checks=checks)

def main():
    cases=[]
    for g in [[1,1,1],[1,1.1,1.2],[1,1,1.1,1.1]]:
        rows=[audit(p,g,1.5)[0] for p in branches(g,1.5)];assert rows and all(r['spectral_error']<1e-6 and r['fixed_residual']<1e-9 for r in rows);cases.append(dict(weights=g,roots=rows,stable=sum(r['radius']<1-1e-7 for r in rows)))
    assert [len(c['roots']) for c in cases]==[4,4,9]
    result=dict(status='PASS',numpy=np.__version__,scipy=scipy.__version__,mu=.2,mass=1,gamma=1.5,cases=cases,critical=critical(),limitations=['Illustrative weights','Root scan not exhaustive or interval certified','Internal Jacobian only','No basin estimates','No canonical or Episode 44 certification'])
    Path(__file__).with_name('higher_support_results.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n');print(json.dumps(result['critical'],indent=2))
if __name__=='__main__':main()
