"""Módulos dinámicos y espectrales en 47D para la rama v1.7 del modelo TRCG / Pirámide-Parábola."""

from dynamics.coupling_47d import (
    build_pi_3_to_4,
    build_sigma_23_operator,
    helical_phase_step,
    step_47d,
)
from dynamics.jacobian_47d import (
    compute_jacobian_47d,
    project_non_neutral,
)
from dynamics.topology_276 import (
    build_edges_276,
    build_parabolic_coordinates,
    build_z4_permutation_matrix,
)

__all__ = [
    "build_edges_276",
    "build_parabolic_coordinates",
    "build_pi_3_to_4",
    "build_sigma_23_operator",
    "build_z4_permutation_matrix",
    "compute_jacobian_47d",
    "helical_phase_step",
    "project_non_neutral",
    "step_47d",
]
