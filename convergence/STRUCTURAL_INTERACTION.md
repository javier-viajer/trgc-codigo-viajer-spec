Interacción estructural entre familias relacionales
Versión 0.2.0 — alcance: subestructura provisional, no arquitectura canónica.
Definiciones y resultados analíticos
Sea G(K) el grupo de permutaciones de los 24 nodos que preserva individualmente las capas no eliminadas del conjunto K. Las capas son C (paso ±1), S23 (j=23−i), T8 (paso ±8), X6 (paso ±6), con índices módulo 24. Las aristas pueden pertenecer a varias capas; se conserva el conjunto exacto de etiquetas.
Definimos D(K)=log₂(|G(K)|/|G(∅)|). Si K⊆L, entonces G(K)⊆G(L); por Lagrange, el cociente de órdenes es entero y D(K)≤D(L). El índice es invariante bajo reetiquetado común de los nodos.
Para dos familias i,j definimos J(i,j)=D({i,j})−D({i})−D({j}). Equivalentemente, J=log₂(|G({i,j})||G(∅)|/(|G({i})||G({j})|)).
En este modelo de ablación pura, J≥0: sean H=G({i}), L=G({j}), M=G({i,j}). Entonces H∩L=G(∅), y el conjunto HL⊆M tiene cardinalidad |H||L|/|H∩L|. Por tanto el argumento del logaritmo es ≥1. No se presupone que HL sea un subgrupo. J=0 si y solo si HL=M. Esta demostración no se aplica automáticamente a ablaciones que reponderan o reconstruyen otras capas.
J mide ampliación conjunta de simetrías respecto al producto de ampliaciones individuales; no es información mutua ni una medida de efecto dinámico.
Método de auditoría
Se construye un grafo simple con etiquetas de arista que codifican todas las capas activas. NetworkX enumera los automorfismos de un representante de cada clase de componentes conexas isomorfas. Si una clase tiene m componentes y cada una tiene a automorfismos, aporta a^m m! al orden total: se pueden permutar las componentes y elegir independientemente sus isomorfismos internos. Se multiplican las contribuciones de las clases. Esto evita enumerar grupos enormes y proporciona cardinalidades exactas, no estimaciones.
Resultados computacionales
Ejecución local con NetworkX 3.6.1. Los 16 subconjuntos de ablación fueron evaluados.
Capas eliminadas
Orden del grupo
Ninguna
4
C
96
S23
48
T8
4
X6
4
C, S23
4608
C, T8
24576
C, X6
497664
S23, T8
48
S23, X6
48
T8, X6
4
C, S23, T8
188743680
C, S23, X6
67722117120
C, T8, X6
1961990553600
S23, T8, X6
48
C, S23, T8, X6
620448401733239439360000
Pareja
J (bits)
C, S23
2.000000000
C, T8
8.000000000
C, X6
12.339850003
S23, T8
0.000000000
S23, X6
0.000000000
T8, X6
0.000000000
La ablación C+X6 queda resuelta exactamente: 497664. Quedan pendientes demostraciones analíticas específicas de las cardinalidades no cubiertas por los teoremas anteriores. Las pruebas automatizadas verifican los órdenes registrados, el grupo de Klein, la divisibilidad, el reetiquetado, una instancia independiente de la fórmula de componentes y los índices de interacción. Los valores esperados registrados no constituyen una segunda implementación independiente.
Reproducción
Desde convergence/:
python -m pip install networkx==3.6.1
python symmetry_audit.py --output symmetry_results.json
python -m unittest -v test_symmetry_audit
Límites y gobernanza
No se ha verificado la arquitectura canónica completa, ni la equivarianza de 44A/44B, ni consecuencias físicas. Una interacción estructural positiva no demuestra interacción dinámica. La campaña del Episodio 44 no se modifica. Nivel II retenido; Nivel III abierto; sin ascenso automático; λ reservado al 4º Factor; v1.6 y v1.7 aisladas; sin reescalados post hoc.
Adenda v0.2.0 — alcance canónico
Las cardinalidades anteriores no son cardinalidades canónicas. La capa S23 auxiliar es una involución de nodos, no un filtro modular de estados. El grupo de Klein auxiliar no es isomorfo al grupo rotacional C4 comunicado para la arquitectura canónica. Véase CANONICAL_SYMMETRY_CORRESPONDENCE.md para hipótesis, intersección y protocolo de cotejo. El grupo máximo canónico sigue abierto. Los resultados y el código auxiliar se conservan sin modificación retrospectiva.
