# Senda

Mapa colaborativo de lugares para ir con niños en Catalunya: parques infantiles, naturaleza, cultura y otros planes, con atributos y adecuación por edad confirmados por las familias.

Trabajo Final del Máster de Desarrollo con IA (Bigschool).

## Stack

| Capa | Tecnología |
| --- | --- |
| Frontend | React + Vite + TypeScript, OpenLayers, react-i18next (ARQ-01, ARQ-02) |
| Backend | Django + GeoDjango, Django REST Framework, djangorestframework-gis, drf-spectacular, django-allauth (ARQ-03, ARQ-06) |
| Base de datos | PostgreSQL + PostGIS (ARQ-04) |
| Desarrollo local | Docker Compose (ARQ-10) |

Los identificadores entre paréntesis remiten al registro de decisiones del MVP (`docs/`).

## Estructura

```
senda/
├── frontend/      SPA React (Vite + TS)
├── backend/       API Django/GeoDjango
├── docs/          visión, PRD, constitución y decisions/ (ADR)
└── specs/         especificaciones SDD: NNN-nombre/{spec,plan,tasks}.md
```

## Puesta en marcha

Pendiente: se documentará al añadir `docker-compose.yml` (PostGIS + backend).

## Licencias y atribución

Datos de lugares © colaboradores de OpenStreetMap, disponibles bajo la licencia ODbL (DAT-09).
