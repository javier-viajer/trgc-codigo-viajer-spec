CONVERGENCE — TRCG / CÓDIGO VIAJER

Programa de investigación sobre convergencia relacional

Versión: 1.3.0
Fecha: 2026-11-27
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

---

## 25. Canonical Stability and Equivariant Bifurcations

### 25.1. Research Scope

This research phase extends the canonical relational operator analysis from single-edge equilibria to higher-support equilibria, critical stability curves and equivariant bifurcations.

The analysis concerns the canonical Pyramid-Parabola relational operator.

It does not establish equivalence with TRGC, validate the hybrid operator or modify the frozen Episode 44 experimental campaign.

### 25.2. Canonical Geometry

The geometric parameter is:

$$
\varepsilon=\frac{h_0}{H},
\qquad 0<\varepsilon<\frac16.
$$

The canonical stratum weights are:

$$
g_j=(1-j\varepsilon)^{-1/2},
\qquad j=1,\ldots,6.
$$

The architecture contains 24 nodes distributed across six strata, with four nodes per stratum.

The geometric rotational group and the effective stratified symmetry group of the relational operator remain distinct:

$$
G_{\mathrm{rot}}=\mathbb Z_4,
$$

$$
G_{\mathrm{strat}}=(S_4)^6.
$$

### 25.3. Higher-Support Equilibrium Reduction

For an equilibrium with positive components on its active support, the scalar reduction is:

$$
g_i^{\frac{2\gamma}{\gamma+1}}
p_i^{\frac{\gamma-1}{\gamma+1}}
(1-p_i)=K,
$$

subject to:

$$
p_i>0,
\qquad
\sum_i p_i=1.
$$

The relational equilibrium is reconstructed through:

$$
b_i=\sqrt{\frac{p_i}{1-p_i}},
$$

$$
R_{ij}
=
C_0
\frac{b_i b_j}
{\sum_{k<l}b_kb_l},
\qquad i\neq j.
$$

This reduction provides a common framework for homogeneous and heterogeneous supports.

### 25.4. Spectral Stability Criterion

Define:

$$
\alpha=\frac{\gamma-1}{\gamma+1}.
$$

The auxiliary symmetric matrix is:

$$
A=bb^T-\operatorname{diag}(b_i^2).
$$

Its eigenvalues satisfy:

$$
1=\ell_1>\ell_2\geq\cdots\geq\ell_m.
$$

The internal dynamic modes are:

$$
\eta_k=
1-\mu+
\mu\gamma\frac{1+\ell_k}{1-\ell_k}.
$$

For the canonical operator, with gamma greater than one and positive admissible update parameter, strict local stability is characterized by:

$$
\ell_2<-\alpha.
$$

Strict instability follows when:

$$
\ell_2>-\alpha.
$$

The critical equality is:

$$
\ell_2=-\alpha.
$$

Critical equality requires nonlinear analysis and cannot be classified through linear stability alone.

### 25.5. Canonical Stability Campaign

The numerical campaign covers all 182 stratified compositions of three-node and four-node supports.

| Support size | Compositions |
|---|---:|
| Three nodes | 56 |
| Four nodes | 126 |
| Total | 182 |

The sampled parameters are:

- Epsilon: 0.05 and 0.15.
- Gamma: 1.5 and 2.5.
- Mu: 0.2.
- Undirected relational mass: 1.0.

The reported campaign contains 728 parameter-composition cases.

| Support | Epsilon | Gamma | Stable | Unstable |
|---|---:|---:|---:|---:|
| Three nodes | 0.05 | 1.5 | 56 | 168 |
| Three nodes | 0.05 | 2.5 | 6 | 118 |
| Three nodes | 0.15 | 1.5 | 20 | 132 |
| Three nodes | 0.15 | 2.5 | 6 | 118 |
| Four nodes | 0.05 | 1.5 | 46 | 1150 |
| Four nodes | 0.05 | 2.5 | 0 | 422 |
| Four nodes | 0.15 | 1.5 | 11 | 605 |
| Four nodes | 0.15 | 2.5 | 0 | 420 |
| Total | | | 145 | 3133 |

The corrected accumulated number of located equilibria is 3278.

These counts aggregate different compositions and parameter configurations. They must not be interpreted as simultaneous attractor counts for a single dynamical system.

Complete composition coverage does not imply exhaustive equilibrium root certification.

### 25.6. Critical Curve Campaign

Critical points are investigated through the simultaneous equilibrium equations and the spectral condition:

$$
\ell_2=-\frac{\gamma-1}{\gamma+1}.
$$

The reported critical campaign uses 12 equally spaced geometric parameter values between 0.001 and 0.165.

| Quantity | Count |
|---|---:|
| Stratified compositions | 182 |
| Geometric samples | 12 |
| Parameter-composition cases | 2184 |
| Located critical points | 2022 |
| Cases without a located critical point | 162 |

The resulting sampled critical loci constitute a preliminary bifurcation atlas.

They do not establish continuous branch connectivity, exhaustive root coverage or mathematical nonexistence in cases where no root was located.

### 25.7. Consolidated Critical Classification

The reported numerical and analytical classification is:

| Critical family | Count |
|---|---:|
| Fold candidates | 1120 |
| Refined subcritical pitchfork candidates | 578 |
| Refined heterogeneous S3 multiple points | 180 |
| Exact homogeneous multiple points | 144 |
| Total located critical points | 2022 |
| Cases without a located critical point | 162 |
| Total examined cases | 2184 |

These counts represent sampled critical points rather than independent global bifurcation events.

Numerical classification remains subject to the acceptance tolerances and hypotheses of the corresponding audit procedures.

### 25.8. Simple Fold Candidates

For a simple critical kernel, the local equilibrium reduction takes the form:

$$
0=A\tau+\frac12Bs^2+
\text{higher-order terms},
$$

where:

$$
\tau=\gamma-\gamma_c.
$$

A generic fold requires:

- A one-dimensional critical kernel.
- An invertible noncritical complement.
- Nonzero parameter transversality.
- A nonzero quadratic coefficient.

Under these conditions:

$$
\tau=-\frac{B}{2A}s^2+
\text{higher-order terms}.
$$

The numerical fold classification does not constitute exhaustive global branch certification.

### 25.9. Simple Symmetry-Breaking Bifurcations

For a simple exchange symmetry between two equivalent nodes, the reduced equilibrium equation is:

$$
0=s(a\tau+bs^2+
\text{higher-order terms}).
$$

The effective cubic coefficient must include the correction induced by the noncritical complement.

The reported simple symmetry-breaking campaign identifies 578 refined subcritical pitchfork candidates.

No supercritical pitchfork was reported in this sampled family.

This observation does not exclude supercritical bifurcations in unexplored parameter regions or different operators.

### 25.10. Multiple Equivariant Normal Forms

For a block of r equivalent critical nodes, define:

$$
E_r=
\left\{
x\in\mathbb R^r:
\sum_i x_i=0
\right\}.
$$

The critical dimension is:

$$
\dim E_r=r-1.
$$

The equivariant projection is:

$$
\Pi_r=
I-\frac1r\mathbf1\mathbf1^T.
$$

The reduced equilibrium equation contains the terms:

$$
0=
a\tau x+
c\Pi_r(x^{\odot2})+
d\Pi_r(x^{\odot3})+
e\|x\|^2x+
\cdots.
$$

For a critical block with gamma greater than one:

$$
c=\frac12h''(p_*)<0.
$$

Consequently, multiple symmetry-breaking bifurcations cannot generally be reduced to a scalar cubic pitchfork.

### 25.11. S3 and S4 Branch Families

The principal two-group symmetry-breaking families are:

| Symmetry | Partition | Leading order |
|---|---|---|
| S2 | 1 + 1 | Cubic |
| S3 | 1 + 2 | Quadratic |
| S4 | 1 + 3 | Quadratic |
| S4 | 2 + 2 | Cubic along the balanced direction |

For S3, the characteristic perturbation is:

$$
x=(2s,-s,-s).
$$

For the unbalanced S4 family:

$$
x=(3s,-s,-s,-s).
$$

For the balanced S4 family:

$$
x=(s,s,-s,-s).
$$

Under the stated kernel, complement and crossing hypotheses, the multiple two-group symmetry-breaking branches possess unstable directions.

The reported numerical refinement of 180 heterogeneous S3 candidates supports the applicability of this conditional analytical framework to those sampled points.

### 25.12. Exact Homogeneous Critical Thresholds

For a homogeneous support of size m greater than two:

$$
\gamma_c=\frac{m}{m-2}.
$$

In particular:

| Support | Critical gamma | Critical dimension |
|---|---:|---:|
| Homogeneous triangle | 3 | 2 |
| Homogeneous four-node support | 2 | 3 |

For the homogeneous balanced S4 branch:

$$
s^2=
\frac9{64}(2-\gamma)
+
O((2-\gamma)^2).
$$

This branch is locally subcritical and possesses unstable transverse directions.

The homogeneous critical thresholds are independent of the common stratum weight because that weight cancels under normalization.

### 25.13. Analytical Lower Bounds on Stable Equilibria

For every admissible canonical geometry and:

$$
0<\mu\leq1,
$$

the following lower bounds hold away from the stated critical equalities:

| Gamma regime | Minimum stable equilibria |
|---|---:|
| 1 < gamma < 2 | 306 |
| 2 < gamma < 3 | 300 |
| gamma > 3 | 276 |

These bounds follow from:

- 276 single-edge equilibria.
- 24 homogeneous triangular equilibria.
- 6 homogeneous four-node equilibria.

The bounds are not exhaustive classifications of all stable equilibria.

### 25.14. Exact Geometric Existence Boundary

For gamma equal to one, consider a support containing one node from a lower stratum a and m-1 nodes from a higher stratum b.

The positive-support existence condition is:

$$
\varepsilon<
\frac{2m-3}
{b(m-1)^2-a(m-2)^2}.
$$

Examples include:

| Composition | Critical epsilon |
|---|---|
| 1, 6, 6 | 3/23 |
| 2, 6, 6 | 3/22 |
| 3, 6, 6 | 1/7 |
| 1, 6, 6, 6 | 1/10 |
| 2, 6, 6, 6 | 5/46 |
| 3, 6, 6, 6 | 5/42 |

These are analytical existence boundaries at gamma equal to one.

They must not be confused with complete nonlinear stability boundaries for gamma greater than one.

### 25.15. Implications for Apical Dominance

The canonical operator admits 276 locally stable single-edge equilibria for gamma greater than one.

Their apical distribution is:

| Apical participation | Equilibria |
|---|---:|
| Both nodes apical | 6 |
| One node apical | 80 |
| No apical nodes | 190 |

The persistence of non-apical stable equilibria prevents a general claim of universal apical attraction for the studied canonical operator.

Geometric weighting can influence collective stability without eliminating all non-apical attractors.

Local bifurcation analysis does not determine global attraction basin membership.

### 25.16. New Documentation and Audit Files

This research phase introduces six files:

- `CANONICAL_STABILITY_MAP.md`: canonical stability campaign, spectral criteria and analytical stability boundaries.

- `CANONICAL_BIFURCATIONS.md`: sampled critical curves, fold candidates and bifurcation classification.

- `EQUIVARIANT_NORMAL_FORMS.md`: scalar and multidimensional equivariant normal forms, including S2, S3 and S4 symmetry-breaking mechanisms.

- `canonical_stability_audit.py`: numerical equilibrium search and spectral stability audit.

- `canonical_bifurcation_audit.py`: critical-point search, symmetry classification and nonlinear reduction audit.

- `canonical_bifurcation_results.json`: consolidated summary of stability campaigns, critical points, equivariant normal forms and verification limits.

The repository JSON is explicitly a summary artifact.

It does not contain the complete individual numerical records of the original consolidated results.

### 25.17. Reproduction Procedure

The numerical audit environment requires:

- Python 3.
- NumPy.
- SciPy.

From the convergence directory, the intended reproduction sequence is:

```bash
python canonical_stability_audit.py
```

```bash
python canonical_bifurcation_audit.py --stability-input canonical_stability_results.json
```

The stability JSON generated by the first command is an intermediate artifact.

The repository contains a consolidated summary; full individual records are intended to be generated by executing the audit scripts.

The complete reproduction procedure, including command-line compatibility and any additional intermediate inputs, must be independently checked before claiming successful end-to-end reproduction.

Executing the full audit may replace the repository summary with a larger individual-record artifact.

Preserving the original complete numerical output separately is recommended.

The summary must not be treated as a substitute for individual numerical records, independent execution logs or exhaustive root certification.

### 25.18. Verification Status

| Research component | Status |
|---|---|
| Scalar equilibrium reduction | Analytical |
| Spectral stability criterion | Analytical under stated hypotheses |
| Single-edge stability | Analytical |
| Homogeneous support thresholds | Analytical |
| Geometric existence boundaries | Analytical |
| Coverage of 182 compositions | Reported numerical campaign |
| Stability classification | Reported numerical evidence |
| Sampled critical curves | Reported numerical evidence |
| Simple cubic reduction | Analytical and reported numerical refinement |
| Heterogeneous S3 refinement | Reported numerical evidence |
| Homogeneous S3 and S4 normal forms | Analytical |
| Complete individual records in repository JSON | Not included |
| Independent end-to-end reproduction | Pending |
| Exhaustive root certification | Pending |
| Global branch continuation | Pending |
| Global basin classification | Pending |
| Hybrid operator validation | Pending |
| TRGC equivalence | Not established |

### 25.19. Scientific Limitations

The present research phase does not establish:

- Exhaustive enumeration of heterogeneous equilibria.
- Exhaustive classification of all bifurcations.
- Continuous connectivity of all sampled critical branches.
- Global attraction basin boundaries.
- Universal apical dominance.
- Global strict contractivity.
- Equivalence between TRGC and Codigo Viajer.
- Validation of the hybrid relational operator.

Missing numerical roots must not be interpreted as mathematical nonexistence.

Numerical tolerances must not be interpreted as exact algebraic certification.

### 25.20. Next Research Objectives

The next research phase should investigate:

1. Independent reproduction of the numerical campaigns.
2. Preservation of complete individual numerical records.
3. Pseudo-arclength continuation of equilibrium branches.
4. Exhaustive or interval-certified equilibrium searches.
5. Exceptional higher-order degeneracies.
6. Global attraction basin classification.
7. Basin correspondence under admissible symmetry groups.
8. Dynamical correspondence with independently specified TRGC operators.

### 25.21. Convergence Interpretation

The present analysis establishes a structured connection between:

- Canonical geometry.
- Effective operator symmetry.
- Equilibrium support.
- Spectral stability.
- Critical multiplicity.
- Equivariant bifurcations.
- Relational identity.
- Quotient-space dynamics.

Symmetry breaking does not necessarily produce a new stable relational configuration.

The correspondence between the mathematical structures of both projects remains a research objective rather than an established equivalence.

### 25.22. Governance

The established governance framework remains unchanged:

- Level II retained.
- Level III open.
- No automatic promotion.
- Lambda reserved exclusively for the Fourth Factor.
- Versions v1.6 and v1.7 remain isolated.
- No post hoc rescaling.
- Episode 44 remains frozen.
- No automatic validation of the hybrid operator.
- No automatic equivalence between TRGC and Codigo Viajer.

Correspondence opens the research path.

Only demonstrations can establish equivalence.

---

## 26. Canonical Computational Reproducibility

### 26.1. Purpose

The canonical stability and equivariant bifurcation campaigns have been subjected to a reported same-algorithm computational reproduction.

The objective is to verify numerical consistency while preserving the published mathematical definitions, campaign parameters and acceptance tolerances.

This verification does not constitute exhaustive mathematical certification or validation through an alternative algorithm.

### 26.2. Audited Repository Reference

Repository:

https://github.com/javier-viajer/trgc-codigo-viajer-spec

Audited commit:

6d8a99c74f45a6518cd892d6b633ca8362e853df

The published audit programs are identified by their Git blob hashes:

| Program | Git blob SHA |
|---|---|
| canonical_stability_audit.py | c1e9e2a4aaeea1ff4652d886ce55124abe9065c6 |
| canonical_bifurcation_audit.py | 02d67cdb40638d5504457dfd5a63a880a34aff12 |

The retained local source files match these repository identifiers.

### 26.3. Computational Environment

The reported reproduction environment is:

- Python 3.13.5.
- NumPy 2.3.5.
- SciPy 1.17.0.

Cross-platform byte-level reproducibility has not been established.

### 26.4. Stability Reproduction

| Quantity | Expected | Observed |
|---|---:|---:|
| Parameter-composition cases | 728 | 728 |
| Located equilibria | 3278 | 3278 |
| Stable equilibria | 145 | 145 |
| Unstable equilibria | 3133 | 3133 |

Maximum matrix equilibrium residual:

$$
r_{\mathrm{max}}
=
4.718447854656915\times10^{-14}.
$$

The retained numerical artifacts reproduce the reported aggregate classification.

### 26.5. Critical Curve Reproduction

| Critical family | Expected | Observed |
|---|---:|---:|
| Fold candidates | 1120 | 1120 |
| Simple subcritical candidates | 578 | 578 |
| Heterogeneous multiple candidates | 180 | 180 |
| Homogeneous multiple points | 144 | 144 |
| Located critical points | 2022 | 2022 |
| Missing critical points | 162 | 162 |
| Total examined cases | 2184 | 2184 |

Maximum critical equation residual:

$$
r_{\mathrm{critical}}
=
9.715907189900008\times10^{-9}.
$$

The critical classifications remain numerical and local.

Missing roots remain unresolved cases.

### 26.6. Multiple-Point Reproduction

All 180 heterogeneous multiple candidates in the retained numerical artifact satisfy the implemented numerical hypothesis checks for the corresponding S3 normal form.

Maximum refinement residual:

$$
r_{\mathrm{multiple}}
=
5.204170427930421\times10^{-16}.
$$

This result does not constitute interval-certified verification of every candidate.

### 26.7. Complete Artifact Integrity

The complete regenerated bifurcation artifact contains 2874010 bytes.

Its SHA-256 identifier is:

```text
607b6f246d18529fe847d112fdb063b9bca975e488385e595c745971db91386f
```

The original complete artifact and the regenerated artifact have matching SHA-256 identifiers.

The intermediate stability artifact contains 623610 bytes.

Its SHA-256 identifier is:

```text
7e399f265e2972f79ba818517fd2b9eea56b1038daa92eb7bab1dec1c379266d
```

The intermediate stability records also match the stability records embedded in the complete bifurcation artifact.

### 26.8. Summary and Complete Artifact Distinction

The repository file:

canonical_bifurcation_results.json

contains a consolidated summary.

It does not contain the complete individual numerical records.

Consequently, the SHA-256 identifier of the complete artifact must not be applied to the repository summary.

Complete numerical artifacts should be preserved separately and regenerated when required.

### 26.9. Reproduction Procedure

From the convergence directory:

```bash
python canonical_stability_audit.py
```

Then:

```bash
python canonical_bifurcation_audit.py \
  --stability-input canonical_stability_results.json \
  --output canonical_bifurcation_results_full.json
```

The explicit output argument preserves the repository summary.

For a complete reproduction from scratch, no previously generated critical-input file should be supplied.

### 26.10. New Reproducibility Documents

This research phase introduces:

- `CANONICAL_REPRODUCIBILITY.md`: formal documentation of the reported computational reproduction, audited source identifiers, artifact hashes, numerical controls and scientific limitations.

- `canonical_reproducibility_results.json`: compact machine-readable record of the reproduction results and verification status.

These documents complement the canonical stability and bifurcation files introduced in Section 25.

### 26.11. Updated Verification Status

The computational reproduction reported in this section updates the pending same-algorithm reproduction status recorded in Section 25.

| Verification component | Status |
|---|---|
| Same-algorithm computational reproduction | Reported successful |
| Source file integrity | Verified |
| Complete artifact hash agreement | Verified |
| Stability aggregate counts | Verified |
| Critical aggregate counts | Verified |
| Cubic classification counts | Verified |
| Multiple-point numerical checks | Verified from retained records |
| Numerical residual checks | Verified |
| Independent alternative algorithm | Pending |
| Cross-platform reproducibility | Pending |
| Exhaustive root certification | Pending |
| Global branch continuation | Pending |
| Global basin classification | Pending |
| Hybrid operator validation | Not tested |
| TRGC equivalence | Not established |

### 26.12. Scientific Interpretation

Computational reproducibility strengthens the numerical evidence supporting the canonical stability and bifurcation research program.

However:

- Reproducibility does not imply exhaustive classification.
- Identical numerical outputs do not exclude shared algorithmic errors.
- Numerical agreement does not replace mathematical demonstration.
- Local stability does not determine global attraction basins.
- Symmetry breaking does not guarantee the emergence of stable configurations.

The distinction between analytical results, numerical evidence and unresolved research objectives remains mandatory.

### 26.13. Next Research Phase

The next objectives are:

1. Independent equilibrium search algorithms.
2. Independent Jacobian and spectral verification.
3. Pseudo-arclength continuation of equilibrium branches.
4. Detection of additional critical branches.
5. Interval-certified equilibrium searches.
6. Global attraction basin classification.
7. Basin correspondence under admissible symmetry groups.
8. Independent TRGC operator correspondence.

The transition toward global basin analysis must preserve the established local stability and bifurcation results without assuming exhaustive root coverage.

### 26.14. Governance

The established governance framework remains unchanged:

- Level II retained.
- Level III open.
- No automatic promotion.
- Lambda reserved exclusively for the Fourth Factor.
- Versions v1.6 and v1.7 remain isolated.
- No post hoc rescaling.
- Episode 44 remains frozen.
- No automatic hybrid operator validation.
- No automatic equivalence between TRGC and Codigo Viajer.

Computational reproducibility strengthens the evidence.

Correspondence opens the research path.

Only demonstrations can establish equivalence.

---

27. Canonical Lyapunov Function and Global Relational Convergence
27.1. Scope
The fixed-parameter canonical relational operator on the nonnegative symmetric zero-diagonal fixed-mass simplex is studied for positive weights, gamma>0 and 0<mu<=1. No operator modification is introduced. Multiple Perron eigenvalues are handled through the correspondence of all admissible nonnegative unit Perron selections.
27.2. Weighted Lyapunov theorem
$$\mathcal L_{\gamma,g}(R)=\frac{\rho(R)}{\left(\sum_{i<j}R_{ij}^{1+1/\gamma}/(g_i g_j)\right)^{\gamma/(\gamma+1)}}.$$
Rayleigh and weighted Holder inequalities prove strict increase at every nonstationary update, for every admissible Perron selection. The function is invariant under weight-preserving permutations.
27.3. Finiteness and global convergence
The exact scalar fixed-point reduction, analytic inverse branches and endpoint analysis prove finiteness for every fixed admissible parameter set. For gamma<1 there is one equilibrium per support of size at least two (16,777,191 for N=24); for gamma=1 at most one per support. The count for gamma>1 is not determined. Compactness of the Perron-pair graph and strict Lyapunov increase imply stationary accumulation points and vanishing step sizes. Finiteness then proves convergence of every trajectory to a single equilibrium, not necessarily the same equilibrium for different initial states. No global strict contraction or universal apical selection follows.
27.4. Homogeneous three-node simplex
Gamma regime
Fixed points
Asymptotically stable points
Basin classification
0<gamma<=1
4
1
Complete
1<gamma<3
7
4
Destinations and median thresholds; global separatrix geometry pending
gamma=3
4
3
Complete
gamma>3
7
3
Complete
At gamma=3 the top-gap factor is 1-4 mu c+O(||r-U||^2), where c is the smallest coordinate deviation. Unique maxima converge to the corresponding edge vertex; tied maxima converge to U. For gamma>3 the tied-maximum segments instead converge to saddles, except U itself. In the coexistence regime the three saddle stable sets contain all attracting-basin boundaries collectively; global regularity and exact shared-boundary equality remain pending.
27.5. Numerical audit
Control
Result
Sampled canonical updates
1440
Decreases below -1e-12
0
Minimum sampled increment
1.1467007343668456e-9
Multiple-Perron selections (homogeneous weights)
44
Minimum multiple-Perron increment
0.04831863081163845
Reverse-direction negative control
-0.0014922493410753912
Critical coefficient samples
9
Saddle examples
7
Maximum saddle fixed-point residual
8.798517470154366e-15
Seed 49. Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0. The portable script was rerun and its JSON matched the retained original byte for byte. The only script change was the output path (relative to the script). These controls are not exhaustive or an alternative-algorithm validation.
27.6. Files and reproduction
HOMOGENEOUS_SIMPLEX_BASINS.md
CANONICAL_LYAPUNOV_FUNCTION.md
GLOBAL_RELATIONAL_CONVERGENCE.md
canonical_lyapunov_audit.py
canonical_lyapunov_results.json
Run from convergence:
python canonical_lyapunov_audit.py
This regenerates the results JSON beside the script. It contains parameter-block aggregates and individual critical, saddle and multiple-Perron controls, not all random initial states.
27.7. Quotient and next objectives
The Lyapunov function descends under weight-preserving permutations. Heteroclinic connections between distinct equilibria must respect strict Lyapunov ordering; directed cycles are excluded. Actual connection existence and basin adjacency remain to be established. Next objectives: global coexistence separatrices, heterogeneous basin classification, independent numerical methods, and explicit connection graphs. No hybrid or TRGC equivalence claim.
27.8. Governance
Level II retained. Level III open. No automatic promotion. Lambda reserved for the Fourth Factor. v1.6 and v1.7 isolated. No post hoc rescaling. Episode 44 frozen.



TRCG — CÓDIGO VIAJER — PIRÁMIDE-PARÁBOLA

Nivel II retenido · Nivel III abierto · λ reservado al 4º Factor.

FIN DE DOCUMENTO
