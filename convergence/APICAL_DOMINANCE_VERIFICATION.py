"""Independent verification of APICAL_DOMINANCE.md (auxiliary model only)."""
import argparse
import json
from pathlib import Path
import numpy as np

A = np.array([5, 11, 17, 23])
B = np.array([i for i in range(24) if i not in A])
TOL = 1e-12


def mass(x):
    return float(np.sum(x[A]))


def step(x, f):
    x, f = np.asarray(x, float), np.asarray(f, float)
    if x.shape != (24,) or f.shape != (24,) or not np.all(np.isfinite(x)) or not np.all(np.isfinite(f)) or np.any(x < 0) or np.any(f <= 0) or abs(x.sum()-1) > TOL:
        raise ValueError('Invalid state or fitness')
    y = x*f
    return y/y.sum()


def fitness(eta):
    f = np.ones(24)
    f[A] = eta
    return f


def verify():
    rng = np.random.default_rng(42)
    results = {}
    def check(name, condition, **details):
        results[name] = dict(status='PASS' if condition else 'FAIL', **details)
    errors = np.zeros(5)
    support = True
    for _ in range(1000):
        x = rng.random(24)
        x[rng.random(24)<.2] = 0
        x /= x.sum()
        f = rng.uniform(.2, 3, 24)
        y = step(x, f)
        a = mass(x)
        support &= bool(np.array_equal(x>0,y>0))
        errors[0] = max(errors[0], abs(y.sum()-1))
        if 0 < a < 1 and x[B].sum()>0:
            fa = np.dot(x[A],f[A])/a
            fb = np.dot(x[B],f[B])/x[B].sum()
            z = a*fa+(1-a)*fb
            errors[1] = max(errors[1],abs(mass(y)-a*fa/z))
            errors[2] = max(errors[2],abs(mass(y)-a-a*(1-a)*(fa-fb)/z))
            errors[3] = max(errors[3],abs(mass(y)-(a*(fa/fb))/(1-a+a*(fa/fb))))
        errors[4] = max(errors[4],abs(mass(np.roll(x,12))-a),abs(mass(np.roll(x,6))-a))
    for name,e in zip(['T01_simplex','T03_mass','T04_increment','T05_ratio','T16_rotation'],errors):
        check(name,e<TOL,max_error=float(e),trials=1000)
    check('T02_support',support,trials=1000)
    x0=np.ones(24)/24
    x=x0.copy(); L=0.; err=0.; bound=True
    for t in range(1,101):
        eta=1.2; x=step(x,fitness(eta)); L+=np.log(eta)
        expected=1/(1+5*np.exp(-L))
        err=max(err,abs(mass(x)-expected)); bound &= mass(x)+TOL>=expected
    check('T06_accumulated',err<TOL,max_error=float(err))
    check('T07_concentration',mass(x)>1-1e-7,final_mass=mass(x))
    check('T08_bound',bound)
    x=x0.copy()
    for t in range(60): x=step(x,fitness(np.exp(2.**(-t-1))))
    expected=float(np.e/(5+np.e))
    check('T09_summable_advantage',abs(mass(x)-expected)<TOL,final_mass=mass(x),limit=expected)
    x=x0.copy()
    for _ in range(60): x=step(x,fitness(.5))
    check('T10_geometry_counterexample',mass(x)<1e-15,final_mass=mass(x),geometric_ratio=2,relational_ratio=.25)
    xb=np.zeros(24); xb[B]=1/20
    xa=np.zeros(24); xa[A]=1/4
    check('T11_nonapical_face',mass(step(xb,fitness(2)))==0)
    check('T12_apical_face',abs(mass(step(xa,fitness(.5)))-1)<TOL)
    check('T13_equilibria',all(np.array_equal(step(v,fitness(2)),v) for v in np.eye(24)),vertices=24)
    # A stable basal equilibrium requires contraction within the basal face too.
    # Constant fitness with one uniquely favored basal node gives an exact example.
    e=np.eye(24)[0]; eps=1e-7
    invasion={}; ok=True
    for eta in (.5,2.):
        f=np.full(24,.25); f[0]=1; f[A]=eta
        p=(1-eps)*e+eps*np.eye(24)[A[0]]
        measured=mass(step(p,f))/eps
        ok &= abs(measured-eta)<1e-6
        invasion[str(eta)]={'multiplier':eta,'finite_difference':measured,'basal_tangent_radius':.25,'full_tangent_radius':max(.25,eta)}
    check('T14_invasion',ok,cases=invasion)
    check('T15_transverse',invasion['0.5']['finite_difference']<1<invasion['2.0']['finite_difference'])
    check('T17_quotient_observable',errors[4]<TOL)
    # Exact finite initial distribution; probability and mean are distinct.
    states=[xb,xa,x0]; weights=np.array([.2,.3,.5]); masses=np.array([mass(step(s,fitness(2))) for s in states])
    prob=float(weights[masses>=.5].sum()); mean=float(weights@masses)
    check('T18_probability',abs(prob-.3)<TOL and abs(mean-(.3+.5*2/7))<TOL,probability=prob,mean_mass=mean)
    for name in ('T19_null_architectures','T20_canonical_operator'):
        results[name]={'status':'NOT_RUN','reason':'Canonical architecture/operator data unavailable'}
    return {'scope':'Auxiliary multiplicative model only','seed':42,'tolerance':TOL,'numpy':np.__version__,'results':results,'counts':{s:sum(v['status']==s for v in results.values()) for s in ('PASS','FAIL','NOT_RUN')}}


if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path,default=Path('apical_verification.json')); args=parser.parse_args()
    report=verify(); args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n',encoding='utf-8'); print(json.dumps(report['counts']))
    raise SystemExit(bool(report['counts']['FAIL']))
