# AGENTS.md · frontend

Lee primero el `AGENTS.md` de la raíz. Aquí solo va lo específico del frontend.

- SPA React + Vite + TypeScript estricto. Mapa con OpenLayers; teselas OSM estándar con atribución visible (ARQ-02, DAT-09).
- Textos solo vía react-i18next (`es`, `ca`, `en`); el idioma va en la URL: `/es/`, `/ca/`, `/en/` (EXP-04).
- El cliente de la API se **genera** desde el contrato OpenAPI del backend; no lo edites a mano (ARQ-06).
- Cada lugar y cada combinación de filtros tiene URL propia (EXP-05).
- Puertas de calidad: ESLint, `tsc --noEmit`, Vitest; flujos con Playwright.

## Diseño

- Referencia visual en `design/` (raíz del repo): prototipos de Claude Design, **no código a copiar** (DIS-01). Lee `design/README.md` y solo las pantallas que enlaza la spec.
- Todos los colores, tipos, espaciados, radios y sombras salen de `src/styles/tokens.css`; ningún valor suelto en componentes (DIS-03). Ya existe, extraído de `design/Senda - Sistema de diseño.dc.html`; si falta un valor, añádelo ahí, no en el componente.
- Fuentes (Bricolage Grotesque, Figtree, JetBrains Mono) e iconos Material Symbols Rounded vía paquetes npm, servidos desde el propio dominio; nunca Google Fonts (DIS-02).
- Los iconos de familias, subcategorías, atributos, estados y escenarios vienen del catálogo (`iconos.yaml`), no del código (DIS-04).
- Estrellas en ámbar siempre con su valor numérico; texto secundario nunca más claro que Tinta 3 (DIS-05).
- Si el diseño contradice al registro de decisiones, manda el registro.

El proyecto Vite se crea en la spec 001 (esqueleto, HAR-09); los comandos se documentarán entonces.
