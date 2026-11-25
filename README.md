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


**Gobernanza**: Nivel II retenido · Nivel III abierto (sin ascenso automático) · v1.6 aislada · \(\lambda\) reservado al 4º Factor.
```
