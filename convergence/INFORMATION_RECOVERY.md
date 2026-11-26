INFORMATION RECOVERY

Recuperabilidad, invertibilidad y pérdida de información relacional

Programa: TRCG — Código Viajer — Pirámide-Parábola
Versión: 1.0.0
Fecha: 2026-11-26
Estado: Desarrollo matemático y resultados condicionados.

---

1. Objetivo

Estudiar las condiciones bajo las cuales la información contenida en una configuración relacional puede conservarse, reconstruirse o perderse durante su evolución.

Se distinguen cinco problemas:

- Reconstrucción de configuraciones.
- Invertibilidad dinámica.
- Recuperabilidad mediante invariantes.
- Recuperabilidad en espacios cociente.
- Pérdida de información asociada a la convergencia hacia atractores.

Estos problemas están relacionados, pero no son matemáticamente equivalentes.

---

2. Documentos relacionados

Este documento complementa:

- "GEOMETRY_IDENTITY.md"
- "GEOMETRIC_IDENTIFIABILITY.md"
- "EFFECTIVE_SYMMETRY_GROUP.md"
- "RELATIONAL_EQUIVARIANCE.md"
- "RELATIONAL_QUOTIENT_METRIC.md"
- "MULTILAYER_INVARIANTS.md"
- "EQUILIBRIUM_CLASSIFICATION.md"
- "REDUCED_SUPPORT_STABILITY.md"
- "CANONICAL_OPERATOR_CORRESPONDENCE.md"

No sustituye las demostraciones contenidas en dichos documentos.

---

3. Espacio relacional

Sea:

[
\mathcal S_N=
{R\in\mathbb R^{N\times N}:R^T=R,\ \operatorname{diag}(R)=0}.
]

Su dimensión es:

[
m=\frac{N(N-1)}2.
]

Para N = 24:

[
m=276.
]

Definimos la representación diádica ordenada:

[
p(R)=(R_{ij})_{i<j}.
]

El orden de los pares se fija previamente y permanece constante.

La aplicación:

[
p:\mathcal S_N\longrightarrow\mathbb R^m
]

es un isomorfismo lineal.

Por tanto, la familia indexada de relaciones diádicas contiene toda la información necesaria para reconstruir R.

Una colección no indexada de valores relacionales no garantiza dicha reconstrucción.

---

4. Reconstrucción exacta

Teorema 1

Dos matrices pertenecientes a (\mathcal S_N) son iguales si y solo si coinciden todas sus relaciones diádicas indexadas.

Demostración

Si:

[
p(R)=p(S),
]

entonces:

[
R_{ij}=S_{ij}
]

para todo i < j.

Por simetría, también coinciden las entradas inferiores.

Ambas diagonales son nulas.

En consecuencia:

[
R=S.
]

La implicación recíproca es inmediata.

Queda demostrado.

Consecuencia

La representación diádica completa no introduce pérdida de información matricial.

Sin embargo, una representación comprimida mediante espectros, momentos o invariantes puede introducir identificaciones adicionales.

---

5. Dominio de masa fija

Para el operador relacional matricial consideramos:

[
\mathcal D_{C_0}=
\left{
R\in\mathcal S_N:
R_{ij}\geq0,
\sum_{i<j}R_{ij}=C_0
\right},
]

con:

[
C_0>0.
]

Para N = 24:

[
\dim(\mathcal D_{C_0})=275.
]

Este dominio no admite universalmente todas las transformaciones con signo del espacio matricial abstracto.

Las transformaciones utilizadas deberán conservar:

- Simetría matricial.
- Diagonal nula.
- No negatividad.
- Masa relacional.
- Restricciones geométricas adicionales, cuando existan.

La recuperabilidad deberá estudiarse respecto del dominio efectivamente considerado.

---

6. Transformaciones conocidas y desconocidas

Sea Q una matriz ortogonal y:

[
S=QRQ^T.
]

Si Q es conocida:

[
R=Q^TSQ.
]

La transformación es algebraicamente reversible.

Si Q es desconocida, la reconstrucción de R no queda garantizada.

Cuando Q pertenece a un grupo admisible G, el conocimiento de S permite identificar la órbita:

[
[R]_G={PRP^T:P\in G},
]

pero no necesariamente el representante original.

Debe distinguirse entre:

1. Recuperar la matriz original.
2. Recuperar su clase de equivalencia.
3. Recuperar propiedades invariantes de dicha clase.

---

7. Invertibilidad dinámica

Sea:

[
F:\mathcal D\longrightarrow\mathcal D
]

un operador dinámico.

La evolución viene dada por:

[
R_{t+1}=F(R_t).
]

La reconstrucción unívoca de un estado anterior a partir de su imagen requiere que F sea inyectivo.

Es decir:

[
F(R)=F(S)\Longrightarrow R=S.
]

La inyectividad garantiza la existencia de una inversa sobre la imagen:

[
F^{-1}:F(\mathcal D)\longrightarrow\mathcal D.
]

No garantiza que:

[
F(\mathcal D)=\mathcal D.
]

Por tanto, deben distinguirse:

- Inyectividad.
- Sobreyectividad.
- Biyectividad.
- Continuidad de la inversa.
- Estabilidad numérica de la reconstrucción.

Un operador puede ser inyectivo sin ser sobreyectivo sobre su dominio.

---

8. Recuperación durante evoluciones finitas

Teorema 2

Si F es inyectivo, entonces todas sus iteraciones finitas son inyectivas.

Demostración

La composición de aplicaciones inyectivas es inyectiva.

Por tanto:

[
F^t=
\underbrace{F\circ\cdots\circ F}_{t\text{ veces}}
]

es inyectiva para todo entero finito t ≥ 1.

Queda demostrado.

Consecuencia

Si se conoce exactamente el operador, el número de iteraciones y el estado final, existe como máximo un estado inicial compatible con dicha evolución.

Esta propiedad no garantiza que la reconstrucción sea numéricamente estable ni computacionalmente viable.

---

9. Ejemplo de relajación afín

Consideremos:

[
F(R)=(1-\alpha)R+\alpha R_*,
]

donde (R_*) es una configuración fija.

Para:

[
0<\alpha<1,
]

la evolución satisface:

[
F^t(R)=R_+(1-\alpha)^t(R-R_).
]

La reconstrucción del estado inicial es:

[
R=R_+
\frac{F^t(R)-R_}{(1-\alpha)^t}.
]

Por tanto, todas las iteraciones finitas son inyectivas.

Si el dominio es convexo y contiene (R_*), el operador conserva dicho dominio.

No obstante, la inversa puede estar definida únicamente sobre la imagen del dominio.

---

10. Amplificación de errores

Supongamos que el estado final observado contiene una perturbación E:

[
\widetilde R_t=R_t+E.
]

La reconstrucción mediante la inversa afín produce:

[
\widetilde R_0-R_0=(1-\alpha)^{-t}E.
]

En cualquier norma matricial:

[
|\widetilde R_0-R_0|

(1-\alpha)^{-t}|E|.
]

El factor de amplificación es:

[
K_t=(1-\alpha)^{-t}.
]

Para 0 < α < 1:

[
K_t\longrightarrow\infty
]

cuando t tiende a infinito.

Por tanto, la recuperabilidad algebraica puede coexistir con una creciente dificultad de reconstrucción numérica.

La pérdida práctica de información no implica necesariamente pérdida exacta de inyectividad.

---

11. Pérdida asintótica de información

Para el operador afín anterior:

[
\lim_{t\to\infty}F^t(R)=R_*.
]

Definimos la aplicación límite:

[
A(R)=\lim_{t\to\infty}F^t(R).
]

Entonces:

[
A(R)=R_*
]

para todo estado inicial del dominio considerado.

Si el dominio contiene más de un estado, A no es inyectiva.

Resultado

Un operador puede conservar la información necesaria para reconstruir el estado inicial durante cualquier evolución finita y perderla en su aplicación límite.

Por tanto:

- Inyectividad finita.
- Recuperabilidad numérica.
- Recuperabilidad asintótica.

son propiedades diferentes.

---

12. Equivariancia dinámica

Sea G un grupo finito de transformaciones admisibles.

Denotamos su acción por:

[
g\cdot R.
]

Para permutaciones matriciales:

[
g\cdot R=PRP^T.
]

El operador F es G-equivariante cuando:

[
F(g\cdot R)=g\cdot F(R)
]

para todo g perteneciente a G y todo R perteneciente al dominio.

La equivariancia permite relacionar la evolución de configuraciones estructuralmente equivalentes.

No implica por sí sola invertibilidad.

---

13. Estabilizadores relacionales

Definimos el estabilizador de una configuración R:

[
\operatorname{Stab}_G(R)=
{g\in G:g\cdot R=R}.
]

El estabilizador contiene las transformaciones del grupo que dejan inalterada la configuración.

Por el teorema órbita-estabilizador:

[
|\operatorname{Orb}_G(R)|

\frac{|G|}{|\operatorname{Stab}_G(R)|}.
]

Una configuración con un estabilizador mayor posee una órbita de menor cardinalidad.

Esta propiedad describe simetría estructural respecto del grupo elegido.

No constituye por sí sola una medida de entropía física.

---

14. Monotonía de estabilizadores

Teorema 3

Si F es G-equivariante, entonces:

[
\operatorname{Stab}_G(R)
\subseteq
\operatorname{Stab}_G(F(R)).
]

Demostración

Sea:

[
g\in\operatorname{Stab}_G(R).
]

Entonces:

[
g\cdot R=R.
]

Por equivariancia:

[
g\cdot F(R)=F(g\cdot R)=F(R).
]

Por tanto:

[
g\in\operatorname{Stab}_G(F(R)).
]

Queda demostrada la inclusión.

Consecuencia

En una dinámica determinista equivariante respecto de un grupo fijo, las simetrías exactas de una configuración no pueden desaparecer durante la evolución.

Los estabilizadores forman una cadena creciente:

[
\operatorname{Stab}_G(R_0)
\subseteq
\operatorname{Stab}_G(R_1)
\subseteq
\operatorname{Stab}_G(R_2)
\subseteq\cdots.
]

Este resultado no se traslada automáticamente a dinámicas estocásticas, actualizaciones asíncronas o cambios de arquitectura.

---

15. Conservación exacta de estabilizadores

Teorema 4

Si F es G-equivariante e inyectivo, entonces:

[
\boxed{
\operatorname{Stab}_G(F(R))

\operatorname{Stab}_G(R)
}
]

para toda configuración admisible.

Demostración

Por el Teorema 3:

[
\operatorname{Stab}_G(R)
\subseteq
\operatorname{Stab}_G(F(R)).
]

Demostraremos la inclusión recíproca.

Sea:

[
g\in\operatorname{Stab}_G(F(R)).
]

Entonces:

[
g\cdot F(R)=F(R).
]

Por equivariancia:

[
F(g\cdot R)=F(R).
]

Como F es inyectivo:

[
g\cdot R=R.
]

Por tanto:

[
g\in\operatorname{Stab}_G(R).
]

Se obtienen ambas inclusiones y, en consecuencia, la igualdad.

Queda demostrado.

---

16. Consecuencias para la evolución finita

Bajo las hipótesis del Teorema 4:

[
\operatorname{Stab}_G(F^t(R))

\operatorname{Stab}_G(R)
]

para todo tiempo entero finito t.

Asimismo:

[
|\operatorname{Orb}_G(F^t(R))|

|\operatorname{Orb}_G(R)|.
]

Por tanto, una dinámica equivariante e inyectiva conserva exactamente:

- El estabilizador de cada configuración.
- La cardinalidad de su órbita.
- Las simetrías exactas respecto del grupo considerado.

Esto no significa que conserve todas las distancias, espectros, invariantes o propiedades geométricas adicionales.

---

17. Aparición de simetrías como criterio de no inyectividad

Corolario 1

Si F es G-equivariante y existe una configuración R tal que:

[
\operatorname{Stab}_G(R)
\subsetneq
\operatorname{Stab}_G(F(R)),
]

entonces F no es inyectivo.

Demostración

Existe una transformación g que satisface:

[
g\cdot R\neq R,
]

pero:

[
g\cdot F(R)=F(R).
]

Por equivariancia:

[
F(g\cdot R)=F(R).
]

Dos estados distintos poseen la misma imagen.

Por tanto, F no es inyectivo.

Queda demostrado.

Limitación

La ausencia de crecimiento de estabilizadores no demuestra inyectividad.

Pueden existir colisiones entre configuraciones pertenecientes a órbitas diferentes sin que aumenten sus estabilizadores.

El criterio es suficiente, pero no necesario.

---

18. Aumento asintótico de simetría

Supongamos que:

[
F^t(R)\longrightarrow R_\infty,
]

y que la acción del grupo es continua.

Si:

[
g\in\operatorname{Stab}_G(R),
]

entonces, por equivariancia:

[
g\cdot F^t(R)=F^t(R).
]

Tomando límites:

[
g\cdot R_\infty=R_\infty.
]

Por tanto:

[
\operatorname{Stab}_G(R)
\subseteq
\operatorname{Stab}G(R\infty).
]

La inclusión puede ser estricta incluso cuando todas las iteraciones finitas son inyectivas.

Ejemplo

Sea (R_*) una configuración invariante bajo G y:

[
F(R)=(1-\alpha)R+\alpha R_*,
]

con 0 < α < 1.

F es equivariante e inyectivo.

Los estabilizadores se conservan durante todas las iteraciones finitas.

Sin embargo:

[
F^t(R)\longrightarrow R_*,
]

y:

[
\operatorname{Stab}G(R*)=G.
]

Una configuración inicialmente asimétrica puede adquirir simetría completa en el límite sin que exista pérdida exacta de inyectividad en tiempo finito.

---

19. Recuperabilidad en el espacio cociente

Sea:

[
\pi:\mathcal D\longrightarrow\mathcal D/G
]

la proyección sobre órbitas.

Si F es G-equivariante, induce:

[
\overline F([R]_G)=[F(R)]_G.
]

Teorema 5

Si F es G-equivariante e inyectivo, entonces el operador inducido (\overline F) es inyectivo.

Demostración

Supongamos:

[
\overline F([R]_G)=\overline F([S]_G).
]

Entonces:

[
[F(R)]_G=[F(S)]_G.
]

Existe g perteneciente a G tal que:

[
F(R)=g\cdot F(S).
]

Por equivariancia:

[
F(R)=F(g\cdot S).
]

Por inyectividad:

[
R=g\cdot S.
]

Por tanto:

[
[R]_G=[S]_G.
]

Queda demostrado.

---

20. Criterio completo de inyectividad mediante órbitas

Teorema 6

Para un operador G-equivariante, las siguientes condiciones conjuntas son equivalentes a la inyectividad de F:

1. El operador inducido (\overline F) es inyectivo.
2. Los estabilizadores se conservan exactamente para todas las configuraciones.

Demostración

La necesidad se obtiene de los Teoremas 4 y 5.

Demostraremos la suficiencia.

Supongamos:

[
F(R)=F(S).
]

Entonces:

[
\overline F([R]_G)=\overline F([S]_G).
]

Por inyectividad del operador inducido:

[
[R]_G=[S]_G.
]

Existe g perteneciente a G tal que:

[
S=g\cdot R.
]

Por equivariancia:

[
F(S)=g\cdot F(R).
]

Como F(S)=F(R):

[
g\in\operatorname{Stab}_G(F(R)).
]

Por conservación exacta de estabilizadores:

[
g\in\operatorname{Stab}_G(R).
]

En consecuencia:

[
S=g\cdot R=R.
]

Por tanto, F es inyectivo.

Queda demostrado.

Interpretación

La pérdida de inyectividad de un operador equivariante puede producirse mediante dos mecanismos:

- Identificación de estados diferentes dentro de una misma órbita.
- Identificación de configuraciones pertenecientes a órbitas distintas.

El primero implica crecimiento de algún estabilizador.

El segundo implica pérdida de inyectividad en el espacio cociente.

---

21. Recuperabilidad mediante invariantes

Sea:

[
I:\mathcal D\longrightarrow\mathbb R^k
]

una familia de invariantes bajo G.

Se cumple:

[
I(g\cdot R)=I(R).
]

La familia es completa respecto de G cuando:

[
I(R)=I(S)
\Longleftrightarrow
[R]_G=[S]_G.
]

Una familia completa permite identificar unívocamente la clase de equivalencia.

No permite necesariamente reconstruir el representante original.

Una familia incompleta puede identificar configuraciones pertenecientes a órbitas diferentes.

Por tanto, deben distinguirse:

- Invariancia.
- Capacidad discriminante.
- Completitud.
- Estabilidad de reconstrucción.

---

22. Aplicación a los equilibrios de una arista

Para N = 24 existen:

[
\binom{24}{2}=276
]

configuraciones de masa fija concentrada en una sola arista.

Bajo las acciones previamente especificadas:

Grupo| Clases
Permutaciones ordinarias| 1
Grupo residual Z2| 144
Grupo rotacional Z4| 72
Grupo estratificado (S4)^6| 21

La clasificación mediante permutaciones ordinarias es combinatoria y no implica equivariancia del operador ponderado respecto de todas ellas.

Todos los equilibrios de una arista poseen el mismo espectro:

[
{C_0,-C_0,0^{(22)}}.
]

Por tanto, los invariantes espectrales no permiten recuperar sus clases rotacionales o estratificadas.

---

23. Recuperación estratificada

Sea:

[
W=\operatorname{diag}(g_1,\ldots,g_{24}),
]

donde los pesos son positivos y constantes dentro de cada estrato.

Consideramos:

[
I_1(R)=\operatorname{tr}(WR^2),
]

[
I_2(R)=\operatorname{tr}(W^2R^2).
]

Para una configuración de una sola arista entre los nodos a y b:

[
I_1=C_0^2(g_a+g_b),
]

[
I_2=C_0^2(g_a^2+g_b^2).
]

Definimos:

[
A=\frac{I_1}{C_0^2},
\qquad
B=\frac{I_2}{C_0^2}.
]

Los pesos se recuperan como:

[
g_{\pm}=
\frac{A\pm\sqrt{2B-A^2}}2.
]

Cuando los seis pesos estratificados son distintos y la masa es conocida, esta familia identifica completamente las 21 clases estratificadas de equilibrios de una sola arista.

La reconstrucción está limitada al par no ordenado de pesos.

No recupera necesariamente:

- Los nodos individuales.
- La orientación angular.
- La clase rotacional.
- La configuración inicial de una trayectoria.
- La estructura completa de una matriz con soporte arbitrario.

---

24. Degeneración y sensibilidad

Definimos el discriminante:

[
\Delta=2B-A^2.
]

Entonces:

[
\Delta=(g_a-g_b)^2.
]

Si Δ = 0, ambos pesos coinciden.

Si Δ > 0, los pesos son diferentes.

Si Δ < 0, los datos no corresponden exactamente a un par de pesos reales.

Para obtener dos pesos estrictamente positivos se requiere:

[
A>0,
]

[
\frac{A^2}{2}\leq B<A^2.
]

Además, los pesos reconstruidos deben pertenecer al conjunto permitido por la arquitectura.

La operación de raíz cuadrada introduce sensibilidad cerca de Δ = 0.

Por tanto, la reconstrucción exacta no garantiza estabilidad uniforme frente a perturbaciones.

Los errores de redondeo deberán distinguirse de las incompatibilidades matemáticas reales.

---

25. Recuperabilidad del operador relacional

Para el operador de referencia:

[
\Phi(R)=(1-\mu)R+\mu H(R),
]

donde:

[
H(R)=\mathcal N(M(R)),
]

se plantea el problema de determinar su inyectividad global.

La presencia del término residual:

[
(1-\mu)R
]

no garantiza por sí sola dicha propiedad.

Teorema 7 — Condición suficiente

Supongamos que H es L-Lipschitz sobre el dominio considerado.

Entonces:

[
|\Phi(R)-\Phi(S)|
\geq
(1-\mu-\mu L)|R-S|.
]

Demostración

Por la desigualdad triangular inversa:

[
\begin{aligned}
|\Phi(R)-\Phi(S)|
&\geq
(1-\mu)|R-S|\
&\quad-\mu|H(R)-H(S)|\
&\geq
(1-\mu-\mu L)|R-S|.
\end{aligned}
]

Queda demostrada la desigualdad.

Si:

[
1-\mu-\mu L>0,
]

equivalentemente:

[
\boxed{
\mu<\frac1{1+L}
}
]

entonces Φ es inyectivo.

Además, su inversa sobre la imagen satisface:

[
|\Phi^{-1}(U)-\Phi^{-1}(V)|
\leq
\frac{|U-V|}{1-\mu-\mu L}.
]

Alcance

La condición es suficiente, no necesaria.

Su aplicación al operador relacional concreto exige demostrar previamente una cota de Lipschitz válida para H sobre el dominio considerado.

No se afirma que dicha cota exista globalmente.

---

26. Dependencia del autovector dominante

El operador relacional estudiado utiliza un autovector dominante normalizado.

La estabilidad de esta construcción depende, entre otros factores, de la separación espectral entre el mayor autovalor algebraico y el siguiente.

Cuando dicha separación disminuye, la sensibilidad del autovector puede aumentar.

Si el mayor autovalor deja de ser simple, la selección del autovector puede dejar de ser única.

Por tanto, cualquier demostración de invertibilidad o regularidad global deberá especificar:

- Dominio de definición.
- Simplicidad del autovalor dominante.
- Separación espectral.
- Normalización.
- Tratamiento de estados de frontera.
- Regla de selección en casos degenerados, si procede.

No deberá suponerse regularidad global sin verificar estas condiciones.

---

27. Caso de actualización completa

Consideremos:

[
\mu=1.
]

El operador queda reducido a:

[
\Phi(R)=\mathcal N(M(R)).
]

Para la formulación estudiada:

[
M_{ij}(R)=
(g_i g_j v_i(R)v_j(R))^\gamma,
]

para i distinto de j.

La imagen depende del autovector dominante normalizado y de los pesos fijados.

Teorema 8

Para N ≥ 4, este operador no es inyectivo sobre el dominio completo de matrices estrictamente positivas fuera de la diagonal, simétricas, de diagonal nula y masa fija.

Demostración

Sea R₀ la matriz con todas las aristas iguales:

[
(R_0)_{ij}=
\frac{C_0}{\binom N2},
\qquad i\neq j.
]

Todas sus sumas por fila son iguales.

Su autovector dominante normalizado es:

[
v_0=\frac1{\sqrt N}(1,\ldots,1)^T.
]

Construimos una matriz simétrica E, de diagonal nula, mediante:

[
E_{12}=E_{34}=1,
]

[
E_{13}=E_{24}=-1,
]

junto con las entradas simétricas correspondientes.

Las demás entradas son cero.

Todas las sumas por fila de E son nulas.

Por tanto:

[
Ev_0=0.
]

Además:

[
\sum_{i<j}E_{ij}=0.
]

Definimos:

[
R_\varepsilon=R_0+\varepsilon E.
]

Para ε suficientemente pequeño y no nulo, (R_\varepsilon) conserva:

- Simetría.
- Diagonal nula.
- Positividad estricta de las aristas.
- Masa fija.
- Sumas por fila.

Por positividad e irreducibilidad, su autovector dominante normalizado continúa siendo (v_0).

En consecuencia:

[
v(R_\varepsilon)=v(R_0).
]

Como los pesos y γ permanecen fijos:

[
M(R_\varepsilon)=M(R_0).
]

Por tanto:

[
\Phi(R_\varepsilon)=\Phi(R_0).
]

Sin embargo:

[
R_\varepsilon\neq R_0.
]

El operador no es inyectivo.

Queda demostrado.

Alcance

Este resultado corresponde al operador matricial de referencia con actualización completa.

No se traslada automáticamente al operador híbrido ni a 44A o 44B.

---

28. Dimensión de la información conservada

La representación diádica de una matriz de 24 nodos y masa fija posee 275 grados de libertad continuos.

Un autovector normalizado de 24 componentes posee como máximo 23 grados de libertad continuos.

Para μ = 1, el operador de referencia factoriza a través de dicho autovector:

[
R\longmapsto v(R)\longmapsto\Phi(R).
]

En consecuencia, la actualización completa utiliza una representación intermedia de dimensión considerablemente inferior a la del dominio matricial.

Esta observación es coherente con la pérdida de inyectividad demostrada en el Teorema 8.

La diferencia dimensional no deberá interpretarse directamente como una cantidad de bits, entropía termodinámica o pérdida física de información.

---

29. Aplicación a los atractores

Sea:

[
A(R)=\lim_{t\to\infty}F^t(R)
]

cuando el límite existe.

Si dos estados iniciales diferentes convergen al mismo equilibrio:

[
A(R)=A(S),
\qquad R\neq S,
]

la aplicación atractora no es inyectiva.

Si F es equivariante y la acción de G es continua:

[
A(g\cdot R)=g\cdot A(R).
]

Por tanto, la aplicación atractora induce una aplicación sobre el espacio cociente de su dominio de convergencia.

La recuperación de la clase inicial a partir de la clase final requiere estudiar independientemente la inyectividad de esta aplicación inducida.

La existencia de múltiples atractores no garantiza recuperabilidad de los estados iniciales.

---

30. Protocolo de verificación computacional

Se propone una auditoría independiente con las siguientes comprobaciones:

Prueba| Objetivo
T01| Reconstrucción diádica exacta.
T02| Recuperación mediante transformaciones conocidas.
T03| Inversión de iteraciones afines.
T04| Amplificación de errores de reconstrucción.
T05| Conservación de estabilizadores bajo operadores inyectivos.
T06| Monotonía de estabilizadores bajo equivariancia.
T07| Detección de colisiones por aumento de simetría.
T08| Aumento asintótico de simetría.
T09| Inyectividad inducida sobre órbitas en ejemplos controlados.
T10| Colisiones entre órbitas distintas.
T11| Reconstrucción mediante invariantes estratificados.
T12| Sensibilidad cerca de pesos degenerados.
T13| Condición suficiente de inyectividad para operadores Lipschitz.
T14| Colisión exacta construida para μ = 1.
T15| Conservación de masa y positividad en el contraejemplo.
T16| Coincidencia de autovectores dominantes.
T17| Controles negativos con ruptura de equivariancia.
T18| Distinción entre pérdida finita y asintótica de información.

Las pruebas deberán registrar parámetros, tolerancias, versiones y resultados observados.

Los contrastes finitos no sustituirán las demostraciones universales.

Estas pruebas se proponen como trabajo futuro y no se presentan como ejecutadas en esta versión.

---

31. Resultados demostrados

Bajo las hipótesis especificadas:

- Reconstrucción exacta mediante relaciones diádicas indexadas.
- Inyectividad de las iteraciones finitas de operadores inyectivos.
- Recuperabilidad algebraica del operador afín.
- Amplificación de errores en su inversión.
- Posibilidad de pérdida asintótica de información.
- Monotonía de estabilizadores bajo equivariancia.
- Conservación exacta de estabilizadores bajo equivariancia e inyectividad.
- Crecimiento de estabilizadores como criterio suficiente de no inyectividad.
- Inyectividad del operador inducido sobre el espacio cociente.
- Caracterización conjunta de la inyectividad mediante órbitas y estabilizadores.
- Recuperación de clases estratificadas de una sola arista.
- Condición suficiente de inyectividad para operadores residuales Lipschitz.
- No inyectividad del operador relacional de referencia para μ = 1 y N ≥ 4.

---

32. Problemas abiertos

Permanecen pendientes:

1. Determinación del dominio canónico exacto.
2. Identificación del grupo dinámico máximo de la implementación original.
3. Inyectividad global para 0 < μ < 1.
4. Cotas de Lipschitz del operador de construcción relacional.
5. Estabilidad de la inversión.
6. Caracterización de las fibras del operador para μ = 1.
7. Reconstrucción mediante invariantes de soportes superiores.
8. Clasificación de las pérdidas de información entre órbitas.
9. Recuperabilidad de trayectorias del operador híbrido.
10. Equivariancia e invertibilidad de 44A y 44B.
11. Auditoría computacional independiente de los resultados de este documento.
12. Correspondencia con la dinámica fundamental de la TRCG.

---

33. Gobernanza

Se mantienen:

- Nivel II retenido.
- Nivel III abierto.
- λ reservado exclusivamente al 4º Factor.
- Versiones 1.6 y 1.7 aisladas.
- Campaña experimental del Episodio 44 congelada.
- Sin reescalados post hoc.
- Sin equivalencias automáticas.
- Sin ascensos automáticos.
- Independencia de los modelos estudiados.
- Conservación de resultados negativos.
- Trazabilidad matemática y computacional.

---

34. Conclusión

La información relacional puede conservarse exactamente, recuperarse parcialmente o perderse dependiendo del operador, el dominio, la representación y el tiempo de evolución.

La equivariancia permite relacionar la recuperabilidad con la estructura de las órbitas y los estabilizadores.

La conservación exacta de estabilizadores y la inyectividad del operador inducido caracterizan conjuntamente la inyectividad de una dinámica equivariante.

Para el operador relacional de referencia, la actualización completa mediante el autovector dominante introduce una pérdida demostrable de inyectividad.

La determinación de los regímenes intermedios de actualización constituye una cuestión abierta de investigación.

La convergencia hacia un equilibrio no implica la conservación de la información inicial.

La equivalencia estructural no implica recuperabilidad dinámica.

La conservación se demuestra. La pérdida se caracteriza. La reconstrucción se verifica.

---

TRCG — Código Viajer — Pirámide-Parábola

Nivel II retenido · Nivel III abierto · λ reservado al 4º Factor.

FIN DEL DOCUMENTO
