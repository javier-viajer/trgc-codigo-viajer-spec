ARCHITECTURE.md
Arquitectura de Código Viajer y TRCG
Estado del documento: propuesta de arquitectura para revisión
Versión de referencia: repositorio v1.7
Fecha de elaboración: 24 de noviembre de 2026
Alcance: descripción de las capas, sus responsabilidades, interfaces conocidas y cuestiones pendientes.
Nota de rigor: este documento organiza la arquitectura descrita en el repositorio. No certifica por sí mismo el código, las simulaciones ni las afirmaciones matemáticas. Las relaciones entre las representaciones 4D, 24D y 47D que no estén definidas explícitamente se marcan como pendientes.

1. Propósito
El repositorio contiene dos líneas relacionadas, pero conceptualmente distintas:
Código Viajer: validador dinámico operativo que representa el estado de un agente mediante cuatro variables y emite decisiones ALLOW, THROTTLE o REJECT.
TRCG / Pirámide-Parábola: marco matemático en desarrollo, con modelos estructurales y dinámicos propios.
La arquitectura experimental de v1.7 añade una representación de 47 dimensiones. Esta representación debe documentarse como una línea experimental específica y no confundirse con el estado operativo 4D ni con el núcleo estructural 24D.
El objetivo de este documento es establecer una terminología común y evitar que distintas dimensiones, matrices o experimentos se presenten como si fueran una única arquitectura indiferenciada.
2. Principios arquitectónicos
La evolución del repositorio debe respetar los siguientes principios:
Separación de responsabilidades: el validador operativo y los modelos matemáticos no deben depender implícitamente unos de otros.
Trazabilidad: cada resultado debe poder vincularse a su código, configuración, datos de entrada, versión y procedimiento de ejecución.
Reproducibilidad: una afirmación experimental debe acompañarse de los artefactos necesarios para repetirla.
Separación epistemológica: una definición, una hipótesis, una observación numérica y un teorema son categorías diferentes.
Compatibilidad controlada: los cambios de una versión experimental no deben modificar silenciosamente una versión estable anterior.
Interfaces explícitas: toda transformación entre espacios debe tener una definición matemática y una implementación identificable.
3. Vista general de las capas
La arquitectura que puede reconstruirse a partir de la documentación actual es:
                         REPOSITORIO
                              |
              +---------------+----------------+
              |                                |
       CÓDIGO VIAJER                         TRCG
       Capa operativa                 Marco matemático
              |                                |
       Estado en R^4                 +----------+----------+
       X = (L,S,I,B)                 |                     |
              |                  Núcleo 24D          Dinámica
       Evaluación de                 |                     |
       trayectoria              J_(24 x 24)          Modelos y
              |                  Z_4 / 264            operadores
       ALLOW / THROTTLE /
          REJECT
                                               |
                                      Línea experimental v1.7
                                               |
                                      Estado de dimensión 47
                                      (mass_24, state_22, theta)
El diagrama expresa una separación documental y funcional. No representa una transformación matemática demostrada entre los espacios.
3.1. Capa operativa: Código Viajer 4D
La documentación del repositorio define el estado del agente como:
[ \mathbf X=(L,S,I,B)\in[0,1]^4 ]
con las etiquetas:
L: Life Preservation.
S: Entropy.
I: Node Integrity.
B: Resource.
El validador evalúa trayectorias en este espacio y contempla tres decisiones:
ALLOW
THROTTLE
REJECT
La documentación disponible no especifica en un único contrato formal todos los detalles necesarios para reproducir la decisión: significado operacional y orientación de cada variable, normalización, umbrales, reglas de precedencia, tratamiento de valores ausentes, persistencia del estado y política ante errores.
Estos detalles deben obtenerse del código y de sus pruebas antes de declarar una especificación ejecutable completa.
Responsabilidad de esta capa: evaluar el estado y la trayectoria del agente y producir una decisión operativa bajo reglas explícitas.
No debe asumirse: que las cuatro variables son una proyección demostrada del espacio 24D o del espacio 47D.
3.2. Capa estructural TRCG: núcleo 24D
STATUS.md describe un núcleo de 24 nodos organizado como 46, construido a partir de una estructura de 264 triples y de su 2-sección.
La documentación registra una matriz:
[ J_{24}\in\mathbb R^{24\times24} ]
y un análisis de simetría y descomposición modal asociado a \(\mathbb Z_4\), con cuatro bloques de tamaño 66.
La documentación informa, entre otros resultados, de simetría de la matriz, diagonal nula, equivariancia \(\mathbb Z_4\) y reconstrucción espectral mediante bloques. Estos resultados se consideran resultados declarados por los artefactos de v1.7, pendientes de reproducción independiente en esta revisión.
La relación entre los 264 triples y las aristas de la 2-sección debe describirse mediante una definición de construcción inequívoca. No debe confundirse automáticamente el número de triples con el número de aristas de un grafo.
Responsabilidad de esta capa: representar la estructura relacional de 24 nodos y estudiar sus propiedades combinatorias, matriciales y modales.
3.3. Capa dinámica experimental: espacio 47D de v1.7
La auditoría AUDITORIA_v17_modo_a.md describe una arquitectura experimental de dimensión 47:
[ z=(m_{24},s_{22},\theta)\in\mathbb C^{47} ]
donde:
mass_24: bloque de 24 componentes.
state_22: bloque de 22 componentes.
: una variable adicional.
La suma de dimensiones es:
[ 24+22+1=47. ]
La auditoría también describe un grafo de 276 aristas, un acoplamiento 34, movimiento helicoidal, conexiones entre triángulo y cruz, nodos contiguos y una denominada Matriz de la Suma 23.
La matriz dinámica se representa como:
[ J_{47}\in\mathbb C^{47\times47}. ]
Se informa de un modo neutro asociado a  y de un análisis de estabilidad transversal mediante proyección. Las cifras y sus condiciones se documentan en AUDITORIA_v17_modo_a.md y en los artefactos de v1.7/.
Responsabilidad de esta capa: estudiar la dinámica experimental de la representación 47D y sus propiedades espectrales y de cuasi-estacionariedad bajo las condiciones ensayadas.
No debe asumirse: que el bloque mass_24 es idéntico, en todos sus detalles, al núcleo estructural 24D de STATUS.md. Esa correspondencia requiere una definición de variables, orden, unidades, reglas de actualización y pruebas de identidad.
4. Relación entre las representaciones
La documentación actual contiene tres representaciones:
Representación
Dimensión
Función documentada
Estado
Código Viajer
4
Estado operativo y decisiones
Capa principal descrita en README
Núcleo TRCG
24
Estructura relacional y análisis \(\mathbb Z_4\)
Documentado en STATUS
Dinámica v1.7
47
Modelo dinámico experimental
Documentado en auditoría v1.7

No existe en la documentación consultada una definición suficiente para afirmar una aplicación formal entre ellas.
Para cerrar esta cuestión se necesita especificar, como mínimo:
Dominio y codominio de cada transformación.
Definición de las variables de origen y destino.
Orden de coordenadas.
Normalización y unidades.
Si la transformación es lineal, afín o no lineal.
Si conserva alguna estructura (simetría, norma, energía, orden o invariantes).
Condiciones bajo las que es válida.
Pruebas que comprueben la implementación.
Hasta que se documente, deben utilizarse expresiones como «representaciones relacionadas dentro del proyecto» y evitar «proyección», «reducción» o «derivación» cuando no exista una aplicación formal que las justifique.
5. Flujo operativo y contrato de decisiones
El flujo conceptual de Código Viajer es:
Entrada del estado / trayectoria
              |
              v
       Validación de entrada
              |
              v
     Evaluación de variables 4D
              |
              v
    Aplicación de reglas y umbrales
              |
              v
       Decisión operativa
              |
      +-------+--------+
      |       |        |
    ALLOW  THROTTLE  REJECT
Este flujo es una vista lógica, no una afirmación de que el código actual implemente exactamente esas etapas o ese orden.
La especificación ejecutable debe definir:
Esquema de entrada y tipos.
Rango permitido de cada variable.
Tratamiento de NaN, infinitos, null y campos ausentes.
Umbrales y comparadores (<, <=, >, >=).
Precedencia cuando varias reglas se activan.
Significado y efecto de cada decisión.
Datos de salida y códigos de error.
Registro de versión y configuración.
Comportamiento seguro ante fallos.
No debe afirmarse que REJECT o THROTTLE garantizan seguridad del agente sin una definición de amenazas, alcance y pruebas que sustenten esa garantía.
6. Organización recomendada del repositorio
La estructura observada incluye dynamics/, tests/, v1.7/, AUDITORIA_v17_modo_a.md, README.md y STATUS.md.
Como objetivo de organización —no como descripción de rutas ya verificadas— se recomienda:
/
├── README.md
├── ARCHITECTURE.md
├── MATHEMATICAL_FOUNDATIONS.md
├── STATUS.md
├── AUDITORIA_v17_modo_a.md
├── core/
├── dynamics/
├── boundary/
├── tests/
└── v1.7/
Antes de crear, mover o renombrar carpetas, comprobar el árbol real y las importaciones existentes. No se deben crear directorios vacíos solo para que el repositorio coincida con este esquema.
7. Versionado y aislamiento
La versión canónica indicada por el README y STATUS consultados es v1.7.
La auditoría declara que v1.7 se mantiene aislada de v1.6.
Cualquier modificación debe conservar la trazabilidad de los artefactos originales.
Las pruebas de una versión no deben sobrescribir resultados de otra.
Una nueva versión debe tener manifiesto, configuración, pruebas y registro de cambios propios.
No se debe declarar que el aislamiento está garantizado solo por una afirmación documental: debe verificarse mediante rutas, historial, dependencias y pruebas.
8. Riesgos y cuestiones abiertas
ID
Cuestión
Evidencia necesaria para cerrarla
ARC-01
Relación 4D–24D
Definición formal de la aplicación y tests
ARC-02
Relación 24D–47D
Correspondencia de coordenadas y operadores
ARC-03
264 triples y 2-sección
Algoritmo de construcción y recuentos reproducibles
ARC-04
276 aristas en v1.7
Definición del grafo, nodos y regla de arista
ARC-05
Contrato de decisiones
Especificación extraída y contrastada con el código
ARC-06
Aislamiento v1.6/v1.7
Verificación de rutas, imports y artefactos
ARC-07
Dependencias entre módulos
Grafo de imports y pruebas de integración

9. Criterios de aceptación de esta arquitectura
Esta arquitectura podrá considerarse consolidada cuando:
Cada capa tenga una responsabilidad inequívoca.
Las dimensiones y variables estén definidas sin ambigüedad.
Las relaciones entre espacios estén formalizadas o se declaren explícitamente inexistentes/no definidas.
La construcción del núcleo 24D pueda reproducirse desde sus datos de origen.
La construcción del modelo 47D pueda reproducirse desde su configuración.
El contrato operativo 4D coincida con el comportamiento del código.
Los tests cubran las interfaces y los casos límite.
Las versiones y sus artefactos permanezcan trazables.
10. Fuentes internas de referencia
README.md: definición inicial de Código Viajer y separación respecto de TRCG.
STATUS.md: núcleo 24D, estructura de 264 triples, análisis \(\mathbb Z_4\), función V y estado epistemológico.
AUDITORIA_v17_modo_a.md: arquitectura experimental 47D, grafo de 276 aristas y resultados espectrales declarados.
tests/, dynamics/ y v1.7/: deben inspeccionarse directamente para confirmar implementación, dependencias y reproducibilidad.

Estado final: documento de arquitectura propuesto. No constituye certificación matemática, auditoría de seguridad ni validación independiente del software
