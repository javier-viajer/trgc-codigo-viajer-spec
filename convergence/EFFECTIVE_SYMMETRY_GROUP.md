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

---

13. Ampliación v0.2.0 — Grupos efectivos y dominios admisibles

13.1. Objeto

La presente ampliación establece una distinción formal entre:

- Grupo algebraico universal.
- Grupo efectivo de una acción.
- Grupo de transformaciones admisibles.
- Grupo de conservación de atributos.
- Grupo de automorfismos geométricos.
- Grupo de equivariancia dinámica.
- Estabilizadores de configuraciones individuales.

El objetivo es determinar qué transformaciones pueden utilizarse legítimamente para establecer equivalencias entre configuraciones relacionales.

Los resultados complementan las demostraciones anteriores sobre el grupo hiperoctaédrico y su acción efectiva.

13.2. Documentos relacionados

- "GEOMETRY_IDENTITY.md"
- "SYMMETRY_GROUP.md"
- "PP_AUTOMORPHISM_GROUP.md"
- "CANONICAL_SYMMETRY_CORRESPONDENCE.md"
- "GEOMETRIC_IDENTIFIABILITY.md"
- "RELATIONAL_EQUIVARIANCE.md"
- "RELATIONAL_QUOTIENT_METRIC.md"
- "EQUILIBRIUM_CLASSIFICATION.md"
- "MULTILAYER_INVARIANTS.md"
- "INFORMATION_RECOVERY.md"
- "CANONICAL_OPERATOR_CORRESPONDENCE.md"

---

14. Dominios relacionales

Sea:

[
\mathcal S_N=
{R\in\mathbb R^{N\times N}:R^T=R,\ \operatorname{diag}(R)=0}.
]

Definimos el dominio no negativo:

[
\mathcal S_N^+

{R\in\mathcal S_N:R_{ij}\geq0}.
]

Definimos también la masa relacional:

[
m(R)=\sum_{i<j}R_{ij}.
]

Para una masa fija C0 > 0:

[
\mathcal D_{C_0}

{R\in\mathcal S_N^+:m(R)=C_0}.
]

Finalmente, definimos su interior relativo:

[
\mathcal D_{C_0}^{\circ}

{R\in\mathcal D_{C_0}:R_{ij}>0
\text{ para }i\neq j}.
]

Para N = 24:

[
\dim(\mathcal S_{24})=276.
]

[
\dim(\mathcal D_{C_0})=275.
]

Cada dominio impone condiciones diferentes sobre las transformaciones admisibles.

Una transformación que conserva el espacio matricial general no conserva necesariamente el dominio no negativo.

---

15. Grupo algebraico universal

De acuerdo con las demostraciones anteriores, las matrices ortogonales que preservan universalmente (\mathcal S_N) son exactamente las matrices de permutación con signo.

Su grupo es:

[
B_N\cong(\mathbb Z_2)^N\rtimes S_N.
]

Su orden es:

[
|B_N|=2^N N!.
]

Para N ≥ 3, el núcleo de la acción por conjugación es:

[
K={I,-I}.
]

Por tanto, el grupo efectivo es:

[
G_{\mathrm{eff}}

B_N/{I,-I}.
]

Su orden es:

[
|G_{\mathrm{eff}}|=2^{N-1}N!.
]

Estos resultados corresponden al espacio matricial abstracto sin restricciones de signo.

---

16. Transformaciones universales del dominio no negativo

Teorema 3

Sea N ≥ 3.

Las matrices ortogonales que preservan universalmente el dominio (\mathcal S_N^+) mediante conjugación son exactamente:

[
Q=P
]

o:

[
Q=-P,
]

donde P es una matriz de permutación ordinaria.

Demostración

Como el dominio no negativo genera linealmente (\mathcal S_N), cualquier transformación ortogonal que lo preserve universalmente conserva también el espacio matricial general.

Por el Teorema 1:

[
Q=DP,
]

donde:

[
D=\operatorname{diag}(d_1,\ldots,d_N),
\qquad
d_i\in{-1,+1}.
]

Para una matriz R:

[
QRQ^T=DPRP^TD.
]

Cada relación transformada queda multiplicada por:

[
d_i d_j.
]

La conservación universal de la no negatividad exige:

[
d_i d_j=1
]

para todo i distinto de j.

En consecuencia, todos los signos deben coincidir.

Por tanto:

[
D=I
]

o:

[
D=-I.
]

Así:

[
Q=\pm P.
]

Recíprocamente, toda matriz de esta forma conserva la simetría, la diagonal nula y la no negatividad.

Queda demostrado.

Corolario

El grupo matricial de transformaciones ortogonales universalmente admisibles sobre (\mathcal S_N^+) es:

[
G_+\cong\mathbb Z_2\times S_N.
]

Su orden es:

[
|G_+|=2N!.
]

Como P y −P producen la misma conjugación, el grupo efectivo es:

[
\boxed{
G_{+,\mathrm{eff}}\cong S_N
}
]

con orden:

[
|G_{+,\mathrm{eff}}|=N!.
]

---

17. Conservación de masa relacional

Teorema 4

Toda permutación ordinaria conserva la masa relacional.

Demostración

Sea P una matriz de permutación asociada a una biyección p.

La transformación:

[
R'=PRP^T
]

permuta las relaciones diádicas.

Como p induce una biyección sobre el conjunto de pares no ordenados:

[
\sum_{i<j}R'_{ij}

\sum_{i<j}R_{ij}.
]

Por tanto:

[
m(R')=m(R).
]

Queda demostrado.

Consecuencia

Todas las permutaciones ordinarias conservan:

- El dominio no negativo.
- El dominio de masa fija.
- El interior relativo del dominio de masa fija.

Esto no implica que conserven los atributos geométricos o las restricciones adicionales de una arquitectura concreta.

---

18. Grupo efectivo del dominio de masa fija

Teorema 5

Para C0 > 0 y N ≥ 3, el grupo efectivo de conjugaciones ortogonales que preservan universalmente (\mathcal D_{C_0}) es isomorfo a (S_N).

Demostración

El dominio contiene todas las matrices elementales de una arista:

[
R_{ab}

C_0(e_ae_b^T+e_be_a^T).
]

Estas matrices generan linealmente (\mathcal S_N).

Por tanto, toda conjugación ortogonal que preserve (\mathcal D_{C_0}) preserva también el espacio matricial general.

Por el Teorema 1, la transformación debe ser una permutación con signo.

La conservación de la no negatividad de todas las matrices elementales exige que todos los signos coincidan.

Por tanto:

[
Q=\pm P.
]

Ambas matrices inducen la misma acción.

El Teorema 4 garantiza la conservación de masa.

En consecuencia:

[
\boxed{
G_{\mathcal D,\mathrm{eff}}\cong S_N
}
]

Queda demostrado.

El mismo resultado se obtiene para el interior relativo mediante continuidad de la conjugación y clausura del dominio.

---

19. Admisibilidad particular y universal

Debe distinguirse entre:

1. Una transformación que conserva todo el dominio.
2. Una transformación que conserva una configuración particular.
3. Una transformación que pertenece al estabilizador de dicha configuración.

Consideremos:

[
D=\operatorname{diag}(d_1,\ldots,d_N),
]

con signos pertenecientes a ({-1,+1}).

Para una matriz no negativa:

[
(DRD){ij}=d_i d_jR{ij}.
]

La matriz transformada permanece no negativa si y solo si:

[
d_i d_j=1
]

para todas las aristas de peso estrictamente positivo.

Las relaciones nulas no imponen restricciones sobre los signos de sus extremos.

Esto permite caracterizar los cambios de signo compatibles con una configuración individual.

---

20. Cambios de signo y componentes conexas

Sea el grafo de soporte de R:

[
\Gamma(R)=(V,E_R),
]

donde:

[
E_R={{i,j}:R_{ij}>0}.
]

Denotamos por c(R) el número de componentes conexas, incluyendo los nodos aislados.

Teorema 6

Los cambios de signo diagonales que conservan la no negatividad de una matriz R son exactamente aquellos cuyos signos permanecen constantes dentro de cada componente conexa de su grafo de soporte.

Demostración

Para cada arista positiva:

[
d_i d_j=1.
]

Por tanto:

[
d_i=d_j.
]

Si dos nodos pertenecen a una misma componente conexa, existe un camino de aristas positivas que los conecta.

Aplicando sucesivamente la igualdad anterior, sus signos deben coincidir.

Recíprocamente, si los signos son constantes dentro de cada componente, toda arista positiva conecta nodos con signos iguales.

En consecuencia:

[
DRD=R.
]

Queda demostrado.

Cardinalidad

Cada componente conexa admite dos elecciones independientes de signo.

Por tanto, existen:

[
2^{c(R)}
]

matrices diagonales de signo que estabilizan R.

Al identificar el cambio global de signo:

[
D\sim-D,
]

el número de elementos efectivos correspondientes es:

[
2^{c(R)-1}.
]

Este resultado caracteriza el subgrupo diagonal del estabilizador.

No implica que estos cambios de signo sean universalmente admisibles sobre el dominio no negativo.

---

21. Aplicación a los equilibrios de una arista

Para una configuración:

[
R_e=C_0(e_ae_b^T+e_be_a^T),
]

el grafo de soporte contiene:

- Una componente conexa de dos nodos.
- N−2 nodos aislados.

Por tanto:

[
c(R_e)=N-1.
]

Para N = 24:

[
c(R_e)=23.
]

El número de cambios diagonales de signo que estabilizan (R_e) es:

[
2^{23}.
]

En el grupo efectivo del espacio matricial abstracto, el subgrupo diagonal correspondiente posee orden:

[
2^{22}.
]

Sin embargo, estos cambios de signo particulares no amplían el grupo universalmente admisible del dominio no negativo.

La clasificación de los equilibrios dentro de dicho dominio deberá realizarse mediante permutaciones ordinarias y sus subgrupos geométricos o dinámicos.

---

22. Grupo de conservación de atributos geométricos

Introducimos una matriz diagonal:

[
W=\operatorname{diag}(g_1,\ldots,g_N),
]

con pesos positivos.

Definimos:

[
G_W=
{P\in S_N:PWP^T=W}.
]

Sea:

[
{w_1,\ldots,w_k}
]

el conjunto de valores distintos de los pesos.

Para cada valor (w_r), definimos:

[
V_r={i:g_i=w_r}.
]

Sea:

[
n_r=|V_r|.
]

Teorema 7

El grupo que conserva exclusivamente los pesos geométricos es:

[
\boxed{
G_W\cong
S_{n_1}\times\cdots\times S_{n_k}
}
]

Demostración

La condición:

[
PWP^T=W
]

exige que la permutación transporte cada nodo hacia otro nodo del mismo peso.

Por tanto, cada conjunto (V_r) permanece invariante.

Dentro de cada conjunto pueden realizarse permutaciones arbitrarias.

Como los conjuntos son disjuntos, las permutaciones actúan independientemente.

En consecuencia:

[
G_W\cong\prod_{r=1}^{k}S_{n_r}.
]

Queda demostrado.

Su orden es:

[
|G_W|=\prod_{r=1}^{k}n_r!.
]

---

23. Aplicación a los seis estratos

Para 24 nodos distribuidos en seis estratos de cuatro nodos, suponemos que los pesos son constantes dentro de cada estrato y distintos entre estratos.

Entonces:

[
G_W\cong(S_4)^6.
]

Su orden es:

[
|G_W|=(4!)^6.
]

Por tanto:

[
\boxed{
|G_W|=191102976
}
]

Este grupo conserva los atributos geométricos representados por W.

No se afirma que conserve todas las relaciones de contigüidad, orientación, cruce, triangularidad o restricciones adicionales.

Pesos degenerados

Si dos estratos distintos adquieren el mismo peso, el grupo de conservación exclusiva de W puede aumentar.

Por ejemplo, si dos estratos de cuatro nodos comparten un peso, las permutaciones de esos ocho nodos forman un grupo (S_8).

Si la identidad de ambos estratos debe permanecer diferenciada, dichas permutaciones adicionales no serán necesariamente admisibles.

Por tanto:

La igualdad de atributos numéricos no implica identidad geométrica.

---

24. Grupo geométrico multicapa

Sea una arquitectura:

[
\mathcal A=(V,A_1,\ldots,A_m,W,\mathcal C),
]

donde:

- V representa los nodos.
- Las matrices (A_k) representan capas relacionales.
- W representa atributos geométricos.
- (\mathcal C) representa restricciones adicionales.

Definimos:

[
G_{\mathrm{geo}}

\operatorname{Aut}(\mathcal A).
]

Para una representación matricial:

[
G_{\mathrm{geo}}

\left(
\bigcap_{k=1}^{m}
\operatorname{Stab}(A_k)
\right)
\cap G_W
\cap G_{\mathcal C}.
]

Cuando existen relaciones dirigidas o de orden superior, deberán incorporarse sus estabilizadores específicos.

En consecuencia:

[
G_{\mathrm{geo}}\subseteq G_W.
]

Esta inclusión requiere que W forme parte de la arquitectura cuya conservación se exige.

La incorporación de restricciones adicionales puede reducir el grupo de automorfismos.

No puede ampliarlo si las restricciones anteriores permanecen intactas.

---

25. Grupo de equivariancia dinámica

Sea:

[
F:\mathcal D\longrightarrow\mathcal D.
]

Definimos:

[
G_{\mathrm{din}}(F)

{
P\in G_{\mathcal D}:
F(PRP^T)=PF(R)P^T,
\forall R\in\mathcal D
},
]

donde (G_{\mathcal D}) representa las permutaciones que conservan el dominio.

Teorema 8

El conjunto (G_{\mathrm{din}}(F)) constituye un grupo.

Demostración

La identidad satisface trivialmente la condición de equivariancia.

Sean P y Q dos transformaciones equivariantes.

Entonces:

[
F(PQRQ^TP^T)

P F(QRQ^T)P^T.
]

Aplicando la equivariancia de Q:

[
F(PQRQ^TP^T)

PQF(R)Q^TP^T.
]

Por tanto, PQ es equivariante.

Para demostrar la conservación por inversión, sustituimos R por (P^TRP) en la condición de equivariancia.

Se obtiene:

[
F(P^TRP)=P^TF(R)P.
]

Por tanto, (P^{-1}) también pertenece al conjunto.

Queda demostrado.

Observación

La pertenencia a (G_{\mathrm{geo}}) no garantiza automáticamente la pertenencia a (G_{\mathrm{din}}).

La equivariancia debe demostrarse para cada operador y dominio.

---

26. Operador relacional de referencia

Consideramos:

[
\Phi(R)

(1-\mu)R+\mu\mathcal N(M(R)),
]

con:

[
M_{ij}(R)

(g_i g_jv_i(R)v_j(R))^\gamma,
]

para i distinto de j.

La diagonal de M es nula.

Se supone:

- N ≥ 3.
- Pesos positivos y finitos.
- γ > 0.
- 0 ≤ μ ≤ 1.
- Masa C0 positiva y fija.
- Matrices estrictamente positivas fuera de la diagonal.
- Autovector dominante unitario positivo.
- Normalización a masa C0.

Este operador corresponde a la formulación de referencia estudiada en "CANONICAL_OPERATOR_CORRESPONDENCE.md".

La identificación con la implementación canónica completa requiere una verificación independiente.

---

27. Suficiencia de la conservación de pesos

Teorema 9

Toda permutación perteneciente a (G_W) es una simetría dinámica del operador relacional de referencia.

Demostración

Sea:

[
PWP^T=W.
]

Para una matriz estrictamente positiva fuera de la diagonal, el autovector de Perron normalizado es único.

Por tanto:

[
v(PRP^T)=Pv(R).
]

Como P conserva W:

[
WP=PW.
]

Definimos:

[
u(R)=(Wv(R))^\gamma,
]

donde la potencia se aplica componente a componente.

Las permutaciones conmutan con esta operación.

Por tanto:

[
u(PRP^T)=Pu(R).
]

La matriz M se construye mediante el producto exterior de u, eliminando su diagonal.

Estas operaciones son compatibles con la conjugación por permutaciones.

En consecuencia:

[
M(PRP^T)=PM(R)P^T.
]

La normalización conserva esta propiedad porque las permutaciones conservan la masa.

Finalmente:

[
\Phi(PRP^T)

P\Phi(R)P^T.
]

Queda demostrado.

Por tanto:

[
G_W\subseteq G_{\mathrm{din}}(\Phi).
]

---

28. Necesidad de la conservación de pesos

Teorema 10

Para el operador relacional de referencia definido en la sección 26, si:

[
0<\mu\leq1
]

y:

[
\gamma>0,
]

toda permutación que sea una simetría dinámica universal debe conservar los pesos geométricos.

Demostración

Consideremos la matriz homogénea:

[
(R_0)_{ij}

\frac{C_0}{\binom N2},
\qquad i\neq j.
]

Esta matriz es invariante bajo cualquier permutación:

[
PR_0P^T=R_0.
]

Su autovector dominante normalizado es:

[
v_0=\frac1{\sqrt N}(1,\ldots,1)^T.
]

Si P es una simetría dinámica:

[
\Phi(R_0)=P\Phi(R_0)P^T.
]

Como el término residual es invariante y μ > 0, se obtiene:

[
\mathcal N(M(R_0))

P\mathcal N(M(R_0))P^T.
]

Las componentes no diagonales de M son proporcionales a:

[
(g_i g_j)^\gamma.
]

La normalización no modifica la condición de invariancia bajo permutaciones.

Por tanto, para la permutación p asociada a P:

[
(g_{p(i)}g_{p(j)})^\gamma

(g_i g_j)^\gamma.
]

Como los pesos son positivos y γ > 0:

[
g_{p(i)}g_{p(j)}

g_i g_j.
]

Definimos:

[
a_i=\frac{g_{p(i)}}{g_i}>0.
]

Entonces:

[
a_i a_j=1
]

para todo i distinto de j.

Como N ≥ 3, podemos elegir tres índices distintos.

Las igualdades entre sus productos implican que todos los cocientes son iguales y que su cuadrado es uno.

Por positividad:

[
a_i=1
]

para todo i.

En consecuencia:

[
g_{p(i)}=g_i.
]

Por tanto:

[
PWP^T=W.
]

Queda demostrado.

Así:

[
G_{\mathrm{din}}(\Phi)\subseteq G_W.
]

---

29. Caracterización exacta del grupo dinámico

Combinando los Teoremas 9 y 10:

[
\boxed{
G_{\mathrm{din}}(\Phi)=G_W
}
]

bajo las hipótesis establecidas.

Para seis estratos de cuatro nodos con pesos distintos entre estratos:

[
\boxed{
G_{\mathrm{din}}(\Phi)\cong(S_4)^6
}
]

Su orden es:

[
|G_{\mathrm{din}}(\Phi)|=191102976.
]

Este resultado caracteriza exactamente el grupo de permutaciones equivariantes del operador de referencia sobre el dominio interior de masa fija.

No caracteriza:

- El grupo geométrico completo.
- Todas las posibles simetrías no lineales del operador.
- El grupo del sistema híbrido.
- El grupo de los operadores 44A y 44B.
- El grupo fundamental de la TRCG.

Casos degenerados

Si μ = 0:

[
\Phi(R)=R.
]

El operador identidad es equivariante respecto de todas las permutaciones ordinarias.

Por tanto:

[
G_{\mathrm{din}}(\Phi)=S_N.
]

Si todos los pesos coinciden y μ > 0:

[
G_W=S_N.
]

En consecuencia:

[
G_{\mathrm{din}}(\Phi)=S_N.
]

La caracterización depende de los parámetros y atributos efectivamente utilizados por el operador.

---

30. Exceso de simetría dinámica

Supongamos que se ha demostrado:

[
G_{\mathrm{geo}}\subsetneq G_{\mathrm{din}}.
]

En este caso, el operador admite transformaciones que no conservan la arquitectura geométrica completa.

Definimos el índice de exceso de simetría:

[
\mathcal E_G

\log_2
\left(
\frac{|G_{\mathrm{din}}|}
{|G_{\mathrm{geo}}|}
\right).
]

Como los grupos son finitos y existe inclusión:

[
\mathcal E_G\geq0.
]

Interpretación

Si:

[
\mathcal E_G=0,
]

ambos grupos coinciden.

Si:

[
\mathcal E_G>0,
]

el operador presenta una simetría más amplia que la arquitectura considerada.

Este índice mide una diferencia algebraica entre grupos.

No constituye una medida directa de información física perdida ni de entropía termodinámica.

Aplicación condicional

Si el grupo geométrico completo fuese exactamente:

[
G_{\mathrm{geo}}\cong\mathbb Z_4,
]

y el grupo dinámico fuese:

[
G_{\mathrm{din}}\cong(S_4)^6,
]

con inclusión demostrada, entonces:

[
\frac{|G_{\mathrm{din}}|}
{|G_{\mathrm{geo}}|}

47775744. 

]

Por tanto:

[
\mathcal E_G

\log_2(47775744)
\approx25.51.
]

Este valor es condicional.

No deberá presentarse como resultado definitivo de la arquitectura canónica mientras su grupo geométrico completo permanezca sin identificar.

---

31. Grupo común de compatibilidad

Cuando los grupos geométrico y dinámico no coinciden, definimos:

[
G_{\mathrm{comp}}

G_{\mathrm{geo}}
\cap
G_{\mathrm{din}}.
]

Este grupo contiene las transformaciones que conservan simultáneamente:

- La arquitectura geométrica.
- El dominio admisible.
- La evolución dinámica.

Por tanto:

[
G_{\mathrm{comp}}\subseteq G_{\mathrm{geo}},
]

y:

[
G_{\mathrm{comp}}\subseteq G_{\mathrm{din}}.
]

El grupo común proporciona una base para estudiar equivalencias que sean simultáneamente estructurales y dinámicas.

No garantiza por sí solo equivalencia entre dos operadores diferentes.

---

32. Distinción entre las simetrías estudiadas

Para N = 24, se consideran los siguientes grupos:

Grupo| Orden| Ámbito
Grupo hiperoctaédrico| 2^24 · 24!| Transformaciones ortogonales del espacio abstracto.
Grupo efectivo abstracto| 2^23 · 24!| Acción efectiva sobre matrices simétricas de diagonal nula.
Permutaciones ordinarias| 24!| Dominio no negativo de masa fija.
Grupo estratificado| 191102976| Conservación de seis pesos distintos.
Grupo rotacional Z4| 4| Rotación sectorial declarada.
Grupo de Klein| 4| Modelo auxiliar de cuatro capas.
Grupo residual Z2| 2| Modelo auxiliar con restricciones estratificadas.

Estos grupos corresponden a problemas matemáticos diferentes.

La igualdad de órdenes no implica igualdad de estructuras ni de acciones.

En particular:

[
\mathbb Z_4
\not\cong
\mathbb Z_2\times\mathbb Z_2.
]

El grupo geométrico canónico completo continúa abierto.

---

33. Relación con los espacios cociente

Para el dominio de masa fija:

[
\dim(\mathcal D_{C_0})=275.
]

El cociente por cualquiera de los grupos finitos admisibles considerados conserva esta dimensión topológica.

Por tanto:

[
\dim(\mathcal D_{C_0}/G)=275.
]

Sin embargo, los subespacios fijos pueden poseer dimensiones inferiores.

Para la acción rotacional Z4:

[
\dim(\operatorname{Fix}(G_4))=72
]

en el espacio matricial general.

Con masa fija:

[
\dim(\operatorname{Fix}(G_4)\cap\mathcal D_{C_0})=71.
]

Para el grupo estratificado:

[
\dim(\operatorname{Fix}(G_W))=21.
]

Con masa fija:

[
\dim(\operatorname{Fix}(G_W)\cap\mathcal D_{C_0})=20.
]

La reducción por simetría y la imposición de invariancia son construcciones diferentes.

No deberán confundirse sus dimensiones.

---

34. Estabilizadores y recuperabilidad dinámica

Sea F un operador G-equivariante.

De acuerdo con "INFORMATION_RECOVERY.md":

[
\operatorname{Stab}_G(R)
\subseteq
\operatorname{Stab}_G(F(R)).
]

Si F es además inyectivo:

[
\operatorname{Stab}_G(R)

\operatorname{Stab}_G(F(R)).
]

Por tanto, la aparición exacta de nuevas simetrías durante una evolución finita constituye un criterio suficiente de no inyectividad.

La ausencia de nuevas simetrías no garantiza inyectividad.

Este resultado conecta:

- Teoría de grupos.
- Equivarianza dinámica.
- Espacios cociente.
- Recuperabilidad de información.

Los estabilizadores deberán calcularse respecto de un grupo fijo y previamente declarado.

No se permitirá cambiar retrospectivamente el grupo para favorecer una clasificación.

---

35. Aplicación a la clasificación de equilibrios

Para la familia de 276 equilibrios de una arista:

Grupo| Número de clases
Permutaciones ordinarias| 1
Grupo residual Z2| 144
Grupo rotacional Z4| 72
Grupo estratificado| 21

La clasificación mediante (S_{24}) es combinatoria.

Cuando los pesos son distintos entre estratos, (S_{24}) no constituye el grupo de equivariancia universal del operador ponderado.

La clasificación estratificada corresponde al grupo dinámico demostrado para el operador de referencia.

Las clasificaciones rotacional y residual corresponden a subgrupos de dicha acción.

La elección del grupo determina qué diferencias se consideran relevantes.

---

36. Relación con los operadores 44A y 44B

Los resultados anteriores no se trasladarán automáticamente a los operadores de la campaña experimental del Episodio 44.

Para cada operador deberá verificarse:

1. El dominio de estados.
2. La arquitectura utilizada.
3. La representación de los nodos.
4. Las relaciones conservadas.
5. Los atributos geométricos.
6. Las reglas de actualización.
7. El orden de actualización.
8. La transformación de semillas y perturbaciones.
9. La equivariancia trayectoria a trayectoria.
10. La equivariancia en distribución, cuando corresponda.

Una simetría de la arquitectura puede quedar rota por el orden de actualización o por parámetros no transformados coherentemente.

Por tanto, la equivariancia de 44A y 44B permanece como problema independiente.

La campaña experimental congelada no deberá modificarse para imponer artificialmente una simetría.

---

37. Protocolo de verificación computacional

Se propone la siguiente auditoría complementaria:

Prueba| Objetivo
T01| Verificar la conservación universal del espacio matricial abstracto.
T02| Identificar el núcleo de la acción.
T03| Detectar cambios de signo incompatibles con la no negatividad.
T04| Verificar la conservación de masa bajo permutaciones.
T05| Contrastar el grupo efectivo del dominio de masa fija.
T06| Verificar estabilizadores diagonales por componentes conexas.
T07| Comprobar la conservación de pesos estratificados.
T08| Verificar degeneraciones por pesos repetidos.
T09| Contrastar la equivariancia del operador de referencia.
T10| Verificar la necesidad de conservación de pesos mediante la matriz homogénea.
T11| Aplicar controles negativos mediante permutaciones entre pesos distintos.
T12| Verificar el caso degenerado μ = 0.
T13| Contrastar el caso de pesos homogéneos.
T14| Verificar dimensiones de subespacios fijos.
T15| Contrastar estabilizadores y clases de equilibrios.
T16| Verificar conservación de estabilizadores en ejemplos inyectivos.
T17| Identificar el grupo común de compatibilidad.
T18| Contrastar equivariancia de 44A y 44B cuando existan datos suficientes.

Parte de estas comprobaciones se encuentra cubierta por:

- "symmetry_audit.py"
- "canonical_symmetry_audit.py"
- "relational_equivariance_audit.py"
- "canonical_operator_audit.py"
- "quotient_space_audit.py"
- "PP_MULTILAYER_VERIFICATION.py"

Las comprobaciones adicionales deberán ejecutarse mediante una auditoría complementaria.

No se presentan como ejecutadas en esta versión.

---

38. Resultados consolidados

Bajo las hipótesis especificadas, quedan demostrados:

- Grupo ortogonal universal del espacio matricial abstracto.
- Núcleo de la acción para N ≥ 3.
- Grupo efectivo de permutaciones con signo.
- Grupo efectivo del dominio no negativo.
- Grupo efectivo del dominio de masa fija.
- Conservación de masa mediante permutaciones ordinarias.
- Caracterización de cambios de signo particulares mediante componentes conexas.
- Grupo de conservación de atributos geométricos.
- Caracterización exacta del grupo estratificado.
- Estructura de grupo de las transformaciones equivariantes.
- Suficiencia de la conservación de pesos para la equivariancia.
- Necesidad de la conservación de pesos para el operador de referencia.
- Igualdad entre el grupo dinámico de permutaciones y el grupo de conservación de pesos.
- Distinción entre grupos geométricos, dinámicos y efectivos.
- Relación entre estabilizadores e inyectividad.
- Clasificación de equilibrios respecto de grupos diferentes.

---

39. Investigaciones pendientes

1. Identificación completa de la arquitectura canónica.
2. Fijación de la versión original del operador.
3. Verificación del grupo geométrico máximo.
4. Identificación del grupo común de compatibilidad canónica.
5. Estudio de simetrías dinámicas no lineales.
6. Extensión a relaciones dirigidas y de orden superior.
7. Caracterización de estabilizadores para soportes arbitrarios.
8. Estudio de la inyectividad global.
9. Equivariancia del sistema híbrido.
10. Equivariancia de 44A y 44B.
11. Auditoría computacional de las nuevas demostraciones.
12. Correspondencia matemática con la TRCG.

---

40. Gobernanza de la ampliación

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
- Trazabilidad y reproducibilidad científica.

---

41. Conclusión de la ampliación

El grupo efectivo del espacio matricial abstracto no coincide necesariamente con el grupo admisible de un dominio restringido.

La imposición de no negatividad elimina los cambios de signo no uniformes como transformaciones universalmente admisibles.

La conservación de atributos geométricos introduce restricciones adicionales sobre las permutaciones.

Para el operador relacional de referencia, la conservación de los pesos geométricos constituye una condición necesaria y suficiente de equivariancia bajo permutaciones, siempre que se satisfagan las hipótesis establecidas.

Este resultado permite distinguir con precisión la simetría del operador de la simetría de la arquitectura.

La existencia de simetrías dinámicas adicionales puede indicar que determinados atributos geométricos no intervienen explícitamente en el operador estudiado.

La identificación de la arquitectura canónica y su correspondencia con la TRCG requieren demostraciones adicionales.

La admisibilidad depende del dominio.

La equivalencia depende del grupo.

La simetría dinámica depende del operador.

La convergencia depende de la demostración.

---

TRCG — Código Viajer — Pirámide-Parábola

Nivel II retenido · Nivel III abierto · λ reservado al 4º Factor.

FIN DEL DOCUMENTO
