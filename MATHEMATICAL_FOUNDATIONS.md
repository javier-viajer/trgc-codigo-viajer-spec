MATHEMATICAL_FOUNDATIONS.md
Fundamentos matemáticos y estado de validación de TRCG / Código Viajer
Estado del documento: marco de formalización y revisión
Versión de referencia: repositorio v1.7
Fecha de elaboración: 24 de noviembre de 2026
Advertencia epistemológica: este documento distingue definiciones, resultados declarados en la documentación del repositorio, consecuencias matemáticas condicionadas e hipótesis pendientes. No afirma que la TRCG sea una teoría física completa ni que las simulaciones citadas hayan sido reproducidas de forma independiente durante la elaboración de este documento.

1. Objetivo y alcance
Este documento reúne las estructuras matemáticas descritas en el repositorio y especifica qué debe demostrarse para que sus afirmaciones sean verificables.
Se consideran tres objetos distintos:
El estado operativo 4D de Código Viajer.
El núcleo estructural 24D asociado a 264 triples y simetría \(\mathbb Z_4\).
La dinámica experimental 47D de v1.7.
No se presupone que estos objetos sean isomorfos, equivalentes o transformaciones unos de otros.
2. Notación y convenciones
Símbolo
Significado en este documento
\(\mathbf X\)
Estado operativo 4D
L,S,I,B
Componentes del estado operativo
T
Estado binario del núcleo de 24 nodos
J24
Matriz estructural de dimensión 24
V(T)
Función de energía/potencial declarada para el modelo discreto
ha(T)
Campo local o función de activación del nodo a
\(\theta_{\mathrm{on}}\)
Umbral de activación
\(\theta_{\mathrm{off}}\)
Umbral de desactivación
a
Término local de potencial/sesgo
z
Estado experimental de dimensión 47
J47
Operador/matriz dinámica de dimensión 47
P
Proyector al subespacio transversal al modo neutro
(A)
Radio espectral de una matriz A
|A|2
Norma espectral inducida por la norma euclídea

La notación  queda reservada al 4.º Factor, de acuerdo con STATUS.md. En este documento se evita usarla para autovalores genéricos; se utiliza  cuando sea necesario.
Las expresiones deben leerse sobre \(\mathbb R\) o \(\mathbb C\) según el espacio correspondiente. La elección debe quedar fijada en cada implementación y prueba.
3. Estado operativo de Código Viajer: espacio 4D
El repositorio define:
[ \mathbf X=(L,S,I,B)\in[0,1]^4. ]
Las etiquetas declaradas son:
L: Life Preservation.
S: Entropy.
I: Node Integrity.
B: Resource.
Esta definición establece un espacio de estados normalizado. Por sí sola no define la semántica completa de las variables ni el algoritmo de decisión.
Para obtener una especificación matemática ejecutable deben definirse:
Qué representa exactamente cada coordenada.
Qué extremo del intervalo es favorable o desfavorable.
Cómo se calculan las coordenadas a partir de observaciones.
Si las coordenadas son independientes o están acopladas.
Qué trayectorias son admisibles.
Qué función o conjunto de reglas transforma el estado en una decisión.
Qué umbrales, márgenes y precedencias se aplican.
En términos generales, el decisor podría escribirse como:
[ D:\mathcal X_{\mathrm{adm}}\longrightarrow {\mathrm{ALLOW},\mathrm{THROTTLE},\mathrm{REJECT}}, ]
donde \(\mathcal X_{\mathrm{adm}}\) debe definirse. Esta expresión es una formalización del contrato deseado, no una afirmación de que el código actual implemente exactamente esa función.
3.1. Propiedades que deben probarse
Totalidad: toda entrada admitida produce una decisión o un error definido.
Determinismo: misma entrada, configuración y versión producen la misma salida, si ese es el requisito.
Robustez numérica: entradas no finitas o fuera de rango se tratan según política explícita.
Monotonicidad, si se pretende: cambios en una coordenada producen cambios de decisión coherentes con su semántica. No debe asumirse sin definir previamente la orientación de cada variable.
Trazabilidad: toda decisión puede reconstruirse a partir de entrada, parámetros y versión.
4. Núcleo estructural 24D
4.1. Espacio de estados
La documentación describe un núcleo de 24 nodos:
[ T=(T_1,\ldots,T_{24})\in{0,1}^{24}. ]
La organización se presenta como 46. La estructura relacional se deriva, según STATUS.md, de una colección de 264 triples y de su 2-sección.
Para evitar ambigüedades, debe incluirse en el repositorio una definición explícita de:
Conjunto de vértices V.
Familia de triples \(\mathcal R\subseteq \binom{V}{3}\), si los triples son no ordenados y sin repetición.
Definición de 2-sección: dos vértices distintos se conectan cuando pertenecen conjuntamente a algún triple.
Tratamiento de multiplicidades, pesos y autoaristas.
Orden canónico de los 24 vértices.
El número 264 identifica la cantidad de triples declarada. No implica por sí solo un número concreto de aristas sin aplicar la regla de construcción y eliminar o conservar multiplicidades de manera definida.
4.2. Matriz estructural
Se declara una matriz:
[ J_{24}\in\mathbb R^{24\times24}. ]
STATUS.md informa de las siguientes comprobaciones numéricas:
Simetría \(J_{24}=J_{24}^{\mathsf T}\).
Diagonal nula.
Traza nula.
Equivarianza respecto de \(\mathbb Z_4\).
Descomposición en cuatro bloques de tamaño 66.
Reconstrucción espectral entre la matriz completa y sus bloques.
Estos valores deben tratarse como resultados reportados por el proyecto hasta que se repita el procedimiento desde los datos fuente y se publiquen los scripts, versiones, tolerancias y artefactos exactos.
4.3. Acción de \(\mathbb Z_4\) y descomposición modal
Sea F4 la matriz de Fourier discreta de orden cuatro, con convención de normalización documentada. La transformación indicada en STATUS.md es:
[ U=F_4\otimes I_6. ]
La matriz transformada se expresa como:
[ \widehat J=UJU^{-1}. ]
Si la acción de \(\mathbb Z_4\) está correctamente representada y J conmuta con el operador de simetría, la transformación permite descomponer el espacio en subespacios invariantes asociados a los cuatro caracteres de \(\mathbb Z_4\).
La forma por bloques debe demostrarse a partir de la matriz de acción y de la relación de conmutación. No basta con observar que una matriz transformada parece tener bloques pequeños.
Para una matriz real simétrica, los autovalores son reales. La hermiticidad de los bloques complejos transformados y la relación de conjugación entre modos deben comprobarse con tolerancias numéricas declaradas.
Pendiente de especificación: publicar la definición exacta de F4, el orden de los nodos, la matriz de acción de \(\mathbb Z_4\), la convención de Fourier y la fórmula de reconstrucción.
4.4. Positividad: tres conceptos diferentes
No deben confundirse:
Entradas o pesos no negativos: Jij0.
Semidefinición positiva: \(x^{\mathsf T}Jx\geq0\) para todo x.
Positividad de una función barrera o de un potencial en un dominio admisible.
Una matriz real simétrica, semidefinida positiva y con traza cero debe ser la matriz nula, porque todos sus autovalores son no negativos y su suma es cero. Por tanto, si J es simétrica, tiene diagonal nula y es no nula, no puede ser semidefinida positiva.
Esta observación debe conservarse al formular cualquier afirmación de positividad sobre J24. La no negatividad entrada a entrada no implica semidefinición positiva.
5. Dinámica binaria asíncrona y función V(T)
STATUS.md describe una actualización asíncrona secuencial, un nodo por paso, con dos transiciones posibles:
[ 0\rightarrow1 \quad\text{si}\quad h_a(T)\geq\theta_{\mathrm{on}}, ]
[ 1\rightarrow0 \quad\text{si}\quad h_a(T)\leq\theta_{\mathrm{off}}. ]
La banda de histéresis se declara como:
[ \theta_{\mathrm{off}}<\theta_{\mathrm{on}}. ]
Para un cambio en el nodo a, se registran las expresiones:
[ \Delta\tilde V_{0\to1}(T;a) =-h_a(T)+\Delta\Phi_a, ]
[ \Delta\tilde V_{1\to0}(T;a) =h_a(T)-\Delta\Phi_a. ]
Si no hay cambio:
[ \Delta T_a=0 \quad\Longrightarrow\quad \Delta\tilde V=0. ]
5.1. Condiciones suficientes para no aumentar el potencial
Para la transición 01, si:
[ h_a(T)\geq\theta_{\mathrm{on}} \quad\text{y}\quad \Delta\Phi_a\leq\theta_{\mathrm{on}}, ]
entonces:
[ \Delta\tilde V_{0\to1} =-h_a(T)+\Delta\Phi_a\leq0. ]
Para la transición 10, si:
[ h_a(T)\leq\theta_{\mathrm{off}} \quad\text{y}\quad \Delta\Phi_a\geq\theta_{\mathrm{off}}, ]
entonces:
[ \Delta\tilde V_{1\to0} =h_a(T)-\Delta\Phi_a\leq0. ]
Una condición suficiente común es:
[ \theta_{\mathrm{off}} \leq\Delta\Phi_a \leq\theta_{\mathrm{on}}, ]
junto con las reglas de transición anteriores.
Estas desigualdades justifican que cada actualización permitida no aumente V, siempre que las expresiones de variación correspondan realmente a la función definida y a la regla de actualización implementada.
5.2. Qué se necesita para afirmar convergencia
El espacio {0,1}24 es finito. Si V es no creciente, la secuencia de valores de potencial no puede disminuir estrictamente de forma indefinida si el potencial está definido sobre ese conjunto finito.
Sin embargo, la no-incrementabilidad por sí sola no excluye ciclos: pueden existir transiciones entre estados distintos con el mismo valor de V.
Para concluir que la dinámica termina en un estado retenido se necesita, además, una condición que excluya ciclos, por ejemplo:
Descenso estricto de V en toda transición de estado no trivial; o
Una regla de desempate/orden que impida ciclos dentro de niveles de igual potencial; o
Una demostración independiente de ausencia de ciclos para la dinámica concreta.
Por tanto, la afirmación de convergencia debe quedar condicionada a una de esas hipótesis y a su comprobación.
5.3. Información pendiente
La documentación actual deja sin completar parámetros y resultados del régimen no vacío, entre ellos ba, \(\theta_{\mathrm{off}}\), \(\theta_{\mathrm{on}}\), a, ocupaciones finales, clasificación de estados, violaciones de monotonía y puntos fijos.
No deben sustituirse esos campos por valores estimados. Deben completarse desde una corrida reproducible y acompañarse de configuración y artefactos.
6. Arquitectura dinámica experimental 47D
La auditoría de v1.7 describe:
[ z=(m_{24},s_{22},\theta)\in\mathbb C^{47}, ]
con:
[ 24+22+1=47. ]
y una matriz:
[ J_{47}\in\mathbb C^{47\times47}. ]
Se informa de un modo neutro asociado a , con autovalor:
[ \mu_{\mathrm{neutro}}=1, ]
y de un radio espectral no trivial reportado:
[ \rho_{\mathrm{ntriv}}=0.974885. ]
La auditoría también informa de:
[ |J_{47}|_2\approx1.002126 ]
y de una norma de la matriz proyectada:
[ |P_\perp J_{47}P_\perp|_2\approx0.990486. ]
Estos números son valores reportados por la auditoría, no resultados reproducidos por este documento.
6.1. Modo neutro y estabilidad transversal
Un autovalor igual a uno puede representar una dirección neutra, por ejemplo una simetría de fase, pero esa interpretación requiere demostrar que el vector asociado corresponde efectivamente a una simetría o familia de soluciones.
Para un vector unitario v0 que represente la dirección neutra, se define:
[ P_\perp=I-v_0v_0^*. ]
La matriz proyectada que aparece en la auditoría es:
[ J_\perp=P_\perp J_{47}P_\perp. ]
Si se demuestra que el subespacio transversal es invariante y que el operador lineal restringido a él tiene norma inducida estrictamente menor que uno, entonces las perturbaciones transversales se contraen en el modelo lineal considerado.
La condición relevante es:
[ |J_\perp|_2<1. ]
No obstante, deben distinguirse:
La estabilidad del sistema linealizado.
La estabilidad local del sistema no lineal original.
La estabilidad global.
La estabilidad transversal respecto de una órbita o simetría.
Una norma proyectada menor que uno no demuestra automáticamente estabilidad global ni estabilidad no lineal. Se necesita justificar la linealización, el dominio de validez, la invariancia del subespacio y el control de términos de orden superior.
6.2. Radio espectral y norma espectral
Para cualquier matriz cuadrada:
[ \rho(A)\leq|A|_2. ]
La norma espectral proporciona una cota superior del radio espectral. Una cota \(\|A\|_2<1\) implica (A)<1 y contracción en la norma euclídea para la aplicación lineal considerada.
En cambio, (A)<1 no implica necesariamente \(\|A\|_2<1\) en una matriz no normal.
La auditoría informa de una norma completa de J47 ligeramente superior a uno y de una norma proyectada inferior a uno. Es correcto no utilizar la norma de la matriz completa como certificado de contracción transversal cuando incluye una dirección neutra; pero la validez del certificado proyectado depende de las condiciones de invariancia y proyección indicadas arriba.
6.3. Resultados experimentales que deben conservar su contexto
La auditoría reporta, entre otros:
\(\rho_{\mathrm{ntriv}}\approx0.974885\).
\(\|J_{47}\|_2\approx1.002126\).
\(\|P_\perp J_{47}P_\perp\|_2\approx0.990486\).
\(\|L_{22}\|_2\approx0.990000\).
Cotas de Gershgorin para L22 de aproximadamente 1.039248.
Un ensayo de ventana larga de 9.600 pasos.
Un ensemble de 11 corridas.
Estos datos deben vincularse a los archivos JSON, scripts, semillas, configuración, definición de matrices y tolerancias concretas. Una salida EXIT=0 acredita que el proceso terminó según el código de salida; no acredita por sí sola la validez matemática de todas las interpretaciones del resultado.
7. Sobre la relación entre 24D y 47D
La coincidencia de un bloque de 24 componentes en ambas descripciones no basta para concluir que se trata del mismo objeto matemático.
Para establecer esa correspondencia se debe demostrar que:
El orden de los 24 nodos coincide.
Las variables tienen la misma definición.
Las matrices o reglas de actualización coinciden cuando se restringen al bloque correspondiente.
Las unidades, pesos y normalizaciones son compatibles.
Los acoplamientos con las 22 variables adicionales y con  están especificados.
La relación se verifica mediante pruebas automatizadas.
Hasta entonces, J_24 y mass_24 deben tratarse como objetos relacionados por investigar, no como objetos idénticos.
8. Candidato (R) y frontera epistemológica
STATUS.md presenta un candidato:
[ \lambda(R)= 1- \frac{ |P_{\mathbb Z_4}RP_{\mathbb Z_4}^{\mathsf T}-R|F }{ |P{\mathbb Z_4}RP_{\mathbb Z_4}^{\mathsf T}|_F+ |R|_F+\varepsilon }. ]
El símbolo  está reservado al 4.º Factor y el propio estado del proyecto indica que su formulación está sujeta a revisión.
Por tanto, esta expresión debe considerarse candidata, no una magnitud validada ni un invariante demostrado.
Antes de aceptarla se deben especificar:
Dominio de R.
Definición y propiedades de \(P_{\mathbb Z_4}\).
Condiciones sobre , incluido que el denominador no se anule.
Rango posible de la expresión.
Casos de igualdad y extremos.
Comportamiento ante escalado de R.
Invariancia bajo cambios de base pertinentes.
Los seis requisitos formales a los que se refiere STATUS.
Interpretación y utilidad operacional, si la tiene.
No debe presentarse como un resultado físico ni como una demostración de emergencia.
9. Niveles de evidencia
Para mantener una frontera epistemológica clara, cada afirmación del proyecto debe etiquetarse con una categoría:
Categoría
Qué significa
Evidencia mínima
Definición
Objeto fijado por convenio
Especificación inequívoca
Identidad algebraica
Consecuencia exacta de las definiciones
Derivación verificable
Teorema
Afirmación demostrada bajo hipótesis
Prueba completa
Resultado numérico
Valor calculado en una ejecución
Código, datos, configuración y salida
Resultado reproducible
Resultado repetido independientemente
Procedimiento y artefactos reproducibles
Hipótesis
Proposición pendiente de prueba
Enunciado y plan de contraste
Conjetura
Patrón sugerido por evidencia parcial
Evidencia exploratoria y límites
No validado
No hay evidencia suficiente
Registro explícito de la carencia

La etiqueta de nivel del proyecto no sustituye esta clasificación por afirmación.
10. Protocolo mínimo de validación matemática y numérica
Cada experimento debe conservar:
Identificador único.
Versión y commit del código.
Configuración completa.
Semilla aleatoria.
Datos de entrada o generador de datos.
Definición y orden de variables.
Parámetros y tolerancias.
Método numérico y versión de dependencias.
Resultado bruto.
Script de verificación.
Criterio de aceptación.
Limitaciones conocidas.
Los tests deben incluir:
Casos nominales.
Casos límite.
Entradas inválidas y no finitas.
Sensibilidad a parámetros.
Sensibilidad a semillas.
Perturbaciones estructurales.
Verificación de invariantes.
Pruebas de regresión entre versiones.
Reproducción de los resultados incluidos en la auditoría.
11. Registro de cuestiones abiertas
ID
Cuestión
Estado
MAT-01
Semántica y reglas completas del decisor 4D
Pendiente de especificación
MAT-02
Construcción reproducible de los 264 triples y la 2-sección
Pendiente de reproducción independiente
MAT-03
Definición exacta de la acción \(\mathbb Z_4\) y la convención de Fourier
Pendiente de formalización documental
MAT-04
Parámetros y resultados del régimen no vacío 24D
Pendiente según STATUS
MAT-05
Exclusión de ciclos de igual potencial en la dinámica asíncrona
Requiere condición adicional o prueba
MAT-06
Identidad o relación formal entre mass_24 y el núcleo 24D
No establecida aquí
MAT-07
Invariancia del subespacio transversal 47D
Requiere demostración
MAT-08
Extensión de estabilidad lineal a estabilidad no lineal
Abierta
MAT-09
Validación formal del candidato (R)
Abierta
MAT-10
Reproducción independiente de los resultados espectrales y de ventana larga
Pendiente

12. Criterios para considerar consolidada la base matemática
Las variables, espacios y dominios están definidos.
Las matrices se construyen mediante procedimientos reproducibles.
Las transformaciones y simetrías se derivan explícitamente.
Las afirmaciones de positividad distinguen positividad de entradas y semidefinición positiva.
La monotonía de V está demostrada para cada actualización permitida.
La convergencia excluye ciclos, no solo incrementos del potencial.
La relación entre los espacios 24D y 47D está definida o se declara pendiente.
El modo neutro y el subespacio transversal están caracterizados.
Las afirmaciones de estabilidad especifican si son lineales, locales, globales o transversales.
Los resultados numéricos pueden reproducirse desde los artefactos publicados.
El candidato (R) no se presenta como validado antes de superar sus requisitos formales.
13. Fuentes internas de referencia
STATUS.md: definiciones y resultados declarados para el núcleo 24D, \(\mathbb Z_4\), V(T), protocolo N1–N4 y candidato (R).
AUDITORIA_v17_modo_a.md: resultados reportados para la arquitectura dinámica 47D, proyección transversal, análisis espectral, ensembles y ventana larga.
README.md: definición del estado operativo 4D y separación entre Código Viajer y TRCG.

Estado final: documento de formalización y revisión. Las expresiones y cifras atribuidas al repositorio deben contrastarse con los artefactos fuente. Este documento no constituye una prueba independiente, certificación de estabilidad ni validación de una teoría física.
