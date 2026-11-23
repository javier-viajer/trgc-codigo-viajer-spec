import json
from pathlib import Path
import re


V17_DIR = Path(__file__).resolve().parent

REQUIRED_10 = [
    "AUDITORIA_v17_modo_a.md",
    "STATUS.md",
    "informe_contrastes_v17.json",
    "certificacion_espectral_v17.json",
    "robustez_certificacion_espectral_v17.json",
    "NOTA_CERTIFICACION_ESPECTRAL_v17.md",
    "ventana_larga_cuasi_estacionariedad_v17.json",
    "verify_v17.py",
    "hooks_47d_map_v17.py",
    "test_long_window_quasistationarity_v17.py",
]

JSON_FILES = [
    "informe_contrastes_v17.json",
    "certificacion_espectral_v17.json",
    "robustez_certificacion_espectral_v17.json",
    "ventana_larga_cuasi_estacionariedad_v17.json",
]


def assert_v17_only(path: Path) -> None:
    resolved = path.resolve()
    if "v1.6" in resolved.parts or "v1.6" in str(resolved):
        raise RuntimeError(f"CONTAMINACION DETECTADA: {resolved}")


def main() -> int:
    cwd = Path.cwd().resolve()
    if "v1.6" in cwd.parts or "v1.6" in str(cwd):
        raise RuntimeError(f"BLOQUEADO: {cwd}")

    present = []
    missing = []
    leaks_v16 = []

    for name in REQUIRED_10:
        p = V17_DIR / name
        assert_v17_only(p)
        if not p.exists() or p.stat().st_size == 0:
            missing.append(name)
            continue
        present.append(name)
        text = p.read_text(encoding="utf-8", errors="replace")
        if re.search(r"(write_text|open\([^)]*v1\.6|mv\s+.*v1\.6|cp\s+.*v1\.6)", text):
            leaks_v16.append(name)

    json_valid = {}
    for jname in JSON_FILES:
        jp = V17_DIR / jname
        try:
            json.loads(jp.read_text(encoding="utf-8"))
            json_valid[jname] = True
        except Exception:
            json_valid[jname] = False

    manifest = {
        "version": "v1.7",
        "step_point": "Punto 4 — Consolidacion final",
        "v1_6_isolated": True,
        "files_present_count": f"{len(present)}/{len(REQUIRED_10)}",
        "present_files": present,
        "missing_files": missing,
        "leaks_v16": leaks_v16,
        "json_valid": json_valid,
        "ready_for_4o_factor_review": (len(present) == len(REQUIRED_10) and len(missing) == 0 and len(leaks_v16) == 0 and all(json_valid.values())),
        "governance_4o_factor": {
            "nivel_II": "retenido",
            "nivel_III": "abierto",
            "auto_promotion": False,
        },
    }

    out = V17_DIR / "manifiesto_consolidacion_v17.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print("[OK] Consolidación Punto 4 | EXIT=0")
    print(f"Archivos presentes: {len(present)}/{len(REQUIRED_10)}")
    print(f"Faltantes: {missing}")
    print(f"Fugas v1.6: {leaks_v16}")
    print(f"ready_for_4o_factor_review: {manifest['ready_for_4o_factor_review']}")
    print("Gobernanza 4º Factor: Nivel II retenido | Nivel III abierto")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
