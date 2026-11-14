# Senda · Registro de decisiones del MVP

> Copia exportada el 2026-11-14 del documento vivo (https://claude.ai/artifact/CsjcUS3pVmJcphzvu1A5UX, rev. 75). Si difieren, manda el documento vivo; vuelve a exportarlo cuando cambie.

Oct 2, 2026 · @Sergi

Este registro recoge las decisiones cerradas antes de iniciar el desarrollo y prevalece sobre la Visión de producto, el PRD inicial y la propuesta UX/UI cuando se contradicen.

Cada decisión tiene un identificador estable (por ejemplo, `DAT-03`) para poder citarla desde especificaciones, ADR y código. Una decisión sustituida no se borra: se marca como sustituida y se indica cuál la reemplaza. La sección de cambios necesarios lista qué hay que actualizar en los documentos previos y en el diseño.

## Alcance y territorio

Se importa toda Catalunya y se valida en localidades escogidas de Catalunya, con la interfaz en tres idiomas.

| ID | Decisión | Motivo |
| --- | --- | --- |
| ALC-01 | La ingesta cubre toda Catalunya. El territorio es un parámetro de la ingesta, no un valor fijo en el código. | Volumen manejable y diseño preparado para escalar a España. |
| ALC-02 | La zona de validación son localidades escogidas de Catalunya (por concretar). Los criterios de éxito con cifras se miden sobre esta zona. | Permite elegir localidades donde haya familias disponibles para las pruebas. |
| ALC-03 | La interfaz estará en castellano, catalán e inglés, con internacionalización desde el primer día. | Público local y visitantes. Añadirlo después es caro. |
| ALC-04 | Textos de interfaz, categorías, atributos y etiquetas se traducen. Los nombres de OSM usan `name:<idioma>` si existe y, si no, `name`. Los comentarios se muestran en su idioma original, sin traducir. | Separar lo traducible de lo que no lo es. |
| ALC-05 | Nombre provisional del producto: Senda. | Cumple los criterios de marca de la visión. Dominio inicial: subdominio gratuito de No-IP. El dominio propio y la comprobación de marca quedan para más adelante; el dominio es configuración, no código. |

## Taxonomía y modelo de Lugar

El MVP parte de cuatro familias de categorías, con una regla objetiva para reducirlas a dos si los datos no las sostienen.

| ID | Decisión | Motivo |
| --- | --- | --- |
| TAX-01 | Cuatro familias: Juego y ocio, Naturaleza y aire libre, Cultura y aprendizaje, Otros planes (antes Servicios y equipamientos). | Clasificación visual y comprensible. "Otros planes" sustituye a la familia más difusa. |
| TAX-02 | Una familia entra en el MVP si en la zona de validación tiene al menos 50 lugares y se define con etiquetas OSM claras. Si no, el MVP se reduce a Juego y ocio + Naturaleza. | Decidir con datos de la auditoría, no por impresión. |
| TAX-03 | Subcategorías de partida, las del diseño: parques infantiles, ludotecas, centros de ocio; parques y áreas verdes, bosques, lagos y playas, zonas de picnic; bibliotecas, museos, centros culturales; espacios familiares, casales infantiles. | Lista corta, ajustable tras la auditoría. |
| TAX-04 | Las rutas quedan fuera del MVP. "Bosques y rutas fáciles" pasa a "Bosques". | En OSM las rutas son líneas y no encajan como Lugar. |
| TAX-05 | Cada lugar tiene una subcategoría principal. | Simplicidad. Las etiquetas adicionales quedan para más adelante. |
| TAX-06 | Un parque y el parque infantil que contiene son dos lugares independientes, sin relación entre ellos. | Lo más simple. Se aceptan marcadores próximos y valoraciones repartidas. |
| TAX-07 | Fuentes, bancos, aseos y cambiadores de OSM no son lugares y se descartan en la ingesta. | Regla de producto: son atributos, no destinos. |
| TAX-08 | Los catálogos (familias, subcategorías y su correspondencia OSM, atributos, franjas, etiquetas) se mantienen como configuración versionada, no como código. | Cambiar el catálogo no debe exigir cambiar código. |

### Subcategorías

Doce subcategorías de partida, cada una con sus etiquetas OSM candidatas; la auditoría confirmará o ajustará la correspondencia.

| Familia | Subcategoría | Qué incluye | Etiquetas OSM candidatas |
| --- | --- | --- | --- |
| Juego y ocio | Parques infantiles | Zonas de juego al aire libre de acceso público. | `leisure=playground` |
| Juego y ocio | Ludotecas | Espacios de préstamo y juego de juguetes. | `amenity=toy_library` |
| Juego y ocio | Centros de ocio | Parques de bolas, trampolines, parques acuáticos y temáticos. | `leisure=indoor_play`, `leisure=trampoline_park`, `leisure=water_park`, `tourism=theme_park` |
| Naturaleza y aire libre | Parques y áreas verdes | Parques urbanos y jardines públicos. | `leisure=park`, `leisure=garden` |
| Naturaleza y aire libre | Bosques | Bosques con nombre y acceso público. | `natural=wood`, `landuse=forest` |
| Naturaleza y aire libre | Lagos y playas | Láminas de agua con nombre y playas. | `natural=water` + `water=lake`, `natural=beach` |
| Naturaleza y aire libre | Zonas de picnic | Áreas habilitadas para comer al aire libre. | `tourism=picnic_site` |
| Cultura y aprendizaje | Bibliotecas | Bibliotecas públicas. | `amenity=library` |
| Cultura y aprendizaje | Museos | Museos y centros de interpretación. | `tourism=museum` |
| Cultura y aprendizaje | Centros culturales | Centros cívicos y de artes con programación. | `amenity=arts_centre` |
| Otros planes | Espacios familiares | Espacios municipales para familias con niños pequeños. | Sin etiqueta clara; probable alta por siembra |
| Otros planes | Casales infantiles | Casales y centros para niños y jóvenes. | `amenity=community_centre` (a validar) |

Reglas comunes de la ingesta: se importan solo elementos con nombre y sin `access=private`; se descartan parques infantiles dentro de recintos escolares; las mesas de picnic sueltas (`leisure=picnic_table`) no son lugares (TAX-07). Los bosques generan polígonos muy grandes y muchos sin nombre, así que son la subcategoría con más riesgo de ruido. "Otros planes" es la que más probablemente no supere TAX-02.

## Datos y procedencia

OSM aporta qué lugares existen, dónde están y qué son; los atributos familiares vienen de la comunidad y del equipo.

| ID | Decisión | Motivo |
| --- | --- | --- |
| DAT-01 | OSM solo proporciona la base: nombre, ubicación, geometría y categoría. No se extraen atributos familiares de OSM. | Las etiquetas familiares de OSM son escasas y poco fiables. |
| DAT-02 | No hay atributos derivados por cercanía (p. ej. fuente a X m del parque). | Simplicidad y honestidad del dato. Posible mejora futura que el modelo no debe impedir. |
| DAT-03 | Cada dato registra su origen: OSM, usuario o equipo. | Requisito de procedencia de la visión y el PRD. |
| DAT-04 | El equipo siembra atributos y adecuación por edad, prioritariamente en la zona de validación, mediante fichero de carga y panel de administración. Los datos sembrados cuentan como consolidados. | Evitar que los filtros devuelvan cero resultados al lanzar. |
| DAT-05 | El horario se muestra solo si viene de OSM (`opening_hours`). El transporte público queda fuera. | El transporte requeriría otra fuente de datos. |
| DAT-06 | La identidad del Lugar es interna y estable. La referencia OSM se guarda aparte. | Las aportaciones de la comunidad no pueden depender de identificadores externos. |
| DAT-07 | La reimportación es idempotente. Un lugar que desaparece de OSM se marca como retirado, nunca se borra. | Conservar valoraciones y comentarios. |
| DAT-08 | Las áreas guardan su geometría original y un punto representativo interior para el marcador. | El centroide puede caer fuera en formas irregulares. |
| DAT-09 | Atribución visible a OpenStreetMap (licencia ODbL). | Obligación de la licencia. |

## Atributos, edad y filtros

Un atributo solo cuenta en los filtros cuando alguien lo ha confirmado; los lugares sin el dato se excluyen.

| ID | Decisión | Motivo |
| --- | --- | --- |
| ATR-01 | Valores posibles de un atributo: sí, parcial, no o sin valor. | El diseño distingue "parcial" (p. ej. vallado solo en la zona de juegos). |
| ATR-02 | Respuestas al confirmar: sí, parcial, no, "no me fijé". Las de "no me fijé" no cuentan. | Evitar respuestas inventadas. |
| ATR-03 | Dos niveles: con 1 respuesta el atributo es visible y cuenta en filtros ("confirmado por 1 familia"); con mayoría y al menos 3 respuestas pasa a consolidado. | Una sola aportación ya es útil; la fiabilidad crece con el uso. |
| ATR-04 | El valor es el de la mayoría de respuestas. En empate, el atributo queda sin valor. | Regla simple y predecible. |
| ATR-05 | En conflicto prevalecen los usuarios. OSM no aporta atributos (DAT-01). | Consecuencia de DAT-01. |
| ATR-06 | Al filtrar por un atributo, los lugares sin valor se excluyen. "Parcial" sí cuenta, con su etiqueta visible en el resultado. | Fiabilidad de los resultados. |
| ATR-07 | Si un filtro deja pocos o ningún resultado, un estado vacío explica que hay pocos lugares con ese dato confirmado y sugiere quitar el filtro. | Que el usuario no confunda falta de datos con falta de lugares. |
| ATR-08 | Atributos de partida, los del diseño: carrito, movilidad reducida, sombra, WC, cambiador, fuente, bancos, picnic, vallado, aparcamiento y coste. Cada categoría pregunta solo los que le aplican. | La lista definitiva por categoría se fija en la especificación de catálogo. |
| ATR-09 | Sin descripciones de texto por atributo en el MVP. La tarjeta muestra icono, nombre y estado. | Nadie las generaría de forma fiable. "Parcial" queda sin explicar. |
| EDA-01 | Franjas de edad: 0-3, 4-7 y 8-12 años. | Se añade 8-12 respecto a los documentos previos, como en el diseño. |
| EDA-02 | Adecuación por franja con escala muy adecuado, adecuado, poco adecuado, no lo sé. No se pregunta la edad de los hijos de quien valora. | Información sobre el lugar, no sobre quien opina. |
| EDA-03 | La ficha muestra una tarjeta por franja con una barra que representa la media. | Diseño aprobado; útil para familias con hijos de varias edades. |
| EDA-04 | El filtro de edad muestra un lugar si su media en esa franja es "adecuado" o superior, con la misma regla de dos niveles que los atributos. | Coherencia con ATR-03. |

### Atributos por tipo de lugar

Las subcategorías se agrupan en tres perfiles, y cada perfil define qué atributos se preguntan y se muestran.

- **Exterior urbano:** parques infantiles, parques y áreas verdes.
- **Naturaleza:** bosques, lagos y playas, zonas de picnic.
- **Interior:** ludotecas, centros de ocio, bibliotecas, museos, centros culturales, espacios familiares, casales infantiles.

| Atributo (es) | Català | English | Exterior urbano | Naturaleza | Interior |
| --- | --- | --- | --- | --- | --- |
| Carrito | Cotxet | Stroller access | Sí | Sí | Sí |
| Movilidad reducida | Mobilitat reduïda | Wheelchair access | Sí | Sí | Sí |
| WC | Lavabos | Toilets | Sí | Sí | Sí |
| Sombra | Ombra | Shade | Sí | Sí |  |
| Fuente | Font | Drinking water | Sí | Sí |  |
| Picnic | Pícnic | Picnic area | Sí | Sí |  |
| Bancos | Bancs | Benches | Sí |  |  |
| Vallado | Tancat | Fenced | Sí |  |  |
| Aparcamiento | Aparcament | Parking |  | Sí | Sí |
| Cambiador | Canviador | Baby changing | Sí |  | Sí |
| Gratuito | Gratuït | Free entry |  |  | Sí |

El atributo "coste" de ATR-08 se pregunta como "Gratuito": sí, parcial (algunas actividades de pago) o no. Cada perfil tiene entre 6 y 9 atributos, más que las 3-5 preguntas de COM-03: el formulario de valoración pregunta primero por los que aún no están consolidados.

### Etiquetas destacadas

Catorce etiquetas iniciales que no repiten atributos; cada familia ofrece solo las suyas al valorar.

| Etiqueta (es) | Català | English | Familias |
| --- | --- | --- | --- |
| Tranquilo | Tranquil | Quiet | Todas |
| Se llena los fines de semana | S'omple els caps de setmana | Busy at weekends | Juego y ocio, Naturaleza |
| Juegos variados | Jocs variats | Varied play equipment | Juego y ocio |
| Ideal para bici y patinete | Ideal per a bici i patinet | Good for bikes and scooters | Juego y ocio, Naturaleza |
| Bueno para cumpleaños | Bo per a aniversaris | Good for birthday parties | Juego y ocio |
| Cafetería cerca | Cafeteria a prop | Café nearby | Juego y ocio, Naturaleza |
| Paseo corto | Passeig curt | Short walk | Naturaleza |
| Buenas vistas | Bones vistes | Great views | Naturaleza |
| Para bañarse | Per banyar-se | Good for swimming | Naturaleza |
| Animales a la vista | S'hi veuen animals | Wildlife to spot | Naturaleza |
| Actividades para niños | Activitats per a infants | Kids' activities | Cultura, Otros planes |
| Interactivo | Interactiu | Hands-on | Cultura |
| Bueno con lluvia | Bo per a dies de pluja | Good on rainy days | Juego y ocio, Cultura, Otros planes |
| Visita corta | Visita curta | Short visit | Cultura |

## Comunidad

Valorar es una sola acción que, además de las estrellas, rellena atributos, adecuación por edad y etiquetas.

| ID | Decisión | Motivo |
| --- | --- | --- |
| COM-01 | Valorar y opinar es una sola acción: estrellas (1-5) obligatorias, comentario opcional. | Fusiona F7 y F8 del PRD, como en el diseño. |
| COM-02 | La media de estrellas es global, no segmentada por edad. | Simplicidad. La adecuación por edad cubre esa necesidad (EDA-02). |
| COM-03 | Al valorar, preguntas cerradas opcionales sobre 3-5 atributos de la categoría del lugar. | La comunidad resuelve la falta de atributos en OSM. |
| COM-04 | Al valorar, pregunta opcional de adecuación por franja de edad (EDA-02). | Fuente de las barras de la ficha y del filtro de edad. |
| COM-05 | Una valoración por usuario y lugar, editable. | Evitar duplicados y sesgos. |
| COM-06 | "Lo que destacan las familias": etiquetas predefinidas por categoría, sin repetir atributos, selección opcional de hasta 3 al valorar. La ficha muestra las 5 más votadas con su contador. | Aporta matices que los atributos no cubren (p. ej. "Ideal para bici", "Tranquilo"). |
| COM-07 | Las opiniones no muestran edades exactas de los hijos. | Privacidad de menores. |
| COM-08 | Los usuarios registrados pueden proponer lugares nuevos. Las propuestas no son visibles hasta que un administrador las aprueba. | Sustituye a la decisión anterior de publicarlas como no verificadas. |
| COM-09 | Al proponer, aviso de lugares parecidos a menos de 150 m, con opción de continuar. | Reducir duplicados. Valor tomado del diseño. |
| COM-10 | Sin aviso de publicación ni apartado "Mis propuestas". El mensaje al enviar indica que el equipo la revisará. | Evita notificaciones fuera de alcance. |
| COM-11 | Fotos fuera del MVP. Modelo de datos y formulario preparados para añadirlas sin rehacer nada. No se muestra un botón inactivo. | Moderación, almacenamiento y privacidad de menores. Si se añaden: prohibido mostrar rostros de menores y fotos denunciables. |

## Moderación y roles

Un rol de administrador con un panel mínimo gestiona propuestas, denuncias y siembra; es una funcionalidad nueva respecto al PRD (F11).

| ID | Decisión | Motivo |
| --- | --- | --- |
| MOD-01 | Roles: anónimo, usuario registrado y administrador. | Las propuestas y denuncias necesitan a alguien que las gestione. |
| MOD-02 | Panel de administración mínimo (F11): cola de propuestas pendientes, comentarios denunciados y siembra de datos. Acciones: aprobar, rechazar, ocultar, editar, eliminar. | Requisito implícito de la regla 4 del PRD. Se apoya en Django Admin. |
| MOD-03 | Estados de una propuesta: pendiente, publicada o rechazada. | Revisión previa (COM-08). |
| MOD-04 | Los comentarios se publican al momento y cualquier usuario registrado puede denunciarlos. | Moderación ligera. |
| MOD-05 | Un comentario se oculta automáticamente tras 3 denuncias hasta que el administrador lo revise. El umbral es configurable. | Reacción rápida sin depender de la revisión manual. |
| MOD-06 | El administrador puede editar u ocultar el texto de un comentario con datos personales. | Complementa la anonimización al borrar cuentas (PRI-01). |

## Experiencia de usuario

La propuesta UX/UI de Senda es la base del diseño, con los ajustes indicados en la sección de cambios.

| ID | Decisión | Motivo |
| --- | --- | --- |
| EXP-01 | En móvil, mapa a pantalla completa con hoja inferior de resultados de tres alturas. | Definido en el diseño. |
| EXP-02 | Un usuario anónimo puede ver mapa, listado, filtros y fichas. Valorar, denunciar o proponer pide iniciar sesión y recuerda la acción pendiente. | Criterio de éxito del PRD: descubrir sin registrarse. |
| EXP-03 | Si se deniega la geolocalización, el mapa se centra en Catalunya y el usuario puede buscar una zona. | La historia 1 del PRD requiere "cerca de mí". |
| EXP-04 | Idioma en la URL (`/es/`, `/ca/`, `/en/`). En la primera visita se usa el del navegador, con castellano de respaldo. Selector de idioma visible. | Enlaces compartibles en el idioma correcto. |
| EXP-05 | Cada lugar y cada combinación de filtros tiene URL propia. | Definido en el diseño. |
| EXP-06 | Autenticación con Google y con email y contraseña. Sin Apple. | Apple exige una cuenta de pago de desarrollador. |
| EXP-07 | Escenarios de entrada rápida: "Con bebé", "Para jugar" y "Escapada". | Del diseño; también sirven como escenarios de validación. |
| EXP-08 | Las fichas no se indexan en buscadores ni generan vistas previas específicas al compartir. | Limitación aceptada de la SPA. Se resolvería con un endpoint de metadatos. |

## Privacidad, accesibilidad y criterios de éxito

El MVP se valida con al menos 5 familias y 50 lugares sembrados en localidades escogidas de Cataluña.

| ID | Decisión | Motivo |
| --- | --- | --- |
| PRI-01 | Al eliminar una cuenta se borran sus datos personales. Sus valoraciones se conservan anónimas (autor "Familia anónima") y siguen contando en medias y consolidación. | Derecho de supresión sin romper los agregados. |
| PRI-02 | Textos legales básicos: política de privacidad, aviso legal y aceptación al registrarse. | RGPD. |
| ACC-01 | Accesibilidad no prioritaria, pero con informe de impacto frente a WCAG 2.2 AA como entregable. | Documentar qué se cumple, qué no y cuánto costaría. |
| ACC-02 | Reglas básicas de obligado cumplimiento: HTML semántico, contraste suficiente, etiquetas en formularios, estados no distinguidos solo por color y atributo `lang` correcto. | Coste casi nulo si se aplican desde el principio. |
| ACC-03 | El listado es la alternativa accesible al mapa y contiene la misma información. | El mapa no es usable con lector de pantalla. |
| EXI-01 | Al menos 50 lugares de la zona de validación sembrados con atributos principales y adecuación por edad. | Concreta el criterio del PRD sobre lugares iniciales suficientes. |
| EXI-02 | Pruebas con al menos 5 familias usando los tres escenarios de EXP-07. | Validación cualitativa del PRD. |
| EXI-03 | Al menos el 80 % encuentra un lugar adecuado en cada escenario en menos de 2 minutos. | Métricas 1 y 2 del PRD con valor objetivo. |

## Arquitectura y stack

Una SPA en React consume una API Django/GeoDjango sobre PostGIS; GeoServer y OGC API Features quedan fuera del MVP.

| ID | Decisión | Motivo |
| --- | --- | --- |
| ARQ-01 | Frontend: SPA con React, Vite y TypeScript. Internacionalización con react-i18next. | Todo el frontend en cliente, coherente con OpenLayers. |
| ARQ-02 | Mapa con OpenLayers. Mapa base: teselas estándar de OpenStreetMap, cumpliendo su política de uso (atribución, identificación de la aplicación, sin descarga masiva). | Coste cero y suficiente para el tráfico del MVP. Si el tráfico crece o se quiere el estilo cálido del diseño, alternativa: teselas vectoriales propias (PMTiles) servidas desde el VPS. |
| ARQ-03 | Backend: Django, GeoDjango, Django REST Framework, djangorestframework-gis y django-allauth (modo para SPA). | Integración geográfica madura, admin incluido, convenciones fuertes para los agentes. |
| ARQ-04 | Base de datos: PostgreSQL con PostGIS. | Consultas por área, distancia y duplicados. |
| ARQ-05 | Una vista del estado publicado de cada lugar, con atributos consolidados y adecuación por edad calculados. La API filtra sobre ella. | Filtros rápidos y única fuente de verdad. Preparada para OGC API Features. |
| ARQ-06 | Contrato OpenAPI generado con drf-spectacular. El cliente TypeScript del frontend se genera desde el contrato. | El contrato forma parte de la especificación; un cambio incompatible rompe la compilación. |
| ARQ-07 | Ingesta como comando independiente: extracto de Catalunya de Geofabrik, transformación con la tabla de correspondencia OSM y carga idempotente. | Reproducible y separada de la web. |
| ARQ-08 | Sin GeoServer. | No sustituye a la API de negocio y añade un servidor pesado sin necesidad. |
| ARQ-09 | OGC API Features como evolución futura, con pygeoapi integrado en Django sobre la vista publicada. Al publicarla, la capa se distribuye bajo ODbL. | Interoperabilidad y valor de portfolio, fuera del alcance del MVP. |
| ARQ-10 | Monorepo con `frontend/` y `backend/`. Docker Compose con PostGIS para desarrollo local. | Un único repositorio para el harness y los agentes. |
| ARQ-11 | Capa alternativa de ortofoto mediante WMTS. Opciones: ICGC (solo Catalunya, mayor detalle local) o PNOA del IGN/CNIG (toda España). La fuente se configura por territorio y debe ofrecer EPSG:3857 para evitar reproyección en el cliente. | Ayuda a reconocer el entorno del lugar. PNOA encaja con la escalabilidad a España; ambas requieren atribución. |
| ARQ-12 | Hosting de frontend, backend y base de datos en un VPS (previsiblemente Hetzner, en la UE) con Docker Compose, proxy inverso con HTTPS automático y copias de seguridad de PostGIS fuera del servidor. | Control total y coste bajo. Datos en la UE (RGPD). Implica asumir actualizaciones, seguridad y copias. |

Alternativas descartadas: Next.js + Supabase (renderizado en servidor incompatible con el mapa en cliente, lógica dispersa en SQL), FastAPI (autenticación, admin y consultas geográficas por ensamblar; segunda opción), NestJS (soporte de PostGIS inferior), Supabase como backend (reglas de negocio en funciones SQL y triggers) y Spring Boot (más lento de desarrollar, fuera de los lenguajes del autor).

## Harness y SDD

El desarrollo sigue un flujo propio de SDD con plantillas markdown, independiente de la herramienta de agentes.

| ID | Decisión | Motivo |
| --- | --- | --- |
| HAR-01 | Agentes: Claude Code, opencode y Codex. | Elección del autor. |
| HAR-02 | `AGENTS.md` en la raíz como única fuente de contexto, más uno breve en `frontend/` y `backend/`. `CLAUDE.md` solo referencia a `AGENTS.md`. | Codex y opencode leen `AGENTS.md`; Claude Code lee `CLAUDE.md`. |
| HAR-03 | El flujo vive en plantillas markdown, no en comandos propios de una herramienta. | Funciona igual con los tres agentes. |
| HAR-04 | Estructura: `docs/` (visión, PRD, constitución, `decisions/` con ADR) y `specs/NNN-nombre/` con `spec.md`, `plan.md` y `tasks.md`. | Separar el qué, el cómo y las tareas. |
| HAR-05 | Ciclo por funcionalidad: spec → revisión humana → plan → revisión humana → tareas → implementación → verificación contra criterios de aceptación. | Las revisiones evitan que el agente decida por el autor. |
| HAR-06 | Criterios de aceptación en formato Dado/Cuando/Entonces, convertibles en tests. | Base para verificar el código generado. |
| HAR-07 | Puertas de calidad: Ruff y pytest (backend); ESLint, TypeScript y Vitest (frontend); Playwright (flujos). En pre-commit y CI. | Feedback automático para los agentes. |
| HAR-08 | Constitución con reglas no negociables: separar datos importados y de usuario, i18n en todos los textos, ACC-02, ningún endpoint sin esquema OpenAPI, ninguna regla de negocio sin test. | Reglas que todos los agentes aplican por defecto. |
| HAR-09 | La primera especificación es un esqueleto de extremo a extremo: un endpoint con lugares de prueba y un mapa OpenLayers que los pinta. | Validar harness, contrato y agentes antes de construir funcionalidad. |
| HAR-10 | Registrar el uso de la IA durante el desarrollo: qué se pidió, qué se corrigió y dónde falló. | Evidencia para la evaluación del curso. |

## Sistema de diseño

El sistema de diseño v0.2 de Claude Design es la referencia visual; sus valores viven en `tokens.css` y sus iconos en el catálogo.

| ID | Decisión | Motivo |
| --- | --- | --- |
| DIS-01 | "Senda - Sistema de diseño" v0.2 es la referencia visual. El paquete de Claude Design se guarda en `design/` como referencia, no como código a copiar. | El prototipo no tiene componentes React, i18n ni datos del API. |
| DIS-02 | Tipografías Bricolage Grotesque (títulos), Figtree (interfaz) y JetBrains Mono (datos), e iconos Material Symbols Rounded, servidos desde el propio dominio mediante paquetes npm, no desde Google Fonts. | Evita enviar la IP de los usuarios a terceros (RGPD) y no depende de un servicio externo. |
| DIS-03 | Todos los colores, tipos, espaciados, radios y sombras salen de `tokens.css`. Ningún valor fuera de los tokens. | Coherencia visual y regla verificable por los agentes. |
| DIS-04 | Cada familia, subcategoría, atributo, estado y escenario tiene su icono en el catálogo (`iconos.yaml`), no en el código. | Coherente con TAX-08. |
| DIS-05 | Las estrellas en ámbar (contraste 2,9:1) siempre van acompañadas del valor numérico. El texto secundario nunca baja de Tinta 3. | El ámbar no alcanza el 3:1 de WCAG para elementos gráficos. |

## Cambios necesarios en visión, PRD y diseño

Tres documentos deben actualizarse para que no contradigan este registro antes de que los lean los agentes.

| Documento | Cambio | Decisión |
| --- | --- | --- |
| Visión | La estrategia de datos: OSM solo como base; atributos de la comunidad y del equipo. | DAT-01, DAT-04 |
| Visión | Nombre provisional Senda y categoría "Otros planes". | ALC-05, TAX-01 |
| PRD | Añadir F11 (panel de administración) y fusionar F7 y F8 en una sola acción de valorar. | MOD-02, COM-01 |
| PRD | Ampliar F7 con preguntas cerradas, adecuación por edad y etiquetas destacadas. | COM-03, COM-04, COM-06 |
| PRD | Franjas de edad 0-3, 4-7 y 8-12. | EDA-01 |
| PRD | Requisitos no funcionales: idiomas, accesibilidad, privacidad. | ALC-03, ACC-01, PRI-01 |
| PRD | Criterios de éxito y métricas con cifras. | EXI-01 a EXI-03 |
| PRD | Cerrar las decisiones abiertas de la sección 15 haciendo referencia a este registro. | Todas |
| Diseño | Quitar acceso con Apple, transporte público, descripciones por atributo y "te avisamos". | EXP-06, COM-11, DAT-05, ATR-09, COM-10 |
| Diseño | Añadir selector de idioma y estado vacío para filtros con pocos resultados. | EXP-04, ATR-07 |
| Diseño | Etiquetas destacadas sin repetir atributos (quitar "Mucha sombra"). | COM-06 |
| Diseño | Cambiar "Bosques y rutas fáciles" por "Bosques". | TAX-04 |
| Diseño | Corregir la nota del mapa (teselas OSM, no Esri) y añadir el cambio de capa a ortofoto. | ARQ-02 |
| Diseño | Revisar el principio "útil desde el primer día con datos públicos". | DAT-01, DAT-04 |
| Diseño | Quitar la zona de subida de fotos del formulario de proponer lugar. | COM-11 |
| Diseño | Quitar la subcategoría "Equipamientos útiles". | TAX-03 |
| Diseño | Quitar "Comida cerca" como atributo y añadir "Gratuito". | ATR-08 |
| Diseño | Estado "Sí": "confirmado por familias o por el equipo", no "por la fuente". | DAT-01 |
| Diseño | Quitar "Mucha sombra" del deck y de la propuesta UX/UI. | COM-06 |

## Cuestiones pendientes y siguientes pasos

Quedan abiertos detalles que se cierran en las primeras especificaciones; ninguno bloquea empezar el harness.

Pendiente de confirmar:

- [x] TAX-05 y COM-05 son supuestos razonables no discutidos explícitamente: una subcategoría principal por lugar y una valoración editable por usuario y lugar.
- [x] Lista de atributos por categoría y de etiquetas destacadas, en los tres idiomas.
- [x] Proveedor de teselas para OpenLayers y hosting de frontend, backend y base de datos.
- [x] Disponibilidad del nombre Senda (dominio y marca).

Siguientes pasos, en orden:

1. Actualizar visión, PRD y diseño según la sección anterior.
2. Auditoría de OSM: lugares por subcategoría en la zona de validación y en Catalunya, y tabla de correspondencia de etiquetas.
3. Catálogo de producto como configuración versionada (TAX-08).
4. Modelo de dominio conceptual: entidades, estados y reglas.
5. Diseño de la ingesta y de la siembra.
6. Lista de endpoints a partir de las pantallas.
7. Harness: monorepo, `AGENTS.md`, constitución, plantillas, puertas de calidad y la especificación del esqueleto (HAR-09).
8. Backlog de especificaciones: esqueleto, catálogo y modelo, ingesta, mapa y listado, filtros, ficha, autenticación, valoración, propuestas, moderación, textos legales e informe de accesibilidad.
