# EQUILIBRIUM CLASSIFICATION

## Clasificación estructural y dinámica de equilibrios

**Proyecto:** Convergencia TRCG — Código Viajer  
**Versión:** 0.1.0  
**Fecha:** 2026-11-26  
**Estado:** Resultados matemáticos condicionales  
**Referencia:** TRCG, Episodios 45 y 46  
**Gobernanza:** Nivel II retenido · Nivel III abierto  

---

## 1. Objeto

Establecer un marco matemático para clasificar
los equilibrios de Pirámide-Parábola mediante:

- Simetrías.
- Órbitas.
- Estabilizadores.
- Estabilidad local.
- Presencia apical.
- Cuencas de atracción.
- Probabilidades de convergencia.

El objetivo es distinguir la multiplicidad
de configuraciones de la diversidad
estructural efectiva.

No se presupone ninguna equivalencia
entre Pirámide-Parábola y la TRCG.

## 2. Documentos relacionados

- EFFECTIVE_SYMMETRY_GROUP.md
- MULTILAYER_INVARIANTS.md
- RELATIONAL_QUOTIENT_METRIC.md
- PP_AUTOMORPHISM_GROUP.md
- PP_MULTILAYER_VERIFICATION.py
- pp_verification.json

## 3. Espacio de estados

Sea X un espacio métrico de estados
admisibles.

Sea:

F : X → X

un operador dinámico determinista.

La evolución viene dada por:

x_(t+1) = F(x_t)

El conjunto de equilibrios se define como:

E(F) = {x ∈ X : F(x) = x}

Un equilibrio es un punto fijo
del operador considerado.

La existencia de un equilibrio no implica
necesariamente su estabilidad.

Tampoco implica que posea una cuenca
de atracción de medida positiva.

## 4. Grupo admisible

Sea G un grupo finito que actúa
sobre X mediante isometrías.

Para cada g ∈ G:

g : X → X

La acción debe preservar:

- El dominio admisible.
- Las restricciones del sistema.
- La identidad de las variables.
- Las condiciones de contorno.

Para el modelo combinatorio parcial
de Pirámide-Parábola con estratos fijos:

G = {e,r}

donde:

r(i) = i+12 mod 24

y:

r² = e

Por tanto:

G ≅ ℤ_2

La utilización de este grupo sobre
el sistema completo exige verificar
previamente su admisibilidad.

## 5. Equivarianza dinámica

El operador F es G-equivariante si:

F(g · x) = g · F(x)

para todo:

g ∈ G

x ∈ X

Esta propiedad no se deduce únicamente
de las simetrías geométricas.

Debe demostrarse para cada operador.

En particular, deberá verificarse
separadamente para:

- Operador relacional.
- Sistema híbrido.
- Dinámica 44A.
- Dinámica 44B.

## 6. Conservación de equilibrios

### Teorema 1

Si F es G-equivariante, su conjunto
de equilibrios es G-invariante.

### Demostración

Sea x* ∈ E(F).

Entonces:

F(x*) = x*

Para cualquier g ∈ G:

F(g · x*) = g · F(x*)

Por tanto:

F(g · x*) = g · x*

En consecuencia:

g · x* ∈ E(F)

Queda demostrado.

### Consecuencia

Los equilibrios pueden organizarse
en clases de equivalencia estructural
bajo las simetrías admisibles.

## 7. Órbitas de equilibrios

Definimos:

Orb_G(x*) = {g · x* : g ∈ G}

Dos equilibrios son equivalentes
respecto de G si pertenecen
a la misma órbita.

Esta equivalencia no implica
identidad de sus coordenadas.

El conjunto cociente es:

E(F)/G

Cada elemento representa una clase
de equilibrios relacionados mediante
transformaciones admisibles.

## 8. Estabilizadores

El estabilizador de un equilibrio es:

Stab_G(x*) =
{g ∈ G : g · x* = x*}

Por el teorema órbita-estabilizador:

|Orb_G(x*)| =
|G| / |Stab_G(x*)|

Los equilibrios con mayor estabilizador
poseen órbitas de menor tamaño.

Esto caracteriza su simetría estructural.

No caracteriza automáticamente
su estabilidad dinámica.

## 9. Clasificación bajo ℤ_2

Para:

G = {e,r}

existen dos tipos de órbitas.

### Tipo I. Equilibrios invariantes

r · x* = x*

Entonces:

|Stab_G(x*)| = 2

|Orb_G(x*)| = 1

El equilibrio conserva la simetría
de rotación de 180 grados.

### Tipo II. Equilibrios emparejados

r · x* ≠ x*

Entonces:

|Stab_G(x*)| = 1

|Orb_G(x*)| = 2

La órbita contiene:

{x*,r · x*}

Los dos equilibrios son distintos,
pero estructuralmente equivalentes
respecto de G.

## 10. Recuento exacto de clases

### Teorema 2

Sea E un conjunto finito G-invariante
de equilibrios.

Definimos:

M = |E|

M_f = |{x ∈ E : r · x = x}|

Entonces:

|E/G| = (M + M_f)/2

### Demostración

Los M_f equilibrios invariantes
forman órbitas unitarias.

Los M−M_f restantes forman
órbitas de dos elementos.

Por tanto:

|E/G| = M_f + (M−M_f)/2

Simplificando:

|E/G| = (M + M_f)/2

Queda demostrado.

### Corolario

M−M_f debe ser un número par.

Esta condición proporciona
una comprobación de consistencia
para conjuntos finitos completos
e invariantes bajo r.

## 11. Aplicación a los 190 equilibrios

Se han comunicado 190 equilibrios
sin presencia de nodos apicales.

Este documento no contiene todavía
sus estados individuales ni una
verificación independiente de su origen.

Supongamos que:

H1. Los 190 estados son equilibrios
    distintos del mismo operador.

H2. El operador es equivariante
    respecto de r.

H3. La ausencia apical se conserva
    bajo r.

H4. El conjunto comunicado es cerrado
    bajo la acción de r.

Entonces:

M = 190

Por el teorema anterior:

N_orb = (190 + M_f)/2

Como:

0 ≤ M_f ≤ 190

obtenemos:

95 ≤ N_orb ≤ 190

Además, M_f debe ser par.

Ejemplos:

| Invariantes | Parejas | Clases |
|-------------|---------|--------|
| 0 | 95 | 95 |
| 20 | 85 | 105 |
| 50 | 70 | 120 |
| 100 | 45 | 145 |
| 150 | 20 | 170 |
| 190 | 0 | 190 |

Estos valores son posibilidades
matemáticas, no resultados observados.

La determinación exacta exige
examinar los 190 estados.

## 12. Clasificación bajo ℤ_4

Si un operador diferente conserva
las cuatro rotaciones espaciales,
podrá utilizarse:

G_rot = {e,t,t²,t³}

donde:

t(i) = i+6 mod 24

y:

t⁴ = e

Las órbitas pueden tener tamaño:

1, 2 o 4

Para un conjunto finito invariante E,
el lema de Burnside establece:

|E/G_rot| =
( M + Fix(t) + Fix(t²) + Fix(t³) )/4

Como t y t³ generan el mismo grupo:

Fix(t) = Fix(t³)

Por tanto:

|E/G_rot| =
( M + 2Fix(t) + Fix(t²) )/4

Aquí Fix(g) representa el número
de elementos de E fijados por g.

Para M = 190:

48 ≤ |E/G_rot| ≤ 190

Este intervalo es una cota general
bajo las hipótesis indicadas.

No se afirma que los 190 equilibrios
sean invariantes bajo ℤ_4.

Los grupos ℤ_2 y ℤ_4 deberán
estudiarse separadamente.

## 13. Representantes canónicos

Para estados nodales:

x ∈ ℝ^24

definimos:

(r · x)_i = x_(i+12 mod 24)

El representante canónico bajo ℤ_2 es:

can(x) = min_lex{x,r · x}

Entonces:

can(x) = can(y)

si y solo si:

Orb_G(x) = Orb_G(y)

Este procedimiento permite identificar
equilibrios equivalentes sin modificar
sus valores originales.

Para estados discretos puede realizarse
mediante aritmética exacta.

Para estados híbridos deben incluirse
todas las variables relevantes.

## 14. Distancia entre equilibrios

Utilizando los resultados de:

RELATIONAL_QUOTIENT_METRIC.md

definimos:

d_G([x],[y]) =
min{||x−y||_2, ||x−r · y||_2}

Esta distancia mide la separación
entre clases estructurales.

Se verifica:

d_G([x],[y]) = 0

si y solo si:

[x] = [y]

Una distancia pequeña no implica
equivalencia exacta.

Tampoco implica que ambos equilibrios
posean las mismas propiedades dinámicas.

## 15. Defecto de simetría

Definimos:

S_r(x) = ||x−r · x||_2

Entonces:

S_r(x) ≥ 0

y:

S_r(x) = 0

si y solo si:

r · x = x

Para estados nodales:

S_r(x)² =
2 Σ_(i=0)^11 (x_i−x_(i+12))²

Esta magnitud permite cuantificar
la ruptura de la simetría de 180 grados.

No constituye por sí sola una
función de Lyapunov.

No se presupone que disminuya
durante la evolución.

## 16. Descomposición simétrica y antisimétrica

Sea P_r la matriz de permutación
asociada a r.

Como:

P_r² = I

definimos los proyectores:

Π_+ = (I+P_r)/2

Π_- = (I−P_r)/2

Para cualquier estado nodal x:

x_+ = Π_+ x

x_- = Π_- x

Se verifica:

x = x_+ + x_-

P_r x_+ = x_+

P_r x_- = −x_-

Los subespacios simétrico y
antisimétrico son ortogonales.

Cada uno posee dimensión 12.

Además:

S_r(x) = 2||x_-||_2

Por tanto, la ruptura de simetría
queda caracterizada exactamente
por la componente antisimétrica.

Esta descomposición no implica
que ambas componentes evolucionen
independientemente bajo un
operador no lineal.

## 17. Invariancia del subespacio simétrico

### Teorema 3

Si F es equivariante respecto de r,
el conjunto de estados simétricos
es invariante bajo F.

### Demostración

Supongamos:

r · x = x

Entonces:

r · F(x) = F(r · x)

Por tanto:

r · F(x) = F(x)

En consecuencia, F(x) también
es simétrico.

Queda demostrado.

### Consecuencia

Una trayectoria que comienza
en un estado exactamente simétrico
permanece simétrica bajo una
dinámica determinista equivariante.

Esto no implica que los estados
iniciales asimétricos converjan
hacia el subespacio simétrico.

## 18. Estabilidad local

Sea x* un equilibrio.

Si F es diferenciable en un entorno
del equilibrio, definimos:

J(x*) = DF(x*)

Para una dinámica discreta:

ρ(J(x*)) < 1

es una condición suficiente
de estabilidad asintótica local.

Si:

ρ(J(x*)) > 1

el equilibrio es inestable.

Si:

ρ(J(x*)) = 1

el análisis lineal no permite
resolver por sí solo la estabilidad.

Estas afirmaciones requieren
las hipótesis habituales de
diferenciabilidad local.

Para sistemas restringidos debe
considerarse el espacio de
perturbaciones admisibles.

Para dinámicas discretas sobre
conjuntos finitos o reglas no suaves,
deberán emplearse criterios
adaptados al operador.

## 19. Equivalencia espectral de equilibrios

### Teorema 4

Sea F diferenciable y equivariante
respecto de una acción lineal g.

Entonces:

J(g · x*) = g J(x*) g⁻¹

### Demostración

Partimos de:

F(g · x) = g · F(x)

Derivando respecto de x:

DF(g · x) g = g DF(x)

Multiplicando por g⁻¹:

DF(g · x) = g DF(x) g⁻¹

Evaluando en x*:

J(g · x*) = g J(x*) g⁻¹

Queda demostrado.

### Consecuencias

Los jacobianos de equilibrios
pertenecientes a una misma órbita
son matrices semejantes.

Por tanto, poseen:

- El mismo espectro.
- El mismo radio espectral.
- El mismo polinomio característico.
- El mismo criterio de estabilidad lineal.

Esta equivalencia requiere que
la acción preserve el espacio
de perturbaciones considerado.

## 20. Equivalencia de estabilidad no lineal

### Teorema 5

Si F es equivariante respecto
de una acción isométrica de G,
la estabilidad de Lyapunov y la
estabilidad asintótica se conservan
dentro de cada órbita.

### Demostración

Para cualquier t ≥ 0:

F^t(g · x) = g · F^t(x)

Como g es una isometría:

d(F^t(g · x),g · x*)

=
d(F^t(x),x*)

Por tanto, las condiciones de
proximidad, permanencia y convergencia
se transfieren entre x* y g · x*.

Queda demostrado.

Este resultado no requiere
diferenciabilidad del operador.

## 21. Separación de modos de estabilidad

Sea x* un equilibrio simétrico:

P_r x* = x*

Si F es diferenciable y equivariante:

J(x*)P_r = P_r J(x*)

Por tanto, el jacobiano conserva
los subespacios:

V_+ = {v : P_r v = v}

V_- = {v : P_r v = −v}

En una base adaptada:

J = diag(J_+,J_-)

Para estados nodales de dimensión 24,
ambos bloques tienen dimensión 12.

El espectro completo satisface:

spec(J) = spec(J_+) ∪ spec(J_-)

Por tanto:

ρ(J) = max{ρ(J_+),ρ(J_-)}

Esto permite distinguir:

- Estabilidad frente a perturbaciones
  que conservan la simetría.

- Estabilidad frente a perturbaciones
  que rompen la simetría.

La estabilidad en V_+ no garantiza
estabilidad en V_-.

Un equilibrio puede ser estable
dentro del subespacio simétrico
e inestable frente a perturbaciones
antisimétricas.

## 22. Presencia apical

En la numeración del modelo parcial:

V_ap = {5,11,17,23}

La rotación de 180 grados conserva
este conjunto:

r(V_ap) = V_ap

Para estados nodales no negativos
puede definirse la masa apical:

A(x) = Σ_(i∈V_ap) x_i

Entonces:

A(r · x) = A(x)

La ausencia apical corresponde a:

A(x) = 0

Esta equivalencia requiere que
las componentes sean no negativas.

Si los estados contienen signos,
fases u otras variables, deberá
definirse un criterio de presencia
apical adecuado a su significado.

## 23. Clasificación por presencia apical

Definimos:

E_0 = {x ∈ E(F) : A(x) = 0}

E_+ = {x ∈ E(F) : A(x) > 0}

Para estados no negativos:

E(F) = E_0 ∪ E_+

E_0 ∩ E_+ = ∅

Si F es equivariante y A es
invariante bajo G, ambos conjuntos
son invariantes bajo G.

Por tanto, pueden clasificarse
separadamente mediante órbitas.

Esta propiedad permite estudiar
la presencia apical sin confundirla
con la equivalencia estructural.

## 24. Obstrucción a la atracción apical universal

### Teorema 6

Supongamos que existe un equilibrio
admisible x* tal que:

A(x*) = 0

Entonces no puede existir convergencia
universal desde todo X hacia estados
con presencia apical positiva.

### Demostración

Tomamos como condición inicial:

x_0 = x*

Como x* es un equilibrio:

F^t(x*) = x*

para todo t ≥ 0.

Por tanto:

A(F^t(x*)) = 0

La trayectoria no converge hacia
un estado con presencia apical positiva.

Queda demostrado.

### Alcance

Este resultado no requiere
que x* sea estable.

Tampoco descarta:

- Atracción apical casi segura.
- Dominancia estadística apical.
- Una cuenca apical mayoritaria.
- Convergencia apical sobre
  dominios iniciales restringidos.

La existencia de equilibrios no apicales
refuta la atracción universal únicamente
sobre dominios que los incluyen.

## 25. Cuencas de atracción

Para un equilibrio x* definimos:

B(x*) =
{x ∈ X : F^t(x) → x*}

### Teorema 7

Si F es G-equivariante:

B(g · x*) = g · B(x*)

### Demostración

Sea x ∈ B(x*).

Entonces:

F^t(x) → x*

Por equivariancia:

F^t(g · x) = g · F^t(x)

Como g es continua:

F^t(g · x) → g · x*

Por tanto:

g · x ∈ B(g · x*)

La inclusión recíproca se obtiene
aplicando g⁻¹.

Queda demostrado.

## 26. Probabilidad de convergencia

Sea μ una distribución de
probabilidad sobre X.

Supongamos que μ es G-invariante:

μ(g · U) = μ(U)

para todo conjunto medible U.

Si las cuencas son medibles,
definimos:

p(x*) = μ(B(x*))

Por el teorema anterior:

p(g · x*) = p(x*)

Los equilibrios pertenecientes
a una misma órbita poseen igual
probabilidad de convergencia.

Para una órbita O de tamaño k:

p(O) = Σ_(x*∈O) p(x*)

Como las cuencas de equilibrios
distintos son disjuntas:

p(O) = k · p(x*)

Este resultado depende de la
invariancia de la distribución inicial.

No debe aplicarse automáticamente
a distribuciones sesgadas.

## 27. Entropía de equilibrios y órbitas

Supongamos una distribución discreta
de estados finales normalizada.

Sea Z la variable aleatoria que
identifica el equilibrio alcanzado.

Sea O la variable que identifica
su órbita.

Como O es función de Z:

H(Z) = H(O) + H(Z|O)

Por tanto:

H(O) ≤ H(Z)

Para grupos de orden dos:

0 ≤ H(Z)−H(O) ≤ 1 bit

Si las probabilidades son iguales
dentro de cada órbita:

H(Z|O) =
Σ_O p(O) log₂|O|

Bajo ℤ_2:

H(Z|O) =
Σ_(|O|=2) p(O)

La diferencia de entropía cuantifica
la diversidad eliminada al identificar
configuraciones equivalentes.

No representa necesariamente
pérdida física de información.

## 28. Comparación entre 44A y 44B

Para cada operador deberán registrarse:

- Número de trayectorias.
- Número de convergencias.
- Número de equilibrios distintos.
- Número de órbitas distintas.
- Número de equilibrios simétricos.
- Número de equilibrios emparejados.
- Frecuencia de cada equilibrio.
- Frecuencia de cada órbita.
- Entropía de estados finales.
- Entropía de órbitas.
- Presencia apical.
- Probabilidades de convergencia.

La comparación deberá utilizar
criterios compatibles de identidad
y admisibilidad.

Los casos no convergentes deberán
registrarse separadamente.

Las entropías condicionadas a la
convergencia deberán identificarse
expresamente como tales.

No se presupone que ambos operadores
compartan el mismo grupo dinámico.

## 29. Protocolo computacional

La clasificación deberá seguir
el siguiente procedimiento:

1. Cargar los estados originales.

2. Verificar su integridad.

3. Identificar el operador y
   sus parámetros.

4. Eliminar duplicados exactos.

5. Verificar la condición de equilibrio.

6. Comprobar la admisibilidad.

7. Identificar el grupo aplicable.

8. Verificar la equivariancia.

9. Transformar cada equilibrio
   mediante los elementos del grupo.

10. Comprobar el cierre del conjunto.

11. Calcular representantes canónicos.

12. Identificar estabilizadores.

13. Clasificar órbitas.

14. Calcular defectos de simetría.

15. Clasificar presencia apical.

16. Evaluar estabilidad local.

17. Estimar las cuencas de atracción.

18. Registrar resultados y limitaciones.

No se introducirán transformaciones
que alteren los estados originales.

## 30. Tratamiento de tolerancias

Para estados discretos se utilizará
igualdad exacta siempre que sea posible.

Para estados continuos se deberán
establecer tolerancias explícitas.

El residuo de equilibrio se define como:

ε_F(x) = d(F(x),x)

El defecto de simetría se define como:

ε_r(x) = d(r · x,x)

Una tolerancia pequeña no convierte
un equilibrio aproximado en un
equilibrio exacto demostrado.

La proximidad numérica tampoco
define necesariamente una relación
de equivalencia transitiva.

No deberán construirse clases exactas
mediante agrupaciones aproximadas
sin justificar el procedimiento.

## 31. Pruebas de consistencia

T01. Integridad de estados.

T02. Unicidad de registros.

T03. Admisibilidad de equilibrios.

T04. Residuo del operador.

T05. Equivariancia dinámica.

T06. Cierre bajo el grupo.

T07. Identificación de estabilizadores.

T08. Representantes canónicos.

T09. Recuento mediante Burnside.

T10. Paridad de M−M_f bajo ℤ_2.

T11. Invariancia de presencia apical.

T12. Correspondencia espectral.

T13. Correspondencia de estabilidad.

T14. Correspondencia de cuencas.

T15. Normalización de probabilidades.

T16. Descomposición de entropías.

T17. Descomposición simétrica
     y antisimétrica.

Las pruebas deberán ejecutarse
sobre datos identificados mediante
versiones y registros reproducibles.

## 32. Resultados demostrados

Bajo las hipótesis correspondientes:

- Invariancia del conjunto de equilibrios.
- Clasificación mediante órbitas.
- Recuento mediante estabilizadores.
- Fórmula de Burnside para ℤ_2.
- Fórmula de Burnside para ℤ_4.
- Representantes canónicos.
- Defecto de simetría.
- Descomposición en subespacios.
- Invariancia del subespacio simétrico.
- Equivalencia espectral.
- Equivalencia de estabilidad.
- Separación de modos de estabilidad.
- Invariancia de masa apical.
- Obstrucción a la atracción universal.
- Correspondencia de cuencas.
- Igualdad de probabilidades bajo
  distribuciones invariantes.
- Descomposición de entropías.

## 33. Resultados pendientes

- Acceso a los 190 estados comunicados.
- Verificación de su condición
  de equilibrio.
- Confirmación del operador generador.
- Confirmación del grupo aplicable.
- Número exacto de órbitas.
- Número de equilibrios invariantes.
- Estabilidad de cada equilibrio.
- Cálculo de jacobianos, cuando proceda.
- Tamaños de cuencas.
- Probabilidades de convergencia.
- Equivarianza de 44A y 44B.
- Comparación con arquitecturas nulas.
- Correspondencia con la TRCG.

## 34. Gobernanza

- Nivel II retenido.
- Nivel III abierto.
- λ reservado al 4º Factor.
- Pirámide-Parábola como candidata experimental.
- Independencia de ambas formulaciones.
- Sin equivalencias automáticas.
- Sin ascensos automáticos.
- Sin reescalados retrospectivos.
- Sin modificación de protocolos congelados.
- Versiones v1.6 y v1.7 aisladas.

## 35. Conclusión

La clasificación de equilibrios
mediante grupos de simetría permite
distinguir multiplicidad numérica
y diversidad estructural.

Bajo equivariancia, los equilibrios
pertenecientes a una misma órbita
comparten propiedades de estabilidad
y poseen cuencas relacionadas
mediante las simetrías del sistema.

La existencia de equilibrios no
apicales establece límites a la
atracción apical universal.

No determina por sí sola la
dominancia estadística del ápice.

Para los 190 equilibrios comunicados,
si constituyen un conjunto invariante
bajo la rotación de 180 grados:

95 ≤ |E_0/G| ≤ 190

La clasificación exacta permanece
pendiente de verificación.

La geometría establece posibilidades.

La dinámica determina evoluciones.

La estabilidad exige demostración.

La dominancia exige cuantificación.

La convergencia exige verificación.

---

36. Ampliación v0.2.0 — Clasificación exacta de equilibrios de una arista

36.1. Objeto y alcance

La presente ampliación integra los resultados analíticos desarrollados para el operador relacional matricial de referencia.

Se complementan las secciones anteriores mediante una clasificación exacta de una familia explícita de 276 equilibrios.

Los resultados no se trasladan automáticamente al modelo nodal multiplicativo, al sistema híbrido, a los operadores 44A y 44B ni a la dinámica fundamental de la TRCG.

Documentos complementarios:

- "REDUCED_SUPPORT_STABILITY.md"
- "CANONICAL_OPERATOR_CORRESPONDENCE.md"
- "RELATIONAL_EQUIVARIANCE.md"
- "RELATIONAL_QUOTIENT_METRIC.md"
- "INFORMATION_RECOVERY.md"
- "MULTILAYER_INVARIANTS.md"

Auditoría asociada:

- "quotient_space_audit.py"
- "quotient_space_results.json"

---

37. Dominio matricial

Consideramos el espacio:

[
\mathcal S=
{R\in\mathbb R^{24\times24}:R^T=R,\ \operatorname{diag}(R)=0}.
]

Definimos la masa relacional:

[
m(R)=\sum_{i<j}R_{ij}.
]

El dominio de masa fija es:

[
\mathcal D_{C_0}=
{R\in\mathcal S:R_{ij}\geq0,\ m(R)=C_0},
]

donde:

[
C_0>0.
]

La dimensión del espacio ambiente es:

[
\dim(\mathcal S)=276.
]

La dimensión del dominio de masa fija es:

[
\dim(\mathcal D_{C_0})=275.
]

La utilización del operador basado en el autovector dominante exige restringirse a estados donde dicho operador esté bien definido.

En particular, los estados de una sola arista poseen un mayor autovalor algebraico simple.

---

38. Existencia de los 276 equilibrios

Sea:

[
e={a,b},
\qquad a\neq b.
]

Definimos:

[
R_e=C_0(e_ae_b^T+e_be_a^T),
]

donde (e_a) y (e_b) son vectores de la base canónica.

Cada configuración concentra toda su masa relacional en una única arista.

Consideramos el operador:

[
\Phi(R)=(1-\mu)R+\mu\mathcal N(M(R)),
]

con:

[
M_{ij}(R)=
(g_i g_j v_i(R)v_j(R))^\gamma,
]

para i distinto de j, y diagonal nula.

Se supone:

- Pesos geométricos estrictamente positivos y finitos.
- γ > 0.
- 0 ≤ μ ≤ 1.
- Autovector dominante unitario no negativo.
- Normalización a masa C0.

Teorema 8

Todas las configuraciones (R_e) son puntos fijos del operador estudiado.

Demostración

El espectro de (R_e) es:

[
{C_0,-C_0,0^{(22)}}.
]

El mayor autovalor algebraico es simple y su autovector unitario no negativo es:

[
v_e=\frac{e_a+e_b}{\sqrt2}.
]

Por tanto, la matriz M únicamente posee entradas no nulas en las posiciones ab y ba.

La normalización a masa C0 devuelve:

[
\mathcal N(M(R_e))=R_e.
]

En consecuencia:

[
\Phi(R_e)
=(1-\mu)R_e+\mu R_e
=R_e.
]

Queda demostrado.

El número de aristas no ordenadas es:

[
|\mathcal E|=
\binom{24}{2}=276.
]

Por tanto, existen al menos 276 puntos fijos distintos en el dominio extendido que contiene estas configuraciones.

No se afirma que sean los únicos puntos fijos del operador.

---

39. Grupos de clasificación

Se adopta la numeración:

[
i=6q+r,
]

con:

[
q\in{0,1,2,3},
\qquad
r\in{0,1,2,3,4,5}.
]

Se distinguen cuatro acciones.

39.1. Grupo de permutaciones ordinarias

[
G_P=S_{24}.
]

Representa el reetiquetado combinatorio general de los nodos.

No constituye necesariamente un grupo de simetrías dinámicas del operador ponderado.

39.2. Grupo residual

[
G_2=\langle h\rangle\cong\mathbb Z_2,
]

donde:

[
h(i)=i+12\pmod{24}.
]

39.3. Grupo rotacional

[
G_4=\langle g\rangle\cong\mathbb Z_4,
]

donde:

[
g(i)=i+6\pmod{24}.
]

39.4. Grupo estratificado

[
G_S=(S_4)^6.
]

Este grupo permite permutar independientemente los cuatro nodos de cada estrato.

Cuando los pesos son constantes dentro de cada estrato, dichas permutaciones conservan la matriz de pesos geométricos.

Para el operador de referencia, bajo las hipótesis de equivariancia correspondientes:

[
G_2\subset G_4\subset G_S\subset S_{24}.
]

Estas inclusiones describen las acciones aquí definidas.

No identifican el grupo geométrico completo de Pirámide-Parábola.

---

40. Clasificación bajo permutaciones ordinarias

Teorema 9

La familia de equilibrios de una arista constituye una única órbita bajo (S_{24}).

Demostración

Sean dos aristas cualesquiera:

[
e={a,b},
\qquad
f={c,d}.
]

Existe una permutación p tal que:

[
p(a)=c,
\qquad
p(b)=d.
]

Por tanto:

[
p\cdot R_e=R_f.
]

En consecuencia:

[
|\mathcal E/S_{24}|=1.
]

Queda demostrado.

Este resultado es combinatorio.

No demuestra equivalencia dinámica de todos los equilibrios bajo un operador con pesos geométricos distintos.

---

41. Clasificación bajo el grupo residual Z2

Teorema 10

La familia de 276 equilibrios contiene exactamente 144 clases bajo la rotación de 180 grados.

Demostración

La identidad fija las 276 aristas.

La rotación:

[
h(i)=i+12\pmod{24}
]

no fija nodos individuales.

Una arista queda invariante bajo h si y solo si sus extremos se intercambian:

[
e={i,i+12}.
]

Existen exactamente 12 aristas de este tipo.

Por el lema de Burnside:

[
|\mathcal E/G_2|

\frac{276+12}{2}
=144.
]

Queda demostrado.

Distribución de órbitas

Tamaño de órbita| Número de órbitas
1| 12
2| 132
Total| 144

Comprobación:

[
12+2(132)=276.
]

---

42. Clasificación bajo el grupo rotacional Z4

Teorema 11

La familia de 276 equilibrios contiene exactamente 72 clases bajo las cuatro rotaciones sectoriales.

Demostración

El grupo está formado por:

[
G_4={e,g,g^2,g^3}.
]

Los números de aristas fijas son:

Transformación| Aristas fijas
Identidad| 276
Rotación de 90 grados| 0
Rotación de 180 grados| 12
Rotación de 270 grados| 0

Las rotaciones de 90 y 270 grados no pueden preservar una arista de dos extremos, porque sus ciclos nodales tienen longitud cuatro.

Por Burnside:

[
|\mathcal E/G_4|

\frac{276+0+12+0}{4}
=72.
]

Queda demostrado.

Distribución de órbitas

Tamaño de órbita| Número de órbitas
2| 6
4| 66
Total| 72

Comprobación:

[
2(6)+4(66)=276.
]

---

43. Clasificación bajo el grupo estratificado

Teorema 12

La familia de 276 equilibrios contiene exactamente 21 clases bajo:

[
G_S=(S_4)^6.
]

Demostración

Cada arista queda caracterizada, respecto de esta acción, por el par no ordenado de estratos al que pertenecen sus extremos.

Existen dos posibilidades.

Caso A. Extremos en el mismo estrato

Hay seis estratos.

Cada uno contiene:

[
\binom42=6
]

aristas internas.

Todas las aristas internas de un mismo estrato son equivalentes bajo su grupo (S_4).

Por tanto, existen seis clases internas.

Caso B. Extremos en estratos diferentes

El número de pares no ordenados de estratos distintos es:

[
\binom62=15.
]

Cada par de estratos contiene:

[
4\cdot4=16
]

aristas.

Las permutaciones independientes dentro de ambos estratos actúan transitivamente sobre estas aristas.

Por tanto, existen 15 clases externas.

En consecuencia:

[
|\mathcal E/G_S|=6+15=21.
]

Queda demostrado.

Distribución de órbitas

Tipo| Clases| Tamaño de cada órbita
Mismo estrato| 6| 6
Estratos diferentes| 15| 16
Total| 21| —

Comprobación:

[
6(6)+15(16)=276.
]

---

44. Clasificación apical exacta

Adoptamos como conjunto apical:

[
A={5,11,17,23}.
]

Su complemento contiene 20 nodos.

Definimos tres familias:

- E0: aristas sin extremos apicales.
- E1: aristas con un extremo apical.
- E2: aristas con dos extremos apicales.

Cardinalidades

[
|E_0|=\binom{20}{2}=190.
]

[
|E_1|=20\cdot4=80.
]

[
|E_2|=\binom42=6.
]

Por tanto:

[
190+80+6=276.
]

44.1. Clasificación bajo Z2

Entre las 12 aristas fijadas por la rotación de 180 grados:

- 10 poseen dos extremos no apicales.
- 2 poseen dos extremos apicales.
- Ninguna posee exactamente un extremo apical.

Aplicando Burnside a cada familia:

[
|E_0/G_2|=\frac{190+10}{2}=100.
]

[
|E_1/G_2|=\frac{80}{2}=40.
]

[
|E_2/G_2|=\frac{6+2}{2}=4.
]

44.2. Clasificación bajo Z4

Las rotaciones de 90 y 270 grados no fijan aristas.

Por tanto:

[
|E_0/G_4|=\frac{190+10}{4}=50.
]

[
|E_1/G_4|=\frac{80}{4}=20.
]

[
|E_2/G_4|=\frac{6+2}{4}=2.
]

44.3. Clasificación bajo el grupo estratificado

Existen cinco estratos no apicales.

Las clases sin extremos apicales son:

[
5+\binom52=15.
]

Las clases con un extremo apical son:

[
5.
]

Las clases con dos extremos apicales son:

[
1.
]

Tabla consolidada

Participación apical| Equilibrios| Z2| Z4| Grupo estratificado
Ningún extremo| 190| 100| 50| 15
Un extremo| 80| 40| 20| 5
Dos extremos| 6| 4| 2| 1
Total| 276| 144| 72| 21

Estos recuentos son exactos para la familia de equilibrios definida en la sección 38.

---

45. Precisión sobre los 190 equilibrios comunicados

Las secciones anteriores del documento establecían la cota:

[
95\leq |E_0/G_2|\leq190.
]

Dicha cota corresponde a un conjunto genérico de 190 equilibrios cerrado bajo la acción del grupo residual, sin conocer el número de estados fijados.

Para la familia explícita de aristas no apicales estudiada en esta ampliación se ha determinado:

[
|\operatorname{Fix}(h)\cap E_0|=10.
]

En consecuencia:

[
|E_0/G_2|=100.
]

Este resultado resuelve el problema para la familia matricial de una arista.

La identificación de esta familia con cualquier conjunto de 190 equilibrios procedente de otra implementación o campaña exige comprobar el operador generador y los estados correspondientes.

La coincidencia de cardinalidades no demuestra identidad entre conjuntos.

---

46. Distancia exacta entre clases

Utilizamos la representación diádica ordenada:

[
p(R)=(R_{ij})_{i<j}.
]

Definimos la métrica cociente:

[
d_G([R],[S])

\min_{g\in G}
|p(R)-p(g\cdot S)|_2.
]

Teorema 13

Para dos equilibrios de una arista:

[
d_G([R_e],[R_f])=
\begin{cases}
0,&[R_e]=[R_f],\
\sqrt2C_0,&[R_e]\neq[R_f].
\end{cases}
]

Demostración

Cada representación diádica contiene una única componente no nula de valor C0.

Si ambas aristas pertenecen a la misma órbita, existe una transformación que hace coincidir sus representaciones.

La distancia mínima es cero.

Si pertenecen a órbitas diferentes, ninguna transformación puede hacer coincidir sus posiciones no nulas.

La diferencia posee exactamente dos componentes no nulas:

[
+C_0,\qquad -C_0.
]

Por tanto:

[
d_G^2=C_0^2+C_0^2=2C_0^2.
]

En consecuencia:

[
d_G=\sqrt2C_0.
]

Queda demostrado.

Convención de normalización

Si se utiliza directamente la norma matricial de Frobenius, la distancia correspondiente es:

[
d_G^{(F)}=2C_0
]

entre clases distintas.

Ambas convenciones se relacionan mediante:

[
|R-S|_F=\sqrt2|p(R)-p(S)|_2.
]

La elección de norma deberá mantenerse fija durante las comparaciones.

---

47. Insuficiencia de la clasificación espectral

Todos los equilibrios de una arista poseen el mismo espectro:

[
{C_0,-C_0,0^{(22)}}.
]

Por tanto, para todo entero k ≥ 1:

[
\operatorname{tr}(R_e^k)

C_0^k+(-C_0)^k.
]

Las trazas de potencias son independientes de la posición de la arista.

En consecuencia, ni el espectro ni las trazas individuales de potencias permiten distinguir las 21 clases estratificadas, las 72 clases rotacionales o las 144 clases residuales.

La clasificación requiere información adicional sobre la arquitectura.

---

48. Invariantes estratificados completos

Sea:

[
W=\operatorname{diag}(g_1,\ldots,g_{24}),
]

con pesos positivos constantes dentro de cada estrato.

Consideramos:

[
I_1(R)=\operatorname{tr}(WR^2),
]

[
I_2(R)=\operatorname{tr}(W^2R^2).
]

Para una arista ab:

[
I_1(R_e)=C_0^2(g_a+g_b),
]

[
I_2(R_e)=C_0^2(g_a^2+g_b^2).
]

Si los seis pesos estratificados son distintos y C0 es conocida, ambos invariantes determinan el par no ordenado de estratos.

Por tanto, constituyen una familia completa para las 21 clases de equilibrios de una arista bajo (G_S).

La demostración de reconstrucción, las condiciones de admisibilidad y el tratamiento de degeneraciones se desarrollan en:

- "INFORMATION_RECOVERY.md"
- La ampliación correspondiente de "MULTILAYER_INVARIANTS.md".

Esta completitud no se extiende automáticamente a configuraciones de soporte arbitrario.

---

49. Estabilidad de los equilibrios

De acuerdo con los resultados analíticos de "REDUCED_SUPPORT_STABILITY.md", para:

[
0<\mu\leq1,
]

y:

[
\gamma>1,
]

cada equilibrio de una arista es localmente asintóticamente estable.

En el dominio de masa fija:

[
\Phi(R_e+E)-R_e

(1-\mu)E+O(|E|^\gamma).
]

La derivada relativa al dominio admisible es:

[
D\Phi(R_e)=(1-\mu)I
]

sobre las direcciones de masa fija.

Su radio espectral es:

[
\rho=1-\mu<1.
]

Para μ = 1, el término lineal desaparece y la convergencia local admite una cota superlineal de orden γ.

Régimen γ = 1

La invasión mediante un nodo exterior k presenta un multiplicador:

[
\eta_k=
1-\mu+
\mu g_k
\left(
\frac1{g_a}+\frac1{g_b}
\right).
]

Cuando los pesos son constantes por estratos de cuatro nodos, existe un nodo exterior de peso máximo.

En consecuencia, existe una dirección admisible de invasión con:

[
\eta_k>1.
]

Los equilibrios de una arista son inestables bajo estas hipótesis.

Régimen 0 < γ < 1

Las perturbaciones exteriores de masa s pueden generar términos de orden:

[
s^\gamma.
]

Como:

[
\frac{s^\gamma}{s}\longrightarrow\infty
]

cuando s tiende a cero por valores positivos, el análisis de invasión sobre una cara de tres nodos establece la inestabilidad local.

Resumen

Régimen| Estabilidad de una arista
μ = 0| Operador identidad; sin atracción asintótica individual.
0 < γ < 1, μ > 0| Inestable.
γ = 1, μ > 0| Inestable bajo las hipótesis estratificadas.
γ > 1, μ > 0| Localmente asintóticamente estable.

Estos resultados corresponden al operador matricial especificado.

No constituyen una clasificación de estabilidad de todos los posibles equilibrios.

---

50. Obstrucción a la contractividad global

Sea G uno de los grupos:

[
G_2,\quad G_4,\quad G_S.
]

Supongamos que el operador es G-equivariante sobre un dominio que contiene los equilibrios estudiados.

El operador inducido satisface:

[
\overline\Phi([R_e])=[R_e].
]

Existen al menos dos clases distintas de puntos fijos para cada uno de estos grupos.

Sean:

[
[R_e]\neq[R_f].
]

Entonces:

[
d_G(\overline\Phi([R_e]),\overline\Phi([R_f]))

d_G([R_e],[R_f])>0.
]

Si el operador inducido admite una constante global de Lipschitz L:

[
d_G(\overline\Phi([R_e]),\overline\Phi([R_f]))
\leq
L,d_G([R_e],[R_f]).
]

Dividiendo por la distancia positiva:

[
L\geq1.
]

Por tanto, no existe una constante uniforme de contracción estricta L < 1 sobre dicho dominio.

Este resultado no requiere estabilidad local de los puntos fijos.

Tampoco requiere completitud del espacio métrico.

La existencia de múltiples clases de equilibrios es suficiente.

---

51. Consecuencias para la dominancia apical

Para γ > 1, los 190 equilibrios sin extremos apicales son localmente asintóticamente estables bajo las hipótesis del operador matricial.

Existen configuraciones estrictamente positivas suficientemente próximas a dichos equilibrios que convergen hacia ellos.

Por tanto, la atracción apical universal queda descartada incluso si las condiciones iniciales se restringen a matrices estrictamente positivas del dominio considerado.

Sin embargo, no se deduce:

- Que las cuencas no apicales sean mayoritarias.
- Que todos los equilibrios tengan igual probabilidad de aparición.
- Que los pesos geométricos carezcan de influencia dinámica.
- Que la dominancia apical estadística sea imposible.

El número de equilibrios y el volumen de sus cuencas son magnitudes diferentes.

---

52. Verificación computacional

La auditoría asociada a esta ampliación se recoge en:

- "quotient_space_audit.py"
- "quotient_space_results.json"

El protocolo contempla:

1. Enumeración de las 276 aristas.
2. Clasificación bajo los grupos considerados.
3. Recuento de aristas fijadas.
4. Verificación de tamaños de órbita.
5. Clasificación por participación apical.
6. Comparación de distancias entre clases.
7. Insuficiencia de invariantes espectrales.
8. Reconstrucción mediante invariantes estratificados.
9. Equivarianza del operador de referencia.
10. Controles negativos.
11. Conservación de masa.
12. Obstrucción a la contractividad global estricta.

Los resultados observados deberán consultarse en el registro JSON correspondiente.

La auditoría complementa las demostraciones analíticas y no sustituye la certificación de la implementación canónica.

---

53. Resultados consolidados

Resultado| Estado
Existencia de 276 equilibrios de una arista| Demostrado para el operador especificado.
Clasificación bajo S24| 1 clase combinatoria.
Clasificación bajo Z2| 144 clases.
Clasificación bajo Z4| 72 clases.
Clasificación bajo el grupo estratificado| 21 clases.
Equilibrios sin extremos apicales| 190.
Clases no apicales bajo Z2| 100.
Clases no apicales bajo Z4| 50.
Clases no apicales estratificadas| 15.
Distancia diádica entre clases distintas| Raíz cuadrada de 2 multiplicada por C0.
Insuficiencia de invariantes espectrales| Demostrada.
Completitud de I1 e I2| Demostrada para la familia estratificada indicada.
Estabilidad para γ > 1| Demostrada localmente.
Contractividad global estricta| Descartada en los dominios indicados.
Atracción apical universal| Descartada bajo las hipótesis especificadas.

---

54. Investigaciones pendientes

1. Clasificación de equilibrios de soporte superior a una arista.
2. Determinación de todos los puntos fijos del operador.
3. Estabilidad de soportes con pesos heterogéneos.
4. Estimación de cuencas de atracción.
5. Dominancia apical estadística.
6. Identificación del grupo geométrico canónico completo.
7. Certificación de la implementación original.
8. Comparación con arquitecturas nulas.
9. Equivariancia de los operadores 44A y 44B.
10. Recuperabilidad dinámica e invertibilidad global.
11. Correspondencia con la TRCG.

---

55. Gobernanza de la ampliación

Se mantienen íntegramente:

- Nivel II retenido.
- Nivel III abierto.
- λ reservado exclusivamente al 4º Factor.
- Versiones 1.6 y 1.7 aisladas.
- Campaña experimental del Episodio 44 congelada.
- Sin reescalados post hoc.
- Sin equivalencias automáticas.
- Sin ascensos automáticos.
- Independencia de las formulaciones matemáticas.
- Conservación de resultados negativos.

---

56. Conclusión de la ampliación

La clasificación exacta de los equilibrios de una arista permite distinguir tres niveles:

- Multiplicidad de configuraciones.
- Diversidad estructural respecto de un grupo.
- Diversidad dinámica respecto de un operador.

Los 276 equilibrios pueden organizarse en 144 clases residuales, 72 clases rotacionales o 21 clases estratificadas.

Estas clasificaciones no son contradictorias.

Responden a diferentes relaciones de equivalencia.

La existencia de 190 equilibrios no apicales y su estabilidad bajo determinadas condiciones establece una limitación matemática concreta a la atracción apical universal.

La coexistencia de múltiples clases de puntos fijos descarta la contractividad global estricta del operador inducido sobre los espacios cociente considerados.

La investigación deberá avanzar hacia la clasificación de soportes superiores, la determinación de cuencas y la recuperabilidad de información.

La geometría establece posibilidades.

La simetría organiza configuraciones.

La dinámica determina evoluciones.

La estabilidad exige demostración.

La dominancia exige cuantificación.

La convergencia exige verificación.

---

FIN DEL DOCUMENTO



