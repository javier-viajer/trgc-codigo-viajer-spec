Correspondencia de simetrías canónicas y provisionales
Versión 0.1.0 — Documento de trabajo de convergencia TRCG–Código Viajer.
1. Alcance y fuentes
Se distingue la subestructura auxiliar de 24 nodos de la arquitectura canónica Pirámide-Parábola. Referencia a cotejar: Documento Maestro v1.2.0. Las definiciones canónicas comunicadas anteriormente se adoptan aquí como hipótesis de trabajo; falta fijar el commit y verificar íntegramente la fuente. No se afirma que el grupo rotacional declarado sea el grupo máximo de automorfismos.
2. Representaciones
Sea V=Z/24Z. El modelo auxiliar tiene capas C: j=i±1; S23: j=23−i; T8: j=i±8; X6: j=i±6, todas módulo 24. Su grupo de automorfismos simultáneos es H={id, i↦i+12, i↦11−i, i↦23−i}, isomorfo al grupo de Klein.
Bajo la numeración sectorial supuesta i=6q+r, con q∈Z/4Z y 0≤r<6, la rotación de sectores es g(i)=i+6. El grupo K=⟨g⟩ es cíclico de orden cuatro. Esta identificación de etiquetas debe cotejarse con la numeración canónica.
3. Comparación demostrada bajo las hipótesis anteriores
K contiene dos elementos de orden cuatro; H no contiene ninguno. Por tanto K y H no son isomorfos. Esto tampoco permite identificar H con el grupo máximo canónico.
Sea s(i)=23−i. Entonces gs(i)=29−i y sg(i)=17−i, distintos módulo 24. En general g^k conmuta con s si y solo si 12k=0 módulo 24, es decir, k es par. Las otras tres capas auxiliares son invariantes bajo toda rotación. Por tanto K∩H={id,g²}, isomorfo a Z/2Z. Esta intersección depende de la identificación común de etiquetas; no es una propiedad intrínseca de dos grupos abstractos.
4. Suma 23: relación frente a filtro
La involución auxiliar s no debe identificarse con un filtro de estados F(x)=1 si Σ_i w_i x_i≡23 (mod M), y 0 en otro caso. Esta última expresión es una hipótesis de transcripción de la definición canónica pendiente de cotejo. Si el dominio es estable bajo g y w_{g(i)}≡w_i (mod M), entonces F(gx)=F(x), usando (gx)i=x{g^{-1}(i)}. Es una condición suficiente, no necesaria en dominios restringidos. No demuestra equivalencia entre filtro e involución.
5. Protocolo de auditoría canónica
Fijar commit, versión, numeración, dominio de estados, pesos, módulo, relaciones dirigidas y de orden superior, restricciones y parámetros.
Construir una representación fiel y comprobar que su decodificación recupera cada objeto original. No reducir hiperrelaciones a pares sin justificar la pérdida de información.
Verificar cada potencia de g sobre cada capa, filtro y dominio. Distinguir grupo declarado, grupo efectivamente preservado y grupo máximo.
Calcular el grupo máximo mediante una codificación fiel de relaciones etiquetadas; contrastar con una segunda implementación o demostración independiente.
Definir ablaciones puras sin reconstruir otras capas; si se reconstruyen, no aplicar automáticamente los teoremas de inclusión e interacción.
Para cada operador F de 44A/44B, contrastar F_{pω}(px)=pF_ω(x), donde ω incluye orden de actualización y aleatoriedad. Distinguir igualdad trayectoria a trayectoria y equivarianza en distribución. No modificar la campaña congelada.
6. Estado y gobernanza
Demostrado condicionalmente: no isomorfismo, intersección y condición suficiente de invariancia del filtro. Pendiente: cotejo documental, grupo máximo, correspondencia fiel, equivarianza dinámica y aplicación física a neutrinos. No hay ascenso automático. Nivel II retenido; Nivel III abierto; λ reservado al 4º Factor; v1.6/v1.7 aisladas; sin reescalados post hoc.
