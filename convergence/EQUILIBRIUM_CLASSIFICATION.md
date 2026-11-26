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

FIN DEL DOCUMENTO
