import itertools
import math
import unittest
import networkx as nx
from symmetry_audit import LAYERS, graph, order, audit, nominal_group, compose

class SymmetryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = audit()
        cls.orders = {tuple(r['removed']):r['order'] for r in cls.data['rows']}

    def test_orders(self):
        expected = [4,96,48,4,4,4608,24576,497664,48,48,4,188743680,67722117120,1961990553600,48,math.factorial(24)]
        self.assertEqual(list(self.orders.values()),expected)

    def test_klein(self):
        g = nominal_group()
        expected = {tuple((s*i+k)%24 for i in range(24)) for s,k in [(1,0),(1,12),(-1,11),(-1,23)]}
        self.assertEqual(g,expected)
        for p,q in itertools.product(g,repeat=2):
            self.assertIn(compose(p,q),g)
            self.assertEqual(compose(p,p),tuple(range(24)))

    def test_monotonicity(self):
        for a,b in itertools.product(self.orders,repeat=2):
            if set(a)<=set(b):
                self.assertEqual(self.orders[b]%self.orders[a],0)

    def test_relabel(self):
        for removed,n in self.orders.items():
            g=graph(k for k in LAYERS if k not in removed)
            self.assertEqual(order(nx.relabel_nodes(g,{i:(5*i+7)%24 for i in range(24)})),n)

    def test_component_formula(self):
        # Two identical triangles and two isolated nodes, independent formula.
        g=nx.disjoint_union_all([nx.complete_graph(3),nx.complete_graph(3),nx.empty_graph(2)])
        nx.set_edge_attributes(g,('test',),'color')
        self.assertEqual(order(g),6**2*2*2)

    def test_interactions(self):
        j={tuple(r['pair']):r['J'] for r in self.data['interactions']}
        self.assertAlmostEqual(j['C','S23'],2)
        self.assertAlmostEqual(j['C','T8'],8)
        self.assertAlmostEqual(j['C','X6'],math.log2(5184))

if __name__=='__main__':
    unittest.main()
