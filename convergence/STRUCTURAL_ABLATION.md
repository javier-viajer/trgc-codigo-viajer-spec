Ablación estructural de familias relacionales
Versión 0.2.0 — revisión de alcance canónico.
1. Definición y teorema
Sea G(K) la intersección de estabilizadores de las capas no eliminadas por K, dentro de un grupo ambiente fijo de permutaciones. Se mantienen los nodos, atributos no ablacionados y las demás relaciones sin cambios. Si K⊆L, G(K)⊆G(L), porque toda simetría que satisface más restricciones satisface las restantes. Por Lagrange, |G(L)|/|G(K)| es entero.
D(K)=log₂(|G(K)|/|G(∅)|) es no negativo y monótono. Un reetiquetado común conjuga los grupos y conserva sus órdenes; por tanto D es invariante. No es entropía de Shannon ni una medida dinámica.
2. Resultados del modelo auxiliar
Capas C (±1), S23 (23−i), T8 (±8), X6 (±6), módulo 24. Grupo nominal de orden 4. Al eliminar S23 queda el grupo diédrico de orden 48, luego D=log₂12. Eliminar T8 o X6 individualmente conserva el grupo nominal y D=0. La auditoría registrada da orden 96 al eliminar C, luego D=log₂24. Las 16 cardinalidades y las interacciones se registran en STRUCTURAL_INTERACTION.md y symmetry_audit.py.
D=0 no implica redundancia dinámica ni redundancia bajo otras ablaciones. Para dos capas, J=D({i,j})−D({i})−D({j})≥0 bajo ablación pura: los grupos de ablación individual H,L tienen intersección G(∅) y HL está contenido en el grupo de ablación doble; |HL|=|H||L|/|H∩L|. La igualdad equivale a que HL agote el grupo doble. No se exige que HL sea subgrupo a priori.
3. Validación dinámica futura
Comparar geometrías nominales, ablaciones y controles nulos con operadores 44A/44B, semillas, estados iniciales, órdenes y presupuestos comparables. Preespecificar métricas, contrastes y correcciones múltiples. Separar convergencia, cuencas, entropía de atractores, recuperación y equivarianza. No inferir efectos dinámicos de los índices estructurales.
4. Límite canónico
Los resultados numéricos pertenecen exclusivamente al modelo auxiliar. La S23 auxiliar no equivale automáticamente al filtro modular canónico. Una ablación que modifica pesos, reconstruye relaciones o altera el dominio no satisface necesariamente el teorema anterior. La auditoría canónica requiere fijar una fuente y representación fiel. Véase CANONICAL_SYMMETRY_CORRESPONDENCE.md.
Nivel II retenido; Nivel III abierto; λ reservado al 4º Factor; sin ascenso automático; v1.6/v1.7 aisladas; sin reescalados post hoc. Episodio 44 congelado.

