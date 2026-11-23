# Especificación de Contraste: Cuasi-Estacionariedad en Ventana Larga (`test_long_window_quasistationarity`)

**Rama:** `v1.7` (`v17`)  
**Nivel de rigor:** Nivel II (Persistencia temporal y estabilidad empírica en ventanas largas)  
**Aislamiento:** Ejecución exclusiva sobre `dynamics/` de `v1.7`; prohibido el acceso a `v1.6`.  
**Convención de notación:** El símbolo $\lambda$ queda reservado exclusivamente para el **4º Factor**.

---

## 1. Objetivo

Evaluar si las trayectorias generadas por `step_47d` en un régimen acoplado (`coup > 0`) mantienen acotamiento, invariancia de norma transversal y ausencia de deriva secular o colapso numérico a lo largo de ventanas temporales largas, distinguiendo entre convergencia a punto fijo, órbita cuasi-periódica acotada e inestabilidad.

---

## 2. Protocolo de Simulación

1. **Horizonte temporal:**
   * Tramo de transitorio descartado: $T_{\text{burn}} = 5\,000$ iteraciones.
   * Ventana de medición: $T_{\text{win}} = 20\,000$ iteraciones adicionales ($t \in [5\,000, 25\,000]$), subdividida en $K = 4$ subventanas consecutivas $W_1, W_2, W_3, W_4$ de $5\,000$ pasos cada una.
2. **Observables registrados en cada subventana $W_j$:**
   * Norma euclídea del bloque estructural de 24 nodos: $M(t) = \|m(t)\|_2$.
   * Norma euclídea del bloque relacional de 22 modos: $S(t) = \|s(t)\|_2$.
   * Radio espectral no trivial instantáneo $\rho_{\text{ntriv}}(t)$ evaluado periódicamente mediante `compute_jacobian_47d` y `project_non_neutral`.
   * Coherencia de fase en el soporte $\mathbb{Z}_4$ (varianza transversal entre las 6 órbitas de 4 nodos).

---

## 3. Criterios Cuantitativos de Cuasi-Estacionariedad

Se considera que la trayectoria supera el contraste de cuasi-estacionariedad en ventana larga si se cumplen todas las condiciones siguientes:

1. **Acotamiento uniforme (sin divergencia ni `NaN`/`Inf`):**
   $$\sup_{t \in [0, 25\,000]} \|(m(t), s(t))\|_2 < B_{\max} \quad (\text{finito y estable en todas las semillas})$$
2. **Estacionariedad estadística entre subventanas $W_1, \dots, W_4$:**
   La deriva relativa de medias y desviaciones típicas entre la primera subventana ($W_1$) y la última ($W_4$) satisface:
   $$\frac{|\langle M \rangle_{W_4} - \langle M \rangle_{W_1}|}{\max(\langle M \rangle_{W_1}, 10^{-8})} < 10^{-3}, \qquad \frac{|\sigma(M)_{W_4} - \sigma(M)_{W_1}|}{\max(\sigma(M)_{W_1}, 10^{-8})} < 5 \times 10^{-3}$$
   (y de forma análoga para $S(t)$).
3. **Consistencia espectral transversal:**
   A lo largo de la ventana de medición, el radio espectral no trivial $\rho_{\text{ntriv}}(t)$ no exhibe crecimiento secular no acotado ($\rho_{\text{ntriv}}(t) \le 1 + \varepsilon_{\text{tol}}$ en regímenes acotados y $\rho_{\text{ntriv}}(t) < 1$ en regímenes contractivos).

---

## 4. Registro de Resultados

Los resultados de este contraste deben serializarse en un artefacto JSON propio de `v1.7` (por ejemplo, `informe_quasistationarity_v17.json`), indicando explícitamente:
* Valores de `coup`, `cuarto_factor` y semillas evaluadas.
* Métricas por subventana ($W_1 \dots W_4$).
* Etiqueta explícita del régimen observado (`contractivo_punto_fijo`, `acotado_cuasiperiodico` o `inestable`), sin inferir estabilidad global fuera de la cuenca muestreada.
