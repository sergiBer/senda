# NNN · <Nombre de la funcionalidad>

> Estado: borrador | en revisión | aprobada | en curso | hecha
> Tipo: completa
> Rama: `NNN-nombre`
> Decisiones relacionadas: <IDs del registro, p. ej. ATR-03, EDA-04>

## Problema y objetivo

<Qué necesidad de la familia resuelve y por qué ahora. 2-4 frases.>

## Alcance

**Incluye:**
- …

**No incluye:**
- …

## Historias de usuario

- Como <rol>, quiero <acción> para <beneficio>.

## Diseño

Pantallas de `design/` que afectan a esta funcionalidad (ver `design/README.md`). Solo estas se leen al implementar.

- `design/<Pantalla>.dc.html`: <qué parte aplica>
- Diferencias con el diseño que manda el registro: <o "ninguna">

## Acceptance criteria

Cada criterio se convierte en al menos un test (HAR-06). Numéralos para citarlos desde `tasks.md` y desde los tests con la etiqueta `NNN/AC-NN` (por ejemplo `# 001/AC-01` en Python o `// 001/AC-01` en TypeScript). El CI comprueba que, al marcar la spec como "hecha", cada AC tiene su etiqueta en algún test (`scripts/check_ac.py`).

### AC-01 · <título corto>
- **Given** <contexto inicial>
- **When** <acción>
- **Then** <resultado observable>

### AC-02 · <título corto>
- **Given** …
- **When** …
- **Then** …

## Textos de interfaz (i18n)

| Clave | es | ca | en |
| --- | --- | --- | --- |
| `…` | … | … | … |

## Preguntas abiertas

- [ ] …
