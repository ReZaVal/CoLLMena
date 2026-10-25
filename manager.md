# manager — Director de coLLMena

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
- **En qué estoy:** Fase 0. `T0.1` 🟡 — nombre elegido (`D10`, coLLMena);
  falta que el dueño cree el repo privado y vacío `collmena` en GitHub para
  subir los commits. `T0.3` 🟡 — faltan datos del MBA. Ningún cambio aprobado.
- **Cambió en las últimas sesiones (S-02 a S-04):** arquitectura aprobada
  (`D6`); Drive como primer almacén (`D7`); problema del producto desde el
  dolor real del grupo (`D8`); usuario final no técnico (`D9`); nombre
  coLLMena (`D10`); entrega del MBA en marzo de 2027 (`D3`).
- **S-05:** formatos Office + .txt (`D11`); abierta `Q11` (separar
  entregables de documentos de control).
- **S-06:** `D12` el LLM lee siempre y edita si la persona elige; hallazgos
  de Drive y ChatGPT en `memoria.md §2.5`.
- **S-08/S-09:** `D13` sin versiones; `D14` una sola bitácora de cambios
  .txt tipo commit para todo el proyecto; `D15` cambios a mano los cuenta la
  persona o los detecta el LLM.
- **Abiertas que más pesan:** `Q7` (cuándo arranca el piloto), `Q9`
  (conectar el LLM sin pasos técnicos), `Q11`, `Q12` (Office vs edición
  desde ChatGPT).
- **Cambios abiertos:** `C001` — 🟡 borrador, antes de P1.
- **Próximos pasos:** repo `collmena` → cerrar `T0.1`; datos del MBA y `Q7`
  → `T0.3` → `T0.4`.

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
| T1.1-T1.5 (C001) | `memoria.md §2.4`, `D3`, `D4`, `specs/PERFIL.md`, `specs/COLAB.md` | `cambios/C001-*/`, (al archivar) `specs/` |
| T1.6-T1.10 (C002) | `memoria.md §2.2`, `D1`, `specs/ACCESO.md`, `specs/VALID.md` | `cambios/C002-*/` |

(Las filas se refinan con anclas exactas al abrir cada cambio.)

## Fases del proyecto

### Fase 0 — Arranque y alineación ⬅ actual
Dueño: `memoria.md`.
- [x] Instalar el harness (2026-10-25).
- [ ] Repo publicado en GitHub (`Q1`).
- [x] Arquitectura aprobada (`D6`, S-02).
- [ ] Datos del MBA y acuerdo del grupo (`Q3-Q5`).
Criterio de salida: `Q1`, `Q2`, `Q3` y `Q4` cerradas como `Dn`; cronograma
recalculado con la fecha real de entrega del MBA.

### Fase 1 — Piloto MBA sin servidor
Dueño: `cambios/` + `specs/`.
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
| 0 — Arranque y alineación | 🟡 en curso |
| 1 — Piloto MBA sin servidor | ⬜ no iniciada |
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
