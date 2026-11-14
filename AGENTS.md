# AGENTS.md · Senda

Fuente única de contexto para los agentes (Claude Code, opencode, Codex). `CLAUDE.md` solo importa este fichero (HAR-02). Hay un `AGENTS.md` breve en `frontend/` y otro en `backend/` con lo específico de cada parte.

## Qué es Senda

SPA para descubrir lugares adecuados para ir con niños en Catalunya. OSM aporta la base (qué lugares hay, dónde y qué son); las familias y el equipo aportan atributos, adecuación por edad y valoraciones. Interfaz en castellano, catalán e inglés.

## Documentos que mandan

Por orden de prioridad cuando se contradicen:

1. `docs/constitucion.md`: reglas no negociables. Nunca las incumplas sin una decisión explícita del autor.
2. Registro de decisiones del MVP (`docs/registro-decisiones.md`). Cita las decisiones por su ID (`DAT-03`, `ARQ-05`…) en specs, ADR y comentarios de código cuando expliquen un porqué.
3. La spec activa en `specs/NNN-nombre/`.
4. ADR en `docs/decisions/`.

Si algo no está decidido, **pregunta**; no decidas por el autor.

## Flujo de trabajo (SDD, HAR-05)

Cada funcionalidad sigue este ciclo. No saltes pasos ni avances sin la revisión humana indicada.

1. **Spec** (`specs/NNN-nombre/spec.md`, desde `specs/_plantillas/spec.md`): qué y por qué, con acceptance criteria Given/When/Then (HAR-06). → **revisión humana**
2. **Plan** (`plan.md`): cómo, qué ficheros, qué decisiones técnicas. → **revisión humana**
3. **Tareas** (`tasks.md`): pasos pequeños y verificables, cada uno con su test.
4. **Implementación**: tarea a tarea; marca cada una al cerrarla.
5. **Verificación**: cada acceptance criterion Given/When/Then tiene al menos un test que lo cubre y pasa.

Al terminar una sesión de trabajo relevante, añade una entrada en `docs/ia/registro-uso-ia.md` (HAR-10): qué se pidió, qué se corrigió y dónde falló el agente.

## Estructura

```
frontend/   SPA React + Vite + TypeScript + OpenLayers   → ver frontend/AGENTS.md
backend/    Django + GeoDjango + DRF + PostGIS            → ver backend/AGENTS.md
docs/       constitución, registro de decisiones, ADR, registro de uso de IA
specs/      NNN-nombre/{spec,plan,tasks}.md y _plantillas/
```

## Comandos

```bash
docker compose up -d                 # PostGIS + backend en http://localhost:8000
docker compose exec backend pytest   # tests del backend
docker compose exec backend ruff check . && docker compose exec backend ruff format --check .
pre-commit run --all-files           # todas las puertas de calidad
```

Los comandos del frontend se añadirán con la spec 001 (esqueleto, HAR-09).

## Puertas de calidad (HAR-07)

Un cambio no está terminado hasta que pasan, en local (pre-commit) y en CI:

- Backend: Ruff (lint + formato) y pytest.
- Frontend: ESLint, `tsc --noEmit` y Vitest.
- Flujos: Playwright.

No desactives una regla ni marques un test como `skip` para que pase; si crees que la regla sobra, dilo.

## Convenciones

- Términos de metodología en inglés: Given/When/Then, acceptance criteria (`AC-01`…), spec, plan, tasks. El registro de decisiones dice "Dado/Cuando/Entonces" (HAR-06): es lo mismo.
- Código, nombres de modelos y comentarios en castellano sin tildes en identificadores (`Lugar`, `Valoracion`, `nombre_visible`), como en el modelo de datos.
- Commits en castellano, estilo Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`, `test:`), referenciando la spec si la hay (`feat(001): ...`).
- Ningún secreto en el repo: variables en `.env` (ignorado), con ejemplo en `.env.example`.
