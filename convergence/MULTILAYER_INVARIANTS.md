# MULTILAYER INVARIANTS

## Invariantes de arquitecturas relacionales multicapa

**Proyecto:** Convergencia TRCG — Código Viajer  
**Versión:** 0.1.0  
**Estado:** Desarrollo matemático abierto  
**Referencia:** TRCG, Episodio 45, sección 9  
**Gobernanza:** Nivel II retenido · Nivel III abierto  

---

## 1. Objeto

Desarrollar magnitudes invariantes capaces
de caracterizar parcialmente la organización
conjunta de una arquitectura relacional
multicapa.

El objetivo es distinguir:

- Propiedades individuales de cada capa.
- Relaciones entre diferentes capas.
- Identidad geométrica conjunta.
- Conservación bajo transformaciones.
- Conservación bajo evolución dinámica.

Estas propiedades no deben confundirse.

## 2. Definición de arquitectura multicapa

Consideramos:

A = (A_1,A_2,...,A_m)

donde:

A_k ∈ S_N

y:

S_N = {R ∈ ℝ^(N×N) :
       Rᵀ = R, diag(R) = 0}

Todas las capas comparten el mismo conjunto
ordenado de N elementos.

La correspondencia entre las capas se fija
antes de realizar las comparaciones.

Para Pirámide-Parábola, N = 24.

Las familias candidatas incluyen:

- Contigüidad.
- Suma 23.
- Relaciones triangulares.
- Relaciones de cruce.
- Acoplamientos adicionales definidos
  en la especificación canónica.

La enumeración anterior no sustituye
a la definición completa de la arquitectura.

Las relaciones dirigidas o de orden superior
requieren una representación adicional cuando
no puedan expresarse fielmente mediante
matrices simétricas.

## 3. Acción simultánea

Sea Q una matriz ortogonal.

Definimos:

A'_k = QA_kQᵀ

para todo k.

La misma transformación debe aplicarse
simultáneamente a todas las capas.

Si se exige que la arquitectura transformada
permanezca en S_N, Q deberá ser admisible
respecto de dicho espacio.

## 4. Matriz de Gram relacional

Definimos:

C_ij = tr(A_i A_j)

La matriz conjunta es:

C(A) = (C_ij) ∈ ℝ^(m×m)

### Teorema 1

C(A) es invariante bajo la conjugación
ortogonal simultánea de todas las capas.

### Demostración

C'_ij = tr(A'_i A'_j)

Sustituyendo:

C'_ij = tr(QA_iQᵀQA_jQᵀ)

Como:

QᵀQ = I

obtenemos:

C'_ij = tr(QA_iA_jQᵀ)

Por la propiedad cíclica de la traza:

C'_ij = tr(A_iA_jQᵀQ)

Por tanto:

C'_ij = tr(A_iA_j) = C_ij

Queda demostrado.

## 5. Propiedades de la matriz de Gram

### 5.1 Simetría

C_ij = C_ji

### 5.2 Semidefinición positiva

Sea v ∈ ℝ^m.

Entonces:

vᵀCv = ||Σ_i v_i A_i||_F² ≥ 0

Por tanto:

C ⪰ 0

Esta propiedad corresponde a la matriz de Gram.

No implica que las matrices relacionales
individuales A_k sean semidefinidas positivas.

### 5.3 Componentes diagonales

C_ii = tr(A_i²)

Como A_i es simétrica:

C_ii = ||A_i||_F²

### 5.4 Rango

El rango de C coincide con la dimensión
del espacio lineal generado por las capas.

Por tanto:

rank(C) ≤ min(m,N(N−1)/2)

La matriz de Gram permite detectar
dependencias lineales entre familias
relacionales.

## 6. Interpretación para capas binarias

Supongamos que:

(A_k)_ij ∈ {0,1}

Cada capa representa un grafo simple
no dirigido con conjunto de aristas E_k.

Entonces:

C_ii = 2|E_i|

Y:

C_ij = 2|E_i ∩ E_j|

Por tanto:

- La diagonal mide el número de aristas
  de cada familia, multiplicado por dos.
- Las componentes no diagonales miden
  el solapamiento entre familias.
- Un valor cero indica ausencia de aristas
  compartidas entre esas dos capas.

Este resultado es aplicable únicamente
a capas binarias simétricas de diagonal nula.

## 7. Solapamiento normalizado

Para capas de norma no nula definimos:

ρ_ij = C_ij / √(C_ii C_jj)

Por Cauchy-Schwarz:

−1 ≤ ρ_ij ≤ 1

Para capas binarias no negativas:

0 ≤ ρ_ij ≤ 1

Interpretación:

ρ_ij = 0:

Ausencia de solapamiento en el caso binario.

ρ_ij = 1:

Coincidencia de las capas binarias no nulas.

En el caso ponderado general, el valor 1
indica proporcionalidad positiva.

La normalización se define previamente.

No se permite utilizarla para ajustar
retrospectivamente resultados experimentales.

## 8. Invariantes mixtos de orden superior

Definimos:

I_(i_1,...,i_p) =
tr(A_(i_1) A_(i_2) ... A_(i_p))

### Teorema 2

Todos los invariantes mixtos anteriores
se conservan bajo conjugación ortogonal
simultánea.

### Demostración

Al sustituir:

A'_k = QA_kQᵀ

en el producto, los factores interiores
QᵀQ se reducen a la identidad.

Por tanto:

A'_(i_1)...A'_(i_p)
=
Q A_(i_1)...A_(i_p) Qᵀ

Aplicando la propiedad cíclica de la traza:

I'_(i_1,...,i_p) = I_(i_1,...,i_p)

Queda demostrado.

## 9. Interpretación combinatoria

Para matrices de adyacencia binarias,
la magnitud:

tr(A_i A_j A_k)

cuenta recorridos cerrados de longitud tres
que utilizan sucesivamente relaciones
de las familias i, j y k.

Análogamente:

tr(A_i A_j A_k A_l)

cuenta recorridos cerrados de longitud cuatro
con la secuencia de familias especificada.

Estos recorridos pueden repetir vértices
cuando la longitud lo permite.

No deben identificarse automáticamente
con ciclos simples.

Los invariantes mixtos permiten investigar
la interacción entre diferentes familias
geométricas.

## 10. Límites de identificación

La coincidencia de matrices de Gram
no demuestra equivalencia geométrica.

Tampoco debe suponerse que un conjunto
finito arbitrario de invariantes mixtos
identifique completamente una arquitectura.

Por tanto:

C(A) = C(B)

no implica necesariamente:

B_k = PA_kPᵀ para todo k

La igualdad de invariantes proporciona
condiciones necesarias de equivalencia
bajo la acción considerada.

La suficiencia requiere demostraciones
adicionales.

## 11. Relación con la dinámica

Sea F un operador que actúa sobre
una arquitectura multicapa.

La conservación dinámica de C exige:

C(F(A)) = C(A)

Esta igualdad no se deriva automáticamente
de los teoremas anteriores.

Debe demostrarse específicamente para F.

Si la arquitectura permanece fija y solo
evolucionan los estados de los nodos,
la constancia de C es estructural y no
demuestra conservación de información
en dichos estados.

Deben distinguirse:

- Invariantes de la arquitectura fija.
- Invariantes de los estados dinámicos.
- Invariantes de una arquitectura evolutiva.
- Invariantes bajo cambios de representación.

## 12. Protocolo de verificación

Antes de aplicar estos invariantes
a Pirámide-Parábola:

1. Fijar la versión canónica de la arquitectura.

2. Identificar el commit de referencia.

3. Construir cada matriz relacional por separado.

4. Verificar dimensiones, simetría y diagonal.

5. Calcular la matriz de Gram.

6. Calcular invariantes mixtos de órdenes
   previamente establecidos.

7. Aplicar permutaciones simultáneas y
   comprobar la conservación.

8. Comparar con arquitecturas nulas y ablaciones.

9. Registrar las coincidencias y diferencias
   sin seleccionar retrospectivamente
   los invariantes favorables.

10. Publicar matrices, código, parámetros
    y resultados reproducibles.

Este protocolo constituye una propuesta
para investigación posterior.

No modifica la campaña congelada del
Episodio 44.

## 13. Relación con 44A y 44B

Los invariantes multicapa pueden utilizarse
para caracterizar las arquitecturas empleadas
en los experimentos.

Sin embargo, no permiten por sí solos
explicar las diferencias observadas
entre los operadores variacional y de consenso.

Para investigar dichas diferencias será
necesario estudiar adicionalmente:

- Equivariancia dinámica.
- Órbitas de los estados finales.
- Entropía de atractores.
- Entropía de clases de equivalencia.
- Cuencas de atracción.
- Recuperabilidad de información.

La contribución geométrica y la contribución
algorítmica deben evaluarse por separado.

## 14. Clasificación epistemológica

RESULTADOS DEMOSTRADOS:

- Invariancia de la matriz de Gram.
- Simetría y semidefinición positiva de C.
- Interpretación del solapamiento binario.
- Invariancia de las trazas de productos.
- Interpretación mediante recorridos cerrados.

RESULTADOS PENDIENTES:

- Matriz de Gram canónica de Pirámide-Parábola.
- Invariantes mixtos específicos.
- Comparación con arquitecturas nulas.
- Capacidad de diferenciación estructural.
- Conservación bajo la dinámica propia.
- Correspondencia matemática con la TRCG.

No se incorporan resultados experimentales
no verificados.

## 15. Gobernanza

- Nivel II retenido.
- Nivel III abierto.
- Pirámide-Parábola como candidata experimental.
- λ reservado al 4º Factor.
- Sin ascensos automáticos.
- Sin reescalados retrospectivos.
- Sin alteración de protocolos congelados.

## 16. Conclusión

La identidad de una arquitectura multicapa
no puede reducirse a las propiedades
individuales de sus matrices.

Las trazas de productos proporcionan
magnitudes verificables que caracterizan
parcialmente la interacción entre familias
relacionales.

Su aplicación a Pirámide-Parábola constituye
una línea concreta de investigación para
evaluar una posible convergencia con la TRCG.

La correspondencia deberá demostrarse,
no presuponerse.
