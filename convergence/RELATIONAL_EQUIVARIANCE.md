RELATIONAL EQUIVARIANCE

Código Viajer — Pirámide-Parábola — TRCG

Versión: 0.1.0
Estado: Formalización matemática condicionada
Ámbito: Investigación de convergencia estructural y dinámica.

1. Objetivo

Establecer las condiciones matemáticas bajo las cuales el operador dinámico relacional conserva las simetrías de Pirámide-Parábola.

Distinguir entre simetría geométrica, simetría combinatoria y equivarianza dinámica.

2. Espacio relacional

Sea V un conjunto de 24 nodos distribuidos en cuatro sectores y seis estratos.

Definimos el espacio relacional:

[
\mathcal S={R\in\mathbb R^{24\times24}:R^T=R,\ \operatorname{diag}(R)=0}.
]

Su dimensión es:

[
\dim\mathcal S=\binom{24}{2}=276.
]

El dominio dinámico considerado estará constituido por matrices no negativas, con masa relacional positiva y bajo las condiciones necesarias para garantizar la existencia y unicidad del autovector dominante utilizado por el operador.

3. Acción de las simetrías

Para una matriz de permutación P, definimos:

[
\rho_P(R)=PRP^T.
]

Un operador dinámico F es equivariante respecto a P cuando:

[
F(PRP^T)=PF(R)P^T.
]

La equivarianza no implica que todas las configuraciones sean invariantes.

Implica que transformar una configuración antes de evolucionarla produce el mismo resultado que evolucionarla y aplicar posteriormente la transformación.

4. Hipótesis del operador

Consideramos operadores de la forma:

[
F(R)=(1-\alpha)R+\alpha N(B(R)).
]

Donde:

- (0\leq\alpha\leq1).
- B representa la construcción relacional.
- N representa la normalización de masa.
- La construcción B utiliza un autovector dominante positivo y un conjunto de pesos nodales.
- Los pesos permanecen constantes dentro de cada estrato.

Esta formulación constituye una clase matemática de operadores. Su identificación exacta con una implementación canónica requiere verificar el código y la versión correspondiente.

5. Teorema de equivarianza

Si R es simétrica, no negativa e irreducible, el teorema de Perron–Frobenius garantiza la unicidad de su autovector dominante positivo bajo una normalización fijada.

Por tanto:

[
v(PRP^T)=Pv(R).
]

Si los pesos nodales son invariantes bajo P y la construcción B utiliza operaciones compatibles con permutaciones, entonces:

[
B(PRP^T)=PB(R)P^T.
]

La normalización por masa relacional también conmuta con P.

En consecuencia:

[
F(PRP^T)=PF(R)P^T.
]

Queda demostrada la equivarianza bajo las hipótesis declaradas.

6. Conservación de los espacios invariantes

Sea G un grupo de permutaciones admisibles.

Definimos:

[
\operatorname{Fix}(G)=
{R\in\mathcal S:\rho_P(R)=R,\ \forall P\in G}.
]

Si F es equivariante respecto a G:

[
F(\operatorname{Fix}(G))
\subseteq\operatorname{Fix}(G).
]

La demostración se obtiene directamente de:

[
\rho_P(F(R))=F(\rho_P(R))=F(R).
]

Por inducción, toda trayectoria inicialmente invariante conserva dicha propiedad mientras el operador permanezca bien definido.

7. Simetría rotacional

Para la acción cíclica de orden cuatro sobre cuatro sectores y seis estratos:

[
G_{\mathrm{rot}}\cong\mathbb Z_4.
]

Las 276 aristas se distribuyen en:

- 6 órbitas de tamaño 2.
- 66 órbitas de tamaño 4.

Por tanto:

[
\dim\operatorname{Fix}(G_{\mathrm{rot}})=72.
]

Al imponer una masa relacional fija y positiva, la dimensión afín correspondiente es 71.

8. Simetría estratificada

Si únicamente se preserva la identidad de los estratos:

[
G_{\mathrm{est}}\cong(S_4)^6.
]

Su cardinalidad es:

[
|G_{\mathrm{est}}|=191102976.
]

Las aristas se clasifican en seis clases internas y quince clases entre estratos.

Por tanto:

[
\dim\operatorname{Fix}(G_{\mathrm{est}})=21.
]

Con masa fija, la dimensión afín correspondiente es 20.

Se establece la inclusión:

[
\operatorname{Fix}(G_{\mathrm{est}})
\subseteq
\operatorname{Fix}(G_{\mathrm{rot}})
\subseteq\mathcal S.
]

9. Descomposición relacional

Bajo la descomposición estándar del espacio de aristas en modos transversales, longitudinales y de masa:

Espacio| Transversal| Longitudinal| Masa| Total
General| 252| 23| 1| 276
Rotacionalmente invariante| 66| 5| 1| 72
Estratificado invariante| 15| 5| 1| 21

Esta clasificación dimensional no implica que los bloques sean necesariamente autoespacios del jacobiano anisótropo.

10. Límites de la demostración

La equivarianza no demuestra:

- Convergencia global.
- Estabilidad de todos los equilibrios.
- Recuperación de información perdida.
- Identificabilidad de la geometría completa.
- Equivarianza efectiva de 44A y 44B.
- Correspondencia física con la TRCG.

La conservación de un espacio invariante tampoco implica que dicho espacio sea atractor.

11. Protocolo de verificación

La auditoría computacional deberá evaluar:

[
\varepsilon_P(R)=
\frac{|F(PRP^T)-PF(R)P^T|_F}
{\max(|F(R)|_F,\epsilon)}.
]

Se utilizarán configuraciones positivas, semillas reproducibles, permutaciones rotacionales y generadores de las permutaciones estratificadas.

Se incorporarán controles negativos que rompan deliberadamente la simetría de los pesos.

Las tolerancias se fijarán antes de ejecutar las pruebas.

12. Gobernanza

- Nivel II retenido.
- Nivel III abierto.
- λ reservado al 4º Factor.
- Versiones 1.6 y 1.7 aisladas.
- Sin ascensos automáticos.
- Sin reescalados post hoc.
- Campaña del Episodio 44 congelada.

13. Conclusión

La equivarianza constituye un puente matemático entre la estructura relacional y su dinámica.

La correspondencia con la arquitectura canónica completa y con la TRCG deberá establecerse mediante demostraciones y verificaciones independientes.
