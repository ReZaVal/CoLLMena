# planner.md — Plan de tareas, sesiones y cronograma de CoLLMena

Descompone las fases de `manager.md` en **tareas atómicas ejecutables en una
sesión**, les pone dependencias, estimación y fecha referencial, y define cómo
se abre y se cierra cada sesión.

División de responsabilidades (no duplicar contenido):
- `manager.md` → qué orden y cuándo una fase está lista (criterio de salida).
- `planner.md` (este) → en cuántas tareas se parte, de qué cambio sale cada
  una y qué escenarios cierra, quién depende de quién, cuántas sesiones cuesta.
- `memoria.md` → qué se decidió. Aquí solo queda la referencia `Dn`/`Qn`.

Un cambio de plan **no** es una decisión de negocio: se actualiza este archivo
(y la tabla de estado de `manager.md` si mueve una fase), no `memoria.md`,
salvo que cambie el alcance.

## 1. Parámetros del plan (definidos por el usuario, 2026-10-25)
| Parámetro | Valor | Consecuencia sobre el plan |
|---|---|---|
| Ritmo | 1-2 sesiones/semana (se planifica con **1,5**) | Cronograma en semanas, no en días |
| Duración de sesión | 30-60 min | Tareas muy pequeñas: una puerta o un entregable acotado por sesión |
| Deadline de negocio | Ninguno: fechas referenciales. La entrega de la tesis del MBA (marzo de 2027) también es referencial (`D31`, `D40`; actualizado en S-16) | El piloto manual (`D40`) arranca en cuanto cierra la Fase 0; el kit formal no tiene que llegar antes de marzo |
| Arranque del plan | 2026-10-26 | Semana 1 = 2026-10-26 → 2026-11-01 |

**Unidad de estimación: la sesión.** No se estima en horas. Una tarea que no
cabe en una sesión está mal partida → hay que partirla.

## 2. Resumen del proyecto en números
| Fase | Tareas | Sesiones est. | Semanas est. (1,5 ses/sem) | Ventana referencial |
|---|---|---|---|---|
| 0 — Arranque y alineación | 5 | 4 est. · **16 reales** (S-01 a S-16) | 1 | 2026-10-25 → 2026-11-01 ✅ |
| 1 — Piloto MBA sin servidor | 16 | 16 | ~11 | 2026-11-02 → 2027-01-24 |
| 2 — Servidor MCP + adaptador | se detalla al cerrar la Fase 1 | — | — | — |
| **Total planificado (Fases 0-1)** | 21 | 16 por delante (Fase 1) | ~12 | **cierre est. 2027-01-24** |

**Recalculado en S-16 (`T0.4`, `D40`).** La Fase 0 se estimó en 4 sesiones y
costó 16: fueron sesiones cortas de decisión, casi todas el 2026-10-25, y
cerraron 40 decisiones (`D1`-`D40`). Por eso no se re-estima el ritmo: sigue
en 1,5 sesiones/semana hasta tener sesiones de ejecución con las que medirlo.
La semana que ahorra la Fase 0 la usa el **piloto manual** (`T1.15`-`T1.16`):
el grupo trabaja con un harness hecho a mano desde ≈ mediados de noviembre y
el kit formal (`C001`, `C002`) llega hacia enero con evidencia de ese uso.

El cierre estimado es una proyección aritmética, no una promesa: se
**recalcula al cerrar cada fase** con las sesiones realmente gastadas.

### Convención de identificadores
- `TX.Y` = tarea Y de la fase X. El ID **no se recicla**: una tarea descartada
  queda tachada con su motivo.
- `S-NN` = sesión real, correlativa (§6).
- Estado: ⬜ pendiente · 🟡 en curso · ✅ hecha · 🔴 bloqueada · ⛔ descartada.
- `🔒` = tarea que no puede cerrarse sin decisión del usuario (siempre la
  aprobación P1 y la disposición P4 de cada cambio).
- Una tarea = un grupo de trabajo = **un commit** que referencia `TX.Y` y
  `Cnnn`. Orden dentro de un cambio: propuesta → diseño/supuestos →
  disposición/validación → implementación → «validar y archivar».

## 3. Cómo se abre una sesión (protocolo)
Cada sesión trabaja **una tarea**. No se abre una sesión "a ver qué hago".
1. Leer `agente.md` → `manager.md` («Contexto activo») → este archivo.
2. Verificación previa: si la tarea toca algo del piloto, confirmar que existe
   `local_privado/glosario.md` y que `local_privado/` está ignorada
   (`git check-ignore -v`).
3. Tomar la primera tarea ⬜ cuyas dependencias estén todas ✅ (si hay varias,
   la de menor ID).
4. Anunciar: «Sesión S-NN, tarea TX.Y del cambio Cnnn — [nombre]. Leo
   [anclas], toco [archivos], cierro [escenarios], termino cuando
   [criterio]». Esperar visto bueno si está marcada 🔒.
5. Registrar la fila de la sesión en §6 como 🟡.

Cierre: el checklist de `agente.md §6`.

## 4. Backlog de tareas por fase

### Fase 0 — Arranque y alineación ✅
Dueño: `memoria.md`. Criterio de salida (`manager.md`): `Q1-Q4` cerradas como
`Dn` y cronograma recalculado.

| ID | Cambio | Tarea | Dep. | Ses. | Escenarios que cierra | Leer | Tocar | Criterio de salida |
|---|---|---|---|---|---|---|---|---|
| ✅ T0.0 | soporte | Instalar el harness | — | 1 | — | skill base | todo el repo | `openspec.py validate --strict` en verde |
| ✅ T0.1 🔒 | soporte | Elegir nombre (`Q1`) y publicar el repo en GitHub (privado) | T0.0 | 1 | — | `memoria.md D5`, `D7`, `D8`, `Q1` | remoto git, `memoria.md` | Repo privado con el commit inicial; `Q1` → `Dn` |
| ✅ T0.2 🔒 | soporte | Revisar y aprobar/corregir la arquitectura | T0.0 | 1 | — | `memoria.md §2`, `Q2` | `memoria.md §3` (→ `D6`) | `Q2` cerrada como `D6` (S-02) |
| ✅ T0.3 🔒 | soporte | Datos del MBA, acuerdo del grupo, planes de LLM y rol del profesor | T0.0 | 1 | — | `memoria.md Q3-Q5`, `Q7` | `memoria.md`, `local_privado/glosario.md` | `Q3` ✅ (S-14, `D20`) y `Q5` ✅ (`D23`); `Q4` referencial (`D31`); `Q7` ✅ (S-16, `D40`) |
| ✅ T0.4 | soporte | Recalcular el plan con la fecha real de entrega | T0.2, T0.3 | 1 | — | este archivo §1-§2 | este archivo §2, §4, §5 | Cronograma coherente con la entrega del MBA |

**Riesgo de la fase:** que el grupo no acepte ser piloto (`Q4`). Entonces se
busca otro proyecto grupal no tecnológico y el plan de la Fase 1 cambia.

### Fase 1 — Piloto MBA sin servidor ⬜
Dueño: `cambios/` + `specs/`. Criterio de salida (`manager.md`): `C001` y
`C002` archivados con escenarios en verde, y el grupo usó el kit en al menos
un avance al profesor.

| ID | Cambio | Tarea | Dep. | Ses. | Escenarios que cierra | Leer | Tocar | Criterio de salida |
|---|---|---|---|---|---|---|---|---|
| 🟡 T1.15 | soporte | Armar a mano el harness MBA del piloto (`D40`): skill actual, vocabulario no técnico, documentos de control .txt (`D21`) | T0.4 | 1 | — | skill base, `memoria.md D21`, `D22`, `D25`, `D27`, `D40` | `local_privado/piloto/` | Carpeta lista y revisada por el dueño; `local_privado/glosario.md` presente y `local_privado/` ignorada |
| ⬜ T1.16 🔒 | soporte | Arranque del piloto manual con el grupo (subir al Drive del grupo, primera sesión de uso) | T1.15 | 1 | — | `local_privado/piloto/`, `memoria.md D4`, `Q17` | Drive del grupo (con confirmación), `learn.md` | El grupo trabaja con el harness; primeros hallazgos anonimizados en `learn.md` (incluido lo que se vea de `Q17`) |
| ⬜ T1.1 🔒 | C001 | Propuesta del perfil MBA (P1) | T1.16 | 1 | — | `memoria.md §2.4`, `D3`, `D4` | `cambios/C001-*/propuesta.md` | Aprobada por el usuario |
| ⬜ T1.2 | C001 | Diseño + delta + verificar supuestos (P2-P3) | T1.1 | 1 | — | `specs/PERFIL.md`, `specs/COLAB.md` | `diseno.md`, `delta.md` | Ningún supuesto ⬜ |
| ⬜ T1.3 🔒 | C001 | Disposición de preguntas + validación (P4-P5) | T1.2 | 1 | — | `diseno.md §6` | `diseno.md`, `delta.md` | `openspec.py validate --strict --cambio C001` en verde |
| ⬜ T1.4 | C001 | Plantillas del perfil MBA (documentos del proyecto del grupo) | T1.3 | 1 | (se fijan en `T1.2`) | `diseno.md §1-2` | `perfiles/mba/` | Escenarios asignados en verde + «Verificado por» |
| ⬜ T1.5 | C001 | Guía de criterios desde la rúbrica + roles del grupo | T1.4 | 1 | (se fijan en `T1.2`) | `diseno.md §1-2` | `perfiles/mba/` | Escenarios asignados en verde |
| ⬜ T1.6 | C001 | Validar y archivar C001 | T1.5 | 1 | todos los de C001 | `delta.md` | `specs/`, `memoria.md` | `--archivo` en verde |
| ⬜ T1.7 🔒 | C002 | Propuesta del kit portable Claude + ChatGPT (P1) | T1.6 | 1 | — | `memoria.md §2.2`, `D1`, `Q3` | `cambios/C002-*/propuesta.md` | Aprobada |
| ⬜ T1.8 | C002 | Diseño + delta + verificar supuestos (P2-P3) | T1.7 | 1 | — | `specs/ACCESO.md`, `specs/VALID.md` | `diseno.md`, `delta.md` | Ningún supuesto ⬜ (incluye probar en ChatGPT real) |
| ⬜ T1.9 🔒 | C002 | Disposición de preguntas + validación (P4-P5) | T1.8 | 1 | — | `diseno.md §6` | `diseno.md`, `delta.md` | `validate --strict --cambio C002` en verde |
| ⬜ T1.10 | C002 | Kit para Claude (instrucciones de proyecto + validación asistida) | T1.9 | 1 | (se fijan en `T1.8`) | `diseno.md` | `kit/` | Escenarios en verde con evidencia |
| ⬜ T1.11 | C002 | Kit para ChatGPT + prueba cruzada (un proyecto, dos LLMs) | T1.10 | 1 | (se fijan en `T1.8`) | `diseno.md` | `kit/` | Escenarios en verde con evidencia |
| ⬜ T1.12 | C002 | Validar y archivar C002 | T1.11 | 1 | todos los de C002 | `delta.md` | `specs/` | `--archivo` en verde |
| ⬜ T1.13 🔒 | soporte | Arranque del piloto con el grupo (onboarding) | T1.12 | 1 | — | `kit/` | `local_privado/` | El grupo tiene su proyecto montado en su almacén |
| ⬜ T1.14 | soporte | Registrar hallazgos tras el primer avance al profesor | T1.13 | 1 | — | `learn.md §4` | `learn.md` | Hallazgos como `Mn`/`Ln`, anonimizados |

**Riesgo de la fase:** que el kit llegue tarde para el trabajo de MBA (ver §5).

## 5. Cronograma referencial
| Semanas | Ventana | Fase | Tareas previstas | Hito |
|---|---|---|---|---|
| 1 | 2026-10-25 → 2026-11-01 | 0 | T0.0-T0.4 | 🏁 Fase 0 cerrada (S-16) ✅ |
| 2-3 | 2026-11-02 → 2026-11-15 | 1 | T1.15-T1.16 | 🏁 Piloto manual en uso |
| 4-7 | 2026-11-16 → 2026-12-13 | 1 | T1.1-T1.6 | 🏁 Perfil MBA archivado (C001) |
| 8-11 | 2026-12-14 → 2027-01-10 | 1 | T1.7-T1.12 | 🏁 Kit portable archivado (C002) |
| 12-13 | 2027-01-11 → 2027-01-24 | 1 | T1.13-T1.14 | 🏁 Grupo pasa del piloto manual al kit |

**Ruta crítica:** `T0.4 → T1.15 → T1.16 → T1.1 → … → T1.12 → T1.13`. `Q19`
tiene que estar cerrada antes de `T1.2` y `Q17` antes de `T1.8`; si no, esas
tareas quedan 🔴 y el cronograma se corre.

**Dónde se puede romper el plan (y qué hacer):**
1. **El kit llega tarde para el grupo** (con el plan base estaría hacia la
   semana 11, ≈ enero de 2027). **Resuelto en S-16 con `D40`: opción (a)**;
   marzo de 2027 es fecha referencial. `T0.4` agregó `T1.15`-`T1.16` y
   recalculó la tabla (S-16). Opciones que se evaluaron en `Q7`:
   - (a) **Piloto temprano manual:** en la Fase 0 se monta a mano un harness
     MBA para el grupo con el skill actual y vocabulario adaptado
     (≈ 2 sesiones). El grupo lo usa ya; `C001`/`C002` formalizan después,
     con evidencia real en vez de suposiciones.
   - (b) **Subir el ritmo** a 2 sesiones/semana de 60 min durante la Fase 1
     (≈ 7 semanas en vez de 10).
   - (c) **Fusionar C001 y C002** en un solo cambio (ahorra ~3 sesiones de
     puertas, pero hace el cambio más grande y más riesgoso de revisar).
   - (d) Aceptar que el piloto sea **otro proyecto** posterior y usar el MBA
     solo como fuente de requisitos.
2. **ChatGPT no se comporta como se asume** (instrucciones largas, lectura de
   archivos, límites de contexto) → se descubre en `T1.8` (supuestos P3); sumar
   1-2 sesiones y registrar en `entorno.md`.
3. **El grupo no acepta** (`Q4`) → ver riesgo de la Fase 0.

## 6. Bitácora de sesiones
Una fila por sesión real, llenada **al cerrar**. La columna «Siguiente» es lo
que permite arrancar en frío la sesión que viene.

| Sesión | Fecha | Tarea | Estado | Qué quedó | Siguiente |
|---|---|---|---|---|---|
| S-01 | 2026-10-25 | T0.0 | ✅ | Harness instalado; `D1-D5`; `Q1-Q7` abiertas; `C001` en borrador | **T0.1 — Publicar el repo (requiere `Q1`)**; en paralelo, el usuario puede adelantar `Q4`/`Q7` con su grupo |
| S-02 | 2026-10-25 | T0.2 (+ avance de T0.1 y T0.3) | ✅ T0.2 · 🟡 T0.1, T0.3 | `Q2` → `D6`; nuevas `D7` (Drive) y `D8` (problema: tokens, multi-LLM, versionado); `D3` con entrega en marzo 2027 y 4 integrantes; glosario creado; 4 nombres candidatos para `Q1` | **T0.1 — el dueño elige nombre y crea el repo vacío**; luego T0.3 con los datos del MBA y `Q7` |
| S-03 | 2026-10-25 | T0.3 (avance) | 🟡 | `D9` usuario no técnico; abiertas `Q8` (formato de documentos) y `Q9` (conexión del LLM sin pasos técnicos) | **T0.1 — nombre + repo vacío**; luego T0.3 |
| S-04 | 2026-10-25 | T0.1 (avance) | 🟡 | `Q1` → `D10` CoLLMena; documentos renombrados; abierta `Q10` (marca y dominio) | **T0.1 — el dueño crea el repo privado vacío `CoLLMena`; el agente sube los commits**; luego T0.3 |
| S-05 | 2026-10-25 | T0.3 (avance) | 🟡 | `Q8` → `D11` (.docx/.pptx/.xlsx + .txt); abierta `Q11` | **T0.1 — repo `CoLLMena`**; luego T0.3 |
| S-06 | 2026-10-25 | T0.3 (avance) | 🟡 | `D12` (leer siempre, editar si la persona elige); hallazgos de versionado en Drive y edición en ChatGPT (`memoria.md §2.5`); abierta `Q12` | **T0.1 — repo `CoLLMena`**; luego T0.3 (`Q7`, `Q11`, `Q12`, datos del MBA) |
| S-07 | 2026-10-25 | T0.3 (avance) | 🟡 | Hallazgo: Edición de Office en Drive mantiene el .docx; `Q12` acotada a si ChatGPT edita Office (`memoria.md §2.5`) | **T0.1 — repo `CoLLMena`**; luego T0.3 |
| S-08 | 2026-10-25 | T0.3 (avance) | 🟡 | `D13` bitácora de cambios en .txt tipo commit, sin versiones; abiertas `Q13` (una bitácora o varias) y `Q14` (cambios hechos a mano) | **T0.1 — repo `CoLLMena`**; luego T0.3 |
| S-09 | 2026-10-25 | T0.3 (avance) | 🟡 | `Q13` → `D14`: MVP con una sola bitácora .txt, sin versiones | **T0.1 — repo `CoLLMena`**; luego T0.3 (`Q7`, `Q11`, `Q12`, `Q14`) |
| S-10 | 2026-10-25 | T0.3 (avance) | 🟡 | `Q14` → `D15`: cambios a mano los cuenta la persona o los detecta el LLM (archivo, fecha, autor; el "qué" lo cuenta la persona) | **T0.1 — repo `CoLLMena`**; luego T0.3 (`Q7`, `Q11`, `Q12`, datos del MBA) |
| S-11 | 2026-10-25 | soporte (no planificada) | ✅ | `README.md` con la descripción no técnica; prompt de landing en `marketing/`; `D16` (más LLMs), `D17` (identidad visual); abierta `Q15` | **T0.1 — repo `CoLLMena`**; luego T0.3 |
| S-12 | 2026-10-25 | soporte (no planificada) | ✅ | `INSTRUCCIONES_PROYECTO.md`: texto para las instrucciones del proyecto de claude.ai | **T0.1 — repo `CoLLMena`** (sin repo, cada chat depende de que se suban los archivos); luego T0.3 |
| S-13 | 2026-10-25 | T0.1 | ✅ | Harness recuperado del zip del chat original (14 commits) y publicado en `ReZaVal/CoLLMena` (privado, `main`); historial sin datos del MBA; GitHub avisa que el repo se movió a `CoLLMena`; el dueño pide CoLLMena en todos los nombres → `D18` | **T0.3** (`Q7`, `Q11`, `Q12`, `Q15`, datos del MBA); luego T0.4 |
| S-14 | 2026-10-25 | T0.3 (avance) | 🟡 | `D19` el MBA es un caso de uso; `D20` LLM de plan gratuito a pago, con inicio de sesión propio (cierra `Q3`, `Q9`); `D21` panal y .txt de control (cierra `Q11`); `D22` Drive + edición Google/Office + registro en cada carga (cierra `Q12`); `D23` el profesor sin rol y carpeta de contexto por panal (cierra `Q5`); `D24` el panal es un proyecto; `D25` el LLM redacta el registro y la persona confirma; `D26` contexto multiformato y ahorro de tokens; `D27` mapa de contexto + conversión a texto (cierra `Q18`); `D28` sin video ni audio; `D29` el panal define objetivo y reglas con SDD u otro framework; `D30` registro obligatorio; `D31` Q4 es referencial (prueba de producto con una tesis; cierra `Q4`); `D32` cada panal elige un framework refinado del SDD (cierra `Q16`); lectura de Drive por LLM verificada en `memoria.md §2.6`; abiertas `Q17` (ChatGPT gratuito sin confirmar) y `Q19` (quién elige el framework) | **T0.3** (`Q7`; `Q17` y `Q19` bloquean el diseño de C002/C001, no la Fase 0); luego T0.4 |
| S-15 | 2026-10-26 | soporte (no planificada) | ✅ | Repo `CoLLMena` clonado en la sesión (protocolo de inicio corrido); `D33` las skills de superpowers complementan al harness (`agente.md` manda); leídas las 15 skills; `Q20` → `D34` (superpowers solo en la ejecución de tareas con código, tras P5), `D35` (ramas y PR) y `D36` (subagentes solo con permiso del dueño, con tarea y fin); PR #1 fusionado en `main` (`e7aa191`, a petición del dueño); `Q21` → `D37` (convención de ramas y PR; queda abierta `Q22`, protección de `main`); `M4` aplicada en `agente.md §8`; PR #2 fusionado (`1fb9ed5`, también a petición del dueño); `D38` el agente fusiona solo cuando el dueño lo pide expresamente en la sesión; `Q22` → `D39` (`main` sin protección técnica, por convención) | **T0.3** (`Q7`; `Q17` y `Q19` bloquean el diseño de C002/C001, no la Fase 0); luego T0.4 |
| S-16 | 2026-10-26 | T0.3, T0.4 | ✅ | `Q7` → `D40`: piloto temprano manual (opción a) y marzo de 2027 como fecha referencial; corregida la restricción dura de `memoria.md §1`; inferencias a confirmar en `D40` (el piloto manual no necesita cambio; Drive del grupo pide confirmación); `T0.4`: nuevas `T1.15` (armar el harness manual) y `T1.16` 🔒 (arranque con el grupo), `T1.1` pasa a depender de `T1.16`, cronograma recalculado (cierre est. 2027-01-24 sin cambio); **Fase 0 cerrada** | **T1.15** — armar el harness manual en `local_privado/piloto/` (antes: recrear `local_privado/glosario.md` con los seudónimos que dicta el dueño; el original se perdió, `learn.md L1`); `Q19` antes de `T1.2` |
| S-17 | 2026-10-26 | T1.15 | 🟡 | Kit del piloto manual armado en `local_privado/piloto/` (9 .txt: léeme, instrucciones para el asistente, panal, en qué estamos, decisiones, tareas, registro de cambios, mapa de contexto, aprendizajes; carpetas `contexto/` y `entregables/`), en plantilla para que lo llene el grupo, con instrucciones para ChatGPT y Claude; glosario de S-16 en uso; flujo «adjuntar y copiar de vuelta» por `memoria.md §2.6`; inferencias a confirmar en `local_privado/piloto_revision_T1.15.md`; nueva `M6` | **T1.15** — revisión del dueño del kit (criterio de cierre) y glosario con datos reales; luego **T1.16** 🔒 |

## 7. Cómo se mantiene vivo este plan
- Al cerrar cada tarea: ✅ en §4 + fila en §6. 30 segundos.
- Al cerrar cada fase: recalcular §2 y §5 con las sesiones realmente gastadas.
- Si una tarea toma más de 2 sesiones: está mal partida → partirla con IDs
  nuevos y anotar por qué.
- Si aparece trabajo no previsto que sea comportamiento nuevo: primero un
  cambio nuevo (propuesta), nunca "de paso" dentro de otra tarea.
