# NOTA DE CERTIFICACIÓN ESPECTRAL — v1.7 (`EXIT=0`)

* **Rama:** Experimental **v1.7** (`v1.6` estrictamente aislada; `Fugas v1.6: []`)
* **Arquitectura:** **47D** (`mass_24`, `state_22`, `theta`), **276 aristas**, **Código Viajer**, **Matriz de la Suma 23**, **movimiento helicoidal**, **conexiones del triángulo a la cruz**, **nodos contiguos** y acoplamiento $\Pi_{3 \to 4}$
* **Gobernanza 4º Factor:** **Nivel II retenido** · **Nivel III abierto** · **sin ascenso automático**

## 1. Referencia (`seed=42`, `coup=0.825`)
* **Modo neutro de fase:** $\lambda_{\text{neutro}}(\theta) = 1.000000$ (deslizamiento de fase, no inestabilidad; $\|J_{\text{47}}\|_2 = 1.002126$ en espacio completo).
* **Bloque no trivial y proyección ortogonal $P_\perp$:** $\rho_{\text{ntriv}} = 0.974885 < 1.0$ y $\|P_\perp J_{\text{47}} P_\perp\|_2 = 0.990486 < 1.0$ (margen lineal nominal $\eta_0 = 0.009514$).
* **Subbloque $L_{\text{22}}$:** $\rho(L_{\text{22}}) = 0.974885$ y $\|L_{\text{22}}\|_2 = 0.990000 < 1.0$ (frente a la cota geométrica de Gershgorin `1.039248`).

## 2. Robustez por ensemble (`11` corridas)
* `8` semillas (`coup=0.825`) + `3` acoplamientos (`0.800`, `0.825`, `0.850` con `seed=42`): **`all_ok = True`**, $\rho_{\text{ntriv}} = 0.974885$, $\|P_\perp J_{\text{47}} P_\perp\|_2 \in [0.990483, 0.990489]$ y $\|L_{\text{22}}\|_2 = 0.990000$ (siempre `< 1.0`).

## 3. Dictamen
Campaña espectral de **v1.7** documentalmente cerrada (`EXIT=0`) bajo **Nivel II retenido** y **Nivel III abierto**, pendiente de revisión de **4º Factor**.
