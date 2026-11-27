CONVERGENCE — TRCG / CÓDIGO VIAJER

Programa de investigación sobre convergencia relacional

Versión: 1.1.0
Fecha: 2026-11-26
Estado: Investigación activa — consolidación documental completada.
Commit de referencia de la auditoría: "cc9faeefaba2d5fc2e4329be77d69f5d930d045e"

---

1. Propósito

La carpeta "convergence/" reúne las investigaciones matemáticas, estructurales y computacionales destinadas a estudiar las posibles correspondencias entre:

- TRCG — Teoría Relacional Cuántico Geométrica.
- Código Viajer.
- Arquitectura Pirámide-Parábola (PP).

Su finalidad no es presuponer la equivalencia entre estas formulaciones, sino determinar las condiciones bajo las cuales dicha equivalencia puede demostrarse, limitarse o descartarse.

Este documento constituye el índice común de las líneas de investigación desarrolladas hasta el momento.

El repositorio representa la referencia documental principal frente a inventarios, propuestas o desarrollos mantenidos en conversaciones independientes.

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

Una auditoría registrada no equivale necesariamente a una auditoría reproducida de forma independiente.

Los resultados negativos deberán conservarse y documentarse con el mismo rigor que los positivos.

---

3. Delimitación de los modelos

3.1. Espacio relacional abstracto

Espacio de matrices reales, simétricas y de diagonal nula.

Su dimensión para N nodos es:

dim(S) = N(N − 1)/2.

Para N = 24:

dim(S) = 276.

Este espacio constituye el marco algebraico general para el estudio de relaciones diádicas y transformaciones matriciales.

3.2. Modelo geométrico auxiliar

Modelo combinatorio utilizado para investigar:

- Capas relacionales.
- Grupos de automorfismos.
- Ablaciones estructurales.
- Interacciones entre restricciones.
- Invariantes multicapa.

Los resultados obtenidos dependen de las relaciones auxiliares adoptadas.

No constituyen una identificación automática de la arquitectura canónica de Pirámide-Parábola.

3.3. Operador relacional matricial

Modelo dinámico definido sobre matrices reales, simétricas, no negativas, de diagonal nula y masa fija.

Para 24 nodos y masa estrictamente positiva, su dominio tiene dimensión 275.

En este modelo se estudian:

- Conservación de masa.
- Equivarianza.
- Estabilidad local.
- Equilibrios de soporte reducido.
- Espacios cociente.
- Invariantes estructurales.
- Recuperabilidad de información.

Su extensión a estados de frontera requiere garantizar las condiciones necesarias para definir unívocamente el autovector dominante utilizado por el operador.

3.4. Modelo nodal multiplicativo

Modelo auxiliar destinado a estudiar mecanismos de selección, distribución nodal y dominancia apical.

Sus resultados deberán mantenerse diferenciados de los obtenidos para el operador matricial.

3.5. Arquitectura canónica e híbrida

La identificación completa de la arquitectura canónica y de su dinámica requiere referencias explícitas a las especificaciones originales.

La correspondencia entre la implementación de referencia y la implementación canónica deberá verificarse mediante una versión identificable del código fuente.

La coincidencia algebraica entre fórmulas declaradas no constituye por sí sola una certificación de la implementación original.

3.6. Operadores 44A y 44B

Los operadores correspondientes a la campaña experimental del Episodio 44 mantienen su independencia metodológica.

No se modificarán sus reglas, parámetros ni criterios de evaluación como consecuencia de los resultados obtenidos en esta carpeta.

---

4. Inventario documental consolidado

En el commit de referencia se encuentran incorporados 36 archivos:

- 17 documentos Markdown.
- 11 programas y pruebas Python.
- 8 registros JSON.

Bloque A — Identidad geométrica

Archivo| Función
GEOMETRY_IDENTITY.md| Identidad geométrica relacional.
GEOMETRIC_IDENTIFIABILITY.md| Identificabilidad estructural y dinámica de la geometría.
CANONICAL_SYMMETRY_CORRESPONDENCE.md| Correspondencia entre simetrías auxiliares y canónicas.

Bloque B — Grupos y transformaciones

Archivo| Función
SYMMETRY_GROUP.md| Grupos de automorfismos del modelo auxiliar.
EFFECTIVE_SYMMETRY_GROUP.md| Grupos efectivos, dominios admisibles y simetrías dinámicas.
PP_AUTOMORPHISM_GROUP.md| Automorfismos del modelo combinatorio parcial de Pirámide-Parábola.

Bloque C — Ablación e interacción estructural

Archivo| Función
STRUCTURAL_ABLATION.md| Contribución estructural de las capas.
STRUCTURAL_INTERACTION.md| Interacción entre restricciones relacionales.

Bloque D — Operadores y dinámica

Archivo| Función
RELATIONAL_EQUIVARIANCE.md| Compatibilidad entre operadores y transformaciones.
CANONICAL_OPERATOR_CORRESPONDENCE.md| Correspondencia algebraica entre operadores de referencia y fórmulas atribuidas al modelo canónico.

Bloque E — Espacio cociente e invariantes

Archivo| Función
RELATIONAL_QUOTIENT_METRIC.md| Espacio cociente, distancia relacional y compatibilidad métrica.
MULTILAYER_INVARIANTS.md| Invariantes multicapa, invariantes estratificados completos y reconstrucción geométrica.

Bloque F — Equilibrios y estabilidad

Archivo| Función
EQUILIBRIUM_CLASSIFICATION.md| Clasificación de equilibrios, órbitas y estabilizadores.
REDUCED_SUPPORT_STABILITY.md| Estabilidad de equilibrios de una sola arista.
APICAL_DOMINANCE.md| Condiciones y limitaciones de la dominancia apical.

Bloque G — Recuperabilidad de información

Archivo| Función
INFORMATION_RECOVERY.md| Inyectividad, recuperabilidad, estabilizadores y pérdida de información.

Bloque H — Coordinación documental

Archivo| Función
README.md| Inventario, gobernanza, estado científico y hoja de ruta común.

---

5. Inventario computacional

5.1. Programas de auditoría

Archivo| Objeto
symmetry_audit.py| Simetrías, ablaciones e interacciones estructurales.
canonical_symmetry_audit.py| Acción rotacional declarada.
relational_equivariance_audit.py| Equivarianza relacional.
canonical_operator_audit.py| Correspondencia algebraica entre operadores.
reduced_support_stability_audit.py| Estabilidad de soporte reducido.
PP_MULTILAYER_VERIFICATION.py| Verificación del modelo multicapa auxiliar.
APICAL_DOMINANCE_VERIFICATION.py| Dominancia apical en el modelo nodal auxiliar.
quotient_space_audit.py| Clasificación de órbitas, métrica cociente e invariantes completos.

5.2. Pruebas automatizadas

- test_symmetry_audit.py
- test_canonical_symmetry_audit.py
- test_relational_equivariance_audit.py

5.3. Registros de resultados

- symmetry_results.json
- canonical_symmetry_results.json
- relational_equivariance_results.json
- canonical_operator_results.json
- reduced_support_stability_results.json
- pp_verification.json
- apical_verification.json
- quotient_space_results.json

5.4. Requisitos de reproducibilidad

Cada auditoría deberá identificar, cuando corresponda:

- Modelo utilizado.
- Versión del código.
- Dependencias.
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

La presencia de un archivo JSON no sustituye la reproducción independiente de la auditoría.

---

6. Grupos de simetría

La investigación contempla diferentes grupos asociados a distintos dominios, estructuras y operadores.

Grupo| Orden| Ámbito
Grupo efectivo de permutaciones con signo| 2^(N−1) N!| Espacio matricial abstracto, N ≥ 3.
Permutaciones ordinarias S24| 24!| Reetiquetado general de nodos.
Grupo de Klein V4| 4| Modelo multicapa auxiliar.
Grupo cíclico Z4| 4| Acción rotacional declarada.
Grupo cíclico Z2| 2| Modelo combinatorio parcial con estratos fijos.
Grupo estratificado (S4)^6| 191102976| Operador de referencia con seis pesos distintos y cuatro nodos por estrato.

La coincidencia del orden de dos grupos no demuestra su isomorfismo ni la igualdad de sus acciones.

La admisibilidad de una transformación depende del dominio considerado.

La simetría de una arquitectura depende de las estructuras que deben conservarse.

La simetría dinámica depende del operador.

Para el operador matricial de referencia, bajo las hipótesis especificadas y con actualización no nula, el grupo dinámico por permutaciones coincide con el estabilizador de sus pesos geométricos.

El grupo geométrico completo de la arquitectura canónica permanece abierto.

---

7. Resultados dimensionales

Para el modelo relacional de 24 nodos:

Espacio| Dimensión
Espacio matricial simétrico de diagonal nula| 276
Dominio de masa fija positiva| 275
Cociente de masa fija por un grupo finito admisible| 275
Subespacio fijo rotacional Z4| 72
Conjunto fijo rotacional de masa fija| 71
Subespacio fijo estratificado| 21
Conjunto fijo estratificado de masa fija| 20

Estos resultados dependen de las acciones de grupo especificadas en los documentos correspondientes.

El espacio cociente y el subespacio fijo son construcciones matemáticas diferentes.

La identificación de configuraciones mediante un grupo finito no implica una reducción de la dimensión topológica del dominio considerado.

La conservación dinámica de un subespacio fijo requiere la equivarianza correspondiente y no implica necesariamente su carácter atractivo.

---

8. Equilibrios de una sola arista

Para el operador relacional matricial estudiado existen 276 configuraciones distintas de equilibrio con masa concentrada en una sola arista, bajo la extensión admisible del operador a estos estados de frontera.

No se afirma que constituyan todos los puntos fijos del operador.

8.1. Clasificación exacta

Grupo de clasificación| Número de órbitas
Identidad| 276
Permutaciones ordinarias S24| 1
Grupo residual Z2| 144
Grupo rotacional Z4| 72
Grupo estratificado (S4)^6| 21

Para Z4, el lema de Burnside proporciona:

(276 + 0 + 12 + 0)/4 = 72.

La distribución de órbitas rotacionales es:

- 6 órbitas de tamaño 2.
- 66 órbitas de tamaño 4.

Para Z2:

- 12 órbitas de tamaño 1.
- 132 órbitas de tamaño 2.

Para el grupo estratificado:

- 6 órbitas intraestrato de tamaño 6.
- 15 órbitas interestrato de tamaño 16.

La clasificación bajo permutaciones ordinarias es combinatoria y no implica que todas esas permutaciones sean simetrías del operador ponderado.

La interpretación dinámica de una clasificación requiere que el grupo sea compatible con el operador estudiado.

8.2. Participación apical

Participación| Equilibrios| Clases Z2| Clases Z4| Clases estratificadas
Ningún nodo apical| 190| 100| 50| 15
Un nodo apical| 80| 40| 20| 5
Dos nodos apicales| 6| 4| 2| 1
Total| 276| 144| 72| 21

Estos recuentos no constituyen estimaciones de las probabilidades de convergencia ni de los tamaños de las cuencas de atracción.

---

9. Estabilidad de soporte reducido

Para el operador matricial de referencia, con pesos positivos finitos y parámetro de actualización 0 < μ ≤ 1:

Régimen γ > 1

Los 276 equilibrios de una sola arista son localmente asintóticamente estables bajo las hipótesis demostradas.

El factor lineal local es:

1 − μ.

La estabilidad se mantiene frente a perturbaciones admisibles suficientemente pequeñas que introducen masa relacional exterior al soporte inicial.

Régimen γ = 1

La estabilidad depende de los multiplicadores de invasión exterior.

Para seis estratos de cuatro nodos con pesos constantes dentro de cada estrato, los equilibrios de una sola arista son inestables.

Régimen 0 < γ < 1

Los equilibrios de una sola arista son inestables respecto del dominio ampliado considerado.

Régimen μ = 0

El operador es la identidad.

No existe atracción asintótica hacia un equilibrio individual desde estados iniciales diferentes.

Alcance

Estos resultados están desarrollados en "REDUCED_SUPPORT_STABILITY.md".

No constituyen una demostración de estabilidad para soportes arbitrarios ni una certificación del operador híbrido o de los operadores 44A y 44B.

---

10. Dominancia apical

La existencia de 190 equilibrios no apicales descarta la convergencia apical universal en un dominio que los contenga.

Para γ > 1, su estabilidad local proporciona además regiones de atracción no apicales en el dominio matricial de referencia.

Debe distinguirse entre:

- Dominancia geométrica.
- Dominancia estructural.
- Dominancia dinámica.
- Dominancia estadística.
- Concentración asintótica.
- Estabilidad frente a invasión exterior.

La existencia de una ventaja geométrica no garantiza automáticamente una ventaja dinámica.

El modelo nodal multiplicativo auxiliar permite estudiar condiciones de crecimiento, concentración e invasión apical, pero sus resultados no se trasladan automáticamente al operador matricial.

La posible dominancia apical estadística permanece abierta y requiere caracterizar las cuencas de atracción y las distribuciones de condiciones iniciales.

---

11. Espacio cociente y distancia relacional

Para un grupo finito G que actúa mediante isometrías sobre un espacio relacional X, se define:

dG([R],[S]) = min{d(R,g·S) : g ∈ G}.

Esta expresión define una métrica sobre el espacio de órbitas correspondiente.

Sobre las configuraciones originales constituye una pseudométrica.

Para los equilibrios de una sola arista y masa conocida C0, la distancia cociente entre clases distintas es:

dG = sqrt(2) C0,

cuando se utiliza la norma euclídea sobre las relaciones diádicas independientes.

Con la norma de Frobenius sobre las matrices simétricas completas, la distancia correspondiente es:

dG = 2 C0.

La convención métrica deberá declararse explícitamente en cada demostración y auditoría.

No deberán compararse directamente distancias obtenidas mediante convenciones diferentes.

La evaluación eficiente de la distancia cociente para matrices densas y grupos de gran orden permanece como problema computacional abierto.

---

12. Invariantes completos y reconstrucción geométrica

Todos los equilibrios de una sola arista con la misma masa poseen idéntico espectro matricial.

Por tanto, el espectro no permite distinguir por sí solo las clases rotacionales o estratificadas.

Introduciendo una matriz diagonal auxiliar W de pesos geométricos positivos, se consideran los invariantes:

I1 = tr(W R²).

I2 = tr(W² R²).

Estos invariantes se consideran respecto de las transformaciones que preservan los atributos correspondientes, o bajo transformación simultánea de relaciones y atributos.

Definiendo:

A = I1 / C0².

B = I2 / C0².

El par no ordenado de pesos geométricos se reconstruye mediante:

g+ = (A + sqrt(2B − A²))/2.

g− = (A − sqrt(2B − A²))/2.

Las condiciones necesarias y suficientes para obtener dos pesos reales estrictamente positivos son:

A > 0.

A²/2 ≤ B < A².

Para identificar una clase de una arquitectura concreta, los pesos reconstruidos deberán pertenecer al conjunto de pesos admitidos y satisfacer las restricciones de multiplicidad.

Cuando los seis estratos poseen pesos distintos, estos invariantes caracterizan completamente las 21 clases estratificadas de equilibrios de una sola arista.

No permiten recuperar por sí solos:

- La orientación angular.
- La identidad individual de los nodos.
- Las 72 clases rotacionales.
- Una configuración relacional arbitraria.

La información angular proporciona descriptores adicionales para la clasificación rotacional de una arista.

Para soportes superiores, los momentos geométrico-relacionales y las matrices de interacción entre estratos permiten reconstruir determinados perfiles agregados.

Su completitud para configuraciones arbitrarias permanece abierta.

---

13. Equivarianza y dinámica del espacio cociente

Si un operador F es equivariante respecto de un grupo G:

F(g·R) = g·F(R),

entonces induce una aplicación bien definida sobre el espacio cociente:

F̄([R]) = [F(R)].

Si G actúa mediante isometrías y F satisface una condición de Lipschitz con constante L, el operador inducido satisface la misma cota respecto de la métrica cociente.

La existencia de dos clases distintas de puntos fijos implica:

L ≥ 1,

para cualquier constante global de Lipschitz del operador inducido, si existe.

Por tanto, la multiplicidad de clases distintas de equilibrio descarta la contractividad global estricta del operador sobre los dominios considerados que contienen dichas clases.

Este resultado no excluye:

- Contracción local.
- Estabilidad local.
- Regiones contractivas.
- Convergencia hacia diferentes atractores.
- Cuencas de atracción diferenciadas.

La compatibilidad dinámica con cada grupo deberá verificarse independientemente.

---

14. Recuperabilidad de información

El documento "INFORMATION_RECOVERY.md" establece el marco matemático para distinguir:

- Recuperación exacta de una configuración.
- Recuperación de una clase de equivalencia.
- Recuperación de invariantes.
- Recuperación de una trayectoria.
- Pérdida finita de información.
- Pérdida asintótica de información.

Para una dinámica equivariante, el estabilizador de una configuración está contenido en el estabilizador de su imagen.

Si el operador es inyectivo, ambos estabilizadores coinciden.

La inyectividad del operador inducido sobre el espacio cociente, junto con la conservación exacta de estabilizadores, caracteriza la inyectividad del operador original bajo las hipótesis establecidas.

El análisis desarrollado para el operador matricial de referencia demuestra la pérdida de inyectividad en el régimen de actualización completa μ = 1.

La inyectividad global para 0 < μ < 1 permanece abierta.

La convergencia hacia un equilibrio no implica necesariamente la pérdida de inyectividad durante cada paso finito de la evolución.

La recuperación estructural y la recuperación dinámica constituyen problemas distintos.

---

15. Resultados computacionales registrados

15.1. Auditoría del espacio cociente

Archivo: "quotient_space_results.json".

Resultados registrados:

Magnitud| Resultado
Aristas clasificadas| 276
Clases ordinarias| 1
Clases estratificadas| 21
Clases rotacionales Z4| 72
Clases residuales Z2| 144
Firmas estratificadas distintas| 21
Error máximo de reconstrucción| 0
Error máximo de equivarianza| 5.84 × 10⁻¹⁶, cota redondeada
Estado registrado| PASS

La auditoría incluye controles negativos relacionados con:

- Coincidencia de pesos.
- Colisiones entre clasificaciones estratificadas y rotacionales.
- Pares de momentos inadmisibles.
- Ruptura de la simetría de los pesos.

15.2. Verificación multicapa auxiliar

Archivo: "pp_verification.json".

Resultados registrados:

- Grupo auxiliar de orden 4.
- Grupo residual con estratos fijos de orden 2.
- Rango de la matriz de Gram igual a 4.
- Determinante de Gram igual a 2617344.
- Conservación de las cuatro capas bajo rotaciones de 0° y 180°.
- Estado registrado: PASS.

Estos resultados corresponden al modelo combinatorio parcial.

15.3. Verificación de dominancia apical

Archivo: "apical_verification.json".

Resultados registrados:

- Pruebas superadas: 18.
- Pruebas fallidas: 0.
- Pruebas no ejecutadas: 2.

Las pruebas no ejecutadas requieren datos de arquitecturas nulas y del operador canónico.

El alcance está limitado al modelo nodal multiplicativo auxiliar.

15.4. Correspondencia del operador

Archivo: "canonical_operator_results.json".

Resultados registrados:

- 480 comparaciones.
- Conservación de masa.
- Equivarianza rotacional.
- Equivarianza estratificada.
- Control negativo de ruptura de pesos.

Limitación:

"status: formula_audit_only"

"upstream_commit: null"

La certificación de una versión concreta de la implementación canónica continúa pendiente.

15.5. Estabilidad de soporte reducido

Archivo: "reduced_support_stability_results.json".

Resultados registrados:

- 276 aristas examinadas por combinación de parámetros.
- Ocho combinaciones de parámetros.
- Conservación numérica de masa.
- Contraste de los regímenes de estabilidad e inestabilidad.
- Todas las combinaciones registradas como superadas.

Las pruebas numéricas complementan las demostraciones analíticas y no constituyen una exploración exhaustiva de las cuencas.

15.6. Ablación estructural

Archivo: "symmetry_results.json".

Resultados registrados:

- 16 configuraciones de ablación.
- Órdenes de los grupos correspondientes.
- Índices de ampliación de simetría.
- Interacciones entre capas.

El alcance declarado de estos resultados es provisional y corresponde al modelo auxiliar.

15.7. Alcance general

Los resultados de esta sección resumen registros existentes en el repositorio.

La reproducción independiente de todas las ejecuciones no se considera completada.

---

16. Estado de las investigaciones

16.1. Resultados analíticos establecidos

Bajo las hipótesis de los documentos correspondientes:

- Dimensión del espacio relacional.
- Dimensión del dominio de masa fija.
- Grupo efectivo del espacio matricial abstracto.
- Automorfismos del modelo multicapa auxiliar.
- Grupos admisibles según el dominio.
- Métrica relacional del espacio cociente.
- Clasificación combinatoria de las 276 aristas.
- Clasificación en 1, 21, 72 y 144 órbitas.
- Dimensiones de los subespacios fijos.
- Invariantes completos de una arista respecto del grupo estratificado.
- Reconstrucción del par de pesos geométricos.
- Estabilidad local de soporte reducido para el operador de referencia.
- Obstrucción a la contractividad global estricta por multiplicidad de clases fijas.
- Limitación de la dominancia apical universal.
- Relación entre equivarianza, estabilizadores e inyectividad.
- No inyectividad de la actualización completa del operador de referencia.

16.2. Resultados condicionados o con certificación pendiente

- Correspondencia algebraica con las fórmulas atribuidas al operador canónico.
- Grupo dinámico de la implementación original.
- Correspondencia con la arquitectura geométrica completa.
- Reproducción independiente de todas las auditorías.
- Extensión de resultados auxiliares al sistema híbrido.

16.3. Investigaciones abiertas

- Grupo geométrico canónico completo.
- Estabilidad de soportes arbitrarios.
- Clasificación exhaustiva de los puntos fijos.
- Existencia de otros atractores.
- Estabilidad de soportes heterogéneos.
- Cuencas de atracción.
- Dominancia apical estadística.
- Inyectividad global para actualización parcial.
- Estabilidad de la inversión.
- Invariantes completos para soportes superiores.
- Recuperabilidad de trayectorias.
- Equivarianza de los operadores 44A y 44B.
- Correspondencia dinámica con la TRCG.
- Equivalencia global TRCG–Pirámide-Parábola.

---

17. Consolidación documental completada

Las actuaciones pendientes de incorporación han sido completadas:

- [x] README.md
- [x] quotient_space_audit.py
- [x] quotient_space_results.json
- [x] INFORMATION_RECOVERY.md
- [x] symmetry_results.json

Las ampliaciones documentales previstas también han sido incorporadas:

- [x] EQUILIBRIUM_CLASSIFICATION.md — ampliación v0.2.0.
- [x] MULTILAYER_INVARIANTS.md — ampliación v0.2.0.
- [x] EFFECTIVE_SYMMETRY_GROUP.md — ampliación v0.2.0.

Los objetivos inicialmente previstos para los siguientes documentos quedan cubiertos por documentos existentes y sus ampliaciones:

Documento inicialmente previsto| Documento de referencia
RELATIONAL_QUOTIENT_SPACE.md| RELATIONAL_QUOTIENT_METRIC.md
ATTRACTOR_ORBIT_CLASSIFICATION.md| EQUILIBRIUM_CLASSIFICATION.md
COMPLETE_STRATIFIED_INVARIANTS.md| MULTILAYER_INVARIANTS.md
ADMISSIBLE_TRANSFORMATIONS.md| EFFECTIVE_SYMMETRY_GROUP.md
ATTRACTOR_EQUIVALENCE.md| EQUILIBRIUM_CLASSIFICATION.md e INFORMATION_RECOVERY.md

No se considera necesaria su creación como documentos independientes mientras sus objetivos permanezcan cubiertos.

La consolidación documental no implica el cierre de todas las investigaciones matemáticas.

---

18. Protocolo de unificación

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
11. Identificar mediante commits las versiones utilizadas en las auditorías.
12. Distinguir la incorporación documental de la validación científica.

Las conversaciones independientes constituyen instrumentos de investigación.

El repositorio constituye la referencia común para los resultados consolidados.

---

19. Hoja de ruta científica

Fase I — Consolidación documental

Estado: completada respecto del inventario de referencia.

Continúan pendientes la reproducción independiente de las auditorías y la certificación de la implementación canónica.

Fase II — Estabilidad generalizada

Estado: siguiente prioridad matemática.

Objetivos:

- Caracterizar equilibrios con más de una arista.
- Investigar soportes de tres a 24 nodos.
- Determinar condiciones de existencia.
- Obtener criterios de estabilidad interna.
- Caracterizar perturbaciones transversales.
- Estudiar mecanismos de invasión exterior.
- Identificar dependencias respecto de γ y μ.
- Determinar posibles bifurcaciones.
- Contrastar resultados analíticos mediante auditorías computacionales.

Fase III — Información relacional

Objetivos:

- Investigar la inyectividad global para actualización parcial.
- Caracterizar las fibras del operador.
- Establecer cotas de recuperabilidad.
- Determinar condiciones de estabilidad de la inversión.
- Extender los invariantes a soportes superiores.

Fase IV — Cuencas de atracción

Objetivos:

- Caracterizar regiones de atracción.
- Estudiar la dependencia de las condiciones iniciales.
- Determinar probabilidades de convergencia bajo distribuciones explícitas.
- Evaluar la posible dominancia apical estadística.
- Incorporar controles negativos, arquitecturas nulas y ablaciones.
- Cuantificar la incertidumbre de las estimaciones.

Fase V — Convergencia estructural y dinámica

Objetivos:

- Identificar y certificar las versiones originales de los operadores.
- Determinar el grupo común de compatibilidad.
- Comparar invariantes y espacios de estados.
- Verificar equivalencias dinámicas.
- Contrastar resultados con la TRCG.
- Investigar la correspondencia con 44A y 44B sin modificar sus reglas originales.

Ninguna fase implicará automáticamente la validación de una equivalencia global.

---

20. Archivos previstos para las siguientes fases

Los siguientes nombres constituyen propuestas documentales, no archivos existentes ni resultados anticipados.

Estabilidad generalizada

- ARBITRARY_SUPPORT_STABILITY.md
- arbitrary_support_stability_audit.py
- arbitrary_support_stability_results.json

Cuencas de atracción

- BASINS_OF_ATTRACTION.md
- basins_of_attraction_audit.py
- basins_of_attraction_results.json

Correspondencia dinámica

- TRCG_PP_DYNAMIC_CORRESPONDENCE.md

Los documentos se incorporarán cuando existan resultados suficientemente desarrollados.

Los registros JSON se incorporarán únicamente después de ejecutar las auditorías correspondientes.

La investigación sobre recuperabilidad podrá continuar mediante ampliaciones de INFORMATION_RECOVERY.md.

No se crearán documentos vacíos ni se anticiparán conclusiones pendientes de demostración.

---

21. Gobernanza

Se mantienen íntegramente los siguientes principios:

- Nivel II retenido.
- Nivel III abierto.
- λ reservado exclusivamente al 4º Factor.
- Versiones 1.6 y 1.7 aisladas.
- Campaña experimental del Episodio 44 congelada.
- Sin reescalados post hoc.
- Sin equivalencias anticipadas.
- Sin ascensos automáticos.
- Independencia matemática de las arquitecturas.
- Conservación de resultados negativos.
- Reproducibilidad científica.
- Trazabilidad documental.
- Transparencia metodológica.
- Independencia crítica entre las formulaciones.

Ningún resultado obtenido en esta carpeta modifica automáticamente el estado de validación de la TRCG o del Código Viajer.

---

22. Historial de versiones

Versión 1.0.0

- Creación del índice común.
- Delimitación de los modelos.
- Organización documental inicial.
- Definición del protocolo de unificación.
- Establecimiento de la hoja de ruta científica.

Versión 1.1.0

- Consolidación del inventario de 36 archivos.
- Incorporación de las cinco altas documentales y computacionales.
- Confirmación de las tres ampliaciones previstas.
- Integración de los resultados del espacio cociente.
- Actualización de la clasificación de órbitas.
- Incorporación del marco de recuperabilidad de información.
- Actualización de las limitaciones computacionales.
- Distinción entre resultados registrados y reproducidos.
- Cierre de la fase inicial de consolidación documental.
- Establecimiento de la estabilidad de soportes arbitrarios como siguiente prioridad.

---

23. Conclusión

La convergencia entre TRCG y Código Viajer constituye un programa de investigación matemática abierto.

Su desarrollo se fundamenta en la identificación de estructuras, la demostración de invariantes, la caracterización de simetrías, el análisis de operadores y la verificación computacional reproducible.

La consolidación documental permite trabajar sobre una referencia común, evitando duplicidades y preservando la independencia crítica de las investigaciones.

La siguiente etapa se orienta hacia la caracterización de equilibrios de soporte arbitrario, la estabilidad generalizada y la recuperabilidad dinámica.

Las correspondencias deberán establecerse mediante resultados matemáticos explícitos.

Las diferencias deberán conservarse y estudiarse.

La geometría establece posibilidades.

La simetría organiza configuraciones.

Los invariantes caracterizan estructuras.

La dinámica determina evoluciones.

La estabilidad exige demostración.

La dominancia exige cuantificación.

La equivalencia exige justificación.

La convergencia no se presupone: se demuestra, se verifica y se consolida.

---

24. Fase II — Equilibrios de soporte superior, estabilidad y bifurcaciones

24.1. Objetivo

La segunda fase del programa de convergencia amplía el estudio de los equilibrios de soporte reducido hacia configuraciones relacionales de tres o más nodos activos.

Se incorporan resultados analíticos y computacionales relativos a:

- Existencia y multiplicidad de equilibrios.
- Soportes homogéneos y heterogéneos.
- Reconstrucción exacta de matrices relacionales.
- Estabilidad local y espectro dinámico.
- Influencia de los pesos geométricos.
- Aparición y desaparición de ramas de equilibrio.
- Bifurcaciones silla-nodo.

24.2. Nuevos documentos incorporados

Archivo| Función
"HIGHER_SUPPORT_EQUILIBRIA.md" (HIGHER_SUPPORT_EQUILIBRIA.md)| Desarrollo matemático de los equilibrios de soporte superior.
"higher_support_audit.py" (higher_support_audit.py)| Auditoría computacional reproducible.
"higher_support_results.json" (higher_support_results.json)| Resultados numéricos y controles de verificación.

Estos documentos complementan los resultados previamente establecidos sobre estabilidad de soporte reducido, clasificación de equilibrios, equivariancia y dinámica en espacios cociente.

24.3. Caracterización general de los equilibrios

Para el operador relacional de referencia estudiado, todo equilibrio posee un soporte activo completamente conectado.

La condición de equilibrio admite una reducción algebraica exacta:

$$
g_i^{\frac{2\gamma}{\gamma+1}}
p_i^{\frac{\gamma-1}{\gamma+1}}
(1-p_i)=K
$$

con:

$$
p_i>0,\qquad \sum_{i\in S}p_i=1.
$$

Esta formulación permite reducir el problema matricial a un sistema de ecuaciones escalares.

Se establecen tres regímenes:

- Para 0 < γ < 1, existe exactamente un equilibrio por soporte admisible de al menos dos nodos.
- Para γ = 1, existe una solución explícita sometida a una condición necesaria y suficiente de positividad.
- Para γ > 1, pueden coexistir múltiples ramas de equilibrio sobre un mismo soporte.

En el sistema de 24 nodos, el primer régimen admite exactamente 16.777.191 equilibrios matemáticos.

Este recuento no constituye una clasificación de atractores.

24.4. Estabilidad de soportes homogéneos

Para soportes homogéneos de tamaño m ≥ 3, el umbral crítico viene dado por:

$$
\gamma_c=\frac{m}{m-2}.
$$

Tamaño del soporte| Umbral crítico
3| 3
4| 2
6| 1,5
12| 1,2
24| 12/11

Los soportes homogéneos de tamaño superior a cuatro representan casos matemáticos de referencia, no configuraciones de peso homogéneo necesariamente presentes en la arquitectura estratificada canónica.

Bajo la hipótesis de seis estratos de cuatro nodos, con pesos positivos constantes dentro de cada estrato, se obtienen las siguientes cotas inferiores:

Régimen| Equilibrios localmente estables
1 < γ < 2| Al menos 306
2 < γ < 3| Al menos 300
γ > 3| Al menos 276

Para 1 < γ < 2, estos equilibrios comprenden al menos 33 clases estratificadas y 84 clases rotacionales, bajo los grupos correspondientes.

No se afirma que estas cotas constituyan una enumeración exhaustiva.

24.5. Estabilidad de soportes heterogéneos

Se establece una reducción espectral mediante la matriz estocástica:

$$
P_{ij}=\frac{p_j}{1-p_i},\qquad i\neq j,
$$

con diagonal nula.

Los autovalores dinámicos no transversales vienen dados por:

$$
\eta_k=1-\mu+
\mu\gamma\frac{1+\ell_k}{1-\ell_k}.
$$

Para γ > 1, 0 < μ ≤ 1 y soportes de al menos tres nodos, el criterio de estabilidad lineal estricta es:

$$
\ell_2<-\frac{\gamma-1}{\gamma+1}.
$$

La desigualdad estricta garantiza estabilidad local asintótica. La desigualdad inversa estricta implica inestabilidad.

La igualdad requiere un análisis no lineal adicional.

Esta reducción permite estudiar el espectro relevante mediante matrices de dimensión igual al número de nodos activos.

24.6. Verificación computacional

La auditoría utiliza NumPy y SciPy y compara el espectro reducido con el Jacobiano obtenido mediante diferenciación numérica directa.

Configuración de referencia:

- γ = 1,5.
- μ = 0,2.
- Masa relacional C₀ = 1.
- Pesos geométricos ilustrativos.

Resultados:

Configuración| Equilibrios encontrados| Estables| Inestables
Triángulo homogéneo| 4| 1| 3
Triángulo heterogéneo| 4| 1| 3
Cuatro nodos heterogéneos| 9| 0| 9
Total| 17| 2| 15

Error espectral máximo observado: aproximadamente 8,03 × 10⁻¹¹.

Estado de los controles programados: PASS.

Este estado se refiere exclusivamente a las comprobaciones ejecutadas y no implica una validación global del modelo.

24.7. Bifurcación silla-nodo heterogénea

Para un soporte triangular con pesos:

$$
g=(1,;1.1,;1.2),
$$

se localiza numéricamente un punto crítico en:

$$
\gamma^*\approx1.56556420.
$$

Las comprobaciones realizadas incluyen:

- Existencia numérica del equilibrio crítico.
- Singularidad simple del Jacobiano reducido.
- Autovalor dinámico unitario simple.
- Transversalidad respecto de γ.
- No degeneración cuadrática.
- Contraste directo con el operador dinámico.
- Consistencia ante distintos pasos de diferenciación.

Los resultados respaldan una bifurcación silla-nodo genérica sobre la cara triangular invariante.

Se identifica la colisión local de una rama estable y otra inestable, seguida de su desaparición al superar el valor crítico.

La existencia exacta de la raíz crítica todavía no ha sido certificada mediante aritmética de intervalos.

Tampoco se extiende automáticamente la forma normal de segundo orden al dominio completo de 24 nodos.

24.8. Consecuencias para la identidad relacional

Los resultados permiten distinguir:

- Selección geométrica de la configuración de equilibrio.
- Selección dinámica de los soportes estables.
- Multiplicidad de equilibrios dentro de un mismo soporte.
- Transformación del conjunto de equilibrios mediante bifurcaciones.
- Clasificación de equilibrios bajo grupos de simetría.
- Estabilidad local frente a convergencia global.

La existencia de pesos geométricos superiores no garantiza por sí sola dominancia apical universal ni una mayor probabilidad de atracción.

La distribución de las cuencas deberá estudiarse independientemente.

24.9. Reproducción

Desde la carpeta convergence:

python -m pip install numpy scipy
python higher_support_audit.py

El programa genera el archivo:

higher_support_results.json

Los resultados deben interpretarse conjuntamente con las hipótesis, limitaciones y condiciones de aplicación recogidas en HIGHER_SUPPORT_EQUILIBRIA.md.

24.10. Trabajo pendiente

- Certificación rigurosa de raíces y bifurcaciones.
- Enumeración exhaustiva de ramas heterogéneas.
- Clasificación de soportes por composición estratificada.
- Verificación mediante pesos geométricos canónicos fijados por commit.
- Auditoría numérica de perturbaciones exteriores al soporte.
- Estudio no lineal de los casos críticos.
- Clasificación de atractores de soporte superior.
- Correspondencia entre cuencas de atracción y espacios cociente.
- Contraste matemático independiente con la TRCG.

24.11. Estado de la convergencia

La incorporación de estos resultados amplía el programa de investigación desde la clasificación estructural de los equilibrios hacia el estudio de su estabilidad, multiplicidad y transformación dinámica.

Se mantiene la independencia matemática de las formulaciones originales.

La correspondencia estructural no implica equivalencia dinámica.

La evidencia computacional no sustituye a la demostración matemática.

La estabilidad local no implica convergencia global.

24.12. Inventario actualizado

- Archivos anteriores: 36.
- Nuevos archivos de soporte superior: 3.
- Total de archivos en convergence: 39, incluido este README.
- Archivos eliminados: 0.

24.13. Gobernanza

Nivel II retenido.

Nivel III abierto.

Sin ascenso automático.

λ reservado al 4º Factor.

Versiones v1.6 y v1.7 aisladas.

Sin reescalados post hoc.

Campaña experimental del Episodio 44 intacta.

La convergencia continúa mediante demostraciones independientes, auditorías reproducibles y delimitación explícita de las condiciones de validez.

La correspondencia abre el camino; únicamente las demostraciones podrán establecer la equivalencia.

TRCG — CÓDIGO VIAJER — PIRÁMIDE-PARÁBOLA

Nivel II retenido · Nivel III abierto · λ reservado al 4º Factor.

FIN DE DOCUMENTO
