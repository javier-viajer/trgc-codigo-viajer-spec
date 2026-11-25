ABLACIÓN ESTRUCTURAL E ÍNDICE DE RESTRICCIÓN DE SIMETRÍAS

Programa de convergencia TRCG — Código Viajer

Versión: 0.1.0
Estado: formalización analítica y protocolo propuesto

1. Objetivo

Determinar la contribución de cada familia relacional a la restricción de las simetrías de Pirámide-Parábola y estudiar su posible relación con las propiedades dinámicas observadas.

2. Definición de ablación estructural

Sea:

𝓡 = (V, A₁, …, Aₘ)

Se define la ablación de la familia k como:

𝓡₋ₖ = (V, A₁, …, Aₖ₋₁, Aₖ₊₁, …, Aₘ)

La ablación conserva el conjunto de nodos y elimina exclusivamente la restricción relacional seleccionada.

No modifica las demás capas.

3. Teorema de monotonía de simetrías bajo ablación

Sean:

G = ⋂ⱼ Gⱼ

G₋ₖ = ⋂ⱼ≠ₖ Gⱼ

Entonces:

G ⊆ G₋ₖ.

Demostración

Toda transformación que conserva todas las familias relacionales conserva necesariamente cualquier subconjunto de ellas.

Por tanto, eliminar una restricción no puede reducir el grupo de automorfismos.

Queda demostrada la inclusión.

4. Índice de restricción de simetrías

Se propone:

Dₖ = log₂(|G₋ₖ| / |G|)

Por el teorema de Lagrange:

|G₋ₖ| / |G| ∈ ℕ.

Por tanto:

Dₖ ≥ 0.

Interpretación

Dₖ = 0:

La familia eliminada no restringe adicionalmente el grupo de simetrías en presencia de las demás familias.

Dₖ > 0:

La familia contribuye a restringir el grupo de simetrías.

El índice se expresa en bits logarítmicos de cardinalidad.

No constituye por sí mismo una entropía de Shannon ni una medida de información dinámica.

5. Independencia de representación

Sea P una permutación común de todos los nodos.

Las matrices transformadas satisfacen:

A′ₖ = PAₖPᵀ.

Los grupos correspondientes son conjugados:

G′ = PGPᵀ.

G′₋ₖ = PG₋ₖPᵀ.

Como la conjugación conserva la cardinalidad de los grupos:

D′ₖ = Dₖ.

Por tanto, el índice es independiente del reetiquetado simultáneo de los nodos.

6. Primera aplicación analítica

Se considera la subestructura provisional:

C: contigüidad circular.

S23: Suma 23.

T8: relaciones de paso 8.

X6: relaciones de paso 6.

El grupo conjunto tiene orden:

|G| = 4.

Al eliminar S23, permanece el grupo diédrico del ciclo:

|G₋S23| = 48.

Por tanto:

Dₛ₂₃ = log₂(48/4)

Dₛ₂₃ = log₂(12)

Dₛ₂₃ ≈ 3,5849625.

Este resultado demuestra que Suma 23 restringe las simetrías de la subestructura considerada.

No demuestra todavía su relevancia dinámica ni su contribución en la arquitectura canónica completa.

7. Ablaciones adicionales

La eliminación individual de T8 no modifica el grupo parcial, puesto que las cuatro simetrías restantes ya conservan esa capa.

Por tanto:

Dₜ₈ = 0.

Análogamente:

Dₓ₆ = 0.

El cálculo de la ablación de C queda pendiente.

Estos resultados no implican que T8 y X6 sean prescindibles para la dinámica o para la identidad geométrica completa.

8. Ablaciones conjuntas

Para un subconjunto K de familias relacionales se define:

G₋K = ⋂ⱼ∉K Gⱼ.

Y:

D(K) = log₂(|G₋K| / |G|).

Se cumple:

D(K) ≥ 0.

Si K₁ ⊆ K₂, entonces:

D(K₁) ≤ D(K₂).

El índice no se presupone aditivo.

La eliminación conjunta de familias puede revelar restricciones que no aparecen mediante ablaciones individuales.

9. Separación entre relevancia estructural y dinámica

La igualdad Dₖ = 0 no implica que la familia relacional sea dinámicamente redundante.

Una capa puede modificar:

- Estabilidad.
- Cuencas de atracción.
- Diversidad de atractores.
- Velocidad de convergencia.
- Conservación de información.
- Sensibilidad a perturbaciones.

Por tanto, la relevancia respecto a las simetrías y la relevancia dinámica deberán estudiarse independientemente.

10. Protocolo experimental propuesto

Se compararán:

- Arquitectura nominal.
- Ablaciones individuales.
- Ablaciones conjuntas.
- Arquitecturas nulas.
- Arquitecturas alternativas.

Cada arquitectura se estudiará mediante 44A y 44B.

Se mantendrán condiciones experimentales equivalentes, incluyendo las semillas, estados iniciales y criterios de convergencia cuando el diseño lo permita.

Las comparaciones deberán controlar las diferencias de densidad, distribución de grados, pesos, conectividad y demás propiedades relevantes.

11. Magnitudes de evaluación

Estructurales

- Orden del grupo de automorfismos.
- Índice de restricción Dₖ.
- Espectro matricial.
- Órbitas de nodos y relaciones.
- Clases de equivalencia estructural.

Dinámicas

- Tasa de convergencia.
- Número de atractores.
- Entropía de atractores.
- Distribución de cuencas.
- Equivarianza.
- Recuperabilidad de estados.

La entropía de atractores se define mediante:

H(A) = −Σᵢ pᵢ log₂(pᵢ).

El número efectivo de atractores es:

Nef = 2ᴴ⁽ᴬ⁾.

La distribución de probabilidades deberá estimarse mediante un protocolo previamente especificado.

12. Hipótesis experimental

H₀:

Las diferencias estructurales estudiadas no producen efectos dinámicos diferenciables bajo los operadores y controles considerados.

H₁:

Al menos una diferencia estructural produce efectos dinámicos diferenciables y reproducibles bajo las condiciones consideradas.

No se presupone una relación monótona entre Dₖ y las magnitudes dinámicas.

13. Criterios de validación

- Definición canónica versionada.
- Enumeración verificable de los automorfismos.
- Reproducción independiente.
- Controles nulos adecuados.
- Métricas preespecificadas.
- Tratamiento de comparaciones múltiples.
- Registro de resultados negativos.
- Ausencia de ajustes retrospectivos.

Los análisis nuevos deberán registrarse como extensiones prospectivas o exploratorias, sin modificar los criterios congelados del Episodio 44.

14. Gobernanza científica

Nivel II retenido.

Nivel III abierto.

λ reservado al 4º Factor.

Versiones v1.6 y v1.7 aisladas.

Sin reescalados post hoc.

Sin ascenso automático de nivel.

15. Conclusión

La ablación estructural permite investigar la contribución de cada familia relacional a la restricción de simetrías.

La existencia de una contribución estructural no implica automáticamente una contribución dinámica.

La relación entre ambas deberá establecerse mediante demostraciones matemáticas y resultados experimentales reproducibles.
