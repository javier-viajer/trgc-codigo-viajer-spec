# PP AUTOMORPHISM GROUP

## Grupo de automorfismos de Pirámide-Parábola

**Proyecto:** Convergencia TRCG — Código Viajer  
**Versión:** 0.1.0  
**Fecha:** 2026-11-26  
**Estado:** Demostración algebraica del modelo parcial  
**Referencia:** TRCG, Episodios 45 y 46  
**Gobernanza:** Nivel II retenido · Nivel III abierto  

---

## 1. Objeto

Determinar el grupo de automorfismos de una
representación combinatoria multicapa de
Pirámide-Parábola y establecer las condiciones
necesarias para extender el resultado a la
arquitectura canónica completa.

El objetivo es identificar las transformaciones
que conservan simultáneamente las familias
relacionales y la identidad de los estratos.

Este documento no presupone una equivalencia
entre Pirámide-Parábola y la TRCG.

## 2. Documentos relacionados

- EFFECTIVE_SYMMETRY_GROUP.md
- MULTILAYER_INVARIANTS.md
- RELATIONAL_QUOTIENT_METRIC.md

## 3. Dominio y convenciones

Consideramos un conjunto de 24 nodos:

V = ℤ_24 = {0,1,...,23}

Todas las operaciones sobre los índices
se realizan módulo 24.

La representación estudiada contiene cuatro
capas relacionales binarias, simétricas
y de diagonal nula.

Estas capas constituyen un modelo combinatorio
parcial de Pirámide-Parábola.

No sustituyen a su especificación canónica
completa.

## 4. Definición de las capas

### 4.1 Contigüidad circular

E_C = {{i,j} : j = i ± 1 mod 24}

Su matriz de adyacencia es A_C.

Número de aristas:

|E_C| = 24

### 4.2 Relaciones triangulares

E_T = {{i,j} : j = i ± 8 mod 24}

Su matriz de adyacencia es A_T.

Número de aristas:

|E_T| = 24

Esta capa contiene ocho componentes
triangulares disjuntas.

### 4.3 Relaciones de cruce

E_X = {{i,j} : j = i ± 6 mod 24}

Su matriz de adyacencia es A_X.

Número de aristas:

|E_X| = 24

Esta capa contiene seis ciclos
disjuntos de longitud cuatro.

### 4.4 Parejas Suma 23

E_S = {{i,j} : j = 23−i}

Su matriz de adyacencia es A_S.

Número de aristas:

|E_S| = 12

La transformación:

s(i) = 23−i

es una involución sin puntos fijos.

La capa E_S representa exclusivamente
el emparejamiento combinatorio Suma 23.

No debe identificarse automáticamente
con cualquier filtro modular Σ_23
definido en otros documentos.

## 5. Arquitectura multicapa parcial

Definimos:

A_4 = (A_C,A_T,A_X,A_S)

Su grupo de automorfismos es:

G_4 = {P ∈ S_24 :
       PA_kPᵀ = A_k para toda capa k}

La identidad de cada capa permanece fija.

No se permiten intercambios entre familias
relacionales diferentes.

## 6. Automorfismos de la contigüidad

### Lema 1

El grupo de automorfismos del ciclo C_24
es el grupo diédrico de orden 48.

### Demostración

Un automorfismo del ciclo queda determinado
por la imagen del nodo 0 y por la elección
de la imagen de uno de sus vecinos.

Existen 24 elecciones para la imagen de 0
y dos elecciones para la orientación.

Las imágenes de los restantes nodos
quedan determinadas sucesivamente por
la conservación de la contigüidad.

Por tanto, todos los automorfismos
tienen la forma:

f_(a,ε)(i) = a + εi mod 24

donde:

a ∈ ℤ_24

ε ∈ {−1,+1}

Existen exactamente:

24 · 2 = 48

transformaciones.

En consecuencia:

Aut(C_24) ≅ D_24

Aquí D_24 designa el grupo diédrico
de orden 48.

Queda demostrado.

## 7. Conservación de triángulos y cruces

### Lema 2

Todos los elementos de D_24 conservan
las capas E_T y E_X.

### Demostración

Sea:

f(i) = a + εi mod 24

Entonces:

f(j)−f(i) = ε(j−i) mod 24

Si:

j−i = ±8 mod 24

entonces:

f(j)−f(i) = ±8 mod 24

Por tanto, E_T permanece inalterada.

Análogamente, si:

j−i = ±6 mod 24

entonces:

f(j)−f(i) = ±6 mod 24

Por tanto, E_X permanece inalterada.

Las capas triangulares y de cruce
no reducen el grupo de automorfismos
de la contigüidad circular.

Queda demostrado.

## 8. Restricción Suma 23

### Lema 3

Un automorfismo f de la contigüidad
conserva E_S si y solo si:

f ∘ s = s ∘ f

### Demostración

Cada nodo i posee un único compañero
en la capa E_S:

s(i) = 23−i

La imagen del compañero de i debe
coincidir con el compañero de f(i).

Por tanto:

f(s(i)) = s(f(i))

Esta condición es necesaria y suficiente
para preservar el emparejamiento.

Sustituimos:

f(i) = a + εi

s(i) = −1−i mod 24

Obtenemos:

f(s(i)) = a−ε−εi

s(f(i)) = −1−a−εi

La igualdad exige:

2a ≡ ε−1 mod 24

Caso 1:

ε = +1

Entonces:

2a ≡ 0 mod 24

Las soluciones son:

a = 0,12

Caso 2:

ε = −1

Entonces:

2a ≡ −2 mod 24

Las soluciones son:

a = 11,23

Existen exactamente cuatro
transformaciones admisibles.

Queda demostrado.

## 9. Teorema fundamental del modelo parcial

### Teorema 1

El grupo de automorfismos de A_4
es isomorfo al grupo de Klein:

G_4 ≅ ℤ_2 × ℤ_2

### Demostración

Por los lemas anteriores, los únicos
automorfismos simultáneos de las cuatro
capas son:

e(i) = i

r(i) = i+12 mod 24

s(i) = 23−i

u(i) = 11−i mod 24

Se verifica:

r² = s² = u² = e

Además:

rs = sr = u

Por tanto, G_4 es un grupo abeliano
de orden cuatro cuyos tres elementos
no triviales tienen orden dos.

En consecuencia:

G_4 ≅ ℤ_2 × ℤ_2

Queda demostrado.

## 10. Generadores y tabla de composición

El grupo queda generado por:

G_4 = <r,s>

Su tabla de composición es:

| · | e | r | s | u |
|---|---|---|---|---|
| e | e | r | s | u |
| r | r | e | u | s |
| s | s | u | e | r |
| u | u | s | r | e |

El grupo no es isomorfo a ℤ_4.

Aunque ambos grupos tienen orden cuatro,
ℤ_4 contiene elementos de orden cuatro.

G_4 no contiene ninguno.

## 11. Incorporación de los estratos

Introducimos seis estratos diferenciados
mediante la función:

h(i) = 1 + (i mod 6)

Cada estrato contiene cuatro nodos.

La conservación de la identidad de los
estratos exige:

h(f(i)) = h(i)

para todo i ∈ V.

Definimos:

G_(4,h) = {f ∈ G_4 :
           h(f(i)) = h(i) para todo i}

Esta condición equivale a preservar
una coloración fija de los vértices.

## 12. Reducción del grupo por estratos

### Teorema 2

El grupo de automorfismos de las cuatro
capas con estratos fijos es:

G_(4,h) ≅ ℤ_2

### Demostración

Para la identidad:

h(e(i)) = h(i)

Para la rotación de 180 grados:

r(i) = i+12 mod 24

Como 12 es múltiplo de 6:

h(r(i)) = h(i)

Para la reflexión:

s(i) = 23−i

Se obtiene:

h(s(i)) = 7−h(i)

Análogamente:

h(u(i)) = 7−h(i)

Ningún estrato entero entre 1 y 6
satisface:

h = 7−h

Por tanto, las dos reflexiones
intercambian estratos diferentes.

No son admisibles cuando la identidad
de cada estrato permanece fija.

En consecuencia:

G_(4,h) = {e,r}

Como:

r² = e

y:

r ≠ e

obtenemos:

G_(4,h) ≅ ℤ_2

Queda demostrado.

## 13. Interpretación geométrica

La transformación:

r(i) = i+12 mod 24

representa un desplazamiento de dos
sectores cuando la numeración se organiza
en cuatro sectores de seis nodos.

Bajo esa convención corresponde a una
rotación espacial de 180 grados.

La rotación de 90 grados:

t(i) = i+6 mod 24

conserva las capas de contigüidad,
triángulos y cruces.

Sin embargo, no conserva E_S.

Por ejemplo:

{0,23} ∈ E_S

Su imagen mediante t es:

{6,5}

Como:

6+5 ≠ 23

la arista transformada no pertenece a E_S.

Por tanto, la incorporación de Suma 23
reduce la simetría rotacional.

Este resultado depende de la definición
combinatoria de E_S utilizada aquí.

## 14. Distinción entre grupos

Deben distinguirse:

A. Grupo de simetrías de la contigüidad:

D_24, de orden 48.

B. Grupo de las cuatro capas:

ℤ_2 × ℤ_2, de orden 4.

C. Grupo de rotaciones de cuatro sectores:

ℤ_4, de orden 4.

D. Grupo de las cuatro capas con
   identidad de estratos:

ℤ_2, de orden 2.

Estos grupos corresponden a estructuras
y restricciones diferentes.

No deben identificarse exclusivamente
por tener el mismo orden.

## 15. Órbitas bajo el grupo de Klein

La órbita de un nodo i es:

Orb_G4(i) =
{i,i+12,23−i,11−i}

con índices módulo 24.

Ninguno de los tres elementos no
triviales posee puntos fijos.

En efecto:

r(i) = i

exigiría:

12 ≡ 0 mod 24

lo cual es imposible.

Para s(i) = i:

2i ≡ 23 mod 24

No existen soluciones.

Para u(i) = i:

2i ≡ 11 mod 24

Tampoco existen soluciones.

Por tanto, la acción sobre los nodos
es libre.

Cada órbita contiene cuatro elementos.

El número de órbitas es:

24/4 = 6

## 16. Órbitas con estratos fijos

Bajo G_(4,h), las órbitas son:

Orb(i) = {i,i+12}

para:

i = 0,...,11

Existen exactamente doce órbitas:

| Órbita | Nodos |
|--------|-------|
| O_0 | 0,12 |
| O_1 | 1,13 |
| O_2 | 2,14 |
| O_3 | 3,15 |
| O_4 | 4,16 |
| O_5 | 5,17 |
| O_6 | 6,18 |
| O_7 | 7,19 |
| O_8 | 8,20 |
| O_9 | 9,21 |
| O_10 | 10,22 |
| O_11 | 11,23 |

Cada estrato contiene dos órbitas.

En particular, si el estrato 6 es
el estrato apical, sus nodos son:

V_apical = {5,11,17,23}

Sus dos órbitas son:

{5,17}

{11,23}

La equivalencia de los cuatro nodos
apicales no se deduce de este grupo.

Tampoco se deduce una diferencia
dinámica entre ambas órbitas.

## 17. Matriz de Gram relacional

Utilizamos el orden fijo de capas:

(C,T,X,S)

Definimos:

M_ij = tr(A_i A_j)

Como las capas son binarias y simétricas:

M_ij = 2|E_i ∩ E_j|

Los tamaños de las capas son:

|E_C| = 24

|E_T| = 24

|E_X| = 24

|E_S| = 12

Las capas C, T y X son disjuntas
dos a dos porque sus diferencias
modulares son distintas.

La capa S contiene únicamente
conexiones entre índices de paridad
opuesta.

Las capas T y X conectan índices
de la misma paridad.

Por tanto:

E_T ∩ E_S = ∅

E_X ∩ E_S = ∅

Para la intersección C y S exigimos:

23−i ≡ i ± 1 mod 24

Las únicas aristas resultantes son:

{0,23}

{11,12}

Por tanto:

|E_C ∩ E_S| = 2

La matriz de Gram exacta es:

    M = | 48 0 0 4 |
        | 0 48 0 0 |
        | 0 0 48 0 |
        | 4 0 0 24 |

## 18. Independencia lineal de las capas

### Teorema 3

Las cuatro matrices relacionales
A_C, A_T, A_X y A_S son linealmente
independientes.

### Demostración

El determinante de M es:

det(M) = 48²(48·24−4²)

Por tanto:

det(M) = 2304·1136

det(M) = 2 617 344

Como:

det(M) > 0

la matriz de Gram tiene rango cuatro.

El rango de una matriz de Gram
coincide con la dimensión del espacio
generado por sus elementos.

En consecuencia:

dim span{A_C,A_T,A_X,A_S} = 4

Queda demostrado.

Esta independencia lineal no implica
independencia estadística, causal
ni dinámica de las capas.

## 19. Invariantes espectrales individuales

### Contigüidad

La capa C es un ciclo de 24 nodos.

Sus autovalores son:

μ_k = 2 cos(2πk/24)

para k = 0,...,23.

### Triángulos

La capa T contiene ocho triángulos.

Su espectro es:

2, con multiplicidad 8.

−1, con multiplicidad 16.

### Cruces

La capa X contiene seis ciclos C_4.

Su espectro es:

2, con multiplicidad 6.

0, con multiplicidad 12.

−2, con multiplicidad 6.

### Suma 23

La capa S contiene doce aristas
disjuntas.

Su espectro es:

1, con multiplicidad 12.

−1, con multiplicidad 12.

Estos espectros corresponden a las
capas individuales aquí definidas.

No representan el espectro del
operador híbrido completo.

## 20. Recuento de configuraciones

Supongamos que cada nodo admite
q estados locales independientes.

Definimos:

Ω_q = {0,...,q−1}^24

Su cardinalidad es:

|Ω_q| = q^24

La acción del grupo se realiza mediante
permutaciones de los estados nodales.

No se imponen restricciones adicionales
de masa, energía o admisibilidad.

## 21. Recuento mediante Burnside

### Teorema 4

El número de órbitas de Ω_q bajo
G_(4,h) es:

|Ω_q/G_(4,h)| =
(q^24 + q^12)/2

### Demostración

Por el lema de Burnside:

|Ω_q/G| =
(1/|G|) Σ_(g∈G) |Fix(g)|

La identidad fija todas las
configuraciones:

|Fix(e)| = q^24

La rotación r intercambia doce
parejas de nodos.

Una configuración permanece fija
si ambos nodos de cada pareja
poseen el mismo estado.

Por tanto:

|Fix(r)| = q^12

Como |G_(4,h)| = 2:

|Ω_q/G_(4,h)| =
(q^24 + q^12)/2

Queda demostrado.

Para q = 2:

|Ω_2| = 16 777 216

|Fix(r)| = 4096

|Ω_2/G_(4,h)| = 8 390 656

## 22. Recuento bajo el grupo de Klein

Los tres elementos no triviales
de G_4 son involuciones sin puntos
fijos sobre los nodos.

Cada uno intercambia doce parejas.

Por tanto, aplicando Burnside:

|Ω_q/G_4| =
(q^24 + 3q^12)/4

Para estados binarios:

|Ω_2/G_4| = 4 197 376

Estos resultados corresponden al
espacio completo de estados nodales.

No constituyen recuentos de equilibrios,
atractores o estados físicamente
admisibles del sistema híbrido.

## 23. Representantes canónicos

Para un estado nodal:

x = (x_0,...,x_23)

definimos:

(r · x)_i = x_(i+12 mod 24)

El representante canónico bajo
G_(4,h) puede obtenerse mediante:

can(x) = min_lex{x,r · x}

Por tanto:

can(x) = can(y)

si y solo si:

x e y pertenecen a la misma órbita.

Este procedimiento requiere comparar
únicamente dos configuraciones.

Su coste es lineal en el número
de componentes del estado.

La extensión a estados híbridos
requiere definir la acción sobre
todas las variables adicionales.

## 24. Distancia cociente específica

Para estados nodales reales:

x,y ∈ ℝ^24

definimos:

d([x],[y]) =
min{||x−y||_2, ||x−r · y||_2}

Por los resultados establecidos en
RELATIONAL_QUOTIENT_METRIC.md,
esta expresión define una métrica
sobre el espacio de órbitas.

Su utilización experimental requiere
confirmar previamente que r pertenece
al grupo admisible de la arquitectura
y del espacio de estados considerado.

## 25. Extensión a la arquitectura completa

Sea:

A_PP = (A_C,A_T,A_X,A_S,B_1,...,B_p)

una extensión del modelo parcial
mediante capas adicionales.

Supongamos que:

1. Las cuatro capas iniciales
   permanecen diferenciadas.

2. La identidad de los estratos
   permanece fija.

3. Las capas adicionales imponen
   restricciones suplementarias.

Entonces:

G_PP ⊆ G_(4,h)

Por tanto:

G_PP ⊆ {e,r}

### Teorema 5

Bajo estas hipótesis, existen únicamente
dos posibilidades para el grupo completo:

G_PP = {e}

o:

G_PP = {e,r} ≅ ℤ_2

### Demostración

G_PP es un subgrupo de un grupo
de orden dos.

Por el teorema de Lagrange,
su orden divide a dos.

Por tanto:

|G_PP| ∈ {1,2}

Queda demostrado.

## 26. Criterio de resolución definitiva

Para determinar cuál de las dos
posibilidades anteriores corresponde
a la arquitectura completa, basta
comprobar la transformación r.

Para cada capa adicional B_k:

P_r B_k P_rᵀ = B_k

También deben verificarse:

- Etiquetas geométricas.
- Relaciones dirigidas.
- Orientaciones.
- Acoplamientos helicoidales.
- Relaciones de orden superior.
- Restricciones de contorno.
- Variables adicionales relevantes.

Si todas las restricciones se conservan:

G_PP ≅ ℤ_2

Si al menos una restricción no
se conserva:

G_PP = {e}

Este criterio resuelve el problema
algebraico de clasificación bajo
las hipótesis de la sección 25.

La decisión entre ambos grupos
requiere verificar la especificación
canónica completa.

Si dicha especificación no contiene
las cuatro capas diferenciadas
aquí definidas, la reducción anterior
deberá revisarse.

## 27. Compatibilidad dinámica

La conservación de la arquitectura
no garantiza la conservación de
las reglas dinámicas.

Sea F un operador sobre los estados.

La equivariancia respecto de r exige:

F(r · x) = r · F(x)

para todo estado admisible x.

Si esta propiedad se cumple, F induce
una dinámica bien definida sobre
el espacio cociente.

Si no se cumple, las configuraciones
geométricamente equivalentes pueden
presentar evoluciones diferentes.

Para operadores dependientes del
orden de actualización σ, debe
examinarse la condición:

F_(rσ)(r · x) = r · F_σ(x)

La equivariancia de la familia de
operadores no implica necesariamente
la equivariancia de un protocolo
con orden fijo.

Para dinámicas estocásticas debe
estudiarse la transformación de
las variables aleatorias o la
equivarianza del núcleo de transición.

## 28. Relación con los equilibrios

Supongamos que F es equivariante
respecto de r.

Si x* es un equilibrio:

F(x*) = x*

Entonces:

F(r · x*) = r · F(x*)

          = r · x*

Por tanto, r · x* también es
un equilibrio.

Los equilibrios pueden clasificarse
en órbitas de tamaño uno o dos.

Una órbita tiene tamaño uno si:

r · x* = x*

En caso contrario tiene tamaño dos.

Si existen M equilibrios y M_f
son invariantes bajo r, el número
de órbitas es:

N_orb = (M + M_f)/2

Esta expresión exige que el conjunto
de equilibrios sea finito e invariante
bajo la acción de r.

No se ha determinado M_f para los
190 equilibrios no apicales comunicados.

Tampoco se ha demostrado todavía
que su conjunto sea invariante
bajo el operador y grupo considerados.

## 29. Relación con las cuencas de atracción

Supongamos que F es equivariante
y que sus iteraciones convergen
desde determinados estados iniciales.

Si B(x*) representa la cuenca
de atracción del equilibrio x*,
entonces:

r · B(x*) = B(r · x*)

### Demostración

Sea:

x ∈ B(x*)

Por definición:

F^t(x) → x*

La equivariancia implica:

F^t(r · x) = r · F^t(x)

Como r es una transformación
lineal continua:

F^t(r · x) → r · x*

Por tanto:

r · x ∈ B(r · x*)

La inclusión recíproca se obtiene
aplicando r nuevamente, dado que:

r² = e

Queda demostrado.

Si la distribución inicial es
invariante bajo r, ambas cuencas
poseen la misma probabilidad.

Este resultado no implica que
todas las cuencas tengan igual tamaño.

Tampoco implica dominancia apical
ni convergencia global.

## 30. Relación con 44A y 44B

Los resultados anteriores permiten
plantear una clasificación de los
atractores por órbitas.

Antes de aplicarla será necesario:

1. Verificar la arquitectura canónica.

2. Identificar el espacio de estados.

3. Determinar el grupo admisible.

4. Comprobar la equivariancia de
   cada operador.

5. Verificar la compatibilidad de
   los órdenes de actualización.

6. Fijar el criterio de identidad
   de los estados finales.

7. Clasificar los atractores.

8. Comparar sus cuencas y frecuencias.

Los resultados de 44A y 44B deberán
mantenerse separados.

No se modifican las reglas congeladas
de la campaña del Episodio 44.

## 31. Protocolo de verificación

La implementación independiente
deberá comprobar:

T01. Existencia de 24 nodos.

T02. Simetría y diagonal nula
     de las cuatro matrices.

T03. Número exacto de aristas:

     C = 24
     T = 24
     X = 24
     S = 12

T04. Enumeración de las 48
     transformaciones diédricas.

T05. Conservación de las capas
     C, T y X por las 48
     transformaciones.

T06. Reducción a cuatro elementos
     al incorporar E_S.

T07. Reducción a dos elementos
     al incorporar los estratos.

T08. Clausura y composición.

T09. Órbitas de los nodos.

T10. Matriz de Gram exacta.

T11. Determinante y rango.

T12. Espectros individuales.

T13. Representantes canónicos.

T14. Conservación de todas las
     capas adicionales por r.

T15. Equivariancia dinámica.

T16. Clasificación de equilibrios
     y atractores.

Las pruebas T01–T13 corresponden
al modelo parcial definido.

Las pruebas T14–T16 requieren
información canónica adicional.

La ejecución reproducible deberá
registrarse en un módulo separado.

Este documento no sustituye a un
registro de ejecución computacional.

## 32. Clasificación epistemológica

### Resultados demostrados

- Grupo diédrico de la contigüidad.
- Conservación de triángulos y cruces.
- Reducción por Suma 23.
- Grupo de Klein de las cuatro capas.
- Reducción a ℤ_2 por estratos.
- Identificación de los generadores.
- Clasificación de órbitas nodales.
- Matriz de Gram del modelo parcial.
- Independencia lineal de las capas.
- Espectros individuales.
- Recuento mediante Burnside.
- Representantes canónicos.
- Criterio de extensión del grupo.

### Resultados condicionales demostrados

- Clasificación del grupo completo
  entre dos posibilidades, bajo
  las hipótesis de extensión.

- Existencia de una dinámica
  cociente bajo equivariancia.

- Correspondencia de equilibrios
  bajo equivariancia.

- Correspondencia de cuencas
  bajo equivariancia.

### Resultados pendientes

- Identificación del commit canónico.
- Verificación de todas las capas.
- Confirmación del grupo completo.
- Ejecución independiente registrada.
- Equivariancia de 44A y 44B.
- Clasificación de los 190 equilibrios
  no apicales comunicados.
- Clasificación de atractores.
- Determinación de las cuencas.
- Correspondencia con la TRCG.

## 33. Gobernanza

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

## 34. Conclusión

La arquitectura combinatoria de cuatro
capas estudiada posee un grupo de
automorfismos isomorfo al grupo de Klein.

La conservación adicional de los
seis estratos reduce dicho grupo
a una simetría de orden dos.

Por tanto:

G_4 ≅ ℤ_2 × ℤ_2

G_(4,h) ≅ ℤ_2

Bajo las hipótesis de extensión
establecidas:

G_PP ⊆ ℤ_2

El grupo completo será trivial
o isomorfo a ℤ_2.

La resolución definitiva depende
de la conservación de todas las
restricciones adicionales mediante
la rotación de 180 grados.

Este resultado reduce el problema
de clasificación de automorfismos
a una única transformación candidata,
si se cumplen las hipótesis indicadas.

La simetría geométrica no implica
automáticamente simetría dinámica.

La convergencia no se presupone.

La equivalencia se demuestra.

La conservación se verifica.

---

FIN DEL DOCUMENTO
