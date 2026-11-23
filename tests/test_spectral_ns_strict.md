# Especificación de Contraste Estricto: Criterio Espectral Neimark–Sacker (`test_spectral_ns_strict`)

**Rama:** `v1.7` (`v17`)  
**Nivel de rigor:** Nivel II $\to$ Nivel III (Criterio espectral estricto de bifurcación)  
**Aislamiento:** Prohibida cualquier importación o referencia a rutas de `v1.6`.  
**Convención de notación:** El símbolo $\lambda$ queda reservado exclusivamente para el **4º Factor**; los autovalores espectrales se denotan por $\mu_k$.

---

## 1. Propósito

Establecer las condiciones espectrales mínimas necesarias (aunque todavía no suficientes sin el cálculo del coeficiente cúbico) para certificar un cruce limpio de tipo Neimark–Sacker en el mapa discreto 47D acoplado `step_47d` tras proyectar el modo neutro de fase (`neutral_idx = 46`).

---

## 2. Condiciones Espectrales Requeridas en $\text{coup} = \text{coup}_c$

Para el espectro $\{\mu_1, \dots, \mu_{46}\}$ del bloque no neutro $J_{\text{sub}}$ obtenido mediante `project_non_neutral(J, neutral_idx=46)`:

1. **Par complejo conjugado único en el borde unidad:**
   Existe un único par complejo conjugado $\mu_{1,2}(\text{coup}_c) = e^{\pm i \vartheta_c}$ con $0 < \vartheta_c < \pi$ tal que:
   $$\big||\mu_{1,2}(\text{coup}_c)| - 1\big| < \text{tol}_{\text{rad}} \quad (\text{con } \text{tol}_{\text{rad}} = 10^{-6})$$
2. **Separación espectral estricta del resto de modos:**
   Todos los demás autovalores no neutros permanecen estrictamente en el interior del disco unidad con brecha acotada:
   $$\max_{k \ge 3} |\mu_k(\text{coup}_c)| \le 1 - \Delta_{\text{gap}} \quad (\text{con } \Delta_{\text{gap}} \ge 5 \times 10^{-3})$$
3. **Condición de transversalidad:**
   $$\left.\frac{d|\mu_1(\text{coup})|}{d\,\text{coup}}\right|_{\text{coup}=\text{coup}_c} > 0$$
4. **Ausencia de resonancias fuertes ($q = 1, 2, 3, 4$):**
   $$e^{i q \vartheta_c} \neq 1 \quad \text{para } q \in \{1, 2, 3, 4\}$$
   (es decir, $\vartheta_c \notin \{0, \pi, \frac{2\pi}{3}, \frac{\pi}{2}\}$ dentro de una banda de exclusión de $\pm 10^{-3}\text{ rad}$).

---

## 3. Veredicto de Auditoría

* **PASS (Espectral):** se cumplen simultáneamente las cuatro condiciones anteriores sobre el Jacobiano acoplado `compute_jacobian_47d`. Habilita el paso al análisis de forma normal (signo del coeficiente cúbico de Lyapunov, Punto Crítico 3 de `STATUS.md`).
* **FAIL / RETAINED:** si existe degeneración de múltiples pares en el borde unidad, resonancia fuerte ($q \le 4$) o ausencia de transversalidad, el régimen queda retenido en **Nivel II** sin ascenso.
