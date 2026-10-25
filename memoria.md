# memoria.md — Decisiones y contexto de ZOr Harness

Fuente de verdad del **porqué**: decisiones de producto y diseño. Nunca
re-proponer desde cero algo que ya está aquí (ni una alternativa rechazada)
sin que el usuario pida revisarlo. El **qué** (comportamiento) vive en
`specs/`.

## 1. Contexto del proyecto

**Qué es.** Un producto de ZOr Labs Peru SAC que generaliza el skill
`harness-agente-multisesion` del dueño (harness de documentación + SDD para que
un agente de IA dirija un proyecto durante muchas sesiones sin memoria) para
que:
- lo usen **varios usuarios** sobre el **mismo proyecto**, cada uno con su
  propio LLM (Claude, ChatGPT y, más adelante, Gemini u otros);
- sirva para **proyectos no tecnológicos**: investigación en grupo, trabajo
  grupal de MBA, consultoría, además de software.

**De dónde viene.** El skill base ya existe y está probado dirigiendo
proyectos de software y de data science de una sola persona. Sus decisiones de
fondo se heredan y no se re-litigan aquí: SDD propio en markdown (no la CLI de
OpenSpec), las tareas viven en `planner.md`, la capa SDD es obligatoria,
agnóstico de proveedor.

**Restricciones duras.**
- Capacidad del dueño: 1-2 sesiones/semana de 30-60 min (`planner.md §1`).
- El piloto es un trabajo de MBA **real, con fecha de entrega** (> 6 semanas
  desde el 2026-10-25): el producto no puede poner en riesgo esa entrega.
- Los datos y el trabajo de los compañeros del MBA no entran al repositorio
  (`agente.md §4`).

## 2. Análisis y hallazgos (2026-10-25, sesión de arranque)

### 2.1 Supuestos del skill base que dejan de valer en el nuevo contexto
| Supuesto del skill base | Por qué se rompe | Consecuencia para el producto |
|---|---|---|
| Hay repositorio git y Python local | Un grupo de MBA no corre `python openspec.py` ni hace commits | Los documentos viven en el almacén del grupo; la validación de puertas la hace el LLM o un servidor, no un script local |
| Un solo operador en sesiones secuenciales | Varias personas trabajan a la vez | Hace falta coordinación: roles, quién aprueba cada 🔒, responsable por tarea, concurrencia al editar `memoria.md` |
| Vocabulario de software | "capacidad", "delta", "verificación automática" no le dicen nada a un estudiante de MBA | Capa de **perfiles**: mismo motor, vocabulario y plantillas por tipo de proyecto |

### 2.2 Estado del soporte MCP entre LLMs (fuentes consultadas 2026-10-25)
- ChatGPT acepta servidores MCP como *Custom Connectors* en planes Plus, Pro,
  Business, Enterprise y Edu con funciones de desarrollador activadas (no en
  el plan gratuito).
- Cursor, Windsurf y VS Code + GitHub Copilot: soporte nativo.
- Gemini: a mayo de 2026 los productos públicos de consumo no permitían
  configurar MCP; Gemini CLI sí. **Revalidar antes de comprometer soporte.**
- Fuentes: docs.fullcontact.com/docs/quickstart ·
  contextbolt.com/blog/ai-tools-mcp-support

### 2.3 Tensión de tiempos
Con 1-2 sesiones/semana, un servidor MCP no estará listo antes de la entrega
del MBA. Por eso la recomendación (pendiente, `Q2`) es un **piloto sin
servidor** que corre en paralelo al desarrollo, y cuyos aprendizajes se
convierten en requisitos.

### 2.4 Mapeo preliminar motor → perfil MBA (borrador del agente, NO decidido)
| Concepto del motor | Perfil "Trabajo grupal MBA" |
|---|---|
| Capacidad (`specs/`) | Entregable o sección del trabajo |
| Cambio `Cnnn` | Iniciativa de trabajo ("Construir el análisis de la competencia") |
| Escenario DADO/CUANDO/ENTONCES | Criterio de aceptación derivado de la rúbrica |
| Tipos de verificación | Fuente citada · Revisión por un par · Cálculo reproducible · Cumple rúbrica |
| Puerta 🔒 | Avance presentado al profesor (`D4`) o acuerdo del grupo |
| `memoria.md` / `learn.md` | Decisiones del grupo / errores y feedback recibido |
| `planner.md` | Tareas con **responsable + fecha**, no solo sesiones |

Se formaliza (o se corrige) en el diseño del cambio que cree el perfil MBA.

## 3. Decisiones tomadas

### D1 — Es un producto de ZOr Labs, multiusuario y multi-LLM
- **Decisión:** la herramienta es un producto de ZOr Labs Peru SAC, para
  cualquier usuario (no una organización cerrada), que debe funcionar con
  distintos LLM. Hoy: Claude y ChatGPT; en algún momento, Gemini.
- **Razón:** los usuarios objetivo (p. ej. compañeros del MBA) ya usan LLMs
  distintos; obligarlos a uno solo excluye al grupo.
- **Alternativas rechazadas:** herramienta solo para Claude; herramienta
  interna para una organización Team/Enterprise.
- **Impacto:** todo formato base debe ser legible por cualquier LLM; las
  capas específicas de un proveedor son opcionales.

### D2 — El almacenamiento lo elige cada grupo
- **Decisión:** los documentos de cada proyecto viven donde el grupo elija.
- **Razón:** pedido explícito del dueño (2026-10-25).
- **Alternativas rechazadas:** almacén único impuesto (solo GitHub, solo
  Drive, solo Claude Docs).
- **Impacto:** el motor no puede depender de un almacén concreto. Cuántos
  almacenes se soportan en la v1 está pendiente (`Q2`).

### D3 — El piloto es el trabajo grupal de MBA real del dueño
- **Decisión:** la primera versión se valida con un trabajo grupal de MBA
  real, con entrega a más de 6 semanas desde 2026-10-25.
- **Razón:** es un caso no tecnológico, con varias personas y varios LLMs:
  justo lo que el producto debe resolver.
- **Alternativas rechazadas:** piloto con investigación académica, con
  software o con consultoría/DMAIC.
- **Impacto:** fase 1 del plan; la fecha de entrega del MBA restringe el
  cronograma. El proyecto del MBA es del grupo, no del producto (`agente.md §4`).

### D4 — En el MBA, las puertas se cierran con los avances al profesor
- **Decisión:** hoy el grupo decide trabajando en conjunto, presenta avances
  al profesor y con su feedback se cierra cada etapa. El perfil MBA modela
  esas presentaciones como las puertas 🔒.
- **Razón:** el proceso ya existe; el producto lo formaliza en vez de inventar
  burocracia nueva.
- **Alternativas rechazadas:** —
- **Impacto:** el profesor actúa como aprobador externo; cómo participa
  (¿usa la herramienta o no?) está pendiente (`Q5`).

### D5 — El proyecto se dirige con el skill `harness-agente-multisesion`, en un repo de GitHub
- **Decisión:** este mismo proyecto usa el harness + SDD del dueño, en un
  repositorio nuevo de GitHub.
- **Razón:** pedido explícito; además el producto se prueba a sí mismo
  (dogfooding): las carencias del harness que aparezcan aquí son requisitos.
- **Alternativas rechazadas:** carpeta local sin git; Google Drive (se pierde
  versionado por commit y la verificación de datos sensibles).
- **Impacto:** `openspec.py` y git disponibles; nombre del repo pendiente
  (`Q1`).

## 4. Contrato de datos / estructura
Aún no hay contrato entre sistemas. Nacerá con el cambio que defina el
formato portable de un proyecto (motor) y el servidor MCP.

## 5. Preguntas abiertas (pendientes de resolver con el usuario)
- [ ] **Q1** — Nombre del producto y del repositorio ("ZOr Harness" es nombre
  de trabajo). Bloquea: publicar el repo (`T0.1`).
- [ ] **Q2** 🔒 — ¿Se aprueba la arquitectura recomendada por el agente?
  (a) separar **motor** (principios, anclas, puertas, ciclo de cambio) de
  **perfiles** (vocabulario por tipo de proyecto) y de **infraestructura**
  (almacén + acceso); (b) **servidor MCP remoto** como capa multi-LLM, con
  validación de puertas del lado del servidor; (c) almacén con **puertos y
  adaptadores**, v1 con un solo adaptador (Google Drive); (d) **piloto sin
  servidor** primero. Bloquea: fases 1-2 (`T0.2`).
- [ ] **Q3** — ¿Qué plan de ChatGPT/Claude usan los compañeros del grupo? Si
  alguno usa plan gratuito, el piloto no puede depender de MCP. Bloquea: el
  diseño del kit del piloto.
- [ ] **Q4** — Datos del trabajo de MBA: curso/tema, número de integrantes,
  fechas de avances con el profesor, fecha exacta de entrega, y **si el grupo
  acepta usar la herramienta** (es su trabajo y su nota). Bloquea: cronograma
  de la fase 1 y el arranque del piloto.
- [ ] **Q5** — Rol del profesor: ¿solo cierra puertas vía avances (fuera de la
  herramienta) o tendría acceso a ella? Bloquea: diseño de roles.
- [ ] **Q6** — Modelo comercial y licencia (pago, freemium, código abierto).
  No bloquea la fase 1; sí la fase 3.
- [ ] **Q7** 🔒 — Con 1,5 sesiones/semana el kit del piloto estaría listo
  hacia la semana 11, probablemente después de la entrega del MBA. ¿Qué se
  hace? (a) piloto temprano manual con el skill actual adaptado; (b) subir el
  ritmo en la Fase 1; (c) fusionar C001 y C002; (d) el MBA solo aporta
  requisitos y el piloto es otro proyecto. Detalle en `planner.md §5`.
  Recomendación del agente: (a). Bloquea: `T0.4` y el orden de la Fase 1.
