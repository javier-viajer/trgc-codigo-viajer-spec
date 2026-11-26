# MULTILAYER INVARIANTS

## Invariantes de arquitecturas relacionales multicapa

**Proyecto:** Convergencia TRCG — Código Viajer  
**Versión:** 0.1.0  
**Estado:** Desarrollo matemático abierto  
**Referencia:** TRCG, Episodio 45, sección 9  
**Gobernanza:** Nivel II retenido · Nivel III abierto  

---

## 1. Objeto

Desarrollar magnitudes invariantes capaces
de caracterizar parcialmente la organización
conjunta de una arquitectura relacional
multicapa.

El objetivo es distinguir:

- Propiedades individuales de cada capa.
- Relaciones entre diferentes capas.
- Identidad geométrica conjunta.
- Conservación bajo transformaciones.
- Conservación bajo evolución dinámica.

Estas propiedades no deben confundirse.

## 2. Definición de arquitectura multicapa

Consideramos:

A = (A_1,A_2,...,A_m)

donde:

A_k ∈ S_N

y:

S_N = {R ∈ ℝ^(N×N) :
       Rᵀ = R, diag(R) = 0}

Todas las capas comparten el mismo conjunto
ordenado de N elementos.

La correspondencia entre las capas se fija
antes de realizar las comparaciones.

Para Pirámide-Parábola, N = 24.

Las familias candidatas incluyen:

- Contigüidad.
- Suma 23.
- Relaciones triangulares.
- Relaciones de cruce.
- Acoplamientos adicionales definidos
  en la especificación canónica.

La enumeración anterior no sustituye
a la definición completa de la arquitectura.

Las relaciones dirigidas o de orden superior
requieren una representación adicional cuando
no puedan expresarse fielmente mediante
matrices simétricas.

## 3. Acción simultánea

Sea Q una matriz ortogonal.

Definimos:

A'_k = QA_kQᵀ

para todo k.

La misma transformación debe aplicarse
simultáneamente a todas las capas.

Si se exige que la arquitectura transformada
permanezca en S_N, Q deberá ser admisible
respecto de dicho espacio.

## 4. Matriz de Gram relacional

Definimos:

C_ij = tr(A_i A_j)

La matriz conjunta es:

C(A) = (C_ij) ∈ ℝ^(m×m)

### Teorema 1

C(A) es invariante bajo la conjugación
ortogonal simultánea de todas las capas.

### Demostración

C'_ij = tr(A'_i A'_j)

Sustituyendo:

C'_ij = tr(QA_iQᵀQA_jQᵀ)

Como:

QᵀQ = I

obtenemos:

C'_ij = tr(QA_iA_jQᵀ)

Por la propiedad cíclica de la traza:

C'_ij = tr(A_iA_jQᵀQ)

Por tanto:

C'_ij = tr(A_iA_j) = C_ij

Queda demostrado.

## 5. Propiedades de la matriz de Gram

### 5.1 Simetría

C_ij = C_ji

### 5.2 Semidefinición positiva

Sea v ∈ ℝ^m.

Entonces:

vᵀCv = ||Σ_i v_i A_i||_F² ≥ 0

Por tanto:

C ⪰ 0

Esta propiedad corresponde a la matriz de Gram.

No implica que las matrices relacionales
individuales A_k sean semidefinidas positivas.

### 5.3 Componentes diagonales

C_ii = tr(A_i²)

Como A_i es simétrica:

C_ii = ||A_i||_F²

### 5.4 Rango

El rango de C coincide con la dimensión
del espacio lineal generado por las capas.

Por tanto:

rank(C) ≤ min(m,N(N−1)/2)

La matriz de Gram permite detectar
dependencias lineales entre familias
relacionales.

## 6. Interpretación para capas binarias

Supongamos que:

(A_k)_ij ∈ {0,1}

Cada capa representa un grafo simple
no dirigido con conjunto de aristas E_k.

Entonces:

C_ii = 2|E_i|

Y:

C_ij = 2|E_i ∩ E_j|

Por tanto:

- La diagonal mide el número de aristas
  de cada familia, multiplicado por dos.
- Las componentes no diagonales miden
  el solapamiento entre familias.
- Un valor cero indica ausencia de aristas
  compartidas entre esas dos capas.

Este resultado es aplicable únicamente
a capas binarias simétricas de diagonal nula.

## 7. Solapamiento normalizado

Para capas de norma no nula definimos:

ρ_ij = C_ij / √(C_ii C_jj)

Por Cauchy-Schwarz:

−1 ≤ ρ_ij ≤ 1

Para capas binarias no negativas:

0 ≤ ρ_ij ≤ 1

Interpretación:

ρ_ij = 0:

Ausencia de solapamiento en el caso binario.

ρ_ij = 1:

Coincidencia de las capas binarias no nulas.

En el caso ponderado general, el valor 1
indica proporcionalidad positiva.

La normalización se define previamente.

No se permite utilizarla para ajustar
retrospectivamente resultados experimentales.

## 8. Invariantes mixtos de orden superior

Definimos:

I_(i_1,...,i_p) =
tr(A_(i_1) A_(i_2) ... A_(i_p))

### Teorema 2

Todos los invariantes mixtos anteriores
se conservan bajo conjugación ortogonal
simultánea.

### Demostración

Al sustituir:

A'_k = QA_kQᵀ

en el producto, los factores interiores
QᵀQ se reducen a la identidad.

Por tanto:

A'_(i_1)...A'_(i_p)
=
Q A_(i_1)...A_(i_p) Qᵀ

Aplicando la propiedad cíclica de la traza:

I'_(i_1,...,i_p) = I_(i_1,...,i_p)

Queda demostrado.

## 9. Interpretación combinatoria

Para matrices de adyacencia binarias,
la magnitud:

tr(A_i A_j A_k)

cuenta recorridos cerrados de longitud tres
que utilizan sucesivamente relaciones
de las familias i, j y k.

Análogamente:

tr(A_i A_j A_k A_l)

cuenta recorridos cerrados de longitud cuatro
con la secuencia de familias especificada.

Estos recorridos pueden repetir vértices
cuando la longitud lo permite.

No deben identificarse automáticamente
con ciclos simples.

Los invariantes mixtos permiten investigar
la interacción entre diferentes familias
geométricas.

## 10. Límites de identificación

La coincidencia de matrices de Gram
no demuestra equivalencia geométrica.

Tampoco debe suponerse que un conjunto
finito arbitrario de invariantes mixtos
identifique completamente una arquitectura.

Por tanto:

C(A) = C(B)

no implica necesariamente:

B_k = PA_kPᵀ para todo k

La igualdad de invariantes proporciona
condiciones necesarias de equivalencia
bajo la acción considerada.

La suficiencia requiere demostraciones
adicionales.

## 11. Relación con la dinámica

Sea F un operador que actúa sobre
una arquitectura multicapa.

La conservación dinámica de C exige:

C(F(A)) = C(A)

Esta igualdad no se deriva automáticamente
de los teoremas anteriores.

Debe demostrarse específicamente para F.

Si la arquitectura permanece fija y solo
evolucionan los estados de los nodos,
la constancia de C es estructural y no
demuestra conservación de información
en dichos estados.

Deben distinguirse:

- Invariantes de la arquitectura fija.
- Invariantes de los estados dinámicos.
- Invariantes de una arquitectura evolutiva.
- Invariantes bajo cambios de representación.

## 12. Protocolo de verificación

Antes de aplicar estos invariantes
a Pirámide-Parábola:

1. Fijar la versión canónica de la arquitectura.

2. Identificar el commit de referencia.

3. Construir cada matriz relacional por separado.

4. Verificar dimensiones, simetría y diagonal.

5. Calcular la matriz de Gram.

6. Calcular invariantes mixtos de órdenes
   previamente establecidos.

7. Aplicar permutaciones simultáneas y
   comprobar la conservación.

8. Comparar con arquitecturas nulas y ablaciones.

9. Registrar las coincidencias y diferencias
   sin seleccionar retrospectivamente
   los invariantes favorables.

10. Publicar matrices, código, parámetros
    y resultados reproducibles.

Este protocolo constituye una propuesta
para investigación posterior.

No modifica la campaña congelada del
Episodio 44.

## 13. Relación con 44A y 44B

Los invariantes multicapa pueden utilizarse
para caracterizar las arquitecturas empleadas
en los experimentos.

Sin embargo, no permiten por sí solos
explicar las diferencias observadas
entre los operadores variacional y de consenso.

Para investigar dichas diferencias será
necesario estudiar adicionalmente:

- Equivariancia dinámica.
- Órbitas de los estados finales.
- Entropía de atractores.
- Entropía de clases de equivalencia.
- Cuencas de atracción.
- Recuperabilidad de información.

La contribución geométrica y la contribución
algorítmica deben evaluarse por separado.

## 14. Clasificación epistemológica

RESULTADOS DEMOSTRADOS:

- Invariancia de la matriz de Gram.
- Simetría y semidefinición positiva de C.
- Interpretación del solapamiento binario.
- Invariancia de las trazas de productos.
- Interpretación mediante recorridos cerrados.

RESULTADOS PENDIENTES:

- Matriz de Gram canónica de Pirámide-Parábola.
- Invariantes mixtos específicos.
- Comparación con arquitecturas nulas.
- Capacidad de diferenciación estructural.
- Conservación bajo la dinámica propia.
- Correspondencia matemática con la TRCG.

No se incorporan resultados experimentales
no verificados.

## 15. Gobernanza

- Nivel II retenido.
- Nivel III abierto.
- Pirámide-Parábola como candidata experimental.
- λ reservado al 4º Factor.
- Sin ascensos automáticos.
- Sin reescalados retrospectivos.
- Sin alteración de protocolos congelados.

## 16. Conclusión

La identidad de una arquitectura multicapa
no puede reducirse a las propiedades
individuales de sus matrices.

Las trazas de productos proporcionan
magnitudes verificables que caracterizan
parcialmente la interacción entre familias
relacionales.

Su aplicación a Pirámide-Parábola constituye
una línea concreta de investigación para
evaluar una posible convergencia con la TRCG.

La correspondencia deberá demostrarse,
no presuponerse.

17. Ampliación v0.2.0 — Invariantes estratificados completos

17.1. Objeto

La presente ampliación desarrolla una familia de invariantes completos para un conjunto explícito de configuraciones relacionales de soporte reducido.

El objetivo es avanzar desde la caracterización parcial mediante invariantes multicapa hasta la identificación exacta de determinadas clases de equivalencia.

Se investigan:

- Completitud de invariantes.
- Reconstrucción de pesos geométricos.
- Separación de clases estratificadas.
- Degeneraciones.
- Sensibilidad numérica.
- Limitaciones de la reconstrucción.
- Extensión a configuraciones de soporte superior.

Los resultados complementan los desarrollos anteriores sobre matrices de Gram y trazas mixtas.

17.2. Documentos relacionados

- "EFFECTIVE_SYMMETRY_GROUP.md"
- "RELATIONAL_QUOTIENT_METRIC.md"
- "EQUILIBRIUM_CLASSIFICATION.md"
- "INFORMATION_RECOVERY.md"
- "GEOMETRIC_IDENTIFIABILITY.md"
- "REDUCED_SUPPORT_STABILITY.md"
- "CANONICAL_OPERATOR_CORRESPONDENCE.md"

Auditoría asociada:

- "quotient_space_audit.py"
- "quotient_space_results.json"

---

18. Invariancia y completitud

Sea X un espacio de configuraciones relacionales y G un grupo que actúa sobre X.

Una aplicación:

[
I:X\longrightarrow\mathbb R^k
]

es invariante bajo G cuando:

[
I(g\cdot x)=I(x)
]

para todo g perteneciente a G y todo x perteneciente a X.

La invariancia garantiza que configuraciones equivalentes poseen el mismo descriptor.

Sin embargo, no garantiza que configuraciones con el mismo descriptor sean equivalentes.

Definición de completitud

Una familia de invariantes I es completa respecto de G sobre X cuando:

[
I(x)=I(y)
\Longleftrightarrow
[x]_G=[y]_G.
]

Por tanto, la aplicación inducida:

[
\overline I:X/G\longrightarrow\mathbb R^k
]

es inyectiva.

La completitud depende simultáneamente de:

- El espacio de configuraciones.
- El grupo considerado.
- La familia de invariantes.

Una familia completa para un dominio restringido puede dejar de ser completa al ampliar dicho dominio.

---

19. Incorporación de atributos geométricos

Consideramos el espacio matricial:

[
\mathcal S_N=
{R\in\mathbb R^{N\times N}:R^T=R,\ \operatorname{diag}(R)=0}.
]

Introducimos una matriz diagonal auxiliar:

[
W=\operatorname{diag}(g_1,\ldots,g_N),
]

donde:

[
g_i>0.
]

Los valores (g_i) representan atributos o pesos geométricos asociados a los nodos.

La matriz W no pertenece, en general, al espacio de matrices relacionales de diagonal nula.

Por tanto, debe interpretarse como un objeto adicional de la arquitectura.

Consideramos el espacio ampliado:

[
\mathcal A=(R,W).
]

La incorporación de W permite construir invariantes que contienen información sobre la relación entre los estados matriciales y los atributos geométricos.

---

20. Acción simultánea sobre relaciones y atributos

Sea P una matriz de permutación.

Definimos:

[
R'=PRP^T,
]

[
W'=PWP^T.
]

La acción simultánea transporta coherentemente tanto las relaciones como los atributos.

Si la arquitectura mantiene W fija, el grupo admisible debe satisfacer:

[
PWP^T=W.
]

Definimos:

[
G_W=
{P\in S_N:PWP^T=W}.
]

Este grupo está formado por las permutaciones que conservan los pesos geométricos.

No tiene por qué coincidir con el grupo de automorfismos de la arquitectura completa.

La incorporación de capas, restricciones o atributos adicionales puede reducirlo.

---

21. Grupo estratificado

Para N = 24 consideramos seis estratos de cuatro nodos.

Adoptamos la numeración:

[
i=6q+r,
]

con:

[
q\in{0,1,2,3},
]

[
r\in{0,1,2,3,4,5}.
]

Los pesos son constantes dentro de cada estrato:

[
g_{6q+r}=w_r.
]

Suponemos inicialmente que:

[
w_r>0
]

y que los seis pesos estratificados son distintos.

En estas condiciones:

[
G_W\cong(S_4)^6.
]

Su orden es:

[
|G_W|=(4!)^6=191102976.
]

Este grupo caracteriza las permutaciones que conservan W.

No se afirma que todas ellas conserven las restantes relaciones geométricas de Pirámide-Parábola.

---

22. Invariantes mixtos geométrico-relacionales

Definimos:

[
I_1(R,W)=\operatorname{tr}(WR^2),
]

[
I_2(R,W)=\operatorname{tr}(W^2R^2).
]

Teorema 3

Ambas magnitudes son invariantes bajo conjugación ortogonal simultánea de R y W.

Demostración

Sea Q una matriz ortogonal.

Entonces:

[
R'=QRQ^T,
]

[
W'=QWQ^T.
]

Como:

[
Q^TQ=I,
]

se obtiene:

[
(R')^2=QR^2Q^T.
]

Por tanto:

[
\begin{aligned}
I_1(R',W')
&=\operatorname{tr}(QWQ^TQR^2Q^T)\
&=\operatorname{tr}(QWR^2Q^T)\
&=\operatorname{tr}(WR^2).
\end{aligned}
]

Análogamente:

[
(W')^2=QW^2Q^T.
]

En consecuencia:

[
I_2(R',W')=\operatorname{tr}(W^2R^2).
]

Queda demostrado.

Corolario

Cuando W permanece fija, (I_1) e (I_2) son invariantes bajo el grupo (G_W).

La conjugación deberá preservar adicionalmente el dominio relacional cuando este posea restricciones específicas.

---

23. Familia de configuraciones de una arista

Sea:

[
C_0>0.
]

Para cada arista no ordenada:

[
e={a,b},
]

definimos:

[
R_e=C_0(e_ae_b^T+e_be_a^T).
]

La familia completa es:

[
\mathcal E_{C_0}

{R_e:e={a,b},\ a\neq b}.
]

Para N = 24:

[
|\mathcal E_{C_0}|=\binom{24}{2}=276.
]

Estas configuraciones constituyen puntos fijos del operador relacional matricial especificado en "REDUCED_SUPPORT_STABILITY.md", bajo las hipótesis allí establecidas.

La clasificación mediante invariantes no requiere por sí misma que los estados sean dinámicamente estables.

---

24. Evaluación exacta de los invariantes

Para una configuración de una arista:

[
R_e^2=C_0^2(e_ae_a^T+e_be_b^T).
]

Por tanto:

[
\boxed{
I_1(R_e,W)=C_0^2(g_a+g_b)
}
]

y:

[
\boxed{
I_2(R_e,W)=C_0^2(g_a^2+g_b^2)
}
]

Estas expresiones muestran que ambos invariantes contienen información sobre los atributos geométricos de los extremos de la arista.

A diferencia de los invariantes espectrales individuales de R, dependen de la posición de la relación dentro de la arquitectura ponderada.

---

25. Teorema de reconstrucción exacta

Teorema 4

Conocidos (I_1), (I_2) y (C_0>0), puede reconstruirse exactamente el par no ordenado de pesos geométricos de una configuración de una arista.

Demostración

Definimos:

[
A=\frac{I_1}{C_0^2},
]

[
B=\frac{I_2}{C_0^2}.
]

Entonces:

[
A=g_a+g_b,
]

[
B=g_a^2+g_b^2.
]

Elevando A al cuadrado:

[
A^2=g_a^2+g_b^2+2g_ag_b.
]

Por tanto:

[
g_ag_b=\frac{A^2-B}{2}.
]

Los pesos (g_a) y (g_b) son las raíces del polinomio:

[
x^2-Ax+\frac{A^2-B}{2}=0.
]

Su discriminante es:

[
\Delta=2B-A^2.
]

Aplicando la fórmula cuadrática:

[
\boxed{
g_{\pm}

\frac{A\pm\sqrt{2B-A^2}}2
}
]

En consecuencia:

[
{g_a,g_b}={g_+,g_-}.
]

Queda demostrado.

La reconstrucción determina el par no ordenado, pero no distingue cuál de los dos pesos corresponde a cada extremo individual.

---

26. Condiciones de admisibilidad

Teorema 5

Los valores A y B corresponden a dos pesos reales estrictamente positivos si y solo si:

[
\boxed{
A>0,
\qquad
\frac{A^2}{2}\leq B<A^2
}
]

Demostración

Para obtener raíces reales se requiere:

[
2B-A^2\geq0.
]

Equivalentemente:

[
B\geq\frac{A^2}{2}.
]

Para que ambas raíces sean positivas se requiere que su suma sea positiva:

[
A>0,
]

y que su producto sea estrictamente positivo:

[
\frac{A^2-B}{2}>0.
]

Equivalentemente:

[
B<A^2.
]

Estas condiciones son necesarias y suficientes.

Queda demostrado.

Clasificación de casos

Condición| Interpretación
B < A²/2| No existen dos pesos reales.
B = A²/2, A > 0| Dos pesos positivos iguales.
A²/2 < B < A², A > 0| Dos pesos positivos diferentes.
B = A², A > 0| Uno de los pesos es cero.
B > A²| Pesos reales de signos opuestos.
A ≤ 0| No pueden existir dos pesos estrictamente positivos.

La admisibilidad algebraica no garantiza la admisibilidad dentro de una arquitectura concreta.

Para ello, los pesos reconstruidos deben pertenecer al conjunto de pesos autorizados y respetar las multiplicidades de nodos disponibles.

---

27. Completitud estratificada

Teorema 6

Supongamos:

1. Seis estratos de cuatro nodos.
2. Pesos positivos constantes dentro de cada estrato.
3. Pesos distintos entre estratos.
4. Masa C0 conocida y fija.
5. Configuraciones pertenecientes a la familia de una arista.

Entonces:

[
I(R)=(I_1(R,W),I_2(R,W))
]

es una familia completa de invariantes respecto del grupo:

[
G_S=(S_4)^6.
]

Demostración

Si dos configuraciones pertenecen a la misma órbita estratificada, sus invariantes coinciden por el Teorema 3.

Recíprocamente, supongamos:

[
I(R_e)=I(R_f).
]

Por el Teorema 4, ambas configuraciones poseen el mismo par no ordenado de pesos.

Como los seis pesos estratificados son distintos, cada peso identifica un único estrato.

Por tanto, ambas aristas conectan el mismo par no ordenado de estratos.

Las permutaciones independientes dentro de los estratos actúan transitivamente sobre las aristas de cada tipo.

En consecuencia, existe:

[
P\in G_S
]

tal que:

[
R_f=PR_eP^T.
]

Por tanto:

[
[R_e]{G_S}=[R_f]{G_S}.
]

Queda demostrado.

---

28. Número exacto de clases identificables

El número de pares no ordenados de seis estratos, permitiendo repetición, es:

[
\binom{6+1}{2}=21.
]

Por tanto, la familia de invariantes:

[
(I_1,I_2)
]

adopta exactamente 21 valores distintos sobre las 276 configuraciones de una arista.

La distribución es:

Tipo de arista| Clases| Configuraciones por clase
Extremos en el mismo estrato| 6| 6
Extremos en estratos distintos| 15| 16
Total| 21| —

Se verifica:

[
6(6)+15(16)=276.
]

Este resultado establece una identificación completa dentro de la familia y el grupo especificados.

No constituye una caracterización completa de todas las matrices relacionales.

---

29. Insuficiencia de los invariantes espectrales

Todas las configuraciones de una arista poseen el mismo espectro:

[
\operatorname{Spec}(R_e)

{C_0,-C_0,0^{(22)}}.
]

Asimismo:

[
\operatorname{tr}(R_e^k)

C_0^k+(-C_0)^k
]

para todo entero k ≥ 1.

Por tanto, ninguna familia formada exclusivamente por trazas de potencias de R permite distinguir las 21 clases estratificadas.

Los invariantes (I_1) e (I_2) incorporan información adicional mediante W.

Este resultado demuestra que la posición geométrica de una relación puede ser identificable mediante invariantes mixtos incluso cuando su espectro individual no contiene información discriminante.

---

30. Insuficiencia individual de los dos momentos

Cada uno de los invariantes puede presentar colisiones entre clases diferentes.

Consideremos pesos ilustrativos:

[
{1,2,3,4,5,6}.
]

30.1. Colisión del primer momento

Los pares:

[
{1,4},
\qquad
{2,3}
]

satisfacen:

[
1+4=2+3=5.
]

Por tanto, poseen el mismo (I_1).

Sin embargo:

[
1^2+4^2=17,
]

[
2^2+3^2=13.
]

El segundo invariante permite distinguirlos.

30.2. Colisión del segundo momento

Los pares:

[
{1,7},
\qquad
{5,5}
]

satisfacen:

[
1^2+7^2=5^2+5^2=50.
]

Sin embargo:

[
1+7=8,
]

[
5+5=10.
]

Este ejemplo utiliza un conjunto ilustrativo diferente de pesos positivos.

El primer invariante permite distinguir ambos pares.

Conclusión

Ninguno de los dos momentos garantiza individualmente la identificación para conjuntos arbitrarios de pesos positivos.

Su utilización conjunta proporciona una reconstrucción universal del par no ordenado.

No se afirma que dos invariantes sean el número mínimo posible para cualquier conjunto finito particular de pesos.

---

31. Diferencia entre clasificación estratificada y rotacional

El grupo rotacional:

[
G_4\cong\mathbb Z_4
]

es un subgrupo del grupo estratificado bajo la numeración adoptada.

La familia de 276 configuraciones posee:

- 72 clases rotacionales.
- 21 clases estratificadas.

Los invariantes (I_1) e (I_2) son invariantes bajo ambos grupos.

Sin embargo, son completos únicamente para la clasificación estratificada de una arista.

Contraejemplo

Consideremos:

[
e={0,6},
]

[
f={0,12}.
]

Ambas aristas conectan nodos del mismo estrato.

Por tanto:

[
I_1(R_e)=I_1(R_f),
]

[
I_2(R_e)=I_2(R_f).
]

Sin embargo, las aristas presentan separaciones sectoriales diferentes.

La primera conecta sectores consecutivos.

La segunda conecta sectores opuestos.

Ninguna rotación sectorial transforma una arista en la otra.

En consecuencia:

[
[R_e]{G_4}\neq[R_f]{G_4}.
]

La familia de invariantes no es completa respecto del grupo rotacional.

---

32. Extensión a una clasificación rotacional completa

Para una arista entre nodos:

[
a=6q_a+r_a,
]

[
b=6q_b+r_b,
]

definimos el desplazamiento sectorial:

[
\delta=q_b-q_a\pmod4.
]

Si los estratos son distintos, ordenamos los extremos de manera que:

[
r_a<r_b.
]

En ese caso, el desplazamiento δ queda definido de forma inequívoca.

Si ambos extremos pertenecen al mismo estrato, el intercambio de extremos identifica:

[
\delta\sim-\delta.
]

Por tanto, basta utilizar:

[
d=\min(\delta,4-\delta).
]

Teorema 7

El par no ordenado de estratos, complementado por el desplazamiento sectorial definido según las convenciones anteriores, constituye una clasificación completa de las aristas bajo (G_4).

Demostración

Una rotación común transforma:

[
(q_a,q_b)
\longmapsto
(q_a+k,q_b+k)
]

módulo cuatro.

Los estratos permanecen fijos y la diferencia sectorial no cambia.

Recíprocamente, dos aristas con los mismos estratos y el mismo desplazamiento sectorial pueden hacerse coincidir mediante una rotación común.

Cuando los extremos pertenecen al mismo estrato, debe permitirse previamente su intercambio.

Por tanto, los descriptores identifican exactamente las órbitas rotacionales.

Queda demostrado.

Recuento

Para extremos en estratos diferentes existen:

[
\binom62=15
]

pares de estratos.

Cada par admite cuatro desplazamientos sectoriales.

Por tanto:

[
15\cdot4=60
]

clases.

Para extremos en el mismo estrato existen dos separaciones posibles:

- Sectores consecutivos.
- Sectores opuestos.

Por tanto:

[
6\cdot2=12
]

clases.

En consecuencia:

[
\boxed{
60+12=72
}
]

La incorporación de información angular permite completar la clasificación rotacional.

Este descriptor adicional utiliza la numeración sectorial explícita y no se deduce exclusivamente de W.

---

33. Degeneración por coincidencia de pesos

Supongamos que dos estratos distintos poseen el mismo peso:

[
w_r=w_s,
\qquad r\neq s.
]

En este caso, la reconstrucción algebraica de los pesos continúa siendo válida.

Sin embargo, el peso reconstruido deja de identificar unívocamente el estrato.

Por tanto, (I_1) e (I_2) dejan de ser completos respecto de la clasificación que mantiene fija la identidad de los seis estratos.

Debe distinguirse entre:

- Grupo que conserva los pesos.
- Grupo que conserva la identidad de los estratos.
- Grupo que conserva la arquitectura completa.

Si un peso aparece en varios estratos, el grupo que conserva exclusivamente W puede permitir permutaciones entre ellos.

Si los estratos siguen siendo objetos geométricos diferenciados, dichas permutaciones pueden resultar inadmisibles.

La coincidencia de pesos no implica identidad geométrica.

---

34. Dependencia respecto de la masa

Las fórmulas de reconstrucción utilizan:

[
A=\frac{I_1}{C_0^2},
]

[
B=\frac{I_2}{C_0^2}.
]

Por tanto, la demostración de completitud presupone que C0 es conocida.

Si la masa es desconocida, no se garantiza en general la reconstrucción mediante (I_1) e (I_2) exclusivamente.

Invariante adicional

Para una configuración de una arista:

[
I_0(R)=\operatorname{tr}(R^2)=2C_0^2.
]

En consecuencia:

[
C_0=\sqrt{\frac{I_0}{2}}.
]

La familia:

[
(I_0,I_1,I_2)
]

permite recuperar la masa positiva y el par no ordenado de pesos.

Equivalentemente:

[
A=\frac{2I_1}{I_0},
]

[
B=\frac{2I_2}{I_0}.
]

Esta ampliación elimina la necesidad de conocer previamente la masa para la familia de una arista.

No elimina las restantes limitaciones de identificabilidad.

---

35. Sensibilidad cerca de configuraciones degeneradas

El discriminante satisface:

[
\Delta=(g_a-g_b)^2.
]

Por tanto:

[
\sqrt{\Delta}=|g_a-g_b|.
]

Cuando los pesos son próximos, Δ puede ser muy pequeño.

Consideremos perturbaciones:

[
\widetilde A=A+\varepsilon_A,
]

[
\widetilde B=B+\varepsilon_B.
]

Entonces:

[
\widetilde\Delta-\Delta

2\varepsilon_B
-2A\varepsilon_A
-\varepsilon_A^2.
]

Para discriminantes no negativos:

[
|\sqrt{\widetilde\Delta}-\sqrt{\Delta}|
\leq
\sqrt{|\widetilde\Delta-\Delta|}.
]

En consecuencia:

[
|\widetilde g_{\pm}-g_{\pm}|
\leq
\frac12
\left(
|\varepsilon_A|
+
\sqrt{
2|\varepsilon_B|
+
2|A||\varepsilon_A|
+
\varepsilon_A^2
}
\right).
]

Esta cota establece continuidad de la reconstrucción en el dominio admisible.

Sin embargo, la sensibilidad puede aumentar cerca de pesos coincidentes.

No se garantiza una cota uniforme de tipo Lipschitz en una vecindad que incluya la degeneración.

---

36. Protocolo de reconstrucción numérica

Toda implementación deberá:

1. Verificar que los invariantes sean finitos.
2. Verificar que la masa sea positiva.
3. Calcular A y B.
4. Calcular el discriminante.
5. Comprobar la admisibilidad algebraica.
6. Reconstruir los pesos.
7. Verificar su positividad.
8. Contrastar los pesos con el conjunto autorizado.
9. Comprobar la disponibilidad de nodos.
10. Registrar el error de reconstrucción.

Un discriminante ligeramente negativo podrá atribuirse a redondeo únicamente bajo una tolerancia previamente especificada y justificada respecto de la escala de los datos.

Un discriminante significativamente negativo deberá registrarse como incompatibilidad.

No se permitirá ajustar retrospectivamente los pesos para favorecer una identificación.

Cuando varios estratos sean compatibles con la tolerancia, el resultado deberá clasificarse como ambiguo.

---

37. Extensión a momentos geométrico-relacionales superiores

Definimos la familia:

[
J_k(R,W)=\operatorname{tr}(W^kR^2),
]

para enteros k ≥ 0.

Para una matriz simétrica de diagonal nula:

[
(R^2){ii}=\sum_jR{ij}^2.
]

Por tanto:

[
J_k(R,W)

\sum_i g_i^k\sum_jR_{ij}^2.
]

Agrupando por estratos:

[
J_k(R,W)

\sum_{r=0}^{5}w_r^k s_r(R),
]

donde:

[
s_r(R)

\sum_{i\in V_r}\sum_jR_{ij}^2.
]

La magnitud (s_r(R)) representa la energía cuadrática relacional incidente sobre los nodos del estrato r.

No debe confundirse con masa relacional lineal.

---

38. Reconstrucción de perfiles estratificados

Teorema 8

Si los seis pesos estratificados son distintos, los seis momentos:

[
J_0,J_1,J_2,J_3,J_4,J_5
]

determinan unívocamente el perfil:

[
s(R)=(s_0,\ldots,s_5).
]

Demostración

La relación entre momentos y perfiles es:

[
\begin{pmatrix}
J_0\
J_1\
J_2\
J_3\
J_4\
J_5
\end{pmatrix}

\begin{pmatrix}
1&1&1&1&1&1\
w_0&w_1&w_2&w_3&w_4&w_5\
w_0^2&w_1^2&w_2^2&w_3^2&w_4^2&w_5^2\
w_0^3&w_1^3&w_2^3&w_3^3&w_4^3&w_5^3\
w_0^4&w_1^4&w_2^4&w_3^4&w_4^4&w_5^4\
w_0^5&w_1^5&w_2^5&w_3^5&w_4^5&w_5^5
\end{pmatrix}
\begin{pmatrix}
s_0\
s_1\
s_2\
s_3\
s_4\
s_5
\end{pmatrix}.
]

La matriz de coeficientes es una matriz de Vandermonde.

Su determinante es:

[
\det(V)=
\prod_{0\leq r<t\leq5}(w_t-w_r).
]

Como los pesos son distintos:

[
\det(V)\neq0.
]

Por tanto, V es invertible y:

[
\boxed{
s=V^{-1}J
}
]

Queda demostrado.

Alcance

Este resultado es aplicable a matrices relacionales de soporte arbitrario.

Permite recuperar seis magnitudes agregadas por estratos.

No permite reconstruir en general las 276 relaciones diádicas individuales.

La estabilidad numérica dependerá del condicionamiento de la matriz de Vandermonde.

---

39. Limitaciones de los perfiles estratificados

La reconstrucción de:

[
s(R)=(s_0,\ldots,s_5)
]

no garantiza la identificación completa de una matriz.

Diferentes configuraciones pueden presentar la misma energía cuadrática incidente sobre cada estrato.

Por tanto, todos los momentos (J_k) pueden coincidir sin que las configuraciones pertenezcan a la misma órbita.

Contraejemplo

Dentro de un mismo estrato de cuatro nodos consideramos dos matrices:

- Una con dos aristas disjuntas de peso a.
- Otra con dos aristas adyacentes de peso a.

Con:

[
a>0.
]

Ambas configuraciones poseen masa:

[
C_0=2a.
]

También poseen la misma energía cuadrática total:

[
\operatorname{tr}(R^2)=4a^2.
]

Como todas las aristas pertenecen al mismo estrato, sus perfiles estratificados coinciden.

En consecuencia, coinciden todos los momentos:

[
J_k(R,W).
]

Sin embargo, los grafos de soporte no son isomorfos.

Sus secuencias de grados son, respectivamente:

[
(1,1,1,1)
]

y:

[
(2,1,1,0).
]

Por tanto, no pertenecen a la misma órbita bajo las permutaciones del estrato.

La familia de momentos (J_k) no es completa para configuraciones de soporte arbitrario, incluso con masa conocida y pesos distintos.

---

40. Invariantes de interacción entre estratos

Para ampliar la información recuperable, definimos los proyectores diagonales:

[
P_r
]

sobre los nodos pertenecientes al estrato r.

Consideramos:

[
K_{rt}(R)

\operatorname{tr}(P_rRP_tR).
]

Como R es simétrica:

[
K_{rt}(R)

\sum_{i\in V_r}
\sum_{j\in V_t}
R_{ij}^2.
]

Se verifica:

[
K_{rt}=K_{tr}.
]

Asimismo:

[
K_{rt}\geq0.
]

Para r distinto de t, la magnitud mide la energía cuadrática de las relaciones entre ambos estratos.

Para r igual a t, contabiliza dos veces las aristas internas del estrato.

La matriz:

[
K(R)=(K_{rt}(R))_{r,t=0}^{5}
]

es simétrica y posee 21 componentes independientes como descriptor.

Teorema 9

K es invariante bajo el grupo estratificado.

Demostración

Las permutaciones pertenecientes al grupo estratificado conservan cada proyector (P_r).

Por tanto, la conjugación de R por dichas permutaciones no modifica las trazas:

[
\operatorname{tr}(P_rRP_tR).
]

Queda demostrado.

Relación con los perfiles

Se cumple:

[
s_r(R)=\sum_tK_{rt}(R).
]

Por tanto, K contiene información sobre la distribución de energía entre pares de estratos, mientras s conserva únicamente los totales incidentes.

La matriz K es un descriptor más detallado que el perfil s.

No se afirma que sea completa para matrices arbitrarias.

El contraejemplo de la sección 39 también presenta la misma matriz K.

---

41. Jerarquía de información relacional

Los resultados anteriores permiten establecer la siguiente jerarquía de representaciones:

Nivel A — Información espectral

Espectro y trazas de potencias de R.

Caracterizan propiedades algebraicas globales, pero no identifican necesariamente la posición geométrica de las relaciones.

Nivel B — Momentos geométrico-relacionales

Familia:

[
J_k=\operatorname{tr}(W^kR^2).
]

Permite recuperar perfiles estratificados bajo las condiciones demostradas.

Nivel C — Interacciones entre estratos

Familia:

[
K_{rt}=\operatorname{tr}(P_rRP_tR).
]

Caracteriza la distribución cuadrática de relaciones entre pares de estratos.

Nivel D — Información angular y estructural

Incorpora separaciones sectoriales, organización de soportes y relaciones adicionales.

Permite distinguir configuraciones que los descriptores estratificados pueden identificar.

Nivel E — Representación diádica completa

Familia indexada:

[
p(R)=(R_{ij})_{i<j}.
]

Permite reconstruir exactamente R.

Esta jerarquía distingue diferentes cantidades y tipos de información conservada.

No implica que cada descriptor contenga necesariamente toda la información espectral del nivel anterior.

Tampoco representa una jerarquía de niveles epistemológicos del 4º Factor.

---

42. Relación con la dinámica

La invariancia bajo transformaciones estructurales no implica conservación temporal.

Para un operador F:

[
I(g\cdot R)=I(R)
]

no implica:

[
I(F(R))=I(R).
]

La conservación dinámica deberá demostrarse independientemente.

Los invariantes pueden utilizarse para:

- Clasificar equilibrios.
- Identificar clases de estados finales.
- Comparar trayectorias en espacios cociente.
- Detectar diferencias estructurales.
- Evaluar pérdidas de información.
- Caracterizar perfiles geométrico-relacionales.

No constituyen automáticamente funciones de Lyapunov ni cantidades dinámicas conservadas.

---

43. Protocolo de verificación computacional

Bloque A — Resultados de una arista

Prueba| Objetivo
T01| Verificar la invariancia de I1 e I2.
T02| Enumerar las 276 configuraciones.
T03| Identificar las 21 clases estratificadas.
T04| Reconstruir los pares de pesos.
T05| Verificar la coincidencia espectral.
T06| Detectar colisiones de invariantes individuales.
T07| Contrastar pesos repetidos.
T08| Verificar condiciones de admisibilidad.
T09| Detectar colisiones entre clases rotacionales.
T10| Verificar sensibilidad cerca de degeneraciones.

Bloque B — Nuevas extensiones

Prueba| Objetivo
T11| Recuperar masa desconocida mediante I0.
T12| Clasificar las 72 órbitas mediante información angular.
T13| Reconstruir perfiles mediante Vandermonde.
T14| Verificar condicionamiento numérico.
T15| Detectar degeneración por pesos repetidos.
T16| Verificar la invariancia de K.
T17| Comprobar la relación entre K y s.
T18| Verificar el contraejemplo de soportes diferentes.
T19| Contrastar configuraciones de soporte arbitrario.
T20| Evaluar conservación o variación temporal de los descriptores.

La auditoría "quotient_space_audit.py" proporciona verificaciones asociadas a parte del bloque A.

Las nuevas extensiones del bloque B requieren una auditoría adicional.

No se presentan como pruebas computacionales ejecutadas en esta versión.

---

44. Resultados demostrados

Bajo las hipótesis correspondientes:

- Invariancia de I1 e I2 bajo conjugación simultánea.
- Reconstrucción exacta del par no ordenado de pesos.
- Condiciones necesarias y suficientes de admisibilidad algebraica.
- Completitud para las 21 clases estratificadas de una arista.
- Insuficiencia de los invariantes espectrales individuales.
- Posibilidad de colisiones de cada momento por separado.
- Insuficiencia de I1 e I2 para la clasificación rotacional.
- Clasificación rotacional completa mediante información angular adicional.
- Recuperación de masa mediante I0.
- Sensibilidad de reconstrucción cerca de pesos degenerados.
- Reconstrucción de perfiles estratificados mediante momentos y matrices de Vandermonde.
- Invariancia de las energías cuadráticas entre estratos.
- Incompletitud de los momentos y de K para soportes arbitrarios.

---

45. Investigaciones pendientes

1. Auditoría computacional de las nuevas extensiones.
2. Caracterización de invariantes completos para soportes superiores.
3. Incorporación de información angular mediante invariantes matriciales.
4. Caracterización de interacciones de orden superior.
5. Estudio del condicionamiento de los momentos geométricos.
6. Comparación con arquitecturas nulas.
7. Conservación dinámica de los descriptores.
8. Identificación de invariantes propios de 44A y 44B.
9. Correspondencia con la implementación canónica.
10. Correspondencia matemática con la TRCG.

---

46. Gobernanza de la ampliación

Se mantienen:

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
- Reproducibilidad computacional.

---

47. Conclusión de la ampliación

Los invariantes relacionales adquieren capacidad discriminante adicional cuando incorporan atributos geométricos de los nodos.

Para las configuraciones de una arista, dos momentos geométrico-relacionales permiten reconstruir exactamente el par de pesos e identificar las 21 clases estratificadas.

La información angular permite ampliar esta clasificación hasta las 72 clases rotacionales.

Para configuraciones de soporte arbitrario, los momentos superiores permiten reconstruir perfiles de energía cuadrática por estratos.

La matriz de interacciones entre estratos proporciona una descripción adicional de la distribución relacional.

Sin embargo, ninguna de estas representaciones agregadas garantiza por sí sola la reconstrucción completa de una configuración arbitraria.

La completitud debe demostrarse respecto de cada dominio y cada grupo de equivalencia.

La invariancia establece conservación estructural.

La completitud establece identificabilidad.

La reconstrucción establece recuperabilidad.

La dinámica exige una demostración independiente.

---

TRCG — Código Viajer — Pirámide-Parábola

Nivel II retenido · Nivel III abierto · λ reservado al 4º Factor.

FIN DEL DOCUMENTO
