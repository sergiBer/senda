# Constitución de Senda

Reglas no negociables (HAR-08). Todo agente y toda persona las aplica por defecto. Cambiar una exige una decisión explícita del autor, registrada como ADR en `docs/decisions/`.

1. **Lo importado y lo aportado por personas no se mezclan en la misma fila.** OSM escribe en `Lugar` y `ReferenciaOSM`; los usuarios en `Valoracion` y sus respuestas; el equipo en `Siembra*`. Lo que se muestra sale de combinarlos en el estado publicado (DAT-03, ARQ-05).
2. **Todo texto visible se internacionaliza** en castellano, catalán e inglés. Ningún literal de interfaz en el código: frontend con react-i18next, backend con `gettext` o con el catálogo traducido (ALC-03, ALC-04).
3. **Accesibilidad básica obligatoria (ACC-02):** HTML semántico, contraste suficiente, etiquetas en formularios, estados no distinguidos solo por color y atributo `lang` correcto. El listado es la alternativa accesible al mapa (ACC-03).
4. **Ningún endpoint sin esquema OpenAPI.** Todo endpoint aparece en el contrato de drf-spectacular y el cliente TypeScript se genera desde él; no se escribe a mano (ARQ-06).
5. **Ninguna regla de negocio sin test.** Cada acceptance criterion Given/When/Then de una spec tiene al menos un test que lo cubre.
6. **Los catálogos son configuración versionada, no código** (TAX-08). Añadir una subcategoría o un atributo no exige tocar código Python ni TypeScript.
7. **Nada se borra si tiene aportaciones de la comunidad.** Los lugares se retiran (DAT-07); las cuentas borradas dejan sus valoraciones anónimas (PRI-01).
8. **Privacidad de menores.** No se guardan ni muestran edades de los hijos (COM-07, EDA-02).
