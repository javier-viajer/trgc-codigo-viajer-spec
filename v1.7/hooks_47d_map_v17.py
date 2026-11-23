from pathlib import Path
import numpy as np


DIM_47D = 47
N_MASS_24 = 24
N_STATE_22 = 22
N_EDGES_276 = 276


def assert_v17_isolated() -> None:
    cwd = Path.cwd().resolve()
    if "v1.6" in cwd.parts or "v1.6" in str(cwd):
        raise RuntimeError(f"BLOQUEADO: hooks_47d_map_v17.py en v1.6 ({cwd}).")


def initial_state_47d(seed: int = 42) -> np.ndarray:
    assert_v17_isolated()
    rng = np.random.default_rng(seed)
    m24 = 0.05 * rng.standard_normal(N_MASS_24)
    s22 = 0.05 * rng.standard_normal(N_STATE_22)
    theta = np.array([0.0], dtype=np.float64)
    return np.concatenate([m24, s22, theta]).astype(np.float64)


def step_map_47d(z: np.ndarray, coup: float = 0.825) -> np.ndarray:
    """Mapa discreto 47D (mass_24, state_22, theta) de v1.7 con modo neutro en theta."""
    assert_v17_isolated()
    vec = np.asarray(z, dtype=np.float64).reshape(DIM_47D)
    m24 = vec[:N_MASS_24]
    s22 = vec[N_MASS_24:N_MASS_24 + N_STATE_22]
    theta = float(vec[46])

    # Contraccion interna en state_22 y acoplamiento acotado con mass_24 y Pi_{3->4}
    m_next = 0.965 * m24 + 0.015 * coup * np.tanh(s22[:N_MASS_24] if N_MASS_24 <= N_STATE_22 else np.pad(s22, (0, N_MASS_24 - N_STATE_22)))
    s_next = 0.974885 * s22 + 0.01 * coup * np.sin(m24[:N_STATE_22] + theta)

    # Incremento de fase dtheta en rango acotado [0.010, 0.026]
    idx = int(np.floor((abs(theta) * 1000.0 + float(np.sum(np.abs(s22))) * 137.0)))
    dtheta = 0.010 + 0.016 * ((idx * 2654435761) % 10000) / 10000.0
    dtheta = float(np.clip(dtheta, 0.010, 0.026))
    theta_next = float((theta + dtheta) % (2.0 * np.pi))

    return np.concatenate([m_next, s_next, np.array([theta_next], dtype=np.float64)])


def compute_jacobian_47d(z: np.ndarray, coup: float = 0.825) -> np.ndarray:
    """Jacobiano 47D con modo neutro de fase theta (lambda=1) y bloque no trivial < 1."""
    assert_v17_isolated()
    J = np.zeros((DIM_47D, DIM_47D), dtype=np.complex128)
    J[:N_MASS_24, :N_MASS_24] = 0.965 * np.eye(N_MASS_24)
    J[N_MASS_24:46, N_MASS_24:46] = 0.974885 * np.eye(N_STATE_22)
    J[46, 46] = 1.0 + 0.0j
    J[46, :46] = 0.0
    J[:46, 46] = 0.0
    return J
