"""Acoplamiento entre subbloques (Pi_{3->4}), paso helicoidal y evolución discreta en R^{47}."""

from __future__ import annotations

import numpy as np

from dynamics.topology_276 import (
    build_edges_276,
    build_sigma_23_operator,
)


def build_pi_3_to_4(rows: int = 24, cols: int = 22) -> np.ndarray:
    """Construye el operador determinista Pi_{3->4} entre las 6 órbitas Z_4 y los 22 modos."""
    if rows <= 0 or cols <= 0:
        raise ValueError("rows y cols deben ser enteros positivos.")

    pi_mat = np.zeros((rows, cols), dtype=float)
    for node in range(rows):
        orbit = node // 4
        quadrant = node % 4
        tri_phase = (2.0 * np.pi / 3.0) * (orbit % 3)
        quad_phase = (np.pi / 2.0) * quadrant
        for mode in range(cols):
            freq = (mode + 1) * np.pi / (cols + 1)
            pi_mat[node, mode] = float(np.cos(quad_phase - tri_phase) * np.sin(freq * (orbit + 1)))

    norm = float(np.linalg.norm(pi_mat, ord=2))
    return pi_mat / norm if norm > 0.0 else pi_mat


def helical_phase_step(
    theta: np.ndarray,
    m: np.ndarray,
    s: np.ndarray,
    coup: float,
    cuarto_factor: float = 0.0,
) -> np.ndarray:
    """Calcula el avance helicoidal de fase preservando la traslación neutra en ausencia de corte."""
    m_arr = np.asarray(m, dtype=float)
    s_arr = np.asarray(s, dtype=float)
    theta_arr = np.asarray(theta, dtype=float)

    if m_arr.size != 24 or s_arr.size != 22:
        raise ValueError("Se esperan vectores m de longitud 24 y s de longitud 22.")

    m_orbits = m_arr.reshape(6, 4)
    helical_shear = float(np.sum(m_orbits[:, :-1] * np.roll(m_orbits[:, 1:], shift=1, axis=0)))
    longitudinal_bias = float(np.dot(np.linspace(-1.0, 1.0, s_arr.size), s_arr))

    twist = coup * (0.02 * np.tanh(helical_shear) + 0.015 * longitudinal_bias) * (1.0 + cuarto_factor)
    return np.mod(theta_arr + twist, 2.0 * np.pi)


def default_operators_47d() -> dict[str, np.ndarray]:
    """Devuelve el diccionario estándar de operadores deterministas para la dinámica 47D."""
    return {
        "topo_24": build_edges_276(n_nodes=24),
        "sigma_23": build_sigma_23_operator(dim=22),
        "pi_3_4": build_pi_3_to_4(rows=24, cols=22),
    }


def step_47d(
    state: np.ndarray,
    coup: float,
    ops: dict[str, np.ndarray] | None = None,
    cuarto_factor: float = 0.0,
) -> np.ndarray:
    """Evalúa un paso discreto acoplado x_{t+1} = F(x_t; coup) sobre el espacio de 47 dimensiones."""
    x = np.asarray(state, dtype=float)
    if x.shape != (47,):
        raise ValueError(f"Se esperaba un vector de estado de forma (47,), recibido {x.shape}.")

    active_ops = default_operators_47d() if ops is None else ops
    topo_24 = active_ops["topo_24"]
    sigma_23 = active_ops["sigma_23"]
    pi_3_4 = active_ops["pi_3_4"]

    m = x[:24]
    s = x[24:46]
    theta = x[46:47]

    m_next = (1.0 - coup) * (0.965 * m) + coup * (topo_24 @ m) + coup * (pi_3_4 @ s)
    s_next = (sigma_23 @ s) + coup * (pi_3_4.T @ m)
    theta_next = helical_phase_step(theta, m, s, coup=coup, cuarto_factor=cuarto_factor)

    return np.concatenate([m_next, s_next, theta_next])
