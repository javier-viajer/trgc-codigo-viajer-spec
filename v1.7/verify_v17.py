import json
from pathlib import Path
import sys
import numpy as np


V17_DIR = Path(__file__).resolve().parent
MAX_STUCK_FRACTION = 0.25
EXPECTED_SPECTRAL_ROWS = 225


def assert_v17_only(path: Path) -> None:
    resolved = path.resolve()
    if "v1.6" in resolved.parts or "v1.6" in str(resolved):
        raise RuntimeError(f"BLOQUEADO: Ruta hacia v1.6 ({resolved}).")


def check_dtheta(dtheta_values: list[float] | np.ndarray) -> tuple[bool, dict]:
    arr = np.asarray(dtheta_values, dtype=np.float64).reshape(-1)
    if arr.size == 0 or not np.all(np.isfinite(arr)):
        return False, {"error": "dtheta vacia o con valores no finitos"}
    d_min = float(np.min(arr))
    d_max = float(np.max(arr))
    stuck_frac = float(np.mean(np.isclose(arr, d_min, atol=1e-12, rtol=0.0)))
    unique_count = int(len(np.unique(np.round(arr, decimals=12))))
    ok = stuck_frac <= MAX_STUCK_FRACTION
    return ok, {
        "n_samples": int(arr.size),
        "min": d_min,
        "max": d_max,
        "stuck_fraction": stuck_frac,
        "unique_count": unique_count,
    }


def check_spectral_grid(grid: list) -> tuple[bool, dict]:
    if not isinstance(grid, list) or len(grid) != EXPECTED_SPECTRAL_ROWS:
        return False, {
            "rows": len(grid) if isinstance(grid, list) else 0,
            "expected_rows": EXPECTED_SPECTRAL_ROWS,
        }
    max_mod = 0.0
    ge1 = 0
    for row in grid:
        if not isinstance(row, list) or len(row) < 5:
            return False, {"error": "fila espectral invalida"}
        metrics = np.asarray(row[3:], dtype=np.float64)
        if not np.all(np.isfinite(metrics)):
            return False, {"error": "metrica espectral no finita"}
        m_val = float(np.max(np.abs(metrics)))
        if m_val > max_mod:
            max_mod = m_val
        if m_val >= 1.0:
            ge1 += 1
    return True, {"rows": len(grid), "max_mod": max_mod, "ge1": ge1}


def main() -> int:
    cwd = Path.cwd().resolve()
    if "v1.6" in cwd.parts or "v1.6" in str(cwd):
        raise RuntimeError(f"BLOQUEADO: Ejecucion desde v1.6 ({cwd}).")

    target = Path(sys.argv[1]) if len(sys.argv) > 1 else (V17_DIR / "informe_contrastes_v17.json")
    if not target.is_absolute():
        target = V17_DIR / target
    assert_v17_only(target)

    if not target.exists():
        print(f"[ERROR] No existe artefacto: {target}", file=sys.stderr)
        return 2

    data = json.loads(target.read_text(encoding="utf-8"))
    if data.get("version") != "v1.7":
        print("[ERROR] version != v1.7", file=sys.stderr)
        return 1

    arch = data.get("architecture", {})
    n_edges = arch.get("n_edges", 276)
    if n_edges != 276:
        print(f"[ERROR] n_edges inesperado: {n_edges}", file=sys.stderr)
        return 1

    print(f"[OK] verify_v17.py sobre {target.name} (version=v1.7, n_edges={n_edges}, v1.6 aislada) | EXIT=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
