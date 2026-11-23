"""Cálculo numérico del Jacobiano 47D y proyección sobre el complemento ortogonal del modo neutro."""

from __future__ import annotations

import numpy as np

from dynamics.coupling_47d import step_47d


def compute_jacobian_47d(
    state: np.ndarray,
    coup: float,
    ops: dict[str, np.ndarray] | None = None,
    eps: float = 1e-7,
    cuarto_factor: float = 0.0,
) -> np.ndarray:
    """Calcula J = dF/dx en R^{47x47} mediante diferencias finitas centradas alrededor de `state`."""
    if eps <= 0.0:
        raise ValueError("eps debe ser estrictamente positivo.")

    x = np.asarray(state, dtype=float)
    if x.shape != (47,):
        raise ValueError(f"Se esperaba un vector de estado de forma (47,), recibido {x.shape}.")

    dim = x.size
    jac = np.zeros((dim, dim), dtype=float)

    for col in range(dim):
        delta = np.zeros(dim, dtype=float)
        delta[col] = eps
        f_plus = step_47d(x + delta, coup=coup, ops=ops, cuarto_factor=cuarto_factor)
        f_minus = step_47d(x - delta, coup=coup, ops=ops, cuarto_factor=cuarto_factor)
        jac[:, col] = (f_plus - f_minus) / (2.0 * eps)

    return jac


def project_non_neutral(
    jacobian: np.ndarray,
    neutral_idx: int = 46,
) -> tuple[np.ndarray, float, float]:
    """Proyecta J sobre el subespacio ortogonal al modo de fase (por defecto índice 46).

    Devuelve `(j_perp, rho_ntriv, norm_j_perp)`.
    """
    jac = np.asarray(jacobian, dtype=float)
    if jac.ndim != 2 or jac.shape[0] != jac.shape[1]:
        raise ValueError("jacobian debe ser una matriz cuadrada.")

    dim = jac.shape[0]
    if not (0 <= neutral_idx < dim):
        raise IndexError("neutral_idx fuera de rango para el tamaño del Jacobiano.")

    proj_perp = np.eye(dim, dtype=float)
    proj_perp[neutral_idx, neutral_idx] = 0.0

    j_perp = proj_perp @ jac @ proj_perp
    mask = [i for i in range(dim) if i != neutral_idx]
    j_sub = jac[np.ix_(mask, mask)]

    eigvals = np.linalg.eigvals(j_sub)
    rho_ntriv = float(np.max(np.abs(eigvals))) if eigvals.size > 0 else 0.0
    norm_j_perp = float(np.linalg.norm(j_perp, ord=2))
    return j_perp, rho_ntriv, norm_j_perp
