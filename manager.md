# manager — Director de CoLLMena

No explica el cómo (eso está en los docs de dominio y en los diseños de cada
cambio): dice en qué orden se hace el trabajo, qué documento es dueño de cada
pieza, y cuál es el criterio para pasar de fase.

## ⚠️ REGLA PRIORITARIA — Nada del trabajo de MBA ni de terceros entra al repo (leer SIEMPRE, antes de cualquier commit)
El piloto usa un trabajo real de un grupo real. Al repositorio solo entran
aprendizajes anonimizados y ejemplos sintéticos. Lo real va a `local_privado/`
(una sola regla en `.gitignore`). Antes de cada commit:
`git diff --cached --stat` + `git check-ignore -v local_privado/<archivo>`.
Seudónimos y glosario: `agente.md §4`.

## Mapa de documentos
| Documento | Responde a |
|---|---|
| `agente.md` | Protocolo de cómo opera el agente (entrada) |
| `memoria.md` | ¿Qué se decidió y por qué? ¿Qué falta confirmar (`§5`)? |
| `planner.md` | ¿En cuántas tareas se parte cada fase, cuánto cuesta y cuándo? |
| `learn.md` | ¿Qué errores se detectaron y qué regla dejaron? ¿Qué le falta al harness (`§4`)? |
| `specs/<cap>.md` | ¿Qué hace hoy el producto y cómo se verifica? |
| `cambios/<Cnnn>/` | ¿Qué cambio está en curso, con qué diseño, supuestos y delta? |
| `openspec.py` | ¿Está el cambio listo para implementar / archivar? |
| `entorno.md` | (nace con el primer hallazgo) Comportamiento real de LLMs, conectores y herramientas |
| `README.md` | ¿Qué es CoLLMena, explicado a alguien no técnico? |
| `INSTRUCCIONES_PROYECTO.md` | Texto que va en las instrucciones del proyecto de claude.ai (cuelga el harness) |
| `marketing/` | Prompts de diseño y textos de comunicación (identidad: `memoria.md D17`) |
| `manager.md` (este) | ¿En qué orden, y cuándo está "listo" cada paso? |

Docs de dominio previstos (se crean con la primera tarea de su tipo, no
antes): `perfiles.md` (cómo se escribe un perfil de proyecto), `mcp.md` (cómo
se construye el servidor).

`manager.md` y `planner.md` son complementarios: **este** dice el orden de las
fases y el criterio para cerrarlas; `planner.md` las descompone en tareas. Si
necesitas saber **qué hacer ahora mismo**, la respuesta está en `planner.md §4`.

Regla de oro: si una decisión cambia, se actualiza `memoria.md` primero, y
luego specs/diseños/código. No dupliques decisiones — referencia por `Dn`.

### Capacidades del producto (una spec por capacidad)
| Prefijo | Capacidad | En una frase |
|---|---|---|
| `MOTOR` | Motor de método | Documentos, anclas, puertas y ciclo de cambio, independientes del dominio |
| `PERFIL` | Perfiles de proyecto | Vocabulario, plantillas y tipos de verificación por tipo de proyecto (v1: MBA) |
| `COLAB` | Colaboración multiusuario | Roles, aprobadores de puertas, responsable por tarea, concurrencia |
| `ACCESO` | Acceso multi-LLM | Cómo un usuario con Claude, ChatGPT u otro LLM opera el mismo proyecto |
| `ALMACEN` | Almacenamiento | Dónde viven los documentos del proyecto del grupo |
| `VALID` | Validación de puertas | Comprobar consistencia P1-P5 sin que el usuario corra Python |

### Puertas de un cambio (resumen; detalle en el skill base, principio §21)
P1 Alcance (🔒 usuario) → P2 Diseño + delta → P3 Supuestos verificados →
P4 Preguntas con disposición (🔒 usuario) → P5 `openspec.py validate
--strict --cambio Cnnn` en verde. Recién ahí se implementa.

## Contexto activo (lo primero que se lee al arrancar; mantener corto)
- **En qué estoy:** Fase 1 🟡: `T1.15` ✅ (S-17, kit aprobado por el dueño);
  sigue `T1.16` 🔒. `T0.1` ✅ (S-13) — repo `ReZaVal/CoLLMena`
  publicado (privado). `T0.3` y `T0.4` ✅ (S-16, `D40`). Ningún
  cambio aprobado. `D18`: el nombre es CoLLMena en todos lados, igual que el repo.
- **Cambió en las últimas sesiones (S-02 a S-04):** arquitectura aprobada
  (`D6`); Drive como primer almacén (`D7`); problema del producto desde el
  dolor real del grupo (`D8`); usuario final no técnico (`D9`); nombre
  CoLLMena (`D10`); entrega del MBA en marzo de 2027 (`D3`).
- **S-05:** formatos Office + .txt (`D11`); abierta `Q11` (separar
  entregables de documentos de control).
- **S-06:** `D12` el LLM lee siempre y edita si la persona elige; hallazgos
  de Drive y ChatGPT en `memoria.md §2.5`.
- **S-08/S-09:** `D13` sin versiones; `D14` una sola bitácora de cambios
  .txt tipo commit para todo el proyecto; `D15` cambios a mano los cuenta la
  persona o los detecta el LLM.
- **S-11:** `README.md` (descripción no técnica), prompt de landing en
  `marketing/`; `D16` más LLMs (Grok, DeepSeek…), `D17` identidad visual.
- **S-13:** `D18` nombre CoLLMena en todos los nombres; `T0.1` cerrada.
- **S-14:** `D19` el MBA es un caso de uso, no el fin; `D20` LLM de plan
  gratuito a pago con inicio de sesión propio; `D21` panal; `D22` Drive,
  edición en Google u Office y registro en cada carga; `D23` el profesor sin
  rol y carpeta de contexto por panal; `D24` el panal es un proyecto; `D25` el
  LLM redacta el registro y la persona confirma; `D26` contexto multiformato y
  ahorro de tokens; `D27` mapa de contexto + conversión a texto; `D28` sin
  video ni audio; `D29` el panal define objetivo y reglas; `D30` registro
  obligatorio; `D31` Q4 es referencial (prueba de producto). Cerradas `Q3`,
  `Q4`, `Q5`, `Q9`, `Q11`, `Q12`, `Q16`, `Q18`. `D32`: cada panal elige un
  framework refinado del SDD; lectura de Drive por LLM verificada (`§2.6`).
- **S-15:** `D33` superpowers complementa al harness (`agente.md` manda);
  `D34` solo en la ejecución de tareas con código, tras P5; `D35` ramas y PR
  en lugar de commits directos en `main`; `D36` subagentes solo con permiso del
  dueño (tarea y fin); `D37` convención de ramas y PR; `D38` el agente fusiona
  solo cuando el dueño lo pide expresamente; `agente.md §8` recoge las reglas
  de `D33`-`D38`. `D39`: `main` sin protección técnica, por convención.
  Cerradas `Q20`, `Q21` y `Q22`.
- **S-16:** `D40` piloto temprano manual (opción a de `Q7`); marzo de 2027 es
  fecha referencial, no restricción dura. Cerradas `Q7` y `T0.3`. `T0.4`:
  nuevas `T1.15`-`T1.16` (piloto manual) y cronograma recalculado; cierre
  estimado de la Fase 1: 2027-01-24.
- **S-17:** `T1.15` ✅: kit del piloto manual en `local_privado/piloto/`
  (plantillas .txt para ChatGPT y Claude); inferencias a confirmar en
  `local_privado/piloto_revision_T1.15.md`; nueva `M6` (modo sin escritura).
- **Abiertas que más pesan:** `Q19` (quién elige el framework; bloquea el
  diseño de `C001`), `Q17` (ChatGPT gratuito y Drive; bloquea el de `C002`).
- **Cambios abiertos:** `C001` — 🟡 borrador, antes de P1.
- **Próximos pasos:** `T1.16` 🔒 (subir el kit al Drive del grupo, con
  confirmación) →
  `T1.1`; `Q19` antes de `T1.2`.

## Mapa de extractos por fase (qué leer/tocar sin abrir todo)
Convención de anclas: `memoria.md` → `§n`, `Dn`, `Qn`; specs → `<CAP>-Rn`;
cambios → `Cnnn`, `Sn`, `Pn`; `learn.md` → `Ln`, `Mn`; tareas → `TX.Y`.
Regla: "leer" = contrato (no editar); "tocar" = dónde va el cambio. Si un ancla
no existe donde dice esta tabla, es un error de la tabla → corregirla aquí.

### Fase 0 — Arranque y alineación
| Tarea | Leer | Tocar |
|---|---|---|
| T0.1 Publicar repo | `memoria.md Q1`, `D5` | remoto git, `memoria.md §3` |
| T0.2 Aprobar arquitectura | `memoria.md §2`, `Q2` | `memoria.md §3` (→ `D6`) |
| T0.3 Datos del MBA y acuerdo del grupo | `memoria.md Q3-Q5`, `D3`, `D4` | `memoria.md §3/§5`, `local_privado/` |
| T0.4 Recalcular plan | `planner.md §1-§2` | `planner.md §2, §5` |

### Fase 1 — Piloto MBA sin servidor
| Tarea | Leer | Tocar |
|---|---|---|
| T1.15-T1.16 (piloto manual, `D40`) | skill base, `memoria.md D4`, `D21`, `D22`, `D40`, `Q17` | `local_privado/piloto/`, Drive del grupo (con confirmación), `learn.md` |
| T1.1-T1.5 (C001) | `memoria.md §2.4`, `D3`, `D4`, `specs/PERFIL.md`, `specs/COLAB.md` | `cambios/C001-*/`, (al archivar) `specs/` |
| T1.6-T1.10 (C002) | `memoria.md §2.2`, `D1`, `specs/ACCESO.md`, `specs/VALID.md` | `cambios/C002-*/` |

(Las filas se refinan con anclas exactas al abrir cada cambio.)

## Fases del proyecto

### Fase 0 — Arranque y alineación ✅
Dueño: `memoria.md`.
- [x] Instalar el harness (2026-10-25).
- [x] Repo publicado en GitHub (`D10`, `D18`, S-13).
- [x] Arquitectura aprobada (`D6`, S-02).
- [x] Datos del MBA y acuerdo del grupo (`Q3`, `Q5` cerradas en S-14; `Q4` referencial por `D31`; `Q7` → `D40`, S-16).
- [x] Cronograma recalculado (`T0.4`, S-16).
Criterio de salida: `Q1`, `Q2`, `Q3` y `Q4` cerradas como `Dn`; cronograma
recalculado con la fecha real de entrega del MBA.

### Fase 1 — Piloto MBA sin servidor ⬅ actual
Dueño: `cambios/` + `specs/`.
- Piloto manual (`D40`): el grupo usa un harness hecho a mano mientras se
  construye el kit (`T1.15`-`T1.16`).
- C001 — Crear el perfil MBA (`PERFIL`, `COLAB` en modo manual).
- C002 — Empaquetar el kit portable para Claude y ChatGPT (`ACCESO`, `VALID`
  asistida por el LLM).
- El grupo usa el kit en su trabajo real; lo aprendido entra como `Mn`/`Ln`.
Criterio de salida: `C001` y `C002` archivados con escenarios en verde, **y**
el grupo usó el kit en al menos un avance presentado al profesor, con sus
hallazgos registrados.

### Fase 2 — Servidor MCP + primer adaptador de almacén
Dueño: `cambios/` + `specs/`. Se detalla al cerrar la Fase 1, con lo que el
piloto enseñó. Candidatos: validación del lado del servidor (`VALID`), roles y
bloqueo de tareas (`COLAB`), adaptador Google Drive (`ALMACEN`), separación
formal motor/perfiles (`MOTOR`).
Criterio de salida: cambios archivados; un segundo grupo (o el mismo) opera un
proyecto desde Claude y ChatGPT contra el mismo servidor.

### Fase 3 — Producto
Más adaptadores, tablero web, autenticación, modelo comercial (`Q6`). Sin
detallar hasta cerrar la Fase 2.

## Estado actual (actualizar en cada sesión)
| Fase | Estado |
|---|---|
| 0 — Arranque y alineación | ✅ completada (S-16) |
| 1 — Piloto MBA sin servidor | 🟡 en curso (S-17) |
| 2 — Servidor MCP + adaptador | ⬜ no iniciada |
| 3 — Producto | ⬜ no iniciada |
Convención: ⬜ no iniciada · 🟡 en curso · ✅ completada · 🔴 bloqueada (por qué).

## Cómo retomar en una sesión nueva
1. Leer `agente.md`, luego este archivo («Contexto activo» primero).
2. Leer `memoria.md §5` para ver preguntas abiertas.
3. Abrir `planner.md`: protocolo de apertura (`§3`), tomar la primera tarea
   pendiente con dependencias cerradas (`§4`); la bitácora (`§6`) dice en qué
   quedó la sesión anterior.
4. Si la tarea pertenece a un cambio, leer su carpeta en `cambios/`.
5. Al cerrar una decisión o fase: `memoria.md` primero, luego `planner.md`,
   luego el estado aquí.
