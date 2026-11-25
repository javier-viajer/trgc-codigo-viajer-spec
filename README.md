### 1. README.md actualizado (sustituye el actual)

```markdown
# Código Viajer + TRCG — Control de Estabilidad Dinámica y Arquitectura Relacional

**Versión canónica: v1.7**

Este repositorio contiene dos capas relacionadas pero distintas:

1. **Código Viajer** — validador dinámico operativo en \(\mathbb{R}^4\) (capa principal histórica).
2. **TRCG / Pirámide-Parábola** — marco matemático relacional en desarrollo (carpetas `dynamics/`, `v1.7/`, tests y documentos de auditoría).

No se afirma que la TRCG esté demostrada como teoría física completa. El estado epistemológico de cada componente se detalla en [`STATUS.md`](./STATUS.md).

---

## Arquitectura del validador (Código Viajer)

Estado del agente: \(\mathbf{X} = (L, S, I, B) \in [0,1]^4\)

- \(L\): Life Preservation  
- \(S\): Entropy  
- \(I\): Node Integrity  
- \(B\): Resource Balance  

El validador operativo completo se mantiene también en el repositorio hermano [`codigo-viajer-spec`](https://github.com/javier-viajer/codigo-viajer-spec).

---

## Capa TRCG / Pirámide-Parábola (v1.7)

Red de 24 nodos (4 sectores \(\times\) 6 estratos) construida a partir de 264 triples de la estructura relacional \(R\).

- Matriz de acoplamiento \(J_{24\times 24}\) simétrica, de diagonal nula y exactamente equivariante bajo \(\mathbb{Z}_4\).
- Descomposición en cuatro bloques hermíticos \(6\times 6\) bajo la base de Fourier de \(\mathbb{Z}_4\).
- Dinámica asíncrona con histéresis y funcional de Lyapunov \(\tilde{V}(T)\).
- Auditoría de regímenes no vacíos, multiplicidad de atractores y modos transversales (\(m=0,1,2,3\)).

### Estructura principal

| Carpeta / archivo | Contenido |
|-------------------|---------|
| `dynamics/` | Operadores de acoplamiento 47D, Jacobiano, topología de 276 aristas y simetría \(\mathbb{Z}_4\) |
| `v1.7/` | Paquete completo de auditoría (JSON, scripts de verificación, manifiestos, ventana larga) |
| `tests/` | Especificaciones y tests de contraste |
| `STATUS.md` | Estado de gobernanza y resultados de auditoría (Nivel II retenido · Nivel III abierto) |
| `ARCHITECTURE.md` | Arquitectura de alto nivel |
| `MATHEMATICAL_FOUNDATIONS.md` | Fundamentos matemáticos |

### Gobernanza (4º Factor)

- **Nivel II retenido**: consistencia estructural, equivariancia, monotonía de \(\tilde{V}\) y convergencia a puntos fijos verificadas.
- **Nivel III abierto**: sin ascenso automático. La multiplicidad de estados retenidos o la estabilidad dinámica no demuestran por sí solas emergencia espontánea desde bases no pre-codificadas ni validan formalmente \(\lambda\).
- v1.6 permanece aislada (`Fugas v1.6: []`).
- El símbolo \(\lambda\) está reservado exclusivamente al 4º Factor.

---

## Uso rápido (capa TRCG)

```bash
# Dependencias
pip install numpy scipy

# Ejemplo de verificación estructural de J_24x24
python -c "
from dynamics.topology_276 import build_edges_276
print('Topología cargada correctamente')
"
```

Los scripts de auditoría y los informes JSON se encuentran en `v1.7/`.

---

## Licencia y autoría

Distribuido bajo **Licencia MIT**.

Proyecto del ecosistema de **Javier Viajer**.

- Web: https://musicalcodes.es
- Repositorio hermano (validador operativo): https://github.com/javier-viajer/codigo-viajer-spec
```

### 2. Apartado para añadir al final de STATUS.md

```markdown
---

## 6. Auditoría detallada del régimen calibrado \(b_a = -2.0\), banda \((0.5, 2.5)\) — 25 de noviembre de 2026

**Parámetros**: \(b_a = -2.0\), \(\theta_{\rm off}=0.5\), \(\theta_{\rm on}=2.5\), \(\Delta\Phi_a=1.5\), 100 semillas, actualización asíncrona.

### Resultados principales
- Violaciones de \(\Delta\tilde{V}\le 0\): **0 / 5616** pasos.
- Atractores distintos: **89**.
- Distancia de Hamming entre atractores: mín = 1, media = **9.11**, máx = 21.

### Top-5 estados retenidos
| Rank | Frecuencia | \(\rho\) | \(m=0\) | \(m=1+3\) | \(m=2\) | Residuo \(\mathbb{Z}_4\) | Margen mín. |
|------|------------|----------|---------|-----------|---------|--------------------------|-------------|
| #1 | 6/100 | 0.000 | 0 % | 0 % | 0 % | 0.00 | 4.500 |
| #2 | 2/100 | 0.583 | 89.3 % | 7.1 % | 3.6 % | 0.33 | 0.700 |
| #3 | 2/100 | 0.167 | 50.0 % | 0 % | 50.0 % | 0.33 | 0.600 |
| #4 | 2/100 | 0.208 | 45.0 % | 50.0 % | 5.0 % | 0.50 | 0.700 |
| #5 | 2/100 | 0.083 | 25.0 % | 50.0 % | 25.0 % | 0.33 | 0.100 |

### Sensibilidad a flips unitarios
- Orden determinista: **61.33 %** de cambios de atractor (salto medio 2.35 bits).
- Orden aleatorio: **92.83 %** de cambios de atractor (salto medio 4.61 bits).

**Lectura**: multiplicidad real de estados retenidos bien diferenciados, presencia de modos transversales y cuencas sensibles a perturbaciones unitarias, manteniendo siempre monotonía de \(\tilde{V}\) y convergencia a puntos fijos.

**Gobernanza**: Nivel II retenido · Nivel III abierto (sin ascenso automático) · v1.6 aislada · \(\lambda\) reservado al 4º Factor.
```
