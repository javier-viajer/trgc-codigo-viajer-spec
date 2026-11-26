# RELATIONAL QUOTIENT METRIC

## Métrica del espacio cociente relacional multicapa

**Proyecto:** Convergencia TRCG — Código Viajer  
**Versión:** 0.1.0  
**Fecha:** 2026-11-26  
**Estado:** Resultado matemático demostrado bajo hipótesis explícitas  
**Referencia:** TRCG, Episodios 45 y 46  
**Gobernanza:** Nivel II retenido · Nivel III abierto  

---

## 1. Objeto

Construir y demostrar una métrica sobre el espacio
de clases de equivalencia de configuraciones
relacionales multicapa.

El objetivo es medir diferencias estructurales
sin confundirlas con diferencias producidas
exclusivamente por transformaciones admisibles
de representación.

Este desarrollo no presupone una equivalencia
entre la TRCG y Pirámide-Parábola.

## 2. Documentos relacionados

- EFFECTIVE_SYMMETRY_GROUP.md
- MULTILAYER_INVARIANTS.md

El presente documento amplía los resultados
algebraicos desarrollados en dichos archivos.

## 3. Espacio relacional

Sea N ≥ 3.

Definimos:

S_N = {R ∈ ℝ^(N×N) :
       Rᵀ = R, diag(R) = 0}

Su dimensión es:

dim(S_N) = N(N−1)/2

Para una arquitectura de m capas definimos:

X = (S_N)^m

Cada elemento de X tiene la forma:

A = (A_1,...,A_m)

Todas las capas comparten el mismo conjunto
ordenado de N elementos.

La dimensión del espacio ambiente es:

dim(X) = mN(N−1)/2

Para N = 24:

dim(X) = 276m

Esta dimensión corresponde al espacio ambiente
sin restricciones geométricas adicionales.

No implica que una arquitectura concreta
posea 276m grados de libertad independientes.

## 4. Hipótesis fundamentales

H1. El número de capas m es finito y positivo.

H2. G es un grupo finito de matrices ortogonales.

H3. G preserva el espacio X.

H4. Cada transformación actúa simultáneamente
    sobre todas las capas.

H5. La correspondencia entre capas permanece fija.

H6. Los pesos w_k son estrictamente positivos.

H7. Los pesos se fijan antes de cualquier
    comparación experimental.

Si existen restricciones adicionales sobre
las configuraciones admisibles, el dominio
restringido deberá ser invariante bajo G.

## 5. Acción del grupo

Para Q ∈ G definimos:

Q · A = (QA_1Qᵀ,...,QA_mQᵀ)

La identidad satisface:

I · A = A

La composición satisface:

P · (Q · A) = (PQ) · A

Por tanto, se trata de una acción de grupo
sobre X.

## 6. Norma multicapa ponderada

Definimos:

||A||_w =
√(Σ_k w_k ||A_k||_F²)

donde:

||A_k||_F² = tr(A_kᵀ A_k)

Como todos los pesos son estrictamente
positivos, esta expresión define una norma
sobre X.

La distancia asociada es:

D_w(A,B) = ||A−B||_w

Equivalentemente:

D_w(A,B) =
√(Σ_k w_k ||A_k−B_k||_F²)

Esta distancia compara configuraciones
con etiquetas y capas fijas.

## 7. Invariancia de la distancia ambiente

### Lema 1

La acción de G es isométrica respecto de D_w.

### Demostración

Para cualquier Q ∈ G:

D_w(Q · A,Q · B)²

= Σ_k w_k ||QA_kQᵀ−QB_kQᵀ||_F²

= Σ_k w_k ||Q(A_k−B_k)Qᵀ||_F²

La norma de Frobenius es invariante
bajo conjugación ortogonal.

Por tanto:

D_w(Q · A,Q · B)²

= Σ_k w_k ||A_k−B_k||_F²

= D_w(A,B)²

En consecuencia:

D_w(Q · A,Q · B) = D_w(A,B)

Queda demostrado.

## 8. Clases de equivalencia

Definimos:

A ~_G B

si y solo si existe Q ∈ G tal que:

A = Q · B

Esta relación es reflexiva, simétrica
y transitiva.

La clase de equivalencia de A es:

[A]_G = {Q · A : Q ∈ G}

El espacio cociente se define como:

X/G = {[A]_G : A ∈ X}

Cada elemento del cociente representa
una órbita completa de configuraciones.

## 9. Definición de distancia relacional

Definimos:

d_G([A]_G,[B]_G)
=
min_(Q∈G) D_w(A,Q · B)

Equivalentemente:

d_G([A]_G,[B]_G)
=
min_(Q∈G)
√(Σ_k w_k ||A_k−QB_kQᵀ||_F²)

Como G es finito y no vacío,
el mínimo existe y se alcanza.

La distancia compara arquitecturas
después de considerar todos los cambios
de representación permitidos por G.

## 10. Independencia de los representantes

### Teorema 1

La distancia d_G no depende de los
representantes elegidos dentro de cada órbita.

### Demostración

Sean:

A' = P · A

B' = U · B

con P,U ∈ G.

Entonces:

min_(Q∈G) D_w(A',Q · B')

= min_(Q∈G) D_w(P · A,QU · B)

Por el carácter isométrico de la acción:

= min_(Q∈G) D_w(A,P⁻¹QU · B)

Como G es un grupo, la aplicación:

Q ↦ P⁻¹QU

es una biyección de G sobre sí mismo.

Por tanto:

min_(Q∈G) D_w(A,P⁻¹QU · B)

= min_(V∈G) D_w(A,V · B)

En consecuencia:

d_G([A']_G,[B']_G)
=
d_G([A]_G,[B]_G)

La distancia está bien definida sobre
el espacio cociente.

Queda demostrado.

## 11. Teorema fundamental de la métrica

### Teorema 2

Bajo las hipótesis de la sección 4,
d_G define una métrica sobre X/G.

### 11.1 No negatividad

Para cualquier Q ∈ G:

D_w(A,Q · B) ≥ 0

Por tanto:

d_G([A]_G,[B]_G) ≥ 0

### 11.2 Identidad de los indiscernibles

Si:

[A]_G = [B]_G

existe Q ∈ G tal que:

A = Q · B

Por tanto:

D_w(A,Q · B) = 0

y:

d_G([A]_G,[B]_G) = 0

Recíprocamente, supongamos:

d_G([A]_G,[B]_G) = 0

Como el mínimo se alcanza,
existe Q* ∈ G tal que:

D_w(A,Q* · B) = 0

Entonces:

Σ_k w_k ||A_k−Q*B_kQ*ᵀ||_F² = 0

Como todos los pesos son positivos
y cada sumando es no negativo:

A_k = Q*B_kQ*ᵀ

para todo k.

Por tanto:

[A]_G = [B]_G

Queda establecido:

d_G([A]_G,[B]_G) = 0

si y solo si:

[A]_G = [B]_G

### 11.3 Simetría

Por simetría de D_w:

D_w(A,Q · B) = D_w(Q · B,A)

Aplicando la isometría Q⁻¹:

D_w(Q · B,A) = D_w(B,Q⁻¹ · A)

Como la inversión es una biyección de G:

min_(Q∈G) D_w(A,Q · B)

= min_(Q∈G) D_w(B,Q⁻¹ · A)

Por tanto:

d_G([A]_G,[B]_G)
=
d_G([B]_G,[A]_G)

### 11.4 Desigualdad triangular

Sean tres configuraciones:

A,B,C ∈ X

Elegimos P,Q ∈ G que alcanzan
los mínimos correspondientes:

d_G([A]_G,[B]_G) = D_w(A,P · B)

d_G([B]_G,[C]_G) = D_w(B,Q · C)

Como PQ ∈ G:

d_G([A]_G,[C]_G)

≤ D_w(A,PQ · C)

Por la desigualdad triangular de D_w:

D_w(A,PQ · C)

≤ D_w(A,P · B)
  + D_w(P · B,PQ · C)

Por invariancia isométrica:

D_w(P · B,PQ · C)
=
D_w(B,Q · C)

En consecuencia:

d_G([A]_G,[C]_G)

≤ d_G([A]_G,[B]_G)
  + d_G([B]_G,[C]_G)

Queda demostrada la desigualdad triangular.

### Conclusión del teorema

d_G satisface las cuatro propiedades
fundamentales de una métrica.

Por tanto:

(X/G,d_G)

es un espacio métrico.

Queda demostrado.

## 12. Métrica y pseudométrica

Sobre el espacio original X definimos:

δ_G(A,B) = min_(Q∈G) D_w(A,Q · B)

Esta expresión es una pseudométrica.

Puede ocurrir:

A ≠ B

pero:

δ_G(A,B) = 0

cuando ambas configuraciones pertenecen
a la misma órbita.

Al pasar al espacio cociente, todas las
configuraciones de una misma órbita
representan un único elemento.

Por tanto, d_G es una métrica sobre X/G,
aunque δ_G no sea necesariamente una
métrica sobre X.

Esta distinción es esencial para separar
identidad matricial y equivalencia estructural.

## 13. Relación con el grupo efectivo

Sea:

K = {Q ∈ G :
     Q · A = A para todo A ∈ X}

el núcleo de la acción.

Definimos:

G_eff = G/K

Las transformaciones pertenecientes a una
misma clase lateral de K producen
exactamente la misma acción sobre X.

Por tanto:

d_G = d_(G_eff)

cuando ambos grupos se interpretan mediante
sus acciones sobre el espacio relacional.

En particular, para el grupo hiperoctaédrico
sobre S_N, con N ≥ 3:

K = {I,−I}

El uso del grupo efectivo evita contabilizar
transformaciones redundantes.

No modifica las órbitas ni las distancias.

## 14. Dependencia respecto del grupo

Sean dos grupos admisibles tales que:

H ⊆ G

Entonces:

δ_G(A,B) ≤ δ_H(A,B)

### Demostración

El mínimo sobre G considera todas las
transformaciones de H y posiblemente otras.

Por tanto, no puede ser mayor que
el mínimo restringido a H.

Queda demostrado.

### Consecuencia

Un grupo más amplio puede identificar
configuraciones que un grupo más
restrictivo considera diferentes.

Por ello, la elección del grupo no es
una decisión exclusivamente computacional.

Determina el significado matemático
de la equivalencia estructural.

No debe ampliarse retrospectivamente
para favorecer una correspondencia
entre TRCG y Pirámide-Parábola.

## 15. Relación con los invariantes multicapa

Definimos la matriz de Gram:

C_ij(A) = tr(A_i A_j)

Si:

d_G([A]_G,[B]_G) = 0

entonces existe Q ∈ G tal que:

A_k = QB_kQᵀ

para todo k.

Por los resultados demostrados en
MULTILAYER_INVARIANTS.md:

C(A) = C(B)

También coinciden todas las trazas mixtas:

tr(A_(i_1)...A_(i_p))

=

tr(B_(i_1)...B_(i_p))

Por tanto, una diferencia en cualquiera
de estos invariantes permite descartar
la equivalencia bajo G.

Sin embargo, la coincidencia de un conjunto
arbitrario de invariantes no demuestra
necesariamente que d_G sea cero.

Los invariantes constituyen filtros
algebraicos de equivalencia.

La distancia cociente proporciona
un criterio exacto respecto del grupo
admisible definido.

## 16. Cota inferior espectral

Sean:

λ_(k,1)(A) ≤ ... ≤ λ_(k,N)(A)

los autovalores ordenados de A_k.

Definimos análogamente los de B_k.

Por la desigualdad de Hoffman-Wielandt
para matrices reales simétricas:

Σ_i (λ_(k,i)(A)−λ_(k,i)(B))²

≤ ||A_k−QB_kQᵀ||_F²

para toda matriz ortogonal Q.

Multiplicando por los pesos y sumando:

Σ_k w_k Σ_i
(λ_(k,i)(A)−λ_(k,i)(B))²

≤ D_w(A,Q · B)²

Tomando el mínimo sobre G:

d_G([A]_G,[B]_G)

≥ √(Σ_k w_k Σ_i
    (λ_(k,i)(A)−λ_(k,i)(B))²)

Esta cota permite descartar equivalencias
cuando los espectros individuales difieren.

La coincidencia espectral no garantiza
que la distancia relacional sea cero.

Este resultado utiliza un teorema
matemático establecido y no introduce
un postulado físico adicional.

## 17. Proyección al espacio cociente

Definimos:

π : X → X/G

mediante:

π(A) = [A]_G

Como la identidad pertenece a G:

d_G(π(A),π(B)) ≤ D_w(A,B)

Por tanto, π es una aplicación
1-Lipschitz.

La proyección no aumenta distancias.

Esto no implica que cualquier operador
dinámico sobre X sea contractivo.

La contracción dinámica requiere
una demostración independiente.

## 18. Compatibilidad con la dinámica

Sea:

F : X → X

un operador dinámico.

Supongamos que F es G-equivariante:

F(Q · A) = Q · F(A)

para todo Q ∈ G y A ∈ X.

### Teorema 3

F induce un operador bien definido
sobre el espacio cociente.

### Demostración

Definimos:

F_bar([A]_G) = [F(A)]_G

Si A y B pertenecen a la misma órbita,
existe Q ∈ G tal que:

B = Q · A

Por equivariancia:

F(B) = F(Q · A)

     = Q · F(A)

Por tanto:

[F(B)]_G = [F(A)]_G

La definición no depende del representante.

Queda demostrado.

La equivariancia es una condición
suficiente para inducir esta dinámica.

No se presupone que 44A o 44B
satisfagan dicha condición.

## 19. Transferencia de cotas dinámicas

### Teorema 4

Supongamos que F es G-equivariante
y L-Lipschitz respecto de D_w:

D_w(F(A),F(B)) ≤ L D_w(A,B)

Entonces el operador inducido satisface:

d_G(F_bar([A]_G),F_bar([B]_G))

≤ L d_G([A]_G,[B]_G)

### Demostración

Sea Q* una transformación que alcanza:

d_G([A]_G,[B]_G)
=
D_w(A,Q* · B)

Por definición de la distancia cociente:

d_G([F(A)]_G,[F(B)]_G)

≤ D_w(F(A),Q* · F(B))

Por equivariancia:

Q* · F(B) = F(Q* · B)

Por la condición Lipschitz:

D_w(F(A),F(Q* · B))

≤ L D_w(A,Q* · B)

Por tanto:

d_G([F(A)]_G,[F(B)]_G)

≤ L d_G([A]_G,[B]_G)

Queda demostrado.

### Consecuencia

Si 0 ≤ L < 1, el operador inducido
es contractivo sobre el espacio cociente.

Si L = 1, es no expansivo.

Estas propiedades son condicionales.

No constituyen una demostración de
contracción para Pirámide-Parábola,
44A, 44B o la dinámica fundamental
de la TRCG.

## 20. Aplicación a Pirámide-Parábola

Sea:

A_PP = (A_1,...,A_m)

la representación multicapa canónica
de Pirámide-Parábola.

Definimos su grupo de automorfismos:

G_PP = {P ∈ S_24 :
        PA_kPᵀ = A_k para todo k}

La determinación de G_PP exige conocer
la especificación completa de las capas.

Deberán incluirse las restricciones
geométricas, etiquetas, orientaciones
y relaciones adicionales que correspondan.

La representación matricial deberá
preservar fielmente la información
que se pretende comparar.

Una vez determinado G_PP, podrá utilizarse
su acción para comparar configuraciones
o estados compatibles con una arquitectura
de referencia fija.

Debe distinguirse:

A. El grupo de automorfismos que deja
   fija la arquitectura de referencia.

B. El grupo de reetiquetados utilizado
   para comparar arquitecturas diferentes.

Ambos grupos responden a preguntas
matemáticas distintas.

En particular, una arquitectura fija
por todo G_PP tiene una órbita unitaria
bajo dicho grupo.

No debe confundirse su órbita con las
órbitas de los estados que evolucionan
sobre ella.

## 21. Aplicación a estados dinámicos

Si los estados dinámicos se representan
mediante vectores de nodos:

x ∈ ℝ^24

y G_PP actúa mediante permutaciones:

x ↦ Px

puede definirse:

d_estado([x],[y])
=
min_(P∈G_PP) ||x−Py||_2

Esta expresión define una métrica
sobre el correspondiente espacio cociente.

Si los estados contienen variables
adicionales, deberá definirse su acción
y comprobarse que es isométrica.

Esta métrica no debe confundirse
con la distancia entre arquitecturas
relacionales multicapa.

## 22. Aplicación a 44A y 44B

Antes de clasificar los atractores:

1. Identificar el espacio real de estados.

2. Fijar el grupo admisible.

3. Determinar su acción sobre los estados.

4. Comprobar la equivariancia del operador.

5. Establecer el criterio de igualdad exacta
   o la tolerancia numérica correspondiente.

6. Clasificar los estados finales por órbitas.

7. Comparar diversidad de estados y
   diversidad de clases de equivalencia.

Si la actualización depende del orden
de los nodos, dicho orden deberá
transformarse de manera compatible.

La equivariancia de un operador elemental
no garantiza automáticamente la
equivariancia de un protocolo completo.

No se modifican las reglas congeladas
de la campaña del Episodio 44.

## 23. Representantes canónicos

Sea p(A) una vectorización ordenada
de todas las componentes independientes
de las capas.

Definimos:

can_G(A)
=
min_lex {p(Q · A) : Q ∈ G}

donde min_lex representa el mínimo
respecto del orden lexicográfico.

Como G es finito, el mínimo existe.

Además:

can_G(A) = can_G(B)

si y solo si:

[A]_G = [B]_G

### Demostración

Si A y B pertenecen a la misma órbita,
los conjuntos de vectorizaciones
transformadas son idénticos.

Por tanto, sus mínimos coinciden.

Recíprocamente, si los mínimos coinciden,
existen P,Q ∈ G tales que:

p(P · A) = p(Q · B)

Como p es inyectiva:

P · A = Q · B

Entonces:

A = (P⁻¹Q) · B

Como P⁻¹Q ∈ G:

[A]_G = [B]_G

Queda demostrado.

El representante canónico proporciona
un identificador exacto de la órbita
en aritmética exacta.

Su cálculo exhaustivo puede resultar
computacionalmente costoso.

## 24. Dimensionalidad del espacio cociente

El espacio ambiente X tiene dimensión:

d = mN(N−1)/2

El cociente por un grupo finito
no elimina grados de libertad continuos
del mismo modo que el cociente por
un grupo continuo.

Para el espacio vectorial completo X
y la acción lineal finita considerada,
la dimensión topológica de X/G
coincide con d.

Sin embargo, el cociente puede presentar
estratos asociados a diferentes
estabilizadores y singularidades
en su estructura geométrica.

La dimensión de una familia restringida
de arquitecturas deberá estudiarse
por separado.

No se deduce de este resultado ninguna
dimensionalidad física fundamental
de la TRCG.

## 25. Protocolo de verificación computacional

La implementación deberá verificar:

T01. Identidad:

d_G([A],[A]) = 0

T02. No negatividad:

d_G([A],[B]) ≥ 0

T03. Simetría:

d_G([A],[B]) = d_G([B],[A])

T04. Invariancia por representantes:

d_G([P · A],[Q · B])
=
d_G([A],[B])

T05. Equivalencia:

d_G([A],[P · A]) = 0

T06. Desigualdad triangular:

d_G([A],[C])
≤ d_G([A],[B]) + d_G([B],[C])

T07. Compatibilidad con invariantes:

d_G([A],[B]) = 0
implica C(A) = C(B)

T08. Cota espectral:

d_G([A],[B]) ≥ cota_espectral(A,B)

T09. Representación canónica:

can_G(A) = can_G(P · A)

T10. Equivariancia dinámica:

F(P · A) = P · F(A)

T11. Monotonía respecto del grupo:

H ⊆ G implica δ_G(A,B) ≤ δ_H(A,B)

T12. Independencia del núcleo:

δ_G(A,B) = δ_(G_eff)(A,B)

Las pruebas numéricas deberán utilizar
tolerancias previamente justificadas.

Una distancia inferior a una tolerancia
no demuestra equivalencia exacta.

La relación de proximidad definida
por una tolerancia tampoco es
necesariamente transitiva.

No se presentan estas pruebas como
ejecutadas en la versión actual.

## 26. Limitaciones computacionales

Para grupos de gran orden, la enumeración
exhaustiva puede ser inviable.

En particular, el grupo simétrico S_24
contiene 24! elementos.

Deberán estudiarse métodos alternativos:

- Generadores de grupos.
- Algoritmos de automorfismos de grafos.
- Representación mediante grafos coloreados.
- Etiquetado canónico.
- Invariantes como filtros previos.
- Optimización con cotas certificadas.

Una aproximación numérica al mínimo
no debe presentarse como distancia
exacta sin certificación.

## 27. Clasificación epistemológica

### Resultados demostrados

- Invariancia isométrica de la acción.
- Independencia de los representantes.
- Existencia de la métrica cociente.
- Distinción entre métrica y pseudométrica.
- Independencia del núcleo de la acción.
- Monotonía respecto de la inclusión
  de grupos.
- Compatibilidad con invariantes multicapa.
- Cota inferior espectral.
- Proyección 1-Lipschitz.
- Existencia de dinámica inducida
  bajo equivariancia.
- Transferencia de cotas Lipschitz.
- Existencia de representantes canónicos
  para grupos finitos.

### Resultados matemáticos utilizados

- Invariancia ortogonal de Frobenius.
- Desigualdad de Hoffman-Wielandt.
- Conservación de dimensión topológica
  bajo cocientes lineales finitos.

### Resultados pendientes

- Determinación completa de G_PP.
- Representación canónica de las capas.
- Implementación computacional.
- Ejecución de las pruebas T01–T12.
- Equivariancia de 44A y 44B.
- Clasificación de atractores.
- Cuencas de atracción.
- Validación de una posible correspondencia
  estructural entre TRCG y Pirámide-Parábola.

## 28. Gobernanza

- Nivel II retenido.
- Nivel III abierto.
- λ reservado al 4º Factor.
- Pirámide-Parábola como candidata experimental.
- Independencia de ambas formulaciones.
- Sin equivalencias automáticas.
- Sin ascensos automáticos.
- Sin reescalados retrospectivos.
- Sin alteración de protocolos congelados.
- Versiones v1.6 y v1.7 mantenidas aisladas.

## 29. Referencias matemáticas

- Hoffman, A. J. y Wielandt, H. (1953).
  The variation of the spectrum of a
  normal matrix.
  Duke Mathematical Journal, 20, 37–39.

- TRCG, Episodio 45.
  Clasificación matemática de las
  transformaciones de R.

- EFFECTIVE_SYMMETRY_GROUP.md

- MULTILAYER_INVARIANTS.md

## 30. Conclusión

La equivalencia estructural puede
formalizarse mediante acciones de grupo
sobre configuraciones relacionales.

La distancia cociente permite distinguir
diferencias estructurales de diferencias
debidas exclusivamente a transformaciones
admisibles de representación.

Bajo las hipótesis establecidas,
la construcción constituye una métrica
matemáticamente demostrada.

Su aplicación a Pirámide-Parábola
requiere identificar el grupo geométrico
específico y verificar la representación
de todas las familias relacionales.

La compatibilidad con la dinámica
requiere demostraciones adicionales
de equivariancia y estabilidad.

La convergencia entre TRCG y Código Viajer
no se presupone.

Se investiga, se demuestra y se verifica.

---

FIN DEL DOCUMENTO
