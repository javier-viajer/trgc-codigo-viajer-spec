Identidad geométrica relacional
Versión 0.2.0 — revisión de alcance canónico.
1. Objeto matemático
Una arquitectura relacional finita es (V,(R_k)_k), con relaciones etiquetadas R_k⊆V^{a_k}, admitiendo pesos, orientación y aridad superior. Para capas binarias ponderadas se emplean matrices A_k. Los atributos de nodos y restricciones de estados se conservan como objetos adicionales, no como aristas ficticias.
La identidad exacta exige igualdad de todos los datos con etiquetas fijas. La equivalencia estructural exige una biyección p que transporte simultáneamente cada relación, atributo y restricción. Para matrices: A'_k=P A_k Pᵀ. La composición y la inversión de biyecciones hacen de esta equivalencia una relación de equivalencia.
2. Simetría e identificabilidad
Aut(R) es el conjunto de biyecciones que preservan todos los datos. Para capas matriciales es la intersección de los estabilizadores de A_k. Un descriptor J es invariante si J(pR)=J(R); es completo en una clase si la igualdad de descriptores implica equivalencia. El espectro por sí solo no garantiza completitud.
3. Estados y estructura
Distinguir x_{t+1}=F_R(x_t) de R_{t+1}=T(R_t). La equivarianza requiere F_{pR}(px)=pF_R(x), con transformación coherente de parámetros, órdenes y ruido. La simetría de R no demuestra esta igualdad. La invertibilidad de F, de T y de una transformación de etiquetas son problemas distintos; la recuperación asintótica tampoco se deduce de la invertibilidad finita.
4. Correspondencia TRCG
Una representación Φ hacia matrices reales simétricas de diagonal nula debe declarar dominio, codominio, información preservada y criterio de recuperación. Relaciones dirigidas o superiores pueden exigir ampliar el espacio. No se presupone una correspondencia inyectiva ni física. La conservación de un invariante exige especificar la transformación.
5. Alcance canónico
La subestructura C/S23/T8/X6 es auxiliar, no una definición de Pirámide-Parábola. La rotación sectorial C4 comunicada para la arquitectura canónica debe verificarse contra una fuente fijada. El grupo máximo sigue abierto. Véase CANONICAL_SYMMETRY_CORRESPONDENCE.md. La aplicación a neutrinos permanece hipotética.
Nivel II retenido; Nivel III abierto; λ reservado al 4º Factor; sin ascenso automático; v1.6/v1.7 aisladas; sin reescalados post hoc. Episodio 44 congelado.
