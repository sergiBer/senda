# NNN · Verificación

> Se rellena al terminar la implementación, antes de pedir la fusión del PR.
> PR: <enlace> · Fecha: AAAA-MM-DD

## Cobertura de acceptance criteria

| AC | Test que lo cubre | Resultado |
| --- | --- | --- |
| AC-01 | `backend/…/test_….py::test_…` | ✅ pasa |
| AC-02 | `frontend/…/….test.tsx` | ✅ pasa |

`python scripts/check_ac.py` → <salida>

## Comandos ejecutados

| Comando | Resultado |
| --- | --- |
| `docker compose exec backend pytest` | <N passed> |
| `docker compose exec backend ruff check .` | <limpio> |
| `pre-commit run --all-files` | <limpio> |
| CI del PR | <enlace al run, en verde> |

## Comprobación manual

<Qué se ha probado a mano (pantalla, flujo) y con qué resultado. "No aplica" si no hay interfaz.>

## Desviaciones

<Qué cambió respecto a spec o plan, y por qué. "Ninguna" si no hay.>
