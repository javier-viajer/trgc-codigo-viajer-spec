"""
Automated tests for the reference
relational equivariance audit.

Version 0.1.0
"""

import unittest
import numpy as np

from relational_equivariance_audit import (
    N,
    TOL,
    SEED,
    STRATA,
    SECTORS,
    rotation,
    transform,
    mass,
    random_relation,
    reference_operator,
    equivariance_error,
    rotational_projection,
    stratified_generators,
    edge_orbits,
    run_audit
)


class TestRelationalEquivariance(unittest.TestCase):

    def setUp(self):
        self.rng = np.random.default_rng(SEED)

        self.R = random_relation(self.rng)

        self.weights = np.tile(
            np.linspace(1.0, 2.0, STRATA),
            SECTORS
        )

    def test_rotation_order(self):
        p = rotation()
        current = np.arange(N)

        for _ in range(4):
            current = current[p]

        np.testing.assert_array_equal(
            current,
            np.arange(N)
        )

        self.assertFalse(
            np.array_equal(p[p], np.arange(N))
        )

    def test_rotational_equivariance(self):
        for k in range(4):
            error = equivariance_error(
                self.R,
                rotation(k),
                self.weights
            )

            self.assertLessEqual(error, TOL)

    def test_stratified_equivariance(self):
        for p in stratified_generators():
            error = equivariance_error(
                self.R,
                p,
                self.weights
            )

            self.assertLessEqual(error, TOL)

    def test_mass_conservation(self):
        evolved = reference_operator(
            self.R,
            self.weights
        )

        self.assertAlmostEqual(
            mass(self.R),
            mass(evolved),
            places=10
        )

    def test_invariant_subspace(self):
        R = rotational_projection(self.R)

        for _ in range(10):
            R = reference_operator(
                R,
                self.weights
            )

            np.testing.assert_allclose(
                R,
                transform(R, rotation()),
                atol=TOL,
                rtol=0
            )

    def test_rotational_dimension(self):
        orbits = edge_orbits([
            rotation(k)
            for k in range(4)
        ])

        sizes = sorted(
            len(o) for o in orbits
        )

        self.assertEqual(len(orbits), 72)
        self.assertEqual(sizes.count(2), 6)
        self.assertEqual(sizes.count(4), 66)
        self.assertEqual(sum(sizes), 276)

    def test_stratified_dimension(self):
        orbits = edge_orbits(
            stratified_generators()
        )

        self.assertEqual(len(orbits), 21)

        self.assertEqual(
            sum(len(o) for o in orbits),
            276
        )

    def test_negative_control(self):
        weights = self.weights.copy()
        weights[0] *= 2

        error = equivariance_error(
            self.R,
            rotation(),
            weights
        )

        self.assertGreater(error, TOL)

    def test_invalid_domain(self):
        R = np.zeros((N, N))

        with self.assertRaises(ValueError):
            reference_operator(
                R,
                self.weights
            )

    def test_complete_audit(self):
        results = run_audit(samples=4)

        self.assertTrue(
            results["reference_checks_passed"]
        )

        self.assertFalse(
            results["episode_44_modified"]
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
