# Especificación de Contraste: Proxy de Deformación Neimark–Sacker (`test_ns_deformation_proxy`)

**Rama:** `v1.7` (`v17`)  
**Nivel de rigor:** Nivel II (Indicador numérico auxiliar — **no** constituye demostración de bifurcación)  
**Convención de notación:** El símbolo $\lambda$ queda reservado exclusivamente para el **4º Factor**. Los autovalores del Jacobiano proyectado $J_\perp$ se denotan por $\mu_k \in \mathbb{C}$.

---

## 1. Objetivo

Definir un indicador operativo (*proxy*) que detecte si la variación del parámetro de acoplamiento `coup` (y del parámetro del **4º Factor**, `cuarto_factor`) desplaza un par de autovalores complejos conjugados no neutros de $J_\perp = P_\perp J P_\perp$ hacia la circunferencia unidad $|\mu| = 1$ con fase no trivial, sin confundir este indicio con una prueba analítica de bifurcación de Neimark–Sacker.

---

## 2. Definición del Indicador (*Proxy*)

Dado el Jacobiano 47D acoplado $J(\text{coup})$ evaluado en $x_\star$ mediante `compute_jacobian_47d` y su proyección ortogonal $J_\perp$ tras excluir el modo neutro de fase (`neutral_idx = 46`):

1. **Par complejo dominante:** se selecciona el autovalor $\mu_\star = r_\star e^{i \vartheta_\star}$ del bloque no neutro `46x46` que maximiza $|\mu|$ sujeto a $|\operatorname{Im}(\mu)| > \varepsilon_{\text{imag}}$ (con $\varepsilon_{\text{imag}} = 10^{-4}$).
2. **Margen radial a la circunferencia unidad:**
   $$\delta_{\mathrm{NS}}(\text{coup}) = 1 - |\mu_\star(\text{coup})|$$
3. **Tasa de cruce radial:**
   $$\chi_{\mathrm{NS}} = \frac{\Delta |\mu_\star|}{\Delta \text{coup}}$$

---

## 3. Criterios de Evaluación (Aceptación / Alerta)

| Condición observada | Interpretación de auditoría | Estado resultante |
| :--- | :--- | :--- |
| $\delta_{\mathrm{NS}} > 0$ y $\chi_{\mathrm{NS}} \approx 0$ en todo el rango | Régimen transversalmente contractivo sin aproximación a cruce | **Estable subcrítico (sin indicio NS)** |
| $\delta_{\mathrm{NS}} \to 0^+$ con $\chi_{\mathrm{NS}} > 0$ y $\vartheta_\star \notin \{0, \pi\}$ | Indicio numérico de aproximación a bifurcación de Neimark–Sacker | **Proxy positivo — remite a `test_spectral_ns_strict.md`** |
| $\delta_{\mathrm{NS}} \le 0$ sin control de fase ($\vartheta_\star \in \{0, \pi\}$) | Posible bifurcación de silla-nodo o doblamiento de periodo, no NS | **Descartado como NS** |

---

## 4. Limitaciones Explícitas

* Un valor positivo de este *proxy* **no demuestra** la existencia de un toro invariante ni determina el signo del primer coeficiente de Lyapunov (carácter supercrítico o subcrítico).
* Todo resultado positivo exige contraste inmediato bajo los criterios estrictos de `tests/v1_7/test_spectral_ns_strict.md`.
