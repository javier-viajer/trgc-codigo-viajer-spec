# Estado del Modelo — TRCG / Pirámide-Parábola (v17)

Este documento registra el estado de validación formal, numérica y de gobernanza del modelo **Pirámide-Parábola / TRCG** en la versión **`v17`** (`v1.7`), bajo los criterios de rigor acordados con el panel de **4º Factor**.

---

## 1. Resumen de Estado por Niveles de Rigor

| Nivel | Alcance | Estado | Situación en v17 |
| :--- | :--- | :--- | :--- |
| **Nivel I** | Álgebra del soporte, simetría y análisis lineal local | **Cerrado (Analítico)** | Discretización en $N = 24$ nodos sobre envolvente parabólica, simetría $G \cong \mathbb{Z}_4$, conteo de órbitas por Burnside ($4\,195\,360$ clases para $q = 2$), espacio diádico de **276 grados de libertad** ($252$ transversales + $23$ longitudinales + $1$ escala/masa) y umbral lineal $\gamma_c = \frac{12}{11} \approx 1.0909$ en torno al equilibrio homogéneo $R_\star$. |
| **Nivel II** | Dinámica acoplada 47D, certificación espectral y aislamiento | **En cierre / Operadores refinados** | Operadores en `dynamics/topology_276.py` y `dynamics/coupling_47d.py` refinados con simetría $\mathbb{Z}_4$, determinismo y `cuarto_factor`, junto a `dynamics/jacobian_47d.py`. Verificados los **6 tests** en `pytest` (`0.16s`, `EXIT=0`) con aislamiento estricto frente a `v1.6`. **Pendiente para cierre total:** contrastar regímenes dinámicos con toda la batería de `tests/` y acotar sensibilidad paramétrica en barridos amplios. |
| **Nivel III** | Dinámica no lineal, bifurcación y acoplamiento completo | **Abierto** | Formalización axiomática en curso (operador de actualización coherente $\Omega_c$, proyector ortogonal $P_c^{(4)}$ sobre $\mathcal{H}_{R_4}$ y cooperación $W_R$, Episodios 40–41). Siguen abiertas las demostraciones analíticas y la validación global del acoplamiento con el **4º Factor**. |

---

## 2. Verificaciones Superadas en v17 (6 Tests en `pytest` — `EXIT=0`)

Con los operadores refinados y el Jacobiano 47D derivado del mapa acoplado (`step_47d`), quedan verificados:

1. **Simetría $\mathbb{Z}_4$ y conmutación exacta (`test_z4_generator_order_and_exact_commutation`):** orden de grupo $P^4 = I$ sobre los 24 nodos y conmutación exacta $P T_{24} = T_{24} P$.
2. **Simetría de operadores y determinismo (`test_operator_symmetry_and_determinism`):** $T_{24} = T_{24}^\top$, $\Sigma_{23} = \Sigma_{23}^\top$ y construcción determinista sin dependencias aleatorias fluctuantes.
3. **Paso acoplado con `cuarto_factor` y modo neutro (`test_coupled_step_and_neutral_mode_with_refined_ops`):** `step_47d` devuelve forma `(47,)` con valores finitos integrando `cuarto_factor`, y la proyección sobre el complemento del modo neutro (índice `46`) se conserva intacta.
4. **Dependencia de `coup` y acoples fuera de la diagonal (`test_jacobian_depends_on_coup_and_rho_changes`, `test_off_diagonal_couplings_reflect_interaction_strength`, `test_neutral_mode_projection_at_index_46`):** $J$ y $\rho_{\mathrm{ntriv}}$ varían al modificar `coup`; los bloques cruzados entre `m` y `s` son nulos para `coup = 0.0` y activos para `coup > 0`; y la fila/columna `46` queda proyectada correctamente.
5. **Coherencia de certificados y aislamiento de rama:** se mantienen consistentes los artefactos JSON (`informe_contrastes_v17.json`, `certificacion_espectral_v17.json`, `cotas_normas_gershgorin_v17.json`) y las salvaguardas frente a rutas de `v1.6`.

---

## 3. Batería de Verificación (`tests/`)

* `tests/test_jacobian_47d_coupling.py`: dependencia espectral de `coup`, bloques fuera de la diagonal y proyección del modo neutro (índice 46).
* `tests/test_z4_symmetry_and_operators.py`: orden $P^4 = I$, conmutación con $\mathbb{Z}_4$, simetría/determinismo de operadores y paso acoplado con `cuarto_factor`.
* `tests/test_ns_deformation_proxy.md`: indicador aproximado (*proxy*) de deformación de tipo Neimark–Sacker.
* `tests/v1_7/test_spectral_ns_strict.md`: criterio espectral estricto sobre radio espectral, cruce de la circunferencia unidad y condiciones de no resonancia.
* `tests/v1_7/test_long_window_quasistationarity.md`: evaluación de cuasi-estacionariedad y persistencia de regímenes en ventanas temporales largas.

---

## 4. Puntos Críticos Abiertos (Directriz de Validación — 4º Factor)

El cierre de **Nivel II** y la resolución del **Nivel III** continúan sujetos a:

1. **Sensibilidad paramétrica y de semilla en régimen acoplado:** extender las pruebas a barridos sistemáticos de `coup`, `cuarto_factor` y condiciones iniciales.
2. **Cruce espectral y no resonancia:** determinar las condiciones exactas de cruce de la circunferencia unidad con fase no trivial y ausencia de resonancias fuertes
