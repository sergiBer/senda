# AGENTS.md · backend

Lee primero el `AGENTS.md` de la raíz. Aquí solo va lo específico del backend.

- Django + GeoDjango + DRF + djangorestframework-gis + drf-spectacular + django-allauth (modo SPA) sobre PostGIS (ARQ-03, ARQ-04).
- Se ejecuta en Docker: `docker compose exec backend <comando>` desde la raíz del repo.
- Apps previstas: `cuentas` (Usuario), `catalogo`, `lugares`, `comunidad`. El modelo de usuario es `cuentas.Usuario` (`AUTH_USER_MODEL`); referéncialo siempre con `settings.AUTH_USER_MODEL`, nunca importándolo directamente en modelos.
- `on_delete`: `PROTECT` hacia catálogo y lugares, `SET_NULL` hacia el usuario (PRI-01), `CASCADE` solo de una valoración a sus respuestas.
- Toda vista de API declara su esquema (drf-spectacular). Comprueba con `python manage.py spectacular --validate --fail-on-warn`.
- Tests con pytest + pytest-django. Las migraciones se generan con `makemigrations` y se revisan antes de commitear; nunca edites una migración ya publicada.
- Lint y formato: `ruff check .` y `ruff format .`.
