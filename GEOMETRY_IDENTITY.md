IDENTIDAD GEOMÉTRICA DE PIRÁMIDE-PARÁBOLA

Programa de convergencia TRCG — Código Viajer

Versión: 0.1.0
Estado: formalización matemática preliminar
Clasificación: desarrollo teórico abierto

1. Objetivo

Establecer una definición matemática verificable de la identidad geométrica de Pirámide-Parábola y determinar las condiciones bajo las cuales dicha identidad permanece conservada.

El objetivo no consiste en presuponer una equivalencia con la TRCG, sino en investigar las condiciones necesarias para establecerla.

2. Representación relacional multicapa

Se define una arquitectura relacional finita mediante:

𝓡 = (V, A₁, A₂, …, Aₘ)

Donde:

- V representa el conjunto de nodos.
- Aₖ representa la matriz correspondiente a la familia relacional k.
- m representa el número de familias relacionales.

Para la arquitectura candidata de Pirámide-Parábola:

V = ℤ₂₄

Las relaciones pueden ser simétricas, dirigidas, ponderadas o incorporar restricciones adicionales.

No se presupone que todas las propiedades de Pirámide-Parábola puedan representarse exclusivamente mediante matrices diádicas.

Las relaciones de orden superior deberán incorporarse mediante estructuras matemáticas adecuadas cuando resulte necesario.

3. Identidad matricial

Dos arquitecturas presentan identidad matricial cuando:

Aₖ = Bₖ para todo k.

Esta condición exige igualdad de todas las relaciones y de su representación ordenada.

4. Identidad por reetiquetado

Dos arquitecturas son relacionalmente equivalentes cuando existe una misma matriz de permutación P tal que:

Bₖ = PAₖPᵀ para todo k.

La permutación debe actuar simultáneamente sobre todas las familias relacionales.

No se permite seleccionar una permutación diferente para cada capa.

Esta definición presupone que las familias relacionales poseen identidades diferenciadas y que sus etiquetas deben conservarse.

5. Grupo de identidad geométrica

Se define:

G(𝓡) = {P ∈ Sₙ : PAₖPᵀ = Aₖ para todo k}

Este conjunto contiene las transformaciones que preservan simultáneamente todas las capas matriciales consideradas.

Cuando la representación es completa y fiel, constituye el grupo de automorfismos de la arquitectura relacional.

6. Separación entre geometría y dinámica

Se distinguen dos procesos:

x(t+1) = F𝓡(x(t))

𝓡(t+1) = T(𝓡(t))

El primero representa la evolución de los estados.

El segundo representa la evolución de la propia estructura relacional.

No se presupone que ambos operadores sean equivalentes ni que compartan los mismos invariantes.

7. Equivarianza dinámica

Una dinámica F𝓡 es equivariante respecto de G(𝓡) cuando:

F𝓡(Px) = PF𝓡(x)

para todo P perteneciente a G(𝓡) y todo estado admisible x.

Esta propiedad deberá demostrarse independientemente para los operadores 44A y 44B.

Si el operador depende del orden de actualización, de parámetros asociados a los nodos o de variables aleatorias, estos elementos deberán incluirse en la transformación correspondiente.

8. Correspondencia con la TRCG

Se considera el espacio relacional estudiado en el Episodio 43:

S = {R ∈ ℝᴺˣᴺ : Rᵀ = R, diag(R) = 0}

La correspondencia candidata se expresa mediante:

Φ : 𝓡PP → S

La existencia de esta aplicación no implica automáticamente que conserve toda la información geométrica.

Deberán estudiarse:

- Inyectividad.
- Conservación de relaciones.
- Compatibilidad con las simetrías.
- Conservación de invariantes.
- Compatibilidad dinámica.
- Recuperación de información.

Si existen capas dirigidas o relaciones de orden superior, deberá justificarse su representación dentro de S o utilizarse un espacio relacional ampliado.

9. Criterio de identificabilidad

Una colección de invariantes J identifica una arquitectura dentro de una clase de comparación cuando:

J(𝓡₁) = J(𝓡₂) implica 𝓡₁ ~ 𝓡₂.

La equivalencia utilizada deberá definirse previamente.

La coincidencia espectral o la igualdad del orden de los grupos de simetrías no garantizan por sí solas la equivalencia relacional.

10. Clasificación epistemológica

Resultados establecidos

- Definición de identidad matricial.
- Definición de equivalencia por reetiquetado simultáneo.
- Separación formal entre evolución estructural y evolución de estados.
- Definición de equivarianza e identificabilidad.

Cuestiones abiertas

- Representación canónica completa de Pirámide-Parábola.
- Grupo completo de automorfismos.
- Invariantes específicos de la arquitectura.
- Equivarianza de 44A y 44B.
- Correspondencia matemática con la TRCG.

11. Gobernanza científica

- Nivel II retenido.
- Nivel III abierto.
- Sin ascenso automático.
- λ reservado al 4º Factor.
- Versiones v1.6 y v1.7 aisladas.
- Sin reescalados post hoc.
- Protocolos experimentales congelados.

La identidad geométrica debe demostrarse. La correspondencia relacional debe verificarse. La integración entre modelos no debe presuponerse.
