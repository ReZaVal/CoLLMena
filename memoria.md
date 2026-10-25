# memoria.md — Decisiones y contexto de coLLMena

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
- El piloto es un trabajo de MBA **real, con fecha de entrega** (marzo de
  2027, `D3`): el producto no puede poner en riesgo esa entrega.
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

### 2.5 Hallazgos sobre Drive y ChatGPT (S-06, 2026-10-25)
- **Versiones de archivos subidos (.docx/.xlsx/.pptx/.txt):** Drive las
  guarda, pero cada versión antigua puede borrarse **a los 30 días o cuando
  hay 100 versiones más nuevas**, salvo que se marque **«Conservar para
  siempre»** (Manage versions → Keep forever). Una versión nueva se crea
  subiéndola **sobre el mismo archivo** (Manage versions → Upload new
  version); subir un archivo nuevo con el mismo nombre **no** continúa el
  historial. Fuente: support.google.com/drive/answer/2409045.
- **Consecuencias para el producto:** (1) toda escritura debe **reemplazar
  el mismo archivo**, nunca crear uno nuevo; (2) en un proyecto de meses (la
  tesis va hasta marzo de 2027) las versiones intermedias se pierden: hay
  que marcar «conservar para siempre» en hitos, y el hito natural es cada
  avance al profesor (`D4`). → **(2) sin efecto desde S-08 por `D13`**: no
  se conservan versiones; se lleva bitácora de cambios.
- **ChatGPT con Drive:** según una nota de prensa de ~agosto de 2026, ChatGPT
  puede crear y editar archivos **nativos** de Google (Docs, Sheets, Slides)
  para usuarios de pago elegibles, con aprobación del usuario antes de
  actuar. No se confirma que edite .docx/.xlsx/.pptx. Fuente:
  letsdatascience.com/news/chatgpt-adds-direct-editing-for-google-drive-files-503e4d8d.
  **Revalidar con documentación oficial de OpenAI.** Tensión con `D11`: ver
  `Q12`.
- **Un .docx subido a Drive "se abre en Google Docs"** (observación del
  dueño, S-07), pero hay **dos modos distintos** (fuente:
  support.google.com/drive/answer/9276408):
  - **Edición de Office** (por defecto): se ve la interfaz de Google Docs,
    pero el archivo **sigue siendo .docx**; los cambios se guardan solos en
    el mismo archivo en formato Office. Límites: algunas funciones de Office
    no se muestran o se pierden (con aviso), los archivos muy grandes pueden
    fallar al guardar, y los comentarios resueltos o borrados no se guardan
    en el .docx.
  - **Conversión a formato Google**: "Archivo → Guardar como Documentos de
    Google", o el ajuste de Drive «Convertir archivos subidos al formato del
    editor de Documentos de Google» (solo afecta a archivos subidos después
    de activarlo). Que la conversión cree una copia aparte no está
    confirmado por la fuente.
  - Para el producto: las **personas** pueden editar Office en Drive sin
    salir del navegador (`D9` y `D11` compatibles). La pregunta abierta es
    solo si **ChatGPT** puede editar un archivo en modo Edición de Office o
    únicamente archivos nativos (`Q12`).

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
- **Decisión:** la primera versión se valida con el trabajo final (tesis) de
  `CURSO_01` en `ESCUELA_01`, un MBA enfocado en sostenibilidad: **4
  integrantes, entrega en marzo de 2027** (día exacto pendiente, `Q4`). El
  tema real está en `local_privado/glosario.md` como `TEMA_01`.
  (Actualizado en S-02; antes decía "entrega a más de 6 semanas".)
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

### D6 — Arquitectura: motor + perfiles + infraestructura (aprobada en S-02)
- **Decisión:** el producto se desarrolla bajo la arquitectura del harness:
  (a) **motor** de método (principios, anclas, puertas, ciclo de cambio)
  separado de los **perfiles** por tipo de proyecto y de la
  **infraestructura** (almacén + acceso); (b) **servidor MCP remoto** como capa
  multi-LLM, con la validación de puertas del lado del servidor; (c) almacén
  con **puertos y adaptadores**; (d) piloto sin servidor antes del servidor.
- **Razón:** el dueño: "es la arquitectura del harness, es lo que ya hemos
  desarrollado". El motor ya está probado; lo nuevo son perfiles e
  infraestructura.
- **Alternativas rechazadas:** skill generalizado sin servidor como producto
  final (no resuelve multiusuario de verdad); app web propia como único canal
  (obliga a dejar el LLM de cada uno).
- **Impacto:** fases 1-2 de `manager.md`; capacidades `MOTOR`, `PERFIL`,
  `ACCESO`, `ALMACEN`, `VALID`, `COLAB`. Cuándo arranca el piloto frente al
  calendario del MBA sigue en `Q7`.

### D7 — Google Drive es parte de la propuesta de valor (primer adaptador)
- **Decisión:** el producto se conecta con Google Drive para **almacenar y
  editar** los documentos del grupo. Es el primer adaptador de `ALMACEN`.
- **Razón:** pedido del dueño (S-02): el nombre y la oferta del producto
  incluyen trabajo en grupo + varios LLMs + Drive.
- **Alternativas rechazadas:** GitHub como almacén del usuario final
  (excluye a no técnicos); almacén propio de ZOr Labs en la v1.
- **Impacto:** `D2` sigue vigente (otros almacenes después), pero Drive va
  primero. Cómo se implementa el **versionado** sobre Drive (historial nativo
  de revisiones u otro mecanismo) es un supuesto a verificar en el cambio que
  cree el adaptador.

### D8 — El problema que resuelve el producto (validado en el piloto)
- **Decisión:** el producto es un **espacio de trabajo de grupo** que:
  (1) **optimiza el uso de tokens** del LLM, (2) permite que cada integrante
  use **el LLM que prefiera**, y (3) da **control versionado de tareas y
  documentos**.
- **Razón:** hoy el grupo piloto trabaja con LLMs dentro de **un solo chat**
  donde mezcla documentos y anotaciones: el consumo de tokens es alto (cada
  mensaje re-carga todo el historial), no hay un repositorio ubicable y no hay
  versiones de los documentos (dueño, S-02).
- **Alternativas rechazadas:** —
- **Impacto:** criterios de éxito de todos los cambios. (1) se apoya en la
  lectura quirúrgica del harness (principio §1 del skill base: «Contexto
  activo» + «Mapa de extractos» en vez de cargar todo); (3) en `planner.md` y
  en el almacén versionado (`D7`).

### D9 — El usuario final NO es técnico
- **Decisión:** el producto debe poder usarlo gente sin conocimientos de
  programación ni de tecnología. Su valor es **facilitar el uso de LLMs en un
  espacio compartido** a quien no sabe nada de estas herramientas (dueño,
  S-03).
- **Razón:** el grupo piloto y el mercado objetivo (estudiantes de MBA,
  equipos de investigación) no son técnicos.
- **Alternativas rechazadas:** producto para desarrolladores o usuarios
  avanzados de IA.
- **Impacto:** regla de diseño para **todos** los cambios:
  - El usuario nunca instala nada, nunca escribe comandos, nunca ve git,
    Python, markdown crudo ni IDs como `D3`, `T1.4` o `C001`. Esa maquinaria
    existe para el LLM, no para la persona.
  - Habla en lenguaje llano: "revisión del profesor", "decisiones del grupo",
    "lo que falta para el próximo avance"; nada de "puerta P4" o "delta".
  - El versionado es automático (no depende de que alguien "haga commit").
  - Conectar el LLM y Drive debe tomar minutos y sin pasos técnicos; si un
    paso requiere configuración técnica, es un **riesgo de producto**, no un
    detalle (ver `Q9`).
  - Criterio de prueba: una persona no técnica del grupo usa una función sin
    ayuda de Renzo.

### D10 — El producto se llama coLLMena
- **Decisión:** nombre del producto **coLLMena** (juego entre "colmena" y
  "LLM"). Repositorio: `collmena` (minúsculas). Hasta S-03 el nombre de
  trabajo era "ZOr Harness".
- **Razón:** elección del dueño (S-04) a partir del candidato "Kolmena":
  colmena = grupo con roles distintos y un panal ordenado; "LLM" va escondido
  en la palabra.
- **Alternativas rechazadas:** Kolmena, Minka (muy usado; ya existe una app
  así), Ayni (muy usado en Perú), Faena (connotación negativa fuera de Perú),
  Quorum (ya usado por productos con IA).
- **Consecuencias a gestionar (señaladas por el agente, no decididas):**
  - Un usuario no técnico (`D9`) no sabe qué es "LLM": leerá "colmena". El
    juego de palabras es un guiño, no el mensaje principal.
  - Quien escuche el nombre escribirá "colmena" (una sola L) y llegará a
    otras colmenas; una búsqueda de "collmena" en S-04 solo devolvió
    resultados de "colmena". Conviene registrar también el dominio con una L
    y que redirija.
  - La mezcla de mayúsculas es para el logotipo; en URLs, correos y el repo
    va en minúsculas.
- **Impacto:** títulos de todos los documentos; repo `collmena` (`T0.1`).

### D11 — Formatos de documento: Office (.docx, .pptx, .xlsx) y .txt
- **Decisión:** los documentos del grupo en Drive son **.docx, .pptx y
  .xlsx**, y pueden ser **.txt** (dueño, S-05). No Google Docs nativos ni
  markdown visible para el usuario.
- **Razón:** son los formatos que el usuario no técnico (`D9`) ya conoce y
  que se entregan en el MBA (tesis, presentación, cálculos).
- **Alternativas rechazadas:** Google Docs nativos; markdown como formato
  visible al usuario.
- **Interpretación del agente a confirmar (`Q11`):** separar
  **documentos de trabajo** (los entregables que el grupo edita: .docx,
  .pptx, .xlsx) de **documentos de control** (decisiones, plan, aprendizajes
  y contexto que mantiene el LLM: .txt con estructura simple). Razón: el
  texto plano lo lee cualquier LLM sin conversión, gasta menos tokens que un
  .docx (`D8`) y cualquiera lo abre en Drive.
- **Impacto:** el motor debe leer/escribir .txt para el control y leer (y
  quizá escribir) Office para el trabajo. Supuestos a verificar en el diseño
  de `C001`/`C002`: (a) si el historial de versiones de Drive cubre archivos
  .docx/.pptx/.xlsx/.txt subidos (requisito de versionado de `D8`); (b) si
  Claude y ChatGPT pueden **escribir** esos formatos en Drive o solo leerlos
  (`Q9`).

### D12 — El LLM siempre lee; edita solo si la persona lo elige
- **Decisión:** el LLM debe poder **leer** todos los documentos del grupo y
  **editarlos solo cuando la persona elige** que lo haga (dueño, S-06).
- **Razón:** el usuario mantiene el control de su trabajo; coincide con
  cómo ya operan los conectores comerciales (aprobación antes de editar,
  `§2.5`).
- **Alternativas rechazadas:** LLM de solo lectura (obliga a copiar y pegar);
  LLM que edita sin preguntar.
- **Impacto:** requisito de `ACCESO` y `COLAB` (confirmación antes de cada
  edición); toda edición reemplaza el mismo archivo para no romper el
  historial (`§2.5`).

### D13 — Trazabilidad de documentos: bitácora de cambios en .txt (no versiones)
- **Decisión:** no hace falta conservar versiones de los documentos. Lo que
  se requiere es un **registro de cambios en .txt** de los documentos que se
  creen, que funcione **como los commits de GitHub**: cada cambio queda
  anotado (dueño, S-08).
- **Razón:** al grupo le importa saber **qué cambió, quién, cuándo y por
  qué**, no volver a una versión anterior.
- **Alternativas rechazadas:** depender del historial de versiones de Drive
  y marcar «conservar para siempre» en cada hito (`§2.5`).
- **Consecuencia aceptada (señalada por el agente):** un commit de git
  guarda el mensaje **y** el contenido; esta bitácora guarda solo el
  mensaje. No permite recuperar el texto anterior de un documento; si alguna
  vez hiciera falta, queda el historial de Drive de los últimos 30 días.
- **Impacto:** precisa el punto (3) de `D8`: "control versionado" =
  bitácora de cambios. Ya no es requisito congelar versiones en hitos
  (`§2.5`, consecuencia 2). Pendientes de diseño: `Q13` y `Q14`.

### D14 — MVP: una sola bitácora de cambios para todo el proyecto
- **Decisión:** en el MVP hay **un solo documento** de bitácora de cambios
  (.txt) para todo el proyecto, con el documento afectado como campo de cada
  entrada. Sin historial de versiones (reafirma `D13`). Dueño, S-09.
- **Razón:** simplicidad para el MVP; además el LLM lee un solo archivo al
  empezar cada sesión (ahorro de tokens, `D8`).
- **Alternativas rechazadas:** una bitácora por documento.
- **Impacto:** cierra `Q13`. Formato preliminar de entrada (borrador del
  agente, se fija en el diseño de `C001`): número correlativo · fecha ·
  integrante · LLM usado · documento · qué cambió · motivo · tarea.

### D15 — Cambios hechos a mano: se cuentan al LLM o el LLM los detecta
- **Decisión:** los cambios que una persona hace directamente en Drive
  entran a la bitácora (`D14`) de dos maneras: (1) la persona se los cuenta
  al LLM, o (2) el LLM los **detecta al empezar la sesión** e informa qué
  documentos cambiaron y quién los cambió (dueño, S-10).
- **Razón:** la bitácora debe reflejar todo el trabajo, no solo lo que pasa
  por el LLM.
- **Alternativas rechazadas:** aceptar el hueco (registrar solo lo que pasa
  por el LLM).
- **Límite señalado por el agente:** sin historial de versiones (`D13`), el
  LLM puede saber **qué archivo** cambió, **cuándo** y **quién** (si Drive
  expone esos datos), pero **no qué texto** cambió. El "qué" y el "por qué"
  los debe contar la persona. Flujo propuesto: el LLM detecta → informa
  "el Capítulo 3 lo modificó la integrante 2 el martes" → pregunta qué se
  hizo → registra la entrada.
- **Supuestos a verificar en el diseño (`C001`/`C002`):** que el conector de
  Drive de Claude y de ChatGPT expongan la fecha de modificación y el último
  usuario que modificó cada archivo.
- **Impacto:** cierra `Q14`. Requisito para `COLAB` y `ACCESO`.

## 4. Contrato de datos / estructura
Aún no hay contrato entre sistemas. Nacerá con el cambio que defina el
formato portable de un proyecto (motor) y el servidor MCP.

## 5. Preguntas abiertas (pendientes de resolver con el usuario)
- [x] ~~**Q1**~~ → cerrada en S-04 como `D10` (coLLMena). Queda pendiente
  la revisión de marca en INDECOPI y de dominio (`Q10`).
- [x] ~~**Q2**~~ → cerrada en S-02 como `D6`.
- [ ] **Q3** — ¿Qué plan de ChatGPT/Claude usan los compañeros del grupo? Si
  alguno usa plan gratuito, el piloto no puede depender de MCP. Bloquea: el
  diseño del kit del piloto.
- [ ] **Q4** — Datos del trabajo de MBA. Ya se sabe (S-02, ver `D3`): tesis
  de MBA en sostenibilidad, 4 integrantes, entrega en marzo de 2027, el grupo
  ya usa LLMs. Falta: día exacto de entrega, fechas de avances con el
  profesor, y **acuerdo explícito del grupo** para usar la herramienta (que
  ya usen LLMs no equivale a aceptar ser piloto). El dueño enviará los datos.
  Bloquea: cronograma fino de la fase 1 y el arranque del piloto.
- [ ] **Q5** — Rol del profesor: ¿solo cierra puertas vía avances (fuera de la
  herramienta) o tendría acceso a ella? Bloquea: diseño de roles.
- [ ] **Q6** — Modelo comercial y licencia (pago, freemium, código abierto).
  No bloquea la fase 1; sí la fase 3.
- [ ] **Q7** 🔒 — Con 1,5 sesiones/semana el kit del piloto estaría listo
  hacia la semana 11 (≈ enero 2027). Con entrega en marzo de 2027 sí llega,
  pero el grupo solo lo usaría en el último tramo y hoy ya sufre el problema
  de `D8`. ¿Qué se hace? (a) piloto temprano manual con el skill actual adaptado; (b) subir el
  ritmo en la Fase 1; (c) fusionar C001 y C002; (d) el MBA solo aporta
  requisitos y el piloto es otro proyecto. Detalle en `planner.md §5`.
  Recomendación del agente: (a). Bloquea: `T0.4` y el orden de la Fase 1.
- [x] ~~**Q8**~~ → cerrada en S-05 como `D11` (Office + .txt).
- [ ] **Q11** — ¿Se confirma la separación de `D11`: entregables en
  .docx/.pptx/.xlsx y documentos de control del LLM en .txt? Bloquea: diseño
  de `C001`.
- [ ] **Q12** — Tensión entre `D11` (Office) y `D12` (editar si la persona
  elige): ChatGPT edita en Drive archivos **nativos** de Google; no está
  confirmado que edite .docx/.xlsx/.pptx (`§2.5`); las personas sí pueden
  editarlos en Drive con Edición de Office (S-07). Opciones a evaluar (no
  decididas): (a) entregables en formato nativo de Google (p. ej. activando
  la conversión automática de Drive) y exportar a Office al entregar; (b) mantener Office y que la edición desde ChatGPT pase por
  coLLMena (servidor propio); (c) mantener Office y, en ChatGPT, solo
  lectura + el LLM propone el texto. Se resuelve verificando en el diseño de
  `C002`. Bloquea: diseño de `C002`.
- [x] ~~**Q13**~~ → cerrada en S-09 como `D14` (una sola bitácora).
- [x] ~~**Q14**~~ → cerrada en S-10 como `D15`.
- [ ] **Q9** — Cómo conecta su LLM una persona no técnica. Tensión detectada
  en S-03 entre `D6`(b) y `D9`: en ChatGPT, un servidor MCP propio requiere
  activar funciones de desarrollador (`§2.2`), un paso técnico. Opciones a
  evaluar (no decididas): usar los **conectores nativos de Drive** que ya
  traen Claude y ChatGPT + instrucciones del proyecto para el piloto; MCP
  solo donde la conexión sea simple; o una app propia que llame a los LLMs.
  Inferencia a confirmar, **no** un cambio de `D6`. Se verifica como
  supuesto en el diseño de `C002`.
- [ ] **Q10** — Registro de marca "coLLMena" en INDECOPI (y otros países si
  se sale de Perú) y compra de dominios (`collmena` y `colmena` con su
  variante disponible). Decisión y trámite del dueño; el agente no es
  abogado. No bloquea el piloto; bloquea cualquier lanzamiento público.
