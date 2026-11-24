Relación entre los repositorios Código Viajer y TRCG

Estado del documento: Propuesta de organización arquitectónica
Versión: 1.0
Fecha: 24 de noviembre de 2026

1. Propósito

Este documento establece la relación entre los dos proyectos:

- Código Viajer Spec: especificación e implementación del sistema de control de estabilidad dinámica en cuatro dimensiones.
- TRCG Código Viajer Spec: investigación y desarrollo de modelos matemáticos de mayor dimensión, incluyendo el núcleo de 24 dimensiones y la línea experimental de 47 dimensiones.

Ambos proyectos comparten una línea conceptual de investigación, pero tienen objetivos, niveles de formalización y responsabilidades diferentes.

El propósito de esta separación es evitar duplicidades, preservar la trazabilidad de los resultados y distinguir claramente entre las funcionalidades implementadas y las hipótesis matemáticas todavía en investigación.

2. Repositorios

2.1. Código Viajer Spec

Repositorio:

https://github.com/javier-viajer/codigo-viajer-spec

Responsabilidad principal:

Desarrollar y mantener el modelo operativo de control de estabilidad dinámica en cuatro dimensiones.

El estado se representa mediante:

[
X=(L,S,I,B)\in[0,1]^4
]

El atractor de referencia es:

[
E=(1,0,1,1)
]

La especificación incorpora una distancia dinámica ponderada:

[
D_h=\min(1,w_p d_p+w_v d_v+w_a d_a)
]

donde se consideran:

- Distancia respecto al estado de referencia.
- Velocidad de variación del estado.
- Aceleración de la variación.

La implementación incluye un validador, umbrales de decisión y experimentos con trayectorias sintéticas.

Este repositorio debe ser la referencia para la implementación operativa del modelo 4D.

2.2. TRCG Código Viajer Spec

Repositorio:

https://github.com/javier-viajer/trgc-codigo-viajer-spec

Responsabilidad principal:

Desarrollar y documentar los fundamentos matemáticos y experimentales de la línea TRCG.

El proyecto incluye diferentes niveles de investigación:

Modelo de 24 dimensiones

- Red binaria de 24 nodos.
- Organización en cuatro sectores de seis nodos.
- Matriz de interacción simétrica.
- Restricciones de diagonal nula.
- Simetría cíclica Z₄.
- Descomposición de Fourier.
- Dinámica asíncrona con histéresis.
- Función de potencial y análisis de estabilidad.

Línea experimental de 47 dimensiones

- Estado ampliado de 47 componentes.
- Estructura de conexiones de 276 aristas.
- Proyecciones y restricciones espectrales.
- Experimentos de estabilidad y auditoría.
- Investigación de propiedades adicionales del modelo.

El estado de validación de cada nivel debe mantenerse explícito. Los resultados experimentales no deben presentarse como demostraciones generales si todavía dependen de las condiciones de los experimentos realizados.

3. Relación arquitectónica

La relación entre ambos repositorios es de continuidad conceptual e investigación, no de equivalencia matemática demostrada.

La organización propuesta es:

Nivel| Proyecto| Función
4D| Código Viajer Spec| Modelo operativo y validador
24D| TRCG| Núcleo matemático de red
47D| TRCG| Extensión experimental

Esta clasificación describe la organización del trabajo. No establece por sí misma que el modelo 4D sea una reducción matemática exacta del modelo 24D, ni que el modelo 47D sea una extensión formalmente equivalente del núcleo 24D.

Cualquier relación de reducción, proyección, embedding o equivalencia deberá definirse mediante una construcción matemática explícita y pruebas reproducibles.

4. Límites de responsabilidad

Código Viajer Spec

Debe mantener:

- La especificación del estado 4D.
- El cálculo de la distancia dinámica.
- Las reglas de decisión.
- La implementación del validador.
- Las pruebas unitarias.
- Los benchmarks del modelo operativo.
- La documentación de integración.

TRCG Código Viajer Spec

Debe mantener:

- La definición formal del sistema de 24 dimensiones.
- Las propiedades de la matriz de interacción.
- La estructura de simetría Z₄.
- La dinámica con histéresis.
- El análisis de la función de potencial.
- Las pruebas de estabilidad y convergencia.
- La línea experimental de 47 dimensiones.
- Las auditorías matemáticas y computacionales.

5. Criterios de rigor científico

Los dos repositorios deben distinguir entre cuatro categorías:

1. Definición: una propiedad establecida por definición del modelo.
2. Demostración: una propiedad deducida matemáticamente bajo hipótesis explícitas.
3. Resultado experimental: una observación obtenida mediante simulaciones o pruebas computacionales.
4. Hipótesis: una propiedad propuesta que todavía requiere demostración o validación.

Los resultados de simulaciones deben indicar, cuando corresponda:

- Parámetros utilizados.
- Número de ejecuciones.
- Semillas aleatorias.
- Condiciones iniciales.
- Métricas evaluadas.
- Limitaciones del experimento.

No debe confundirse la ausencia de fallos en una muestra de simulaciones con una garantía matemática universal.

6. Relación entre versiones

Las versiones de ambos proyectos son independientes.

Una actualización del modelo 4D no implica automáticamente una actualización del núcleo TRCG.

Del mismo modo, una nueva versión del modelo 24D o de la línea 47D no implica que el validador 4D haya cambiado.

Cuando una modificación afecte a ambos proyectos, deberá documentarse:

- Qué definición ha cambiado.
- Qué repositorio contiene la fuente canónica.
- Qué interfaces o correspondencias se ven afectadas.
- Qué pruebas deben repetirse.
- Qué resultados dejan de ser compatibles con versiones anteriores.

7. Política de integración

No se recomienda fusionar ambos repositorios en uno solo en esta etapa.

La separación permite:

- Mantener una implementación operativa independiente.
- Desarrollar la investigación matemática sin introducir inestabilidad en el validador.
- Auditar por separado los resultados.
- Evitar que una hipótesis experimental se convierta accidentalmente en una funcionalidad presentada como validada.

Si en el futuro se desarrolla una integración entre ambos modelos, deberá especificarse mediante una interfaz formal que incluya entradas, salidas, transformaciones, invariantes y pruebas de compatibilidad.

8. Criterio de madurez

La madurez de cada nivel debe evaluarse de forma independiente.

- 4D: madurez de implementación, pruebas y reproducibilidad del validador.
- 24D: madurez de las definiciones matemáticas, demostraciones y validación computacional.
- 47D: madurez de la formulación ampliada, auditorías y demostraciones pendientes.

La madurez de un nivel no debe utilizarse como prueba automática de la madurez de los demás.

9. Conclusión

Código Viajer y TRCG forman parte de una misma línea de desarrollo, pero deben conservar responsabilidades diferenciadas.

Código Viajer proporciona el modelo operativo 4D.

TRCG desarrolla los fundamentos matemáticos y las extensiones experimentales de 24D y 47D.

La conexión entre ambos debe construirse de manera explícita, verificable y reproducible.

Principio rector: continuidad conceptual sin confundir equivalencia matemática, implementación operativa y evidencia experimental. 
