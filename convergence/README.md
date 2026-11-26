CONVERGENCE — TRCG / CÓDIGO VIAJER

Programa de investigación sobre convergencia relacional

Versión: 1.0.0
Fecha: 2026-11-26
Estado: Investigación activa
Referencia documental inicial: e82afc8f30bc4fb7ac19af49851f6b208d2b46e5

---

1. Propósito

La carpeta "convergence/" reúne las investigaciones matemáticas, estructurales y computacionales destinadas a estudiar las posibles correspondencias entre:

- TRCG — Teoría Relacional Cuántico Geométrica.
- Código Viajer.
- Arquitectura Pirámide-Parábola.

Su finalidad no es presuponer la equivalencia entre estas formulaciones, sino determinar las condiciones bajo las cuales dicha equivalencia puede demostrarse, limitarse o descartarse.

Este documento constituye el índice común de las líneas de investigación desarrolladas hasta el momento.

El repositorio será la referencia documental principal frente a inventarios, propuestas o desarrollos mantenidos en conversaciones independientes.

---

2. Principios metodológicos

Toda investigación deberá distinguir entre:

1. Definiciones matemáticas.
2. Hipótesis de trabajo.
3. Demostraciones analíticas.
4. Verificaciones computacionales.
5. Resultados experimentales.
6. Limitaciones e incompatibilidades.
7. Cuestiones abiertas.

Una coincidencia numérica no constituye por sí sola una demostración.

Una equivalencia estructural no implica necesariamente una equivalencia dinámica.

Una propiedad demostrada para un modelo auxiliar no podrá trasladarse automáticamente a la arquitectura canónica.

Los resultados negativos deberán conservarse y documentarse con el mismo rigor que los positivos.

---

3. Delimitación de los modelos

3.1. Espacio relacional abstracto

Espacio de matrices reales, simétricas y de diagonal nula.

Su dimensión para N nodos es:

dim(S) = N(N − 1)/2

Para N = 24:

dim(S) = 276

Este espacio constituye un marco algebraico general y admite el estudio de permutaciones con signo.

3.2. Modelo geométrico auxiliar

Modelo combinatorio utilizado para investigar relaciones entre capas, grupos de automorfismos, ablaciones e interacciones estructurales.

Los resultados obtenidos para este modelo dependen de las relaciones auxiliares adoptadas.

No constituyen una identificación automática de la geometría canónica de Pirámide-Parábola.

3.3. Operador relacional matricial

Modelo dinámico definido sobre matrices simétricas, no negativas, de diagonal nula y masa fija.

Para 24 nodos y masa estrictamente positiva, su dominio tiene dimensión 275.

En este modelo se estudian:

- Equivarianza.
- Conservación de masa.
- Estabilidad local.
- Equilibrios de soporte reducido.
- Espacios cociente.
- Invariantes estructurales.
- Recuperabilidad de información.

3.4. Modelo nodal multiplicativo

Modelo utilizado para estudiar mecanismos de selección, distribución nodal y dominancia apical.

Sus resultados deberán mantenerse diferenciados de los obtenidos para el operador matricial.

3.5. Arquitectura canónica e híbrida

La identificación completa de la arquitectura canónica y de su dinámica requiere referencias explícitas a las especificaciones originales.

La correspondencia entre una implementación de referencia y la implementación canónica deberá verificarse mediante una versión identificable del código fuente.

3.6. Operadores 44A y 44B

Los operadores correspondientes a la campaña experimental del Episodio 44 mantienen su independencia metodológica.

No se modificarán sus reglas, parámetros ni criterios de evaluación como consecuencia de los resultados obtenidos en esta carpeta.

---

4. Inventario documental

Bloque A — Identidad geométrica

Archivo| Función
"GEOMETRY_IDENTITY.md"| Identidad geométrica relacional.
"GEOMETRIC_IDENTIFIABILITY.md"| Identificabilidad de la geometría mediante propiedades estructurales y dinámicas.
"CANONICAL_SYMMETRY_CORRESPONDENCE.md"| Correspondencia entre simetrías auxiliares y canónicas.

Bloque B — Grupos y transformaciones

Archivo| Función
"SYMMETRY_GROUP.md"| Grupos de automorfismos del modelo auxiliar.
"EFFECTIVE_SYMMETRY_GROUP.md"| Grupo efectivo y transformaciones relacionales.
"PP_AUTOMORPHISM_GROUP.md"| Automorfismos del modelo combinatorio de Pirámide-Parábola.

Bloque C — Ablación e interacción estructural

Archivo| Función
"STRUCTURAL_ABLATION.md"| Análisis de la contribución estructural de las capas.
"STRUCTURAL_INTERACTION.md"| Interacción entre restricciones y capas relacionales.

Bloque D — Operadores y dinámica

Archivo| Función
"RELATIONAL_EQUIVARIANCE.md"| Compatibilidad entre operadores y transformaciones.
"CANONICAL_OPERATOR_CORRESPONDENCE.md"| Correspondencia algebraica entre operadores de referencia y formulaciones canónicas.

Bloque E — Espacio cociente e invariantes

Archivo| Función
"RELATIONAL_QUOTIENT_METRIC.md"| Espacio cociente, distancia relacional y compatibilidad métrica.
"MULTILAYER_INVARIANTS.md"| Invariantes conjuntos y caracterización multicapa.

Bloque F — Equilibrios y estabilidad

Archivo| Función
"EQUILIBRIUM_CLASSIFICATION.md"| Clasificación estructural de equilibrios.
"REDUCED_SUPPORT_STABILITY.md"| Estabilidad de equilibrios de soporte reducido.
"APICAL_DOMINANCE.md"| Condiciones y limitaciones de la dominancia apical.

Bloque G — Recuperabilidad de información

Archivo| Estado
"INFORMATION_RECOVERY.md"| Pendiente de incorporación.

---

5. Auditorías computacionales

Los programas Python y los archivos JSON asociados constituyen la capa de verificación reproducible del programa de investigación.

Se distinguen las siguientes familias:

- Auditoría de simetrías auxiliares.
- Auditoría de simetrías canónicas.
- Auditoría de equivarianza relacional.
- Auditoría de correspondencia entre operadores.
- Auditoría de estabilidad de soporte reducido.
- Verificación multicapa.
- Verificación de dominancia apical.
- Auditoría del espacio cociente, pendiente de incorporación.

Cada auditoría deberá identificar, cuando corresponda:

- Modelo utilizado.
- Versión del código.
- Parámetros.
- Semilla aleatoria.
- Tolerancias numéricas.
- Hipótesis verificadas.
- Controles positivos.
- Controles negativos.
- Resultados.
- Limitaciones.
- Comprobaciones no ejecutadas.

Los archivos JSON deberán proceder de ejecuciones reales de los programas correspondientes.

Los resultados esperados no deberán presentarse como resultados computacionales observados.

---

6. Distinción entre grupos de simetría

La investigación contempla diferentes grupos, asociados a distintos dominios y estructuras.

Grupo| Orden| Ámbito
Grupo efectivo de permutaciones con signo| 2^(N−1) N!| Espacio matricial abstracto, N ≥ 3.
Grupo de permutaciones ordinarias| N!| Reetiquetado general de nodos.
Grupo de Klein| 4| Modelo auxiliar multicapa estudiado.
Grupo cíclico Z4| 4| Acción rotacional declarada de Pirámide-Parábola.
Grupo cíclico Z2| 2| Modelo combinatorio parcial con restricciones específicas.
Grupo estratificado (S4)^6| 191102976| Operador relacional con seis pesos estratificados distintos y cuatro nodos por estrato.

La coincidencia del orden de dos grupos no demuestra su isomorfismo ni la igualdad de sus acciones.

El grupo geométrico completo de la arquitectura canónica permanece pendiente de identificación definitiva.

La admisibilidad de una transformación deberá determinarse respecto del dominio y las estructuras que deben conservarse.

---

7. Resultados dimensionales

Para el modelo relacional de 24 nodos:

Espacio| Dimensión
Espacio matricial simétrico de diagonal nula| 276
Dominio de masa fija| 275
Cociente de masa fija por un grupo finito admisible| 275
Subespacio fijo rotacional| 72
Subespacio fijo rotacional de masa fija| 71
Subespacio fijo estratificado| 21
Subespacio fijo estratificado de masa fija| 20

Estos resultados dependen de las acciones de grupo especificadas en los documentos correspondientes.

El espacio cociente y el subespacio fijo son construcciones matemáticas diferentes.

La identificación de configuraciones mediante una acción finita no implica una reducción de la dimensión topológica del dominio considerado.

---

8. Equilibrios de una sola arista

Para el operador relacional matricial estudiado, existen 276 configuraciones de equilibrio con masa concentrada en una sola arista, bajo la extensión del operador a estos estados de frontera.

Su clasificación bajo diferentes grupos de permutaciones es:

Grupo| Número de clases
Permutaciones ordinarias| 1
Grupo rotacional Z4| 72
Grupo estratificado (S4)^6| 21

La clasificación mediante permutaciones ordinarias es combinatoria y no implica que todas estas permutaciones sean simetrías del operador ponderado.

Para gamma > 1 y un parámetro de actualización comprendido entre cero excluido y uno incluido, estos equilibrios son localmente asintóticamente estables bajo las hipótesis del operador estudiado.

Participación apical

Participación| Equilibrios| Clases estratificadas
Dos nodos apicales| 6| 1
Un nodo apical| 80| 5
Ningún nodo apical| 190| 15
Total| 276| 21

Estos resultados no constituyen estimaciones de las probabilidades de convergencia ni de los tamaños de las cuencas de atracción.

Tampoco deberán confundirse con resultados procedentes de otros modelos o campañas experimentales.

La dominancia apical universal queda descartada para el operador estudiado bajo las condiciones demostradas.

La posible dominancia apical estadística permanece abierta.

---

9. Espacio cociente e invariantes completos

Para la familia de equilibrios de una sola arista y masa conocida C0, la distancia cociente entre clases diferentes es:

dG = sqrt(2) C0

Esta expresión utiliza la norma euclídea sobre las relaciones diádicas independientes.

Todos estos equilibrios poseen idéntico espectro matricial.

Por tanto, el espectro no permite distinguir por sí solo las clases rotacionales o estratificadas.

Introduciendo una matriz diagonal auxiliar W de pesos geométricos, se consideran los invariantes:

I1 = tr(W R²)

I2 = tr(W² R²)

Definiendo:

A = I1 / C0²

B = I2 / C0²

El par no ordenado de pesos geométricos se reconstruye mediante:

g+ = (A + sqrt(2B − A²)) / 2

g− = (A − sqrt(2B − A²)) / 2

Las condiciones necesarias y suficientes para obtener dos pesos reales estrictamente positivos son:

A > 0

A²/2 ≤ B < A²

Para identificar una clase de la arquitectura concreta, los pesos reconstruidos deberán pertenecer al conjunto de pesos admitidos y satisfacer las restricciones de multiplicidad.

Cuando los seis estratos poseen pesos distintos, estos invariantes caracterizan completamente las 21 clases estratificadas de equilibrios de una sola arista.

No permiten recuperar, en general, la orientación angular ni la identidad individual de los nodos.

La extensión de estos resultados a soportes superiores permanece abierta.

---

10. Dinámica del espacio cociente

Si un operador F es equivariante respecto de un grupo finito de isometrías G, induce una evolución bien definida sobre el espacio cociente.

Si además F satisface una condición de Lipschitz con constante L, el operador inducido satisface la misma cota respecto de la métrica cociente.

La existencia de dos clases distintas de puntos fijos implica:

L ≥ 1

para cualquier constante global de Lipschitz del operador inducido, si existe.

En consecuencia, la existencia de múltiples clases de equilibrios descarta la contractividad global estricta en los dominios considerados que contienen dichos equilibrios.

Este resultado no excluye:

- Contracción local.
- Estabilidad local.
- Convergencia hacia diferentes atractores.
- Existencia de cuencas de atracción diferenciadas.

La compatibilidad dinámica con cada grupo deberá verificarse independientemente.

---

11. Estado de las investigaciones

Investigación| Estado
Simetrías del modelo auxiliar| Desarrollo analítico y auditorías registradas.
Acción rotacional Z4| Caracterizada bajo la acción declarada.
Grupo geométrico canónico completo| Abierto.
Equivarianza del operador de referencia| Verificaciones registradas.
Correspondencia con la implementación canónica original| Pendiente de certificación mediante una versión identificable.
Estabilidad de equilibrios de una arista| Demostrada bajo las hipótesis especificadas.
Clasificación en 1, 21 y 72 clases| Demostrada analíticamente; auditoría conjunta pendiente.
Invariantes completos de una arista| Demostrados bajo las hipótesis especificadas.
Reconstrucción de pesos geométricos| Demostrada analíticamente; contraste numérico pendiente.
Contractividad global estricta| Descartada en los dominios y grupos indicados.
Estabilidad de soportes arbitrarios| Abierta.
Cuencas de atracción| Abierta.
Invertibilidad global| Abierta.
Recuperabilidad dinámica de información| Abierta.
Correspondencia con 44A y 44B| Abierta.
Equivalencia global TRCG–Pirámide-Parábola| No establecida.

La existencia de resultados registrados no implica que todas las auditorías hayan sido reproducidas independientemente.

---

12. Plan de consolidación documental

Archivos nuevos pendientes

- [ ] "quotient_space_audit.py"
- [ ] "quotient_space_results.json"
- [ ] "INFORMATION_RECOVERY.md"
- [ ] "symmetry_results.json"

Archivos existentes pendientes de ampliación

- [ ] "EQUILIBRIUM_CLASSIFICATION.md"
- [ ] "MULTILAYER_INVARIANTS.md"
- [ ] "EFFECTIVE_SYMMETRY_GROUP.md"

Los archivos de resultados se incorporarán después de ejecutar las auditorías correspondientes.

No se eliminarán documentos existentes sin una revisión de su contenido, dependencias y alcance científico.

---

13. Protocolo de unificación

Para evitar duplicidades entre líneas de investigación:

1. Consultar el inventario del repositorio antes de crear un documento.
2. Ampliar el documento existente cuando el objeto matemático sea el mismo.
3. Crear un documento independiente cuando exista una diferencia sustancial de modelo, dominio u objetivo.
4. Mantener referencias cruzadas entre resultados relacionados.
5. Identificar explícitamente las hipótesis de cada demostración.
6. Conservar la trazabilidad de las modificaciones.
7. Actualizar este índice cuando cambie el estado de las investigaciones.
8. No sustituir resultados anteriores sin justificar las modificaciones.
9. Registrar las incompatibilidades y los resultados negativos.
10. Utilizar el repositorio como referencia documental común.

---

14. Hoja de ruta científica

Fase I — Consolidación

Completar las ampliaciones documentales y las auditorías pendientes.

Fase II — Estabilidad generalizada

Estudiar equilibrios de soporte superior a dos nodos.

Determinar condiciones de existencia, estabilidad interna e invasión exterior.

Fase III — Información relacional

Investigar invertibilidad, recuperabilidad, conservación de estabilizadores y pérdida de información.

Fase IV — Cuencas de atracción

Estudiar la dependencia respecto de las condiciones iniciales y la posible dominancia apical estadística.

Fase V — Convergencia estructural y dinámica

Contrastar los resultados con la TRCG y con los operadores 44A y 44B.

Ninguna fase implicará automáticamente la validación de una equivalencia global.

---

15. Gobernanza

Se mantienen los siguientes principios:

- Nivel II retenido.
- Nivel III abierto.
- λ reservado exclusivamente al 4º Factor.
- Versiones 1.6 y 1.7 aisladas.
- Campaña experimental del Episodio 44 congelada.
- Sin reescalados post hoc.
- Sin equivalencias anticipadas.
- Sin ascensos automáticos.
- Independencia matemática de las arquitecturas.
- Reproducibilidad y transparencia científica.

---

16. Conclusión

La convergencia entre TRCG y Código Viajer constituye un programa de investigación abierto.

Su desarrollo se fundamenta en la identificación de estructuras, la demostración de invariantes, la caracterización de simetrías, el análisis de operadores y la verificación computacional reproducible.

Las correspondencias deberán establecerse mediante resultados matemáticos explícitos.

Las diferencias deberán conservarse y estudiarse.

Primero las demostraciones; después, las conclusiones y la convergencia.

---

TRCG — Código Viajer — Pirámide-Parábola

Nivel II retenido · Nivel III abierto · λ reservado al 4º Factor.
