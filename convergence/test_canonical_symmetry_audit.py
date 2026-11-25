import unittest
from canonical_symmetry_audit import audit, orbit_counts, rotation, preserves_weights

class TestCanonical(unittest.TestCase):
    def test_group(self):
        a=audit(); self.assertTrue(a['composition_verified']); self.assertEqual(a['rotation_order'],4)
    def test_cycles(self):
        self.assertEqual(audit()['cycle_lengths'],[[1]*24,[4]*6,[2]*12,[4]*6])
    def test_orbits(self):
        a=orbit_counts(2); self.assertEqual(a['total'],4195360); self.assertEqual(sum(k*a[k] for k in (1,2,4)),2**24)
    def test_weights(self):
        self.assertTrue(preserves_weights(rotation(1),[i%6 for i in range(24)],29)); self.assertFalse(preserves_weights(rotation(1),list(range(24)),29))
    def test_intersection(self): self.assertEqual(audit()['intersection_with_auxiliary_order'],2)
    def test_edges(self):
        a=audit()['edge_orbits_by_size']; self.assertEqual(sum(int(k)*v for k,v in a.items()),276)

if __name__=='__main__': unittest.main()
