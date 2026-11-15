# Diseño · referencia visual

Sistema de diseño y pantallas de Senda hechos con Claude Design (v0.2), descargados el 2026-11-15 del canvas https://claude.ai/artifact/1Kq1jAnANainKkPn5zvXGZ.

**Es referencia visual, no código a copiar (DIS-01).** Los ficheros `.dc.html` son prototipos del editor de Claude Design: no tienen componentes React, i18n ni datos de la API, y usan estilos en línea y Google Fonts. El frontend reproduce el aspecto con sus propios componentes, los tokens de `tokens.css` (DIS-03) y las fuentes servidas desde el propio dominio (DIS-02).

## Cuando el diseño contradice al registro, manda el registro

El diseño es anterior a algunas decisiones. Diferencias conocidas (ver "Cambios necesarios" en `docs/registro-decisiones.md`):

- Atributo "Comida cerca": no existe; en su lugar va "Gratuito" (ATR-08).
- Datos de ejemplo de Barcelona: la zona de validación son localidades por concretar (ALC-02).
- Fotos de lugares y subida de fotos: fuera del MVP (COM-11). Los huecos "foto del lugar" no se implementan.
- Estado "Sí" de un atributo: "confirmado por familias o por el equipo", no "por la fuente" (DAT-01).
- Etiqueta "Mucha sombra": no existe (COM-06).

## Qué mirar para cada cosa

| Fichero | Contenido | Úsalo para |
| --- | --- | --- |
| `Senda - Sistema de diseño.dc.html` | Colores, tipografía, espaciado, radios, sombras, iconos, componentes base | Extraer `tokens.css` y los iconos del catálogo |
| `Home.dc.html` | 01 Inicio (escritorio) | Portada, buscador, escenarios rápidos (EXP-07) |
| `MapExplore.dc.html` | 02 Mapa y resultados (escritorio) | Mapa + listado + filtros |
| `PlaceDetail.dc.html` | 04 Ficha de lugar (escritorio) | Ficha, atributos, edades, opiniones |
| `AddPlace.dc.html` | 05 Proponer lugar | Propuestas (COM-08, COM-09) |
| `Auth.dc.html` | 06 Registro | Autenticación (EXP-06) |
| `MobileMap.dc.html` | 07 Móvil · mapa | Mapa con hoja inferior (EXP-01) |
| `MobilePlace.dc.html` | 08 Móvil · ficha | Ficha en móvil |
| `RateForm.dc.html` | 10 Valorar lugar | Valoración (COM-01 a COM-06) |
| `AppHeader.dc.html`, `MapCanvas.dc.html` | Cabecera y mapa reutilizables | Componentes compartidos |
| `Senda - Propuesta UX-UI.dc.html` | Propuesta UX/UI completa | Contexto general; no hace falta para una spec concreta |
| `Senda - Deck.dc.html` | Presentación (24 diapositivas) | Contexto; no para implementar |

`support.js`, `ios-frame.jsx`, `deck-stage.js` y `compat.json` son el motor del editor y su lista de páginas; no forman parte del diseño.

Para agentes: no cargues todo el directorio. Cada spec enlaza las pantallas que le afectan en su sección "Diseño"; lee solo esas y el sistema de diseño si necesitas un valor.
