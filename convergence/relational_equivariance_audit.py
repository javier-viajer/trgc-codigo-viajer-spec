"""
Relational Equivariance Audit
Codigo Viajer - Piramide-Parabola - TRCG
Version 0.1.0

Reference operator only.
Not a certified canonical implementation.
Episode 44 remains unchanged.
"""

from __future__ import annotations

import json
import math
import numpy as np

N = 24
SECTORS = 4
STRATA = 6
TOL = 1e-10
SEED = 20261125

MODEL_STATUS = "reference_operator_not_canonical"


def rotation(k=1):
    return (np.arange(N) + STRATA * k) % N


def stratified_generators():
    generators = []

    for r in range(STRATA):
        for s in range(SECTORS - 1):
            p = np.arange(N)

            i = s * STRATA + r
            j = (s + 1) * STRATA + r

            p[i], p[j] = p[j], p[i]
            generators.append(p)

    return generators


def transform(R, p):
    p = np.asarray(p)
    return R[np.ix_(p, p)]


def mass(R):
    return float(np.triu(R, 1).sum())


def normalize(R, target=1.0):
    m = mass(R)

    if not np.isfinite(m) or m <= 0:
        raise ValueError("Invalid relational mass")

    return R * (target / m)


def random_relation(rng):
    A = rng.uniform(0.1, 1.0, (N, N))
    R = (A + A.T) / 2

    np.fill_diagonal(R, 0.0)

    return normalize(R)


def dominant_vector(R):
    _, vectors = np.linalg.eigh(R)
    v = np.abs(vectors[:, -1])

    return v / np.linalg.norm(v)


def reference_operator(
    R,
    weights,
    alpha=0.2,
    gamma=1.2
):
    R = np.asarray(R, dtype=float)
    weights = np.asarray(weights, dtype=float)

    if R.shape != (N, N):
        raise ValueError("Invalid matrix shape")

    if weights.shape != (N,):
        raise ValueError("Invalid weights")

    if not np.all(np.isfinite(R)):
        raise ValueError("Nonfinite relation")

    if not np.all(np.isfinite(weights)):
        raise ValueError("Nonfinite weights")

    if not np.allclose(R, R.T, atol=TOL, rtol=0):
        raise ValueError("R must be symmetric")

    if np.any(np.diag(R) != 0):
        raise ValueError("Diagonal must vanish")

    offdiag = ~np.eye(N, dtype=bool)

    if np.any(R[offdiag] <= 0):
        raise ValueError(
            "Reference domain requires positive edges"
        )

    if np.any(weights <= 0):
        raise ValueError("Weights must be positive")

    if not 0 <= alpha <= 1:
        raise ValueError("Invalid alpha")

    if not np.isfinite(gamma) or gamma <= 0:
        raise ValueError("Invalid gamma")

    v = dominant_vector(R)
    u = weights * np.power(v, gamma)

    B = np.outer(u, u)
    np.fill_diagonal(B, 0.0)

    B = normalize(B, mass(R))

    return (1 - alpha) * R + alpha * B


def equivariance_error(R, p, weights):
    left = reference_operator(
        transform(R, p),
        weights
    )

    right = transform(
        reference_operator(R, weights),
        p
    )

    denominator = max(
        np.linalg.norm(right),
        1e-15
    )

    return float(
        np.linalg.norm(left - right)
        / denominator
    )


def rotational_projection(R):
    return sum(
        transform(R, rotation(k))
        for k in range(4)
    ) / 4


def edge_orbits(permutations):
    remaining = {
        (i, j)
        for i in range(N)
        for j in range(i + 1, N)
    }

    orbits = []

    while remaining:
        start = min(remaining)
        orbit = {start}
        pending = [start]

        while pending:
            i, j = pending.pop()

            for p in permutations:
                edge = tuple(
                    sorted((int(p[i]), int(p[j])))
                )

                if edge not in orbit:
                    orbit.add(edge)
                    pending.append(edge)

        remaining.difference_update(orbit)
        orbits.append(orbit)

    return orbits


def run_audit(samples=32):
    rng = np.random.default_rng(SEED)

    weights = np.tile(
        np.linspace(1.0, 2.0, STRATA),
        SECTORS
    )

    broken_weights = weights.copy()
    broken_weights[0] *= 2

    rotations = [
        rotation(k)
        for k in range(4)
    ]

    generators = stratified_generators()

    rotational_errors = []
    stratified_errors = []
    negative_errors = []
    mass_errors = []
    invariant_errors = []

    for _ in range(samples):
        R = random_relation(rng)

        for p in rotations:
            rotational_errors.append(
                equivariance_error(R, p, weights)
            )

        for p in generators:
            stratified_errors.append(
                equivariance_error(R, p, weights)
            )

        negative_errors.append(
            equivariance_error(
                R,
                rotation(),
                broken_weights
            )
        )

        evolved = reference_operator(R, weights)

        mass_errors.append(
            abs(mass(evolved) - mass(R))
        )

        symmetric_R = rotational_projection(R)

        evolved_symmetric = reference_operator(
            symmetric_R,
            weights
        )

        invariant_errors.append(
            float(np.linalg.norm(
                transform(
                    evolved_symmetric,
                    rotation()
                ) - evolved_symmetric
            ))
        )

    rot_orbits = edge_orbits(rotations)
    est_orbits = edge_orbits(generators)

    results = {
        "version": "0.1.0",
        "model_status": MODEL_STATUS,
        "seed": SEED,
        "samples": samples,
        "tolerance": TOL,
        "general_dimension": math.comb(N, 2),
        "rotational_dimension": len(rot_orbits),
        "stratified_dimension": len(est_orbits),
        "rotational_orbit_sizes": sorted(
            len(o) for o in rot_orbits
        ),
        "rotational_max_error": max(
            rotational_errors
        ),
        "stratified_max_error": max(
            stratified_errors
        ),
        "negative_control_min_error": min(
            negative_errors
        ),
        "mass_max_error": max(mass_errors),
        "invariant_max_error": max(
            invariant_errors
        ),
        "episode_44_modified": False,
        "level_II": "retained",
        "level_III": "open",
        "lambda": "reserved_fourth_factor"
    }

    results["reference_checks_passed"] = bool(
        results["rotational_dimension"] == 72
        and results["stratified_dimension"] == 21
        and max(rotational_errors) <= TOL
        and max(stratified_errors) <= TOL
        and max(mass_errors) <= TOL
        and max(invariant_errors) <= TOL
        and min(negative_errors) > TOL
    )

    return results


if __name__ == "__main__":
    results = run_audit()

    with open(
        "relational_equivariance_results.json",
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(results, f, indent=2)

    print(json.dumps(results, indent=2))

    if not results["reference_checks_passed"]:
        raise SystemExit(1)
