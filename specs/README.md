# Especificaciones

**Índice de estado.** Es lo primero que se lee al empezar una sesión: dice qué spec está activa y en qué rama. Se actualiza al cambiar el estado de una spec.

| Spec | Tipo | Estado | Rama / PR | Siguiente paso |
| --- | --- | --- | --- | --- |
| 001-esqueleto | completa | pendiente | — | Redactar `spec.md` |

Estados: `borrador` → `en revisión` → `aprobada` → `en curso` → `hecha`.

## Cómo se trabaja

Una carpeta por funcionalidad, `NNN-nombre-corto/`, numerada con tres dígitos y creada desde `_plantillas/` (HAR-04):

| Fichero | Cuándo | Contenido |
| --- | --- | --- |
| `spec.md` | Siempre | Qué y por qué, con acceptance criteria Given/When/Then |
| `plan.md` | Solo spec completa | Cómo: cambios por capa, contrato, decisiones técnicas |
| `tasks.md` | Si hay más de un paso | Tareas pequeñas con los AC que cubren |
| `verification.md` | Al terminar | Qué test cubre cada AC, comandos ejecutados y resultado |

**Spec completa o ligera.** La completa (`spec.md` + `plan.md`) es para funcionalidades y para cualquier cambio en el modelo de datos, el contrato de API, una regla de negocio o más de una pantalla. La ligera (`spec-ligera.md`, sin plan) es para cambios pequeños y acotados.

**Ciclo (HAR-05):** spec → revisión humana → plan → revisión humana → tareas → implementación → verificación.

**Ramas y PR.** Cada spec se trabaja en su rama (`001-esqueleto`) y entra en `main` por pull request. `main` está protegida: no se fusiona sin el CI en verde.

**Trazabilidad.** Los tests llevan la etiqueta `NNN/AC-NN` del criterio que cubren. `scripts/check_ac.py` (en el CI) falla si una spec "hecha" tiene algún AC sin test.

La primera es `001-esqueleto`: un endpoint con lugares de prueba y un mapa OpenLayers que los pinta (HAR-09).
