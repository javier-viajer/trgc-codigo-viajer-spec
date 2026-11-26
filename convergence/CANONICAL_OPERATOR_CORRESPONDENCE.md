CANONICAL OPERATOR CORRESPONDENCE
Código Viajer — Pirámide-Parábola — TRCG
Versión: 0.1.0
Estado: identidad algebraica demostrada para las fórmulas declaradas; auditoría numérica reproducida; certificación del código canónico pendiente.
1. Dominio y alcance
Sea R una matriz real simétrica de 24 nodos, diagonal nula y aristas estrictamente positivas. Sea m(R) la suma de las aristas únicas y C0 > 0 la masa fijada. Se exige m(R)=C0, 0 ≤ μ ≤ 1, γ > 0 y factores g_i positivos y finitos. El autovector de Perron v se normaliza con norma euclídea uno y signo positivo. Estas condiciones garantizan su unicidad.
La fórmula atribuida al Documento Maestro v1.2.0 se toma aquí como hipótesis de trabajo. No se ha fijado ni verificado en esta auditoría un commit del repositorio original. No se certifica la dinámica híbrida completa.
2. Correspondencia algebraica
Para i ≠ j, sean M_ij=(g_i v_i g_j v_j)^γ y B_ij=(w_i v_i^γ)(w_j v_j^γ). Ambas diagonales se fijan a cero. Definimos N_c(X)=c X/m(X).
El operador estudiado es Φ(R)=(1−μ)R+μ N_C0(M). El operador de referencia es F(R)=(1−α)R+α N_m(R)(B).
Si α=μ y w_i=g_i^γ, entonces M=B componente a componente. Como m(R)=C0, ambas normalizaciones coinciden y Φ(R)=F(R). La igualdad es exacta en aritmética real. La masa permanece C0 y las aristas siguen siendo positivas, de modo que la identidad se extiende por inducción a toda trayectoria finita.
3. Factores geométricos
Se estudia g_i=(1−z_i/H)^(−1/2), con H>0 y z_i/H<1. Si los factores son constantes dentro de cada estrato, también lo son w_i. En el ensayo se usa la convención ilustrativa z/H=j r, j=0,...,5, repetida en cuatro sectores. Esta indexación no se presenta como certificación de las alturas originales.
4. Grupo dinámico por permutaciones
Toda permutación P que conserve los pesos satisface v(PRP^T)=Pv(R), conserva la masa y conmuta con la construcción M. Por ello Φ(PRP^T)=PΦ(R)P^T.
Para demostrar la necesidad, tomamos R homogénea de masa C0, invariante bajo toda permutación. Su autovector dominante es constante. Si μ>0 y P es una simetría universal, Φ(R) debe ser invariante bajo P. Sus términos de actualización son proporcionales a w_i w_j para i≠j. La normalización no cambia al permutar los pesos.
Por tanto, escribiendo a_i=w_{p(i)}/w_i>0, se exige a_i a_j=1 para todo i≠j. Con al menos tres nodos, esto implica a_i=1 para todos los i. Así, el grupo dinámico es exactamente el estabilizador de los pesos.
Con seis pesos distintos, cada uno repetido cuatro veces, G_din=(S4)^6, de orden 24^6=191102976. Si μ=0, el operador es la identidad y el grupo por permutaciones es S24. Si existen pesos repetidos entre estratos, el estabilizador puede ser mayor.
5. Espacios invariantes
La rotación simultánea de los cuatro sectores genera Z4. Sus órbitas de aristas son seis de tamaño dos y 66 de tamaño cuatro: dimensión 72. Bajo (S4)^6 hay seis clases internas y quince entre estratos: dimensión 21. Con masa fija las dimensiones afines son 71 y 20, respectivamente. La equivarianza conserva estos espacios, pero no demuestra que sean atractores.
6. Auditoría reproducible
Ejecutar python canonical_operator_audit.py con NumPy instalado. El programa compara las dos fórmulas, comprueba rotación, los 18 generadores estratificados y conservación de masa, e incluye un control negativo intercambiando nodos de distinto peso cuando μ>0. Semilla 20261125; tolerancia 1e-10; 480 casos. Los resultados efectivos se guardan en canonical_operator_results.json. El código de salida es distinto de cero si falla un criterio.
Las pruebas numéricas no sustituyen la demostración universal. El grupo geométrico máximo, la invertibilidad, la estabilidad apical y la correspondencia con 44A/44B permanecen pendientes. La coincidencia de fórmulas no implica equivalencia física con la TRCG.
7. Gobernanza
Nivel II retenido; Nivel III abierto; λ reservado al 4º Factor; versiones 1.6 y 1.7 aisladas; sin ascenso automático ni reescalados post hoc; campaña del Episodio 44 intacta.
