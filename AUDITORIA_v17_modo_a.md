# AUDITORÍA v1.7 — Modo A (`Modo_A_NS_EW_continuo`)

* **Repositorio / Rama:** Experimental **v1.7** (aislada y separada de **v1.6**)
* **Estado del workspace:** Regenerado y verificado tras reinicio (`informe_contrastes_v17.json`, `verify_v17.py`, `AUDITORIA_v17_modo_a.md`, `STATUS.md`), ampliado con cotas de Gershgorin, normas y proyección del modo neutro de $\theta$, consolidado en `v1.7/certificacion_espectral_v17.json`, verificado en ensemble (`v1.7/robustez_certificacion_espectral_v17.json`, `all_ok = True` en 11 corridas), dotado del **Anexo A (Ejes A–D)**, empaquetado en `v1.7/NOTA_CERTIFICACION_ESPECTRAL_v17.md` (`EXIT=0`), verificado en ventana larga con mapa 47D real (`v1.7/ventana_larga_cuasi_estacionariedad_v17.json`, `EXIT=0`, `quasistationary_ok = True`) y consolidado mediante manifiesto (`v1.7/manifiesto_consolidacion_v17.json`, `EXIT=0`, `10/10` archivos, `Fugas v1.6: []`, `ready_for_4o_factor_review: True`)
* **Verificadores / scripts / artefactos:** `verify_v17.py` (`EXIT=0`), `hooks_47d_map_v17.py`, `test_long_window_quasistationarity_v17.py` (`EXIT=0`), `consolidar_v17_punto4.py` (`EXIT=0`), `v1.7/informe_contrastes_v17.json`, `v1.7/certificacion_espectral_v17.json`, `v1.7/robustez_certificacion_espectral_v17.json`, `v1.7/NOTA_CERTIFICACION_ESPECTRAL_v17.md`, `v1.7/ventana_larga_cuasi_estacionariedad_v17.json` y `v1.7/manifiesto_consolidacion_v17.json`
* **Criterio de gobernanza (4º Factor):** **Nivel II retenido** | **Nivel III abierto**

---

## 1. Alcance, aislamiento de v1.6 y trazabilidad de artefactos

Este registro documenta la auditoría numérica, de contraste, de certificación espectral/normativa, de robustez por ensemble, de contraste formal analítico, de empaquetado documental, de cuasi-estacionariedad en ventana larga y de consolidación final de **v1.7**, conservando la trazabilidad completa tras el reinicio del workspace:

* **Aislamiento de v1.6:** Las pruebas, parámetros, JSON, tablas, scripts, verificaciones, certificados, ensembles, notas formales, pruebas de ventana larga, anexos analíticos y manifiestos de **v1.7** permanecen en su entorno experimental sin modificar ni mezclar la rama base de **v1.6** (`Fugas v1.6: []`).
* **Arquitectura de referencia en v1.7:** La rama **v1.7** opera sobre el espacio de estado **47D** (`mass_24`, `state_22`, `theta`), con grafo de **276 aristas**, acoplamiento $\Pi_{3 \to 4}$, **movimiento helicoidal**, **conexiones del triángulo a la cruz**, **nodos contiguos** y **Matriz de la Suma 23**, en el marco del **Código Viajer**.
* **Trazabilidad documental y analítica:** Tras el reinicio del directorio de trabajo, se regeneraron y verificaron (`EXIT=0`) en `v1.7/` el informe consolidado `informe_contrastes_v17.json` (7 entradas), `verify_v17.py`, `STATUS.md` y `AUDITORIA_v17_modo_a.md`, incorporándose posteriormente las cotas de Gershgorin, normas, proyección del modo neutro de $\theta$, el paquete consolidado **`v1.7/certificacion_espectral_v17.json`**, la comprobación de robustez **`v1.7/robustez_certificacion_espectral_v17.json`** (11 corridas, `all_ok = True`), el **Anexo A (Ejes A, B, C y D)**, la nota formal cerrada **`v1.7/NOTA_CERTIFICACION_ESPECTRAL_v17.md`** (`EXIT=0`), la prueba de ventana larga **`v1.7/ventana_larga_cuasi_estacionariedad_v17.json`** (`EXIT=0`, `quasistationary_ok = True`, `9600` pasos vía `hooks_47d_map_v17.py`) y la consolidación final **`v1.7/manifiesto_consolidacion_v17.json`** (`EXIT=0`, `10/10` archivos, `ready_for_4o_factor_review: True`). Se descartan plantillas vacías (`spectral_grid: []`) como evidencia de ejecución.

---

## 2. Comprobaciones realizadas con `verify_v17.py`

Al ejecutar `verify_v17.py` sobre los artefactos de **v1.7**, el verificador comprueba:

1. **Metadatos y topología:**
   * Confirma `version == "v1.7"` y lee los parámetros de `metadata` (`mode: "Modo_A_NS_EW_continuo"`, `coup: 0.825`, `seed: 42`, `n_steps: 2399`, `start_step: 800`, `source: "grok_execution_v1.7_mode_a"`).
   * Verifica `n_edges == 276` y evalúa las claves de estado 47D (`mass_24`, `state_22`, `theta` / dimensión 47) cuando están presentes en el artefacto.
2. **Dinámica de `dtheta`:**
   * Comprueba que la serie numérica `dtheta` exista, tenga valores finitos y no presente saturación de suelo por encima del umbral permitido (`MAX_STUCK_FRACTION = 0.25`).
   * En la referencia base (`2400` muestras, `min ≈ 0.010`, `max ≈ 0.026`, `2141` valores únicos y saturación mínima `~0.08%`), y en horizonte extendido (`9600` pasos, `2161` valores únicos, `stuck = 0.23%`, deriva inter-ventana `1.14×10⁻⁴`), la trayectoria evoluciona sin colapso ni deriva secular.
3. **Barrido espectral (`spectral_grid`) y panel consolidado:**
   * Valida que `spectral_grid` contenga las **225 filas** esperadas con valores finitos y que `informe_contrastes_v17.json` verifique sin errores (`EXIT=0`).
   * En las filas de 5 columnas `[p1, p2, p3, metric_4, metric_5]`, extrae las métricas espectrales de las columnas finales (`row[3:]`) sin confundir parámetros de barrido o paso con módulos espectrales.
   * Verifica que ninguna entrada supere el umbral `1.0` (`ge1 = 0`, con `max_mod` entre `0.9749` y `0.9900`).

---

## 3. Dictamen base bajo el criterio de 4º Factor

* **Nivel II — Retenido:** La consistencia interna de los metadatos (`n_edges = 276`, `coup = 0.825`, `seed = 42`, `n_steps = 2399`, `start_step = 800`), la ausencia de saturación patológica en `dtheta`, la acotación por debajo de `1.0` (`ge1 = 0` en contrastes), la certificación espectral/normativa consolidada en `v1.7/certificacion_espectral_v17.json`, su estabilidad en el ensemble de 11 corridas (`v1.7/robustez_certificacion_espectral_v17.json`, `all_ok = True`), el cierre documental en `v1.7/NOTA_CERTIFICACION_ESPECTRAL_v17.md` (`EXIT=0`), la cuasi-estacionariedad en ventana larga (`v1.7/ventana_larga_cuasi_estacionariedad_v17.json`, `EXIT=0`, `quasistationary_ok = True`) y el manifiesto consolidado (`10/10` archivos, `Fugas v1.6: []`, `ready_for_4o_factor_review: True`) respaldan **retener el Nivel II**.
* **Nivel III — Abierto:** La evidencia numérica empaquetada, el ensemble de robustez, la nota técnica, la verificación en ventana larga, la estructuración analítica del **Anexo A** y el manifiesto de consolidación **no** ascienden automáticamente a **Nivel III**. El **Nivel III permanece abierto** (sin ascenso automático) a la espera del cierre analítico formal y la revisión de **4º Factor**.

---

## 4. Barrido de sensibilidad (`seed` × `coup`) y revalidación con `verify_v17.py`

Tras resolver la incidencia inicial de ejecución (`EXIT=2`) y dejar `verify_v17.py` operativo en la rama **v1.7** (aislada de **v1.6**), se verificaron **9 corridas** sobre el marco **47D** (`mass_24`, `state_22`, `theta`, **276 aristas**, acoplamiento $\Pi_{3 \to 4}$, **Código Viajer**, **Matriz de la Suma 23**, **movimiento helicoidal**, **conexiones del triángulo a la cruz** y **nodos contiguos**):

### Bloque A — Variación de semilla (`coup = 0.825` fijo)

| `seed` | `EXIT` | `max_mod` | `ge1` | Rango `dθ` | `stuck` | Valores únicos `dθ` |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `42` | `0` | `0.9749` | `0` | `0.010–0.026` | `0.08%` | `2141` |
| `101` | `0` | `0.9749` | `0` | `0.010–0.026` | `0.08%` | `2140` |
| `202` | `0` | `0.9749` | `0` | `0.010–0.026` | `0.08%` | `2142` |
| `303` | `0` | `0.9749` | `0` | `0.010–0.026` | `0.08%` | `2140` |
| `404` | `0` | `0.9749` | `0` | `0.010–0.026` | `0.08%` | `2141` |

### Bloque B — Variación de `coup` alrededor de `0.825` (`seed = 42` fijo)

| `coup` | `EXIT` | `max_mod` | `ge1` | Rango `dθ` | Valores únicos `dθ` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| `0.800` | `0` | `0.9749` | `0` | `0.010–0.026` | `2140` |
| `0.815` | `0` | `0.9749` | `0` | `0.010–0.026` | `2142` |
| `0.825` | `0` | `0.9749` | `0` | `0.010–0.026` | `2141` |
| `0.835` | `0` | `0.9749` | `0` | `0.010–0.026` | `2146` |
| `0.850` | `0` | `0.9749` | `0` | `0.010–0.026` | `2137` |

### Lectura del barrido bajo criterio de 4º Factor

* **Nivel II — Retenido:** Las 9 corridas superan `verify_v17.py` (`EXIT=0`), mantienen `ge1 = 0` (`max_mod ≈ 0.9749`, por debajo del umbral `1.0`) y conservan `dtheta` en `0.010–0.026` con saturación mínima (`~0.08%`).
* **Nivel III — Abierto:** La invariancia local en esta ventana **no** cierra el **Nivel III**, que permanece **abierto** sin ascenso automático.

---

## 5. Campaña de contrastes estructurales en `v1.7` (`informe_contrastes_v17.json`)

* **Rama / Entorno:** `v1.7` (aislada de `v1.6`)
* **Arquitectura de referencia:** espacio **47D** (`mass_24`, `state_22`, `theta`), grafo de **276 aristas**, acoplamiento $\Pi_{3 \to 4}$, **Código Viajer**, **Matriz de la Suma 23**, **movimiento helicoidal**, **conexiones del triángulo a la cruz** y **nodos contiguos**
* **Verificador e informe regenerado:** `verify_v17.py` | `v1.7/informe_contrastes_v17.json` (`EXIT=0`)
* **Estado de campaña:** **Cerrada y regenerada tras reinicio del workspace**
* **Criterio de gobernanza (4º Factor):** **Nivel II retenido** | **Nivel III abierto**

### Panel consolidado de contrastes (`v1.7/informe_contrastes_v17.json`)

| Entrada (`id`) | Ejes OFF | `EXIT` | `max_mod` | `ge1` | Filas `Im≠0` | `unique dθ` | Lectura estructural |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| `referencia` | — (`todo ON`) | `0` | `0.9749` | `0` | `225` | `2141` | Línea base (`seed=42`, `coup=0.825`, `276` aristas `1/dist`) |
| `pi34_off` | $\Pi_{3 \to 4}$ | `0` | `0.9749` | `0` | `225` | `180` | `max_mod` invariante (`0.9749`); cae la variedad de `dθ` (`2141 → 180`) |
| `aristas_276` | pesos `1/dist` (nodos contiguos uniformes) | `0` | `0.9749` | `0` | `225` | `2141` | Efecto nulo en estas métricas frente a la referencia |
| `helicoidal_off` | hélice (`state_22`) | `0` | `0.9900` | `0` | `0` | `2139` | Desaparece `Im≠0` (`225 → 0`) y sube `max_mod` a `0.9900` sin cruzar `1.0` |
| `suma23_off` | Suma 23 | `0` | `0.9900` | `0` | `225` | `2139` | Conserva `Im≠0` (`225`) y sube `max_mod` a `0.9900` sin cruzar `1.0` |
| `helical+s23_off` | hélice + Suma 23 | `0` | `0.9900` | `0` | `0` | `2143` | Sin efecto aditivo extra en `max_mod` (`0.9900`, `ge1 = 0`); `Im≠0` en `0` |
| `ablación completa` | $\Pi_{3 \to 4}$ + hélice + Suma 23 (`los tres`) | `0` | `0.9900` | `0` | `0` | `180` | Espectro real en `0.9900` (`ge1 = 0`, `Im≠0` en `0`) + `dθ` regular/pobre (`180` únicos) |

### Mapa causal consolidado
* **Coherencia con `v1.6`:** `v1.7` permanece aislada; `v1.6` no se modifica ni se mezcla con los artefactos regenerados de `v1.7`.
* **Movimiento helicoidal (`state_22`):** Necesario para las filas con `Im≠0` (`225` con hélice activa frente a `0` al apagarla).
* **Matriz de la Suma 23:** Amortigua o contiene `|λ|` (`0.9749` con Suma 23 activa frente a `0.9900` al apagarla, siempre con `ge1 = 0`).
* **Acoplamiento $\Pi_{3 \to 4}$:** Sostiene la riqueza de `dθ` (`2141` valores únicos en referencia frente a `180` al apagarlo).
* **Pesos de 276 aristas:** Efecto nulo en estas métricas bajo el contraste ejecutado (`2141` únicos, `max_mod = 0.9749`).

---

## 6. Certificación espectral consolidada, robustez por ensemble, nota técnica, ventana larga y manifiesto (`v1.7`)

* **Artefactos:** `v1.7/certificacion_espectral_v17.json`, `v1.7/robustez_certificacion_espectral_v17.json` (`11` corridas, `all_ok = True`), `v1.7/NOTA_CERTIFICACION_ESPECTRAL_v17.md` (`EXIT=0`), `v1.7/ventana_larga_cuasi_estacionariedad_v17.json` (`EXIT=0`, `quasistationary_ok = True`, `9600` pasos vía `hooks_47d_map_v17.py`) y `v1.7/manifiesto_consolidacion_v17.json` (`EXIT=0`, `10/10` archivos, `Fugas v1.6: []`, `ready_for_4o_factor_review: True`)

| Bloque / Eje | Magnitud / Cota | Valor / Rango | ¿$< 1$? | Dictamen técnico |
| :--- | :--- | :---: | :---: | :--- |
| $L_{\text{22}}$ | $\rho(L_{\text{22}})$ numérico | `0.974885` | **Sí** | Medido; coherente con `max_mod ≈ 0.9749 < 1.0` |
| $L_{\text{22}}$ | $\|L_{\text{22}}\|_2$ (norma espectral) | `0.990000` (`[0.990000, 0.990000]`) | **Sí** | **Certifica** $\rho(L_{\text{22}}) \le 0.990000 < 1.0$ en todo el ensemble |
| $L_{\text{22}}$ | Gershgorin (`L_22`) | `1.039248` (`~1.039`) | No | Conservadurismo geométrico; no certifica por sí solo |
| $J_{\text{47}}$ | $\lambda_{\text{neutro}}$ ($\theta$) | `1.000000` | `= 1` | Modo neutro de deslizamiento de fase $\theta$, no inestabilidad |
| $J_{\text{47}}$ | $\rho_{\text{ntriv}}$ | `0.974885` (`max = 0.974885` en 9600 pasos) | **Sí** | Radio espectral no trivial estable por debajo de `1.0` |
| $J_{\text{47}}$ | $\|J_{\text{47}}\|_2$ completo | `1.002126` (`~1.002`) | No | Incluye el modo neutro; no se usa como certificado del bloque `ntriv` |
| $J_{\text{47}}$ | $\|P_\perp J_{\text{47}} P_\perp\|_2$ | `0.990486` (`[0.990483, 0.990489]`; `max = 0.990361` en 9600 pasos) | **Sí** | **Certifica** contracción numérica en el complemento no neutro (`all_ok = True`, `quasistationary_ok = True`) |

### Consolidación Punto 4 (`consolidar_v17_punto4.py` · `manifiesto_consolidacion_v17.json`, `EXIT=0`)
* **Inventario verificado:** `10/10` archivos presentes (`Faltantes: []`), JSON válidos, cero contaminación (`Fugas v1.6: []`) y `ready_for_4o_factor_review: True`.
* **Gobernanza 4º Factor:** **Nivel II retenido** · **Nivel III abierto** · **sin ascenso automático** · `v1.6` aislada.

---

## Anexo A — Contraste Formal Analítico (Ejes A, B, C y D) para Revisión de 4º Factor

* **Gobernanza (4º Factor):** **Nivel II retenido** | **Nivel III abierto** (sin ascenso automático)

### Eje A — Descomposición Espectral, Modo Neutro de $\theta$ y Proyección $P_\perp$ en $J_{\text{47}}$
Para $J_{\text{47}} \in \mathbb{C}^{47 \times 47}$ en la arquitectura **47D** de **v1.7**, $\sigma(J_{\text{47}}) = \{\lambda_{\text{neutro}}(\theta)\} \cup \sigma_{\text{ntriv}}(J_{\text{47}})$ con $\lambda_{\text{neutro}}(\theta) = 1.000000 + 0.000000j$ (deslizamiento neutro de fase $\theta$, no divergencia) y $\rho_{\text{ntriv}}(J_{\text{47}}) = 0.974885 < 1.0$. En el espacio completo de `47` dimensiones, $\rho(J_{\text{47}}) = 1.000000$ y $\|J_{\text{47}}\|_2 = 1.002126$ quedan condicionados por el modo neutro. Con el proyector ortogonal $P_\perp = I_{47} - v_{\text{neutro}} v_{\text{neutro}}^H$ y $J_\perp = P_\perp J_{\text{47}} P_\perp$, se verifica $\rho(J_\perp) = \rho_{\text{ntriv}} = 0.974885 < 1.0$ y $\|P_\perp J_{\text{47}} P_\perp\|_2 = 0.990486 < 1.0$ (`[0.990483, 0.990489]` en el ensemble de 11 corridas, `all_ok = True`, y `max = 0.990361` en `9600` pasos con `quasistationary_ok = True`), con margen lineal nominal en la referencia de $\eta_0 = 1 - 0.990486 = 0.009514$.

### Eje B — Certificación de $L_{\text{22}}$ vía $\|L_{\text{22}}\|_2 = 0.990000$ frente a Gershgorin `1.039248` y Rol de Suma 23 y Movimiento Helicoidal
Para $L_{\text{22}} \in \mathbb{C}^{22 \times 22}$, $\rho(L_{\text{22}}) = 0.974885 \le \|L_{\text{22}}\|_2 = 0.990000 < 1.0 < 1.039248 = \text{Gershgorin}(L_{\text{22}})$. La norma espectral $\|L_{\text{22}}\|_2 = 0.990000 < 1.0$ certifica $\rho(L_{\text{22}}) \le 0.990000 < 1.0$ de forma estable en las 11 corridas (`all_ok = True`), mientras Gershgorin (`1.039248`) sobreestima por sumar módulos absolutos sin compensaciones de fase/signo. El **movimiento helicoidal** aporta la estructura compleja/rotacional (`Im ≠ 0` en `225` filas frente a `0` al apagarlo) y la **Matriz de la Suma 23** ejerce amortiguación espectral (`0.9749` en referencia frente a `0.9900` al desactivarla, siempre con `ge1 = 0`).

### Eje C — Acoplamiento de Bloques (`mass_24`, `state_22`, $\theta$), Topología de 276 Aristas y Rol de $\Pi_{3 \to 4}$
En $z = (m_{24}, s_{22}, \theta) \in \mathbb{C}^{47}$, la proyección $P_\perp$ mantiene $\|P_\perp J_{\text{47}} P_\perp\|_2$ en `[0.990483, 0.990489] < 1.0` (`0.990486` en referencia; `0.990361` en ventana larga de `9600` pasos), apenas `0.000486` por encima de $\|L_{\text{22}}\|_2 = 0.990000$, indicando que los acoplamientos con `mass_24` sobre las **276 aristas** (**Código Viajer**, **conexiones del triángulo a la cruz**, **nodos contiguos**) no desbordan la contracción transversal. En `informe_contrastes_v17.json`, apagar $\Pi_{3 \to 4}$ (`pi34_off`) deja `max_mod = 0.9749` (`ge1 = 0`) pero reduce los valores únicos de `dθ` (`2141 → 180`), y uniformar pesos `1/dist` (`aristas_276`) mantiene `max_mod = 0.9749` y `2141` valores únicos.

### Eje D — Cobertura Paramétrica, Residuo No Lineal y Condiciones para Nivel III
En la dinámica no lineal $z_{k+1} = F(z_k; p)$, el crecimiento transversal satisface $\|\delta z_{\perp, k+1}\|_2 \le (\|J_\perp(p_0)\|_2 + \|\Delta J_\perp(p)\|_2 + L_R(\delta))\|\delta z_{\perp, k}\|_2$. La comprobación de robustez en `v1.7/robustez_certificacion_espectral_v17.json` (`8` semillas y `coup` $\in [0.80, 0.85]`, `all_ok = True`) y la prueba en ventana larga de `9600` pasos (`v1.7/ventana_larga_cuasi_estacionariedad_v17.json`, `EXIT=0`, `quasistationary_ok = True`, deriva inter-ventana `1.14×10⁻⁴`, `stuck = 0.23%`) respaldan la estabilidad en horizonte extendido; el cierre del **Nivel III** ante **4º Factor** sigue sujeto a la revisión colegiada y al cierre analítico formal.
