"""Topología sobre soporte de N=24 nodos (simetría Z_4), red de 276 aristas y operador Sigma_23."""

from __future__ import annotations

import numpy as np


def build_z4_permutation_matrix(n_nodes: int = 24) -> np.ndarray:
    """Construye la matriz de permutación del generador cíclico Z_4 sobre 6 órbitas de 4 nodos."""
    if n_nodes <= 0 or n_nodes % 4 != 0:
        raise ValueError("n_nodes debe ser un entero positivo múltiplo de 4 para simetría Z_4.")

    perm = np.zeros((n_nodes, n_nodes), dtype=float)
    n_orbits = n_nodes // 4
    for orbit in range(n_orbits):
        base = 4 * orbit
        for k in range(4):
            src = base + k
            dst = base + ((k + 1) % 4)
            perm[dst, src] = 1.0
    return perm


def build_parabolic_coordinates(n_nodes: int = 24) -> np.ndarray:
    """Asigna coordenadas (x, y, z) sobre envolvente parabólica z = r^2 con simetría Z_4."""
    if n_nodes <= 0 or n_nodes % 4 != 0:
        raise ValueError("n_nodes debe ser un entero positivo múltiplo de 4.")

    coords = np.zeros((n_nodes, 3), dtype=float)
    n_orbits = n_nodes // 4
    for orbit in range(n_orbits):
        radius = (orbit + 1) / n_orbits
        z_height = radius**2
        phase_offset = (np.pi / 8.0) * (orbit % 2)
        for k in range(4):
            angle = (np.pi / 2.0) * k + phase_offset
            idx = 4 * orbit + k
            coords[idx, 0] = radius * np.cos(angle)
            coords[idx, 1] = radius * np.sin(angle)
            coords[idx, 2] = z_height
    return coords


def build_edges_276(n_nodes: int = 24, length_scale: float = 1.0) -> np.ndarray:
    """Construye el operador simétrico y Z_4-invariante de las 276 aristas (C(24, 2) = 276)."""
    if length_scale <= 0.0:
        raise ValueError("length_scale debe ser estrictamente positivo.")

    coords = build_parabolic_coordinates(n_nodes=n_nodes)
    adj = np.zeros((n_nodes, n_nodes), dtype=float)

    for i in range(n_nodes):
        for j in range(i + 1, n_nodes):
            dist_sq = float(np.sum((coords[i] - coords[j]) ** 2))
            weight = float(np.exp(-dist_sq / (2.0 * (length_scale**2))))
            adj[i, j] = weight
            adj[j, i] = weight

    degrees = np.sum(adj, axis=1)
    inv_sqrt_deg = np.diag(1.0 / np.sqrt(np.maximum(degrees, 1e-12)))
    laplacian_norm = np.eye(n_nodes, dtype=float) - inv_sqrt_deg @ adj @ inv_sqrt_deg

    op_24 = np.eye(n_nodes, dtype=float) - 0.035 * laplacian_norm
    op_24 = 0.5 * (op_24 + op_24.T)
    norm = float(np.linalg.norm(op_24, ord=2))
    return op_24 / norm if norm > 1.0 else op_24


def build_sigma_23_operator(dim: int = 22) -> np.ndarray:
    """Construye el operador simétrico Sigma_23 sobre el bloque de 22 modos transversales/relacionales."""
    if dim <= 0:
        raise ValueError("dim debe ser un entero positivo.")

    idx = np.arange(1, dim + 1, dtype=float)
    denom = float(max(dim - 1, 1))
    radial_profile = 0.974885 - 0.012 * (((idx - 1.0) / denom) ** 2)
    diag_op = np.diag(radial_profile)

    anti_diag = np.fliplr(np.eye(dim, dtype=float)) * 0.0025
    np.fill_diagonal(anti_diag, 0.0)
    sigma_op = diag_op + anti_diag
    return 0.5 * (sigma_op + sigma_op.T)
