# STATUS.md — Estado Epistemológico y Auditoría Técnica (`v1.7`)

**Versión canónica:** `v1.7`  
**Fecha:** 23 de noviembre de 2026  
**Gobernanza:** **Nivel II retenido · Nivel III abierto** (sin ascenso automático)  
**Aislamiento de versión:** `v1.6` aislada (`Fugas v1.6: []`)  
**Reserva de notación:** El símbolo $\lambda$ queda estrictamente reservado al **4º Factor** (sometido a validación o refinamiento de **4º Factor**).

---

## 1. Marco de Gobernanza y Frontera Epistemológica

* **Código Viajer (`v1.7`):** Validador dinámico operativo en $\mathbb{R}^4$ con decisiones `ALLOW` / `THROTTLE` / `REJECT` sobre estado $\mathbf{X} = (L, S, I, B) \in [0,1]^4$.
* **TRCG / Pirámide-Parábola (`core/`, `dynamics/`, `boundary/`):** Marco matemático en desarrollo. No se afirma como teoría física completa.
* **Nivel II retenido:** Consistencia estructural, derivación interna desde la 2-sección de los 264 triples, propiedades espectrales de $J_{24\times 24}$, variaciones explícitas de $\tilde{V}(T)$ con condiciones suficientes de monotonía en régimen asíncrono, análisis modal $\mathbb{Z}_4$ ($m=0,1,2,3$) y trazabilidad numérica afinada.
* **Nivel III abierto:** Permanece abierto **sin ascenso automático**. La estabilidad dinámica o consistencia estructural sobre una arquitectura dada no acredita **emergencia espontánea** desde bases no pre-codificadas ni cierra la formalización de $\lambda$.
* **Aislamiento de `v1.6`:** `v1.6` permanece aislada (`Fugas v1.6: []`).

---

## 2. Verificación Estructural y Espectral de $J_{24\times 24}$ (264 Triples de $R$)

* **Derivación interna:** Estructura binaria/relacional $E_R$ y acoplamientos $J_{24\times 24}$ derivados directamente de la 2-sección de los **264 triples** ($4 \times 6 = 24$ nodos), sin distancias geométricas externas.
* **Comprobación matricial y bloques $6\times 6$ bajo $\mathbb{Z}_4$ ($U = F_4 \otimes I_6$):**
  * Simetría $J = J^\top$: `0.00e+00` (exacta).
  * Diagonal nula: `0.00` · Traza: `0.0`.
  * Equivariancia $\mathbb{Z}_4$ (error relativo): `0.00` (exacta).
  * Hermiticidad de los cuatro bloques de $6\times 6$ ($\widehat{J}^{(0)}, \widehat{J}^{(1)}, \widehat{J}^{(2)}, \widehat{J}^{(3)}$): $\sim 10^{-16}$ o mejor.
  * Conjugación entre bloques rotacionales opuestos ($m=1$ y $m=3$): $\|\widehat{J}^{(3)} - \overline{\widehat{J}^{(1)}}\|_F = 3.26 \times 10^{-16}$ (mismo espectro real).
  * Reconstrucción espectral (bloques frente a $J_{24\times 24}$ completa): error `4.50e-14`, espectro completo en `[-14.959, 72.226]` (valores extremos concentrados en $m=0$; modos transversales en $m=1,2,3$).
* **Criterios de positividad deslindados:** (1) entradas/pesos no negativos, (2) semidefinición/definición positiva espectral o cuadrática (donde simetría con diagonal/traza nula y $M \succeq 0$ obliga a $M = 0$), y (3) dominio admisible y función barrera logarítmica.

---

## 3. Variaciones de $\tilde{V}(T)$ y Monotonía Asíncrona

* **Actualización asíncrona (secuencial, 1 nodo por paso):** Condiciones de estabilidad no intercambiables directamente con la actualización síncrona.
* **Expresiones de variación ($\Delta \tilde{V} = \tilde{V}(T') - \tilde{V}(T)$) para un cambio en el nodo $a$:**
  * Transición $0 \to 1$ ($h_a(T) \ge \theta_{\text{on}}$): $\Delta \tilde{V}_{0\to 1}(T; a) = -h_a(T) + \Delta \Phi_a$.
  * Transición $1 \to 0$ ($h_a(T) \le \theta_{\text{off}}$): $\Delta \tilde{V}_{1\to 0}(T; a) = h_a(T) - \Delta \Phi_a$.
  * Sin cambio ($\Delta T_a = 0$): $\Delta \tilde{V} = 0$.
* **Condiciones suficientes de monotonía ($\Delta \tilde{V} \le 0$):** Actualización secuencial (1 nodo/paso), simetría $J_{ac} = J_{ca}$, banda de histéresis no degenerada $\theta_{\text{off}} < \theta_{\text{on}}$ con $\theta_{\text{off}} \le \Delta\Phi_a \le \theta_{\text{on}}$, y acotación inferior de $\tilde{V}$ sobre el espacio finito $\{0,1\}^{24}$ (impidiendo ciclos infinitos y garantizando convergencia a estados retenidos).
* **Modos transversales ($m=1,2,3$) bajo histéresis:** La saturación binaria $\{0,1\}$ y la banda $[\theta_{\text{off}}, \theta_{\text{on}}]$ mezclan energía entre modos y permiten sostener estados retenidos no uniformes ($m=1,3$ ligados a giros/desfases helicoidales y nodos contiguos; $m=2$ a alternancia opuesta / conexiones triángulo–cruz) sin romper la monotonía asíncrona de $\tilde{V}(T)$.

---

## 4. Estado del Protocolo N1–N4 y Candidatura de $\lambda(R)$

* **N1 (30 semillas, 24 nodos / 264 triples):** Última corrida con ocupación final `0.000`, residuo $\mathbb{Z}_4$ `0.0000`, $P_{\text{sel,estricta}} = 0.00$ y `30/30 saturated_or_empty` (colapso al estado vacío por ajuste de umbral/sesgo; pendiente calibración en régimen no vacío).
* **N3 (perturbación no $\mathbb{Z}_4$-equivariante):** Error normalizado $E_{\text{eq}}$ lineal con $\epsilon \in \{0, 0.05, 0.10, 0.20\}$ (`0.000`, `0.0111`, `0.0222`, `0.0444`); pendiente complementar con `hamming_diff_frac` en régimen no vacío.
* **N4 (relajación lineal auxiliar, 10 pasos):** Error inicial `12.2764`, error final `0.6913`, ratio `0.0563`, $\alpha$ implícito `0.2500` ($(1-0.25)^{10} \approx 0.05631$).
* **Candidato $\lambda(R)$ (sujeto a revisión de 4º Factor):**
  $$\lambda(R) = 1 - \frac{\|P_{\mathbb{Z}_4} R P_{\mathbb{Z}_4}^\top - R\|_F}{\|P_{\mathbb{Z}_4} R P_{\mathbb{Z}_4}^\top\|_F + \|R\|_F + \varepsilon}$$
  formulado frente a los seis requisitos formales, reservando estrictamente el símbolo $\lambda$ al **4º Factor**.

---

## 5. Registro Dinámico $J_{24\times 24}$ (Régimen No Vacío) — [FECHA]

- **Versión / Gobernanza:** `v1.7` · Nivel II retenido · Nivel III abierto (sin ascenso automático)
- **Aislamiento de versión:** `v1.6` aislada (`Fugas v1.6: []`)
- **Reserva de notación:** $\lambda$ reservado en exclusiva al **4º Factor**
- **Núcleo y régimen:** $N = 24$ ($4 \times 6$), 264 triples de $R$ · Actualización asíncrona (1 nodo/paso) · Parámetros: $b_a = [\,]$, $\theta_{\text{off}} = [\,]$, $\theta_{\text{on}} = [\,]$, $\Delta\Phi_a = [\,]$, semillas = `30`.

### 5.1 Régimen no vacío y simetría (N1 calibrado)
- **Ocupación final ($\rho_{\text{fin}}$):** media `[ ]` · rango `[mín, máx]` · fracción con $\rho_{\text{fin}} \in (0.05, 0.95)$: `[ ]`
- **Residuo $\mathbb{Z}_4$ ($\Delta_{\mathbb{Z}_4}$) / $P_{\text{sel,estricta}}$:** `[ ]` / `[ ]`
- **Etiquetas de régimen:** `saturated_or_empty`: `[ ]/30` · `near_z4_symmetric`: `[ ]/30` · `asymmetric_or_mixed`: `[ ]/30`

### 5.2 Monotonía de $\tilde{V}(T)$ y convergencia
- **Violaciones de $\Delta \tilde{V} \le 0$ (pasos secuenciales):** `[0 / total]`
- **Regla de variación verificada:** `0 -> 1`: $\Delta\tilde{V} = -h_a(T) + \Delta\Phi_a \le 0$ · `1 -> 0`: $\Delta\tilde{V} = h_a(T) - \Delta\Phi_a \le 0$ · `0 -> 0` / `1 -> 1`: `0`
- **Puntos fijos retenidos alcanzados:** `[n/30]` · **Ciclos abiertos:** `[n/30]`

### 5.3 Modos transversales $\mathbb{Z}_4$ ($m=1,2,3$) y retención en banda
- **Energía modal en estados finales ($m=0$ vs. $m=1,2,3$):** $m=0$: `[ ]%` · $m=1,3$ (helicoidal / contiguos): `[ ]%` · $m=2$ (cuadrupolar / triángulo-cruz): `[ ]%`
- **Margen mínimo a banda $[\theta_{\text{off}}, \theta_{\text{on}}]$:** `[ ]`
- **Sensibilidad al orden asíncrono:** `[baja / media / alta — nota breve]`

### 5.4 Lectura de estado (sin ascenso automático)
- **Nivel II retenido:** `[consistencia dinámica y modal comprobada / pendiente ajuste de umbral]`
- **Nivel III abierto:** Permanece abierto (no acredita emergencia espontánea desde bases no pre-codificadas ni valida formalmente $\lambda$).
