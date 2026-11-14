# AGENTS.md · frontend

Lee primero el `AGENTS.md` de la raíz. Aquí solo va lo específico del frontend.

- SPA React + Vite + TypeScript estricto. Mapa con OpenLayers; teselas OSM estándar con atribución visible (ARQ-02, DAT-09).
- Textos solo vía react-i18next (`es`, `ca`, `en`); el idioma va en la URL: `/es/`, `/ca/`, `/en/` (EXP-04).
- El cliente de la API se **genera** desde el contrato OpenAPI del backend; no lo edites a mano (ARQ-06).
- Cada lugar y cada combinación de filtros tiene URL propia (EXP-05).
- Puertas de calidad: ESLint, `tsc --noEmit`, Vitest; flujos con Playwright.

El proyecto Vite se crea en la spec 001 (esqueleto, HAR-09); los comandos se documentarán entonces.
