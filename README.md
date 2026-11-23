# Código Viajer — Control de Estabilidad Dinámica en ℝ⁴

**Versión canónica: v1.7**

Módulo experimental de gobernanza preventiva para sistemas de IA autónomos.  
Evalúa trayectorias en un espacio de estados de cuatro dimensiones y emite decisiones `ALLOW` / `THROTTLE` / `REJECT`.

> Este repositorio contiene dos capas relacionadas pero distintas:
>
> 1. **Código Viajer** — validador dinámico operativo (capa principal).
> 2. **TRCG / Pirámide-Parábola** — marco matemático en desarrollo (carpetas `core/`, `dynamics/`, `boundary/`).
>
> No se afirma que la TRCG esté demostrada como teoría física completa.  
> El estado epistemológico de cada componente se detalla en `STATUS.md`.

---

## Arquitectura del validador (Código Viajer)

Estado del agente: $\mathbf{X} = (L, S, I, B) \in [0,1]^4$

- $L$: Life Preservation  
- $S$: Entropy  
- $I$: Node Integrity  
- $B$: Resource
