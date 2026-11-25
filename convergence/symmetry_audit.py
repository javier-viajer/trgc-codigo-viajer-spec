"""Exact automorphism orders for the provisional 24-node multilayer model.
Requires networkx. No Episode 44 code or data is used.
"""
import argparse
import itertools
import json
import math
import networkx as nx

LAYERS = ('C', 'S23', 'T8', 'X6')
N = 24

def graph(active=LAYERS):
    active = tuple(active)
    if not set(active) <= set(LAYERS):
        raise ValueError('Unknown layer')
    g = nx.Graph()
    g.add_nodes_from(range(N))
    for i, j in itertools.combinations(range(N), 2):
        d = (j-i) % N
        flags = (d in (1,23), i+j == 23, d in (8,16), d in (6,18))
        color = tuple(k for k, f in zip(LAYERS, flags) if f and k in active)
        if color:
            g.add_edge(i,j,color=color)
    return g

def matcher(a,b):
    return nx.algorithms.isomorphism.GraphMatcher(a,b,edge_match=lambda x,y:x['color']==y['color'])

def order(g):
    # Isomorphic connected components can be permuted freely. Count each
    # component's internal automorphisms only once, avoiding huge enumeration.
    classes = []
    for nodes in nx.connected_components(g):
        c = g.subgraph(nodes).copy()
        for entry in classes:
            if matcher(c,entry[0]).is_isomorphic():
                entry[1] += 1
                break
        else:
            classes.append([c,1])
    result = 1
    for c,m in classes:
        a = sum(1 for _ in matcher(c,c).isomorphisms_iter())
        result *= a**m * math.factorial(m)
    return result

def nominal_group():
    g = graph()
    return {tuple(p[i] for i in range(N)) for p in matcher(g,g).isomorphisms_iter()}

def compose(p,q):
    return tuple(p[q[i]] for i in range(N))

def audit():
    base = order(graph())
    rows = []
    for n in range(len(LAYERS)+1):
        for removed in itertools.combinations(LAYERS,n):
            a = order(graph(k for k in LAYERS if k not in removed))
            assert a % base == 0
            rows.append(dict(removed=list(removed),order=a,index=a//base,D=math.log2(a//base)))
    lookup = {tuple(r['removed']):r for r in rows}
    interactions = []
    for i,j in itertools.combinations(LAYERS,2):
        a,b,c = (lookup[k]['order'] for k in ((i,), (j,), (i,j)))
        interactions.append(dict(pair=[i,j],J=math.log2(c*base/(a*b))))
    group = nominal_group(); identity=tuple(range(N))
    assert identity in group and all(compose(p,q) in group for p in group for q in group)
    assert all(compose(p,p)==identity for p in group)
    return dict(scope='provisional only',networkx=nx.__version__,rows=rows,interactions=interactions,nominal_group=sorted(group))

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',help='Optional JSON output path')
    args=parser.parse_args()
    data=json.dumps(audit(),indent=2,allow_nan=False)
    if args.output:
        from pathlib import Path
        Path(args.output).write_text(data+'\n',encoding='utf-8')
    else:
        print(data)
