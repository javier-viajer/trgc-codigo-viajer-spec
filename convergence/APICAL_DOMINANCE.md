# APICAL DOMINANCE

## Fundamentos matemáticos de la dominancia apical

**Proyecto:** Convergencia TRCG — Código Viajer  
**Versión:** 0.1.0  
**Fecha:** 2026-11-26  
**Estado:** Demostraciones algebraicas condicionales  
**Gobernanza:** Nivel II retenido · Nivel III abierto  

---

## 1. Objeto

Establecer las condiciones matemáticas bajo
las cuales una ventaja geométrica apical
puede convertirse en dominancia dinámica
y concentración asintótica.

Se pretende distinguir rigurosamente:

- Ventaja geométrica.
- Dominancia relacional.
- Crecimiento de masa apical.
- Estabilidad local.
- Concentración asintótica.
- Dominancia estadística.
- Atracción universal.

Estas propiedades no son equivalentes.

El presente documento desarrolla resultados
generales aplicables a una familia de
operadores multiplicativos normalizados.

Su correspondencia con el operador canónico
completo de Pirámide-Parábola deberá
verificarse independientemente.

No se presupone una equivalencia entre
Pirámide-Parábola y la TRCG.

## 2. Documentos relacionados

- EFFECTIVE_SYMMETRY_GROUP.md
- MULTILAYER_INVARIANTS.md
- RELATIONAL_QUOTIENT_METRIC.md
- PP_AUTOMORPHISM_GROUP.md
- PP_MULTILAYER_VERIFICATION.py
- pp_verification.json
- EQUILIBRIUM_CLASSIFICATION.md

## 3. Dominio matemático

Consideramos el modelo nodal parcial
de 24 nodos:

V = {0,1,...,23}

Distribuidos en seis estratos
de cuatro nodos cada uno.

Definimos el conjunto apical:

A = {5,11,17,23}

Y su complemento:

B = V \ A

Por tanto:

|A| = 4

|B| = 20

Esta identificación utiliza la numeración
adoptada en PP_AUTOMORPHISM_GROUP.md.

El espacio de estados considerado es
el simplex normalizado:

X = {x ∈ ℝ²⁴ :
     x_i ≥ 0,
     Σ_i x_i = 1}

La aplicación a estados relacionales
matriciales o híbridos exige definir
previamente una representación nodal
compatible con su dinámica.

## 4. Masa apical

Definimos:

a(x) = Σ_(i∈A) x_i

La masa no apical es:

b(x) = Σ_(i∈B) x_i

Por normalización:

a(x) + b(x) = 1

Por tanto:

0 ≤ a(x) ≤ 1

Los casos extremos son:

a(x) = 0

Ausencia completa de masa apical.

a(x) = 1

Concentración completa de masa
en el conjunto apical.

La concentración apical no implica
concentración en un único nodo.

## 5. Referencia uniforme

Para una distribución uniforme:

x_i = 1/24

La masa apical es:

a_ref = |A|/|V|

Por tanto:

a_ref = 4/24 = 1/6

Esta referencia permite comparar
la representación apical con su
proporción dentro del conjunto nodal.

No constituye una predicción dinámica.

Tampoco sustituye a los controles
experimentales mediante arquitecturas nulas.

## 6. Índice de dominancia apical

Definimos:

D_A(x) = a(x)/a_ref

Por tanto:

D_A(x) = 6a(x)

Su intervalo de valores es:

0 ≤ D_A(x) ≤ 6

Interpretación:

| Valor | Interpretación |
|-------|----------------|
| D_A = 0 | Ausencia apical |
| 0 < D_A < 1 | Infrarrepresentación |
| D_A = 1 | Representación proporcional |
| 1 < D_A < 6 | Sobrerrepresentación |
| D_A = 6 | Concentración completa |

El índice D_A mide sobrerrepresentación
respecto de la referencia uniforme.

No mide directamente estabilidad,
causalidad ni capacidad de atracción.

## 7. Diferentes formas de dominancia

### 7.1 Dominancia geométrica

Existe cuando el factor geométrico
apical supera al de los demás nodos.

### 7.2 Dominancia dinámica instantánea

Existe cuando:

a(F(x)) > a(x)

### 7.3 Dominancia dinámica acumulada

Existe una ventaja acumulada cuando
el balance temporal favorece al ápice.

### 7.4 Concentración asintótica

Existe cuando:

lim_(t→∞) a(x_t) = 1

### 7.5 Dominancia estadística

Existe sobrerrepresentación apical
en promedio cuando:

E[D_A(x_final)] > 1

respecto de una distribución inicial
y un protocolo previamente definidos.

### 7.6 Atracción apical universal

Existe cuando todas las condiciones
iniciales del dominio especificado
convergen hacia un conjunto apical
previamente definido.

Estas definiciones deben mantenerse
separadas durante la investigación.

## 8. Familia de operadores multiplicativos

Consideramos:

F_i(x) = x_i f_i(x)/Z(x)

donde:

Z(x) = Σ_j x_j f_j(x)

y:

f_i(x) > 0

para todo nodo y estado admisible.

Los factores f_i representan ventajas
efectivas que pueden depender de:

- Geometría.
- Relaciones.
- Estado nodal.
- Acoplamientos.
- Parámetros dinámicos.

Como Z(x) > 0:

F_i(x) ≥ 0

Además:

Σ_i F_i(x) = 1

Por tanto:

F : X → X

El operador conserva el simplex.

Esta familia constituye un modelo
matemático auxiliar.

No se afirma que reproduzca
automáticamente las reglas de 44A,
44B o del sistema híbrido completo.

## 9. Ventajas efectivas medias

Para estados con:

0 < a(x) < 1

definimos:

f_A(x) =
Σ_(i∈A) x_i f_i(x)/a(x)

f_B(x) =
Σ_(i∈B) x_i f_i(x)/(1−a(x))

Ambas cantidades son positivas.

Representan las ventajas medias
ponderadas de los grupos apical
y no apical.

El normalizador puede escribirse:

Z(x) = a(x)f_A(x)
       + (1−a(x))f_B(x)

## 10. Teorema de evolución apical

### Teorema 1

Para el operador multiplicativo
normalizado se cumple:

a(F(x)) =
a(x)f_A(x) /
[a(x)f_A(x)+(1−a(x))f_B(x)]

### Demostración

Por definición:

a(F(x)) = Σ_(i∈A) F_i(x)

Sustituyendo el operador:

a(F(x)) =
Σ_(i∈A) x_i f_i(x)/Z(x)

Por definición de f_A:

Σ_(i∈A) x_i f_i(x) = a(x)f_A(x)

Sustituyendo Z(x):

a(F(x)) =
a(x)f_A(x) /
[a(x)f_A(x)+(1−a(x))f_B(x)]

Queda demostrado.

## 11. Criterio exacto de crecimiento

### Teorema 2

Para estados con 0 < a < 1:

a(F(x))−a(x) =

a(1−a)(f_A−f_B) /
[af_A+(1−a)f_B]

### Demostración

Restamos a a la expresión obtenida
en el teorema anterior.

Agrupando términos:

a(F(x))−a =

[af_A−a²f_A−a(1−a)f_B] /
[af_A+(1−a)f_B]

Factorizando:

a(F(x))−a =

a(1−a)(f_A−f_B) /
[af_A+(1−a)f_B]

Queda demostrado.

### Corolario

Como el denominador es positivo:

a(F(x)) > a(x)

si y solo si:

f_A(x) > f_B(x)

Análogamente:

a(F(x)) = a(x)

si y solo si:

f_A(x) = f_B(x)

Y:

a(F(x)) < a(x)

si y solo si:

f_A(x) < f_B(x)

La ventaja efectiva media determina
exactamente el crecimiento apical.

La posición geométrica, por sí sola,
no determina este crecimiento.

## 12. Cociente de ventaja apical

Definimos:

η(x) = f_A(x)/f_B(x)

Entonces:

a(F(x)) =
a(x)η(x) /
[1−a(x)+a(x)η(x)]

Para una trayectoria:

x_(t+1) = F(x_t)

escribimos:

a_t = a(x_t)

η_t = η(x_t)

Por tanto:

a_(t+1) =
a_t η_t /
[1−a_t+a_t η_t]

Esta ecuación describe exactamente
la evolución agregada de la masa
apical para la familia estudiada.

No implica que η_t dependa
exclusivamente de a_t.

La dinámica agregada puede depender
del estado nodal completo.

## 13. Evolución de la razón apical

Definimos:

Q_t = a_t/(1−a_t)

Para 0 < a_t < 1:

Q_(t+1) = η_t Q_t

Iterando:

Q_t = Q_0 Π_(k=0)^(t−1) η_k

Por tanto:

a_t =
1 /
[1+((1−a_0)/a_0)
Π_(k=0)^(t−1) η_k^(-1)]

Esta identidad es exacta.

## 14. Teorema de concentración apical

### Teorema 3

Supongamos:

0 < a_0 < 1

y que existe una constante δ > 0
tal que:

η_t ≥ 1+δ

para todo t ≥ 0.

Entonces:

lim_(t→∞) a_t = 1

### Demostración

Por la identidad anterior:

Q_t = Q_0 Π_k η_k

Como:

η_k ≥ 1+δ

obtenemos:

Q_t ≥ Q_0(1+δ)^t

Dado que:

1+δ > 1

se cumple:

Q_t → +∞

Como:

a_t = Q_t/(1+Q_t)

resulta:

a_t → 1

Queda demostrado.

### Alcance

El teorema garantiza concentración
de masa en el conjunto apical.

No garantiza:

- Convergencia del estado completo.
- Existencia de un único equilibrio.
- Selección de un nodo apical.
- Estabilidad de un atractor concreto.
- Ausencia de oscilaciones internas
  entre los nodos apicales.

## 15. Cota de velocidad de concentración

Bajo las hipótesis del teorema 3:

a_t ≥

1 /
[1+((1−a_0)/a_0)(1+δ)^(-t)]

Equivalentemente:

1−a_t ≤
((1−a_0)/a_0)(1+δ)^(-t)

Por tanto, la masa no apical
decrece al menos exponencialmente
según esta cota.

Para alcanzar:

a_t ≥ 1−ε

con 0 < ε < 1,

es suficiente que:

t ≥ max{0, ceil(L)}

donde:

L =

log[((1−a_0)(1−ε))/(a_0 ε)]
/
log(1+δ)

Esta cota depende de:

- Masa apical inicial.
- Ventaja efectiva mínima.
- Precisión de concentración deseada.

No representa un tiempo físico
sin una correspondencia temporal
adicional.

## 16. Ventaja acumulada

Definimos:

L_t = Σ_(k=0)^(t−1) log(η_k)

Entonces:

log(Q_t) = log(Q_0)+L_t

Por tanto:

a_t =
1 /
[1+((1−a_0)/a_0)exp(−L_t)]

La evolución apical queda determinada
por la ventaja logarítmica acumulada.

## 17. Condición necesaria y suficiente

### Teorema 4

Para 0 < a_0 < 1:

a_t → 1

si y solo si:

L_t → +∞

### Demostración

Por la identidad anterior:

a_t → 1

si y solo si:

exp(−L_t) → 0

Esto ocurre si y solo si:

L_t → +∞

Queda demostrado.

### Corolarios

Si:

L_t → −∞

entonces:

a_t → 0

Si:

L_t → L_finito

entonces:

a_t → a_infinito

donde:

a_infinito =
1 /
[1+((1−a_0)/a_0)exp(−L_finito)]

En este último caso:

0 < a_infinito < 1

Por tanto, una ventaja acumulada
finita puede producir concentración
parcial, pero no concentración total.

## 18. Contraejemplo a la ventaja permanente

Una ventaja apical positiva en cada
iteración no garantiza por sí sola
la concentración completa.

Consideremos:

η_t = exp(1/2^(t+1))

Para todo t:

η_t > 1

Sin embargo:

log(η_t) = 1/2^(t+1)

Por tanto:

Σ_(t=0)^∞ log(η_t) = 1

La ventaja acumulada es finita.

Para una distribución inicial uniforme:

a_0 = 1/6

obtenemos:

a_infinito = exp(1)/(5+exp(1))

Numéricamente:

a_infinito ≈ 0.352187

Por tanto:

D_A(x_infinito) ≈ 2.11312

Existe sobrerrepresentación apical.

La masa apical aumenta en cada paso.

Sin embargo, no converge a uno.

Esta sucesión de ventajas puede
realizarse mediante una familia
multiplicativa dependiente del tiempo.

El contraejemplo demuestra que
dominancia instantánea permanente
y concentración completa son
propiedades diferentes.

## 19. Separación geométrico-relacional

Supongamos que:

f_i(x) = g_i c_i(x)

donde:

g_i > 0

representa el factor geométrico,

y:

c_i(x) > 0

representa la contribución efectiva
relacional y dinámica.

Definimos:

g_A_min = min_(i∈A) g_i

g_B_max = max_(i∈B) g_i

Supongamos que existen cotas uniformes:

c_i(x) ≥ c_A_min > 0

para i ∈ A,

y:

c_j(x) ≤ c_B_max

para j ∈ B.

Entonces:

f_A(x) ≥ g_A_min c_A_min

f_B(x) ≤ g_B_max c_B_max

## 20. Umbral de dominancia efectiva

### Teorema 5

Bajo las hipótesis anteriores:

η(x) ≥

(g_A_min c_A_min) /
(g_B_max c_B_max)

Si:

g_A_min c_A_min >
g_B_max c_B_max

entonces existe δ > 0 tal que:

η(x) ≥ 1+δ

para todo estado interior admisible.

### Demostración

Las ventajas medias ponderadas
están acotadas por los extremos
de sus factores individuales.

Por tanto:

f_A/f_B ≥

(g_A_min c_A_min) /
(g_B_max c_B_max)

Si el cociente del lado derecho
es estrictamente mayor que uno,
definimos:

δ =

(g_A_min c_A_min) /
(g_B_max c_B_max) − 1

Entonces:

δ > 0

Aplicando el teorema 3:

a_t → 1

para toda condición inicial con:

a_0 > 0

El caso a_0 = 1 permanece
concentrado en A.

Queda demostrado.

### Interpretación

La ventaja geométrica debe ser
suficiente para superar cualquier
compensación relacional adversa
dentro del dominio estudiado.

La condición es suficiente,
pero no necesaria.

Su incumplimiento no demuestra
ausencia de dominancia apical.

## 21. Contraejemplo a la suficiencia geométrica

Consideremos:

g_i = 2 para i ∈ A

g_j = 1 para j ∈ B

Existe una ventaja geométrica apical.

Sin embargo, supongamos:

c_i = 1/4 para i ∈ A

c_j = 1 para j ∈ B

Entonces:

f_A = 2·(1/4) = 1/2

f_B = 1·1 = 1

Por tanto:

η = 1/2

La masa apical disminuye
en cada iteración interior.

Además:

a_t → 0

para toda condición inicial con:

0 < a_0 < 1

Queda demostrado mediante
contraejemplo que una ventaja
geométrica estricta no garantiza
dominancia dinámica.

Este ejemplo es auxiliar.

No representa parámetros medidos
de Pirámide-Parábola.

## 22. Conservación del soporte

### Teorema 6

Para el operador multiplicativo
con factores estrictamente positivos:

F_i(x) = 0

si y solo si:

x_i = 0

### Demostración

Por definición:

F_i(x) = x_i f_i(x)/Z(x)

Como:

f_i(x) > 0

Z(x) > 0

se cumple:

F_i(x) = 0 ⇔ x_i = 0

Queda demostrado.

### Consecuencia

El soporte nodal permanece
inalterado en cada iteración finita.

Los nodos inicialmente ausentes
no aparecen espontáneamente.

Los nodos inicialmente presentes
pueden tender a cero asintóticamente,
pero no desaparecen en tiempo finito
bajo aritmética exacta.

Esta propiedad puede dejar de
cumplirse si existen:

- Términos aditivos.
- Mutaciones.
- Inyección de masa.
- Difusión.
- Umbrales.
- Redondeos.
- Reglas discretas de activación.

## 23. Cara no apical invariante

Definimos:

X_0 = {x ∈ X : a(x) = 0}

### Teorema 7

Para el operador multiplicativo:

F(X_0) ⊆ X_0

### Demostración

Si:

a(x) = 0

Como x_i ≥ 0:

x_i = 0

para todo i ∈ A.

Por conservación del soporte:

F_i(x) = 0

para todo i ∈ A.

Por tanto:

a(F(x)) = 0

Queda demostrado.

La cara no apical es invariante.

Su dimensión afín es:

dim(X_0) = 20−1 = 19

## 24. Cara apical invariante

Definimos:

X_1 = {x ∈ X : a(x) = 1}

Por conservación del soporte:

F(X_1) ⊆ X_1

La cara apical posee dimensión afín:

dim(X_1) = 4−1 = 3

La invariancia de X_1 no implica
la existencia de un único atractor.

Pueden existir diferentes equilibrios,
órbitas periódicas u otras dinámicas
dentro de la cara apical.

## 25. Existencia de equilibrios no apicales

### Teorema 8

Si los factores f_i son continuos
y estrictamente positivos en X,
existe al menos un equilibrio
en la cara no apical X_0.

### Demostración

X_0 es un conjunto no vacío,
compacto y convexo.

El operador F es continuo.

Por el teorema 7:

F(X_0) ⊆ X_0

Por el teorema del punto fijo
de Brouwer, existe:

x* ∈ X_0

tal que:

F(x*) = x*

Queda demostrado.

### Observación

En esta familia multiplicativa,
la existencia puede demostrarse
también directamente.

Cada vértice del simplex
es un equilibrio.

En particular, los veinte vértices
no apicales son equilibrios.

Esto no implica que sean estables.

Tampoco permite deducir la existencia
de exactamente 190 equilibrios.

## 26. Condición de equilibrio

### Teorema 9

Un estado x* es equilibrio si
y solo si:

f_i(x*) = Z(x*)

para todo i perteneciente
al soporte de x*.

### Demostración

La condición de equilibrio es:

x_i* f_i(x*)/Z(x*) = x_i*

Para x_i* > 0 podemos dividir
por x_i* y obtener:

f_i(x*) = Z(x*)

Para x_i* = 0 la igualdad
se satisface automáticamente.

Queda demostrado.

### Corolario

En un equilibrio con presencia
apical y no apical:

0 < a(x*) < 1

necesariamente:

f_A(x*) = f_B(x*)

Por tanto:

η(x*) = 1

No puede existir un equilibrio
mixto bajo una ventaja efectiva
apical estricta en todo el dominio
de estados mixtos.

## 27. Estabilidad transversal no apical

Sea:

x* ∈ X_0

un equilibrio.

Supongamos que F admite una
extensión continuamente diferenciable
en un entorno de x*.

Definimos:

Z* = Σ_(j∈B) x_j* f_j(x*)

Para cada nodo apical:

m_i = f_i(x*)/Z*

El valor m_i representa el
multiplicador lineal de invasión
apical en ese equilibrio.

## 28. Derivación de los multiplicadores

Como:

F_i(x) = x_i f_i(x)/Z(x)

y para i ∈ A:

x_i* = 0

la derivada en x* satisface:

∂F_i/∂x_j (x*) =
δ_ij f_i(x*)/Z*

donde δ_ij es el delta de Kronecker.

Por tanto:

DF_i(x*)v = m_i v_i

para una perturbación v.

El bloque apical del jacobiano
es diagonal:

J_A = diag(m_i : i ∈ A)

Las perturbaciones apicales
deben compensarse mediante cambios
en la masa no apical para conservar
la normalización.

El análisis debe realizarse sobre
las perturbaciones admisibles.

## 29. Criterio de invasión apical

### Teorema 10

Si existe un nodo apical i tal que:

m_i > 1

entonces el equilibrio no apical
es inestable frente a perturbaciones
apicales admisibles.

### Demostración

Por continuidad, existe un entorno
de x* y una constante κ > 1
tales que:

f_i(x)/Z(x) ≥ κ

dentro de dicho entorno.

Introducimos una perturbación
admisible con masa positiva en i.

Mientras la trayectoria permanezca
en el entorno:

x_i(t+1) ≥ κ x_i(t)

Por tanto:

x_i(t) ≥ κ^t x_i(0)

Si permaneciera indefinidamente
en el entorno, esta componente
crecería sin límite.

Esto contradice:

x_i(t) ≤ 1

Por tanto, la trayectoria debe
abandonar el entorno.

Pueden elegirse perturbaciones
iniciales arbitrariamente pequeñas.

El equilibrio es inestable.

Queda demostrado.

## 30. Resistencia a la invasión

Si:

max_(i∈A) m_i < 1

las componentes apicales son
contractivas a primer orden.

Por continuidad existe κ < 1
tal que, en un entorno adecuado:

a(F(x)) ≤ κ a(x)

Esta desigualdad es válida mientras
la trayectoria permanezca dentro
de dicho entorno.

No garantiza por sí sola estabilidad
del equilibrio completo.

También deben analizarse:

- Perturbaciones internas no apicales.
- Nodos no apicales ausentes.
- Acoplamientos entre componentes.
- Restricciones adicionales.

Si algún multiplicador es igual a uno,
el análisis lineal resulta insuficiente
para resolver esa dirección.

## 31. Estabilidad completa

Sea J el jacobiano del operador
sobre el espacio afín normalizado.

Para un equilibrio situado en
la cara no apical, la invariancia
de dicha cara permite una estructura
por bloques:

J = | J_B C |
    | 0 J_A |

donde:

J_B representa la dinámica interna
de la cara no apical.

J_A contiene los multiplicadores
de invasión apical.

C representa el acoplamiento
de las perturbaciones apicales
sobre las variables no apicales.

Por tanto:

spec(J) = spec(J_B) ∪ spec(J_A)

Y:

ρ(J) =
max{ρ(J_B), max_(i∈A) m_i}

Bajo las hipótesis de regularidad
y admisibilidad correspondientes,
una condición suficiente de
estabilidad asintótica local es:

ρ(J_B) < 1

y:

max_(i∈A) m_i < 1

La estabilidad interna de la cara
no apical no garantiza estabilidad
frente a invasiones apicales.

## 32. Obstrucción a la atracción universal

La existencia de un equilibrio
no apical admisible impide afirmar
que toda condición inicial del
dominio converge hacia estados
con presencia apical positiva.

En efecto, si:

x_0 = x*

y:

F(x*) = x*

entonces:

F^t(x*) = x*

para todo t.

Si:

a(x*) = 0

la trayectoria permanece
no apical indefinidamente.

Este resultado no exige que
el equilibrio sea estable.

No descarta:

- Dominancia apical estadística.
- Atracción apical casi segura.
- Concentración desde estados mixtos.
- Cuencas apicales mayoritarias.

La universalidad debe formularse
respecto de un dominio explícito.

## 33. Relación con los 190 equilibrios

Se han comunicado 190 equilibrios
sin presencia de nodos apicales.

Este documento no contiene
los estados originales ni verifica
independientemente su condición
de equilibrio.

Si su existencia y admisibilidad
se confirman, constituyen una
obstrucción a la atracción apical
universal del operador correspondiente.

Si además dicho operador pertenece
a la familia multiplicativa aquí
estudiada, podrá analizarse:

- Conservación del soporte.
- Invariancia de la cara no apical.
- Multiplicadores de invasión.
- Estabilidad interna.
- Estabilidad transversal.
- Cuencas de atracción.

Para cada equilibrio x* deberán
calcularse, cuando proceda:

m_5

m_11

m_17

m_23

El mayor multiplicador apical
proporcionará un criterio inicial
de resistencia o vulnerabilidad
frente a invasiones apicales.

No se atribuyen valores numéricos
a estos multiplicadores sin disponer
de los estados y del operador exacto.

## 34. Dominancia y simetría

Sea:

r(i) = i+12 mod 24

La transformación conserva
el conjunto apical:

r(A) = A

Por tanto:

a(r · x) = a(x)

También:

D_A(r · x) = D_A(x)

La masa apical y su índice
de dominancia son invariantes
bajo esta transformación.

Si las cuatro rotaciones espaciales
son admisibles, el mismo resultado
se extiende a ellas.

La invariancia del observable apical
no demuestra la equivariancia
del operador dinámico.

## 35. Dominancia en el espacio cociente

Sea G un grupo admisible
que conserva el conjunto A.

Definimos:

a_G([x]) = a(x)

D_(A,G)([x]) = D_A(x)

Estas expresiones son independientes
del representante de la órbita.

Por tanto, la clasificación
estructural de equilibrios puede
realizarse sin alterar su masa
apical ni su índice de dominancia.

La existencia de una dinámica
inducida sobre el espacio cociente
requiere condiciones adicionales
de equivariancia.

## 36. Dominancia estadística

Sea μ una distribución de
condiciones iniciales.

Para un horizonte T definimos:

M_A(T) = E_μ[a(F^T(x))]

El índice medio correspondiente es:

D̄_A(T) = 6M_A(T)

Si:

D̄_A(T) > 1

existe sobrerrepresentación apical
media respecto de la referencia
uniforme nodal.

Sin embargo, para atribuir dicha
sobrerrepresentación a la geometría
es necesario comparar con:

- La distribución inicial.
- Una arquitectura basal.
- Arquitecturas nulas.
- Ablaciones geométricas.
- Operadores equivalentes.

La referencia uniforme no constituye
por sí sola un control causal.

## 37. Probabilidad de concentración

Para un umbral previamente fijado:

0 < τ ≤ 1

definimos:

P_A(T,τ) =
μ({x : a(F^T(x)) ≥ τ})

Esta magnitud representa la
probabilidad de alcanzar al menos
una masa apical τ en el horizonte T.

Debe distinguirse de:

M_A(T)

Una masa media elevada no implica
que todas las trayectorias presenten
dominancia apical.

Para τ = 1, la concentración exacta
en tiempo finito puede ser imposible
desde estados mixtos bajo una
dinámica multiplicativa positiva.

Por ello deberán distinguirse:

- Concentración exacta.
- Concentración aproximada.
- Concentración asintótica.

## 38. Dominancia estadística asintótica

Si existe el límite:

a_infinito(x) =
lim_(t→∞) a(F^t(x))

para μ-casi toda condición inicial,
definimos:

M_A_infinito = E_μ[a_infinito(x)]

Como:

0 ≤ a(F^t(x)) ≤ 1

el teorema de convergencia dominada
permite establecer:

lim_(t→∞) M_A(t) = M_A_infinito

La existencia del límite de masa
apical no exige necesariamente
convergencia del estado completo.

Cuando existan trayectorias
sin límite apical, deberán
registrarse separadamente o
utilizarse observables temporales
previamente especificados.

## 39. Protocolo experimental

Para cada arquitectura y operador
deberán registrarse:

1. Masa apical inicial.

2. Masa apical final.

3. Índice de dominancia inicial.

4. Índice de dominancia final.

5. Variación de masa apical.

6. Frecuencia de crecimiento apical.

7. Frecuencia de retroceso apical.

8. Probabilidad de concentración.

9. Distribución de estados finales.

10. Equilibrios no apicales.

11. Equilibrios mixtos.

12. Equilibrios completamente apicales.

13. Multiplicadores de invasión,
    cuando sean aplicables.

14. Ventaja acumulada,
    cuando el operador permita
    definirla de manera exacta.

15. Casos no convergentes.

Las métricas deberán conservar
la identificación de la arquitectura,
el operador y las condiciones iniciales.

## 40. Controles geométricos y dinámicos

Para separar las contribuciones
geométricas y algorítmicas se
propone comparar:

A. Arquitectura nominal.

B. Arquitectura basal.

C. Arquitecturas nulas.

D. Ablación del factor geométrico.

E. Ablación de capas relacionales.

F. Variaciones previamente fijadas
   de los factores de acoplamiento.

Las comparaciones deberán utilizar:

- Condiciones iniciales compatibles.
- Semillas emparejadas.
- Órdenes de actualización compatibles.
- Presupuestos computacionales iguales.
- Criterios de convergencia comunes.
- Umbrales definidos previamente.

No se modificarán retrospectivamente
los protocolos congelados.

Estas comparaciones constituyen
propuestas para investigaciones
posteriores.

## 41. Relación con 44A y 44B

La dinámica variacional 44A y
la dinámica de consenso circular
44B deberán estudiarse por separado.

No se presupone que ninguna de
ellas pertenezca a la familia
multiplicativa normalizada.

Antes de aplicar los teoremas
anteriores deberá verificarse:

- Espacio de estados.
- Representación nodal.
- Definición de masa apical.
- Conservación de la normalización.
- Conservación del soporte.
- Forma exacta del operador.
- Admisibilidad de perturbaciones.
- Equivarianza dinámica.

Si estas hipótesis no se cumplen,
deberán desarrollarse criterios
específicos para cada dinámica.

Los resultados de este documento
no modifican el Episodio 44.

## 42. Pruebas computacionales propuestas

T01. Conservación del simplex.

T02. Conservación del soporte.

T03. Evolución exacta de masa apical.

T04. Identidad del incremento apical.

T05. Cociente de ventaja efectiva.

T06. Identidad de ventaja acumulada.

T07. Concentración con ventaja uniforme.

T08. Cota de velocidad de concentración.

T09. Contraejemplo de ventaja decreciente.

T10. Contraejemplo geométrico-relacional.

T11. Invariancia de la cara no apical.

T12. Invariancia de la cara apical.

T13. Condición de equilibrio.

T14. Multiplicadores de invasión.

T15. Estabilidad transversal.

T16. Invariancia bajo rotación.

T17. Dominancia sobre el cociente.

T18. Consistencia de probabilidades.

T19. Comparación con arquitecturas nulas.

T20. Compatibilidad con operadores
     canónicos.

Las pruebas deberán implementarse
en un módulo independiente.

Las pruebas numéricas no sustituyen
a las demostraciones algebraicas.

## 43. Resultados demostrados

Para la familia multiplicativa
y bajo las hipótesis correspondientes:

- Conservación del simplex.
- Evolución exacta de masa apical.
- Criterio necesario y suficiente
  de crecimiento instantáneo.
- Concentración con ventaja uniforme.
- Cota exponencial de concentración.
- Criterio necesario y suficiente
  de ventaja acumulada.
- Umbral geométrico-relacional.
- Insuficiencia de la ventaja
  geométrica aislada.
- Insuficiencia de la ventaja
  instantánea permanente.
- Conservación del soporte.
- Invariancia de las caras.
- Existencia de equilibrios no apicales.
- Caracterización de equilibrios.
- Multiplicadores de invasión.
- Criterio de inestabilidad transversal.
- Invariancia del observable apical
  bajo simetrías compatibles.

## 44. Resultados pendientes

- Correspondencia con el operador
  canónico de Pirámide-Parábola.

- Determinación de los factores
  geométricos efectivos.

- Determinación de las cotas
  relacionales.

- Verificación de los 190 equilibrios.

- Cálculo de sus multiplicadores
  de invasión.

- Clasificación de su estabilidad.

- Determinación de sus cuencas.

- Dominancia apical estadística.

- Comparación con arquitecturas nulas.

- Aplicación específica a 44A y 44B.

- Correspondencia matemática
  con la TRCG.

- Verificación computacional
  independiente registrada.

## 45. Gobernanza

- Nivel II retenido.
- Nivel III abierto.
- λ reservado al 4º Factor.
- Pirámide-Parábola como candidata
  experimental.
- Independencia de ambas formulaciones.
- Sin equivalencias automáticas.
- Sin ascensos automáticos.
- Sin reescalados retrospectivos.
- Sin modificación de protocolos
  congelados.
- Versiones v1.6 y v1.7 aisladas.

## 46. Conclusión

La dominancia apical no puede
deducirse exclusivamente de una
posición geométrica privilegiada.

Para la familia multiplicativa
normalizada, la condición exacta
de crecimiento apical es:

f_A > f_B

La condición necesaria y suficiente
de concentración asintótica,
desde estados mixtos, es:

Σ_(k=0)^(t−1) log(η_k) → +∞

La ventaja geométrica se convierte
en dominancia efectiva únicamente
cuando las contribuciones dinámicas
y relacionales permiten mantener
un balance favorable.

La conservación del soporte explica
cómo pueden coexistir una tendencia
apical dominante y equilibrios
sin presencia apical.

La existencia de estos equilibrios
no determina automáticamente
su estabilidad ni el tamaño
de sus cuencas de atracción.

La clasificación definitiva exige
conocer el operador generador,
sus restricciones y las condiciones
iniciales admisibles.

La geometría establece ventajas.

Las relaciones pueden reforzarlas
o compensarlas.

La dinámica determina su evolución.

La estabilidad determina su
resistencia a perturbaciones.

Las cuencas determinan su alcance.

La dominancia se cuantifica.

La convergencia se demuestra.

---

FIN DEL DOCUMENTO
