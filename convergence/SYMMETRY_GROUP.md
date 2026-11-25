Grupo de simetrías relacionales
Versión 0.2.0 — revisión de alcance canónico.
1. Grupo multicapa
Para matrices etiquetadas A_k sobre N nodos, G={P permutación: PA_kPᵀ=A_k para todo k}. La identidad pertenece a G; si P,Q pertenecen a G, PQ preserva cada capa; multiplicando la igualdad por Pᵀ y P se obtiene la preservación por P⁻¹. Por tanto G es un grupo. Los atributos y relaciones superiores añaden restricciones de estabilización.
2. Demostración para el modelo auxiliar
V=Z/24Z; C: paso ±1; S23: i↦23−i; T8: paso ±8; X6: paso ±6. El ciclo C tiene grupo diédrico de orden 48: cada automorfismo queda determinado por la imagen de 0 y la elección de uno de sus dos vecinos como imagen de 1. Sus elementos son i↦i+k o i↦−i+k.
Preservar S23 equivale a conmutar con su involución. Para rotaciones exige 2k≡0 (mod 24), y para reflexiones 2k≡22 (mod 24). T8 y X6 son preservadas por todo el grupo diédrico. Resulta G={id,r,s,rs}, r(i)=i+12, s(i)=23−i. r²=s²=id y rs=sr. El grupo es Klein.
·
e
r
s
rs
e
e
r
s
rs
r
r
e
rs
s
s
s
rs
e
r
rs
rs
s
r
e
Si una arquitectura ampliada conserva exactamente estas cuatro capas como relaciones individuales sobre los mismos nodos, su grupo es un subgrupo de G y tiene orden 1, 2 o 4. Esta hipótesis no se ha establecido para la arquitectura canónica.
3. Transformaciones ortogonales universales
Sea S el espacio de matrices reales simétricas de diagonal nula. Si Q es ortogonal y QSQᵀ⊆S, para cada fila i se exige 2Σ_{j<k}q_ij q_ik R_jk=0 para todo R∈S. La independencia de las entradas implica q_ij q_ik=0 para j≠k. Cada fila tiene exactamente una entrada ±1 y la ortogonalidad impone columnas distintas. Recíprocamente toda permutación con signo preserva S. El grupo tiene orden 2^N N!; su acción por conjugación no es fiel (±I actúan igual). Para una matriz particular pueden existir otras transformaciones. Restricciones adicionales, como no negatividad, requieren análisis separado.
La semejanza ortogonal conserva espectro, trazas de potencias y norma de Frobenius. Con Q conocido se recupera R=QᵀR'Q; esto no implica invertibilidad de la dinámica ni completitud espectral.
4. Distinción canónica
Bajo numeración sectorial supuesta, g(i)=i+6 genera C4, no isomorfo a Klein. Su intersección con el grupo auxiliar es {id,g²}. El grupo rotacional declarado no equivale necesariamente al grupo máximo canónico. Véase CANONICAL_SYMMETRY_CORRESPONDENCE.md. Pendientes cotejo de fuente y equivarianza de 44A/44B.
Nivel II retenido; Nivel III abierto; λ reservado al 4º Factor; sin ascenso automático; v1.6/v1.7 aisladas; sin reescalados post hoc. Episodio 44 congelado.
