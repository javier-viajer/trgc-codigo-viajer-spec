HIGHER SUPPORT EQUILIBRIA
Existencia, estabilidad y bifurcaciones de equilibrios de soporte superior
Proyecto: TRCG — Código Viajer — Pirámide-Parábola
Versión: 1.0.0
Fecha: 2026-11-27
Estado: Resultados analíticos condicionados y verificación numérica de referencia.
1. Dominio y alcance
Sea R una matriz simétrica no negativa de diagonal nula, con N=24 y masa de aristas C₀>0. Se considera el operador de referencia, no una certificación de la implementación canónica:
$$\Phi(R)=(1-\mu)R+\mu\mathcal N(M(R)),\qquad M_{ij}=(g_i g_j v_i v_j)^\gamma\ (i\ne j).$$
Aquí gᵢ>0, γ>0, 0<μ≤1, v es el autovector de Perron unitario no negativo y N normaliza la suma de aristas a C₀. Se exige autovalor dominante simple en el dominio estudiado. No se presupone una selección global de Perron en matrices reducibles degeneradas.
2. Caracterización exacta
En un punto fijo R*=N(M(R*)). Si S es el soporte de v, entonces m=|S|≥2 y todas las aristas internas son positivas; las exteriores son nulas. Sea uᵢ=(gᵢvᵢ)^γ, T=Σuᵢvᵢ y pᵢ=uᵢvᵢ/T. La ecuación espectral da ρvᵢ=cTuᵢ(1−pᵢ), con c la constante de normalización. Eliminando v se obtiene
$$g_i^{2\gamma/(\gamma+1)}p_i^{(\gamma-1)/(\gamma+1)}(1-p_i)=K,\quad p_i>0,\quad \sum_{i\in S}p_i=1.$$
Recíprocamente, toda solución reconstruye un equilibrio:
$$v_i=\sqrt{\frac{p_i(1-p_i)}{1-\sum_jp_j^2}},\qquad b_i=\sqrt{\frac{p_i}{1-p_i}},\qquad R^*{ij}=\frac{C_0 b_i b_j}{\sum{k<l}b_kb_l}.$$
En efecto, la ecuación escalar implica u proporcional a b y R*v proporcional a v. La positividad interna garantiza que v es Perron simple. Los equilibrios son independientes de μ en el intervalo indicado.
3. Regímenes de existencia
Para 0<γ<1, f(p)=p^((γ−1)/(γ+1))(1−p) decrece estrictamente de infinito a cero. Cada pᵢ(K) decrece de uno a cero; su suma cruza uno exactamente una vez. Hay un equilibrio por soporte, 2²⁴−25=16.777.191 en total. No es un recuento de atractores.
Para γ=1, K=(m−1)/(Σ1/gᵢ) y pᵢ=1−K/gᵢ. Existe un único equilibrio de soporte S si y solo si g_min Σ1/gᵢ>m−1.
Para γ>1, f tiene un máximo en p_c=(γ−1)/(2γ). Cada nodo admite hasta dos ramas. Para cada elección de ramas se resuelve Σpᵢ(K)=1, con 0<K≤minᵢ gᵢ^(2γ/(γ+1)) f(p_c). Una exploración por cambios de signo no certifica raíces tangenciales ni próximas a los extremos.
4. Equilibrios homogéneos
Si todos los pesos del soporte coinciden, pᵢ=1/m y R* tiene aristas de valor a=2C₀/[m(m−1)]. Para una perturbación interna E de masa nula, sᵢ=ΣⱼEᵢⱼ y δvᵢ=sᵢ/(ma√m). La derivada normalizada es γ(sᵢ+sⱼ)/m.
Para m≥3 los modos transversales (s=0) tienen multiplicidad m(m−3)/2 y autovalor 1−μ. Los longitudinales Eᵢⱼ=xᵢ+xⱼ, Σxᵢ=0, tienen multiplicidad m−1 y autovalor 1−μ+μγ(m−2)/m. Así γ_c=m/(m−2). Para γ>1, las perturbaciones exteriores generan aristas de orden O(||E||^γ) y O(||E||^(2γ)); su bloque lineal es (1−μ)I. La derivada relativa en el dominio no negativo tiene estructura triangular. Por ello 1<γ<γ_c implica estabilidad local asintótica; γ>γ_c implica inestabilidad. En igualdad no se concluye estabilidad no lineal. Para m=2 no hay modos internos de masa nula y γ>1 garantiza estabilidad local.
Con seis estratos de cuatro nodos de pesos distintos entre estratos existen 24 triángulos homogéneos y seis soportes homogéneos de cuatro nodos, además de las 276 aristas. Para 1<γ<2 hay al menos 306 equilibrios estables, 33 clases estratificadas y 84 rotacionales (rotación sectorial de orden cuatro). Para 2<γ<3 hay al menos 300, y para γ>3 al menos 276. Son cotas inferiores, no una clasificación exhaustiva.
5. Criterio espectral heterogéneo
Defínase Pᵢⱼ=pⱼ/(1−pᵢ) para i≠j, Pᵢᵢ=0. P es estocástica y reversible respecto de πᵢ=vᵢ². Es semejante a A=bbᵀ−diag(d), dᵢ=pᵢ/(1−pᵢ). Su espectro es 1=ℓ₁>ℓ₂≥…≥ℓₘ≥−1, con los restantes autovalores negativos por inercia de la actualización de rango uno.
Para zᵢ=δvᵢ/vᵢ, la perturbación relativa de las aristas generadas es γ(zᵢ+zⱼ) menos una constante de normalización. Diferenciando la ecuación espectral se obtiene, módulo constantes, (I−P)z_nuevo=γ(I+P)z. Los operadores de derivación de Perron y de generación de aristas componen en orden inverso en el espacio de aristas y el espacio nodal; sus espectros no nulos coinciden. Para m≥3, los m−1 modos nodales tienen factores βₖ=γ(1+ℓₖ)/(1−ℓₖ); los restantes modos internos tienen factor cero para el término no residual. El Jacobiano dinámico tiene autovalores
$$\eta_k=1-\mu+\mu\gamma\frac{1+\ell_k}{1-\ell_k},\quad k=2,\ldots,m.$$
Los modos transversales y exteriores tienen autovalor 1−μ (exteriores para γ>1). Para m≥3 y γ>1, la estabilidad lineal estricta equivale a
$$\ell_2<-\frac{\gamma-1}{\gamma+1}.$$
La desigualdad estricta implica estabilidad local asintótica; la inversa estricta implica inestabilidad. La igualdad requiere análisis no lineal. El caso m=2 se trata separadamente.
6. Criterios por ramas
Sea α=(γ−1)/(γ+1). A+αI=diag(α−dᵢ)+bbᵀ. Si todos pᵢ>p_c, la diagonal es negativa definida y la actualización de rango uno deja exactamente un autovalor positivo; el equilibrio es estable. Si dos o más pᵢ<p_c, existen al menos dos direcciones positivas y el equilibrio es inestable.
Si exactamente uno está en rama inferior y ninguno en p_c, defínase Δ=1+Σdᵢ/(α−dᵢ). La fórmula de inercia por complemento de Schur de la matriz bordeada con bloques diag(α−d), b y −1 da: Δ>0, estabilidad; Δ<0, inestabilidad; Δ=0, modo crítico. Si algún pᵢ=p_c debe usarse el criterio espectral directamente. La rama superior estricta exige m<2γ/(γ−1); no se afirma esta cota para todas las soluciones mixtas.
7. Auditoría numérica
El script higher_support_audit.py utiliza NumPy y SciPy. Explora ramas por cambios de signo, reconstruye matrices, verifica residuos de punto fijo y compara el espectro reducido con diferencias finitas centrales del operador en coordenadas independientes de masa fija (paso 10⁻⁶). Para γ=1,5, μ=0,2 y C₀=1 encuentra:
Pesos
Soluciones encontradas
Estables
Inestables
1,1,1
4
1
3
1,1.1,1.2
4
1
3
1,1,1.1,1.1
9
0
9
Los radios de los dos equilibrios estables son aproximadamente 0,9 y 0,9596331. Los resultados completos y las versiones de dependencias están en higher_support_results.json. La búsqueda no es exhaustiva certificada.
8. Punto crítico heterogéneo y bifurcación
Para g=(1,1.1,1.2), defínase hᵢ=2γ log(gᵢ)/(γ+1)+α log(pᵢ)+log(1−pᵢ). Con p₃=1−p₁−p₂, F=(h₁−h₃,h₂−h₃). Sea d̃ᵢ=α/pᵢ−1/(1−pᵢ). Entonces DₚF=diag(d̃₁,d̃₂)+d̃₃11ᵀ. Se resuelve F=0 y det(DₚF)=0.
El resultado numérico es γ*=1,5655641967327147, p*=(0,1245748114;0,3961190940;0,4793060945). Las aristas (12,13,23) son (0,2115064783;0,2505541859;0,5379393358). El Jacobiano reducido tiene espectro aproximadamente (−3,3933533962;0).
Para q unitario del núcleo con primera componente positiva, A_f=qᵀF_γ y B_f=qᵀD²ₚF[q,q]. Se usan hᵢ,γ=2(log gᵢ+log pᵢ)/(γ+1)² y hᵢ,pp=−α/pᵢ²−1/(1−pᵢ)². Se obtiene A_f≈−0,3619279240, B_f≈−9,4172711434. La forma normal local de las ecuaciones de equilibrio da γ−γ*≈−13,009870914 s². Ambos coeficientes son no nulos numéricamente.
El operador dinámico interno para μ=0,2 tiene autovalores aproximadamente 1 y 0,8387871912. Para G=Φ−Id, se calculan vectores nulos derecho v e izquierdo w de DG por SVD, con ||v||=1, v₁>0 y wᵀv=1. Diferencias finitas con pasos 10⁻⁴, 3·10⁻⁵ y 10⁻⁵ dan wᵀG_γ≈−0,01893845 y wᵀD²G[v,v]≈−0,65553. Los coeficientes no nulos y el modo unitario simple respaldan una bifurcación silla-nodo local en la cara triangular: dos ramas a la izquierda y ninguna de esas ramas a la derecha. Los otros 273 modos del dominio de 24 nodos tienen autovalor 0,8 por el argumento analítico, no por diferenciación numérica completa.
La evidencia es numérica, no una certificación por intervalos de una raíz exacta. No se afirma una forma normal C² en todo el dominio de frontera para 1<γ<2, donde las potencias exteriores pueden no ser C². La cara triangular es invariante y suave localmente.
9. Reproducción y limitaciones
python -m pip install numpy scipy
python higher_support_audit.py
El script genera el JSON junto al propio archivo y aplica aserciones sobre residuos, espectros, recuentos observados y coeficientes críticos. PASS se limita a esos controles. No certifica todas las raíces, pesos canónicos, cuencas, estabilidad no lineal crítica, ni los operadores híbridos o 44A/44B. Los pesos y μ son ilustrativos. No se infieren probabilidades de dominancia apical. La independencia matemática de TRCG y Código Viajer se mantiene.
10. Referencias internas y trabajo pendiente
REDUCED_SUPPORT_STABILITY.md
EQUILIBRIUM_CLASSIFICATION.md
CANONICAL_OPERATOR_CORRESPONDENCE.md
RELATIONAL_QUOTIENT_METRIC.md
higher_support_audit.py
higher_support_results.json
Pendientes: certificación de raíces y bifurcaciones, auditoría de pesos canónicos fijados por commit, enumeración de composiciones estratificadas, perturbaciones exteriores numéricas, cuencas y comparación independiente con TRCG.
11. Gobernanza
Nivel II retenido · Nivel III abierto · λ reservado al 4º Factor · Campaña experimental del Episodio 44 intacta. Sin ascenso automático ni equivalencia entre formulaciones presupuesta.
