# EFFECTIVE SYMMETRY GROUP

## Grupo efectivo de simetrías del espacio relacional R

**Proyecto:** Convergencia TRCG — Código Viajer  
**Versión:** 0.1.0  
**Estado:** Desarrollo matemático abierto  
**Referencia:** TRCG, Episodio 45  
**Gobernanza:** Nivel II retenido · Nivel III abierto  

---

## 1. Objeto

Caracterizar el grupo efectivo de transformaciones
ortogonales que preservan universalmente el espacio
de configuraciones relacionales simétricas de
diagonal nula.

Este documento no presupone que dicho grupo sea
el grupo fundamental de simetrías de la TRCG
ni el grupo específico de Pirámide-Parábola.

## 2. Espacio relacional

Sea N ≥ 3.

Definimos:

S_N = {R ∈ ℝ^(N×N) : Rᵀ = R, diag(R) = 0}

Su dimensión es:

dim(S_N) = N(N−1)/2

Para N = 24:

dim(S_24) = 276

Estas 276 componentes representan el espacio
diádico general, no necesariamente las aristas
activas de una arquitectura concreta.

## 3. Transformaciones ortogonales admisibles

Consideramos la acción:

Φ_Q(R) = QRQᵀ

con:

QᵀQ = I

Exigimos:

Φ_Q(S_N) = S_N

### Teorema 1

Las matrices ortogonales que preservan
universalmente S_N son exactamente las matrices
de permutación con signo.

### Demostración

Sea q_ij la entrada de Q situada en la fila i
y columna j.

La componente diagonal de QRQᵀ satisface:

(QRQᵀ)_ii = 2 Σ_(j<k) q_ij q_ik r_jk

Como las componentes r_jk son independientes,
la conservación universal de la diagonal nula
exige:

q_ij q_ik = 0

para todo j ≠ k.

Por tanto, cada fila de Q contiene como máximo
una componente no nula.

La ortogonalidad exige que cada fila y cada
columna tengan norma unitaria.

En consecuencia, cada fila y cada columna
contienen exactamente una componente no nula,
de valor +1 o −1.

Así:

Q = DP

donde P es una matriz de permutación y D es
diagonal con entradas pertenecientes a {−1,+1}.

Recíprocamente, toda matriz de esta forma
preserva la simetría y la diagonal nula.

Queda demostrado.

## 4. Grupo hiperoctaédrico

El grupo de permutaciones con signo es:

B_N ≅ (ℤ₂)^N ⋊ S_N

Su orden es:

|B_N| = 2^N N!

Sin embargo, la acción de B_N sobre S_N
no es fiel.

## 5. Núcleo de la acción

Definimos:

K = {Q ∈ B_N : QRQᵀ = R para todo R ∈ S_N}

### Teorema 2

Para N ≥ 3:

K = {I, −I}

### Demostración

Es inmediato que:

IRIᵀ = R

(−I)R(−I)ᵀ = R

Por tanto:

{I,−I} ⊆ K

Consideremos ahora Q = DP perteneciente a K.

Sea E_ij la matriz elemental y definamos:

B_ij = E_ij + E_ji

para i < j.

Estas matrices forman una base de S_N.

La conjugación por Q transforma cada B_ij
en una matriz elemental simétrica asociada
al par de índices permutados, posiblemente
multiplicada por −1.

Para que todas las matrices B_ij permanezcan
inalteradas, la permutación debe fijar cada
par no ordenado {i,j}.

Cuando N ≥ 3, esto implica que P = I.

Por tanto, Q = D.

Escribimos:

D = diag(d_1,...,d_N)

con d_i ∈ {−1,+1}.

La conservación de B_ij exige:

d_i d_j = 1

para todo i ≠ j.

En consecuencia, todos los signos d_i
deben coincidir.

Por tanto:

D = I o D = −I

Queda demostrado que:

K = {I,−I}

## 6. Grupo efectivo

Definimos:

G_eff = B_N / {I,−I}

Su acción sobre S_N es fiel.

El orden del grupo efectivo es:

|G_eff| = 2^(N−1) N!

Para N = 24:

|G_eff| = 2^23 · 24!

Este resultado caracteriza el grupo efectivo
de las semejanzas ortogonales que preservan
universalmente S_24.

No caracteriza automáticamente las simetrías
de una arquitectura geométrica particular.

## 7. Estabilizadores y órbitas

Para R ∈ S_N:

Stab_B(R) = {Q ∈ B_N : QRQᵀ = R}

Como el núcleo pertenece a todo estabilizador:

{I,−I} ⊆ Stab_B(R)

Por tanto, ningún estabilizador de B_N
puede ser trivial.

En el grupo efectivo:

Stab_eff(R) = Stab_B(R) / K

El teorema órbita-estabilizador proporciona:

|Orb(R)| = |B_N| / |Stab_B(R)|

Equivalentemente:

|Orb(R)| = |G_eff| / |Stab_eff(R)|

Ambas expresiones producen la misma órbita.

## 8. Restricciones geométricas adicionales

La admisibilidad matricial no implica
admisibilidad física o geométrica.

Si las relaciones están restringidas a valores
no negativos, las permutaciones con signo
pueden producir configuraciones inadmisibles.

Si existen etiquetas físicas, estratos,
orientaciones o familias relacionales,
deben conservarse explícitamente.

Por tanto, el grupo efectivo matricial
constituye un marco algebraico general.

El grupo geométrico específico debe
determinarse mediante restricciones adicionales.

## 9. Aplicación multicapa

Sea una arquitectura:

A = (A_1,...,A_m)

Definimos su grupo de automorfismos bajo
permutaciones ordinarias:

Aut(A) = {P ∈ S_N :
          PA_kPᵀ = A_k para todo k}

Equivalentemente:

Aut(A) = ⋂_(k=1)^m Stab(A_k)

Esta definición permite investigar el grupo
de simetrías propio de Pirámide-Parábola.

Su orden y sus generadores permanecen abiertos
hasta verificar la arquitectura completa.

## 10. Clasificación epistemológica

RESULTADOS DEMOSTRADOS EN EL MODELO DEFINIDO:

- Clasificación de las semejanzas ortogonales
  universalmente admisibles.
- Identificación del núcleo para N ≥ 3.
- Construcción del grupo efectivo.
- Correspondencia entre las órbitas del grupo
  original y las del grupo efectivo.

RESULTADOS PENDIENTES:

- Grupo específico de Pirámide-Parábola.
- Admisibilidad física de los cambios de signo.
- Equivariancia de los operadores 44A y 44B.
- Correspondencia estructural con la TRCG.

## 11. Gobernanza

- Nivel II retenido.
- Nivel III abierto.
- Pirámide-Parábola como candidata experimental.
- λ reservado al 4º Factor.
- Sin ascensos automáticos.
- Sin ajustes retrospectivos.
- Sin modificación de los protocolos congelados.

## 12. Conclusión

La identidad relacional debe estudiarse
respecto de una acción algebraica explícita.

Distinguir el grupo abstracto de su acción
efectiva evita contabilizar como diferentes
transformaciones que producen exactamente
el mismo efecto relacional.

La convergencia entre TRCG y Código Viajer
permanece como cuestión matemática abierta.
