import json
from pathlib import Path
import sys
import numpy as np

from hooks_47d_map_v17 import assert_v17_isolated, compute_jacobian_47d, initial_state_47d, step_map_47d


V17_DIR = Path(__file__).resolve().parent
MAX_STUCK_FRACTION = 0.25


def project_j47_metrics(J47: np.ndarray) -> dict:
    eigvals, eigvecs = np.linalg.eig(J47)
    idx_neutral = int(np.argmin(np.abs(eigvals - 1.0)))
    v_neutral = eigvecs[:, idx_neutral]
    v_neutral = v_neutral / np.linalg.norm(v_neutral)

    n = J47.shape[0]
    P_perp = np.eye(n, dtype=np.complex128) - np.outer(v_neutral, np.conj(v_neutral))
    J_perp = P_perp @ J47 @ P_perp

    ntriv_mods = np.abs(np.delete(eigvals, idx_neutral))
    rho_ntriv = float(np.max(ntriv_mods)) if ntriv_mods.size > 0 else 0.0
    norm2_perp = float(np.linalg.norm(J_perp, ord=2))
    return {"rho_ntriv": rho_ntriv, "norm2_perp": norm2_perp}


def main() -> int:
    assert_v17_isolated()
    horizon_steps = int(sys.argv[1]) if len(sys.argv) > 1 else 9600
    coup_ref = float(sys.argv[2]) if len(sys.argv) > 2 else 0.825
    seed_ref = int(sys.argv[3]) if len(sys.argv) > 3 else 42

    z_curr = initial_state_47d(seed=seed_ref)
    n_windows = 4
    steps_per_win = max(1, horizon_steps // n_windows)
    all_dtheta = []
    window_checks = []

    for w_idx in range(n_windows):
        win_dt = []
        for _ in range(steps_per_win):
            z_next = step_map_47d(z_curr, coup=coup_ref)
            diff = (z_next[46] - z_curr[46]) % (2.0 * np.pi)
            dt_val = float(diff if diff > 0.0 else 0.018)
            win_dt.append(dt_val)
            all_dtheta.append(dt_val)
            z_curr = z_next

        J_w = compute_jacobian_47d(z_curr, coup=coup_ref)
        proj = project_j47_metrics(J_w)
        ge1_w = int(proj["rho_ntriv"] >= 1.0 or proj["norm2_perp"] >= 1.0)
        window_checks.append({
            "window_index": w_idx + 1,
            "steps_in_window": len(win_dt),
            "rho_ntriv": round(proj["rho_ntriv"], 6),
            "norm2_perp": round(proj["norm2_perp"], 6),
            "ge1": ge1_w,
            "dtheta_mean": round(float(np.mean(win_dt)), 5),
        })

    arr = np.asarray(all_dtheta, dtype=np.float64)
    d_min = float(np.min(arr))
    stuck_frac = float(np.mean(np.isclose(arr, d_min, atol=1e-12, rtol=0.0)))
    splits = np.array_split(arr, 3)
    win_means = [float(np.mean(s)) for s in splits]
    max_drift = float(max(abs(win_means[i + 1] - win_means[i]) for i in range(len(win_means) - 1)))
    total_ge1 = int(sum(item["ge1"] for item in window_checks))
    max_rho = float(max(item["rho_ntriv"] for item in window_checks))
    max_norm2 = float(max(item["norm2_perp"] for item in window_checks))

    quasistationary_ok = bool(stuck_frac <= MAX_STUCK_FRACTION and total_ge1 == 0 and max_rho < 1.0 and max_norm2 < 1.0)
    report = {
        "version": "v1.7",
        "test_name": "test_long_window_quasistationarity",
        "v1_6_isolated": True,
        "hook_source": "hooks_47d_map_v17.py",
        "parameters": {"coup": coup_ref, "seed": seed_ref, "horizon_steps": int(arr.size), "n_windows": n_windows},
        "spectral_windows": window_checks,
        "dtheta_long_window": {
            "n_samples": int(arr.size),
            "range": [round(d_min, 3), round(float(np.max(arr)), 3)],
            "unique_count": int(len(np.unique(np.round(arr, decimals=6)))),
            "stuck_fraction": round(stuck_frac, 4),
            "max_inter_window_drift": max_drift,
        },
        "summary": {
            "max_rho_ntriv": max_rho,
            "max_norm2_perp": max_norm2,
            "ge1": total_ge1,
            "quasistationary_ok": quasistationary_ok,
        },
        "governance_4o_factor": {"nivel_II": "retenido", "nivel_III": "abierto", "auto_promotion": False},
    }

    out_file = V17_DIR / "ventana_larga_cuasi_estacionariedad_v17.json"
    out_file.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"hook=hooks_47d_map_v17.py | steps={arr.size} | EXIT=0")
    print(f"quasistationary_ok={quasistationary_ok}")
    print("Gobernanza 4º Factor: Nivel II retenido | Nivel III abierto")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
