# planner.md — Plan de tareas, sesiones y cronograma de ZOr Harness

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
| Deadline de negocio | Producto: ninguno (fechas referenciales). **Piloto: entrega de la tesis del MBA en marzo de 2027** (día exacto pendiente, `Q4`; actualizado en S-02) | El piloto debe empezar con margen para que el grupo lo use en al menos un avance antes de marzo |
| Arranque del plan | 2026-10-26 | Semana 1 = 2026-10-26 → 2026-11-01 |

**Unidad de estimación: la sesión.** No se estima en horas. Una tarea que no
cabe en una sesión está mal partida → hay que partirla.

## 2. Resumen del proyecto en números
| Fase | Tareas | Sesiones est. | Semanas est. (1,5 ses/sem) | Ventana referencial |
|---|---|---|---|---|
| 0 — Arranque y alineación | 4 | 4 | ~3 | 2026-10-26 → 2026-11-15 |
| 1 — Piloto MBA sin servidor | 14 | 14 | ~9-10 | 2026-11-16 → 2027-01-24 |
| 2 — Servidor MCP + adaptador | se detalla al cerrar la Fase 1 | — | — | — |
| **Total planificado (Fases 0-1)** | 18 | 18 | ~12-13 | **cierre est. 2027-01-24** |

⚠️ **Con el ritmo actual, el kit llega justo:** estaría listo (`T1.12`)
cerca de la semana 11 (≈ enero 2027) y la entrega es en marzo de 2027. El
grupo lo usaría solo ~6-8 semanas, y el problema de `memoria.md D8` lo sufre
hoy. Ver §5, «Dónde se puede romper el plan», y `memoria.md Q7`.

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

### Fase 0 — Arranque y alineación 🟡
Dueño: `memoria.md`. Criterio de salida (`manager.md`): `Q1-Q4` cerradas como
`Dn` y cronograma recalculado.

| ID | Cambio | Tarea | Dep. | Ses. | Escenarios que cierra | Leer | Tocar | Criterio de salida |
|---|---|---|---|---|---|---|---|---|
| ✅ T0.0 | soporte | Instalar el harness | — | 1 | — | skill base | todo el repo | `openspec.py validate --strict` en verde |
| 🟡 T0.1 🔒 | soporte | Elegir nombre (`Q1`) y publicar el repo en GitHub (privado) | T0.0 | 1 | — | `memoria.md D5`, `D7`, `D8`, `Q1` | remoto git, `memoria.md` | Repo privado con el commit inicial; `Q1` → `Dn` |
| ✅ T0.2 🔒 | soporte | Revisar y aprobar/corregir la arquitectura | T0.0 | 1 | — | `memoria.md §2`, `Q2` | `memoria.md §3` (→ `D6`) | `Q2` cerrada como `D6` (S-02) |
| 🟡 T0.3 🔒 | soporte | Datos del MBA, acuerdo del grupo, planes de LLM y rol del profesor | T0.0 | 1 | — | `memoria.md Q3-Q5`, `Q7` | `memoria.md`, `local_privado/glosario.md` | `Q3`, `Q4`, `Q7` cerradas (`Q5` puede quedar abierta) |
| ⬜ T0.4 | soporte | Recalcular el plan con la fecha real de entrega | T0.2, T0.3 | 1 | — | este archivo §1-§2 | este archivo §2, §4, §5 | Cronograma coherente con la entrega del MBA |

**Riesgo de la fase:** que el grupo no acepte ser piloto (`Q4`). Entonces se
busca otro proyecto grupal no tecnológico y el plan de la Fase 1 cambia.

### Fase 1 — Piloto MBA sin servidor ⬜
Dueño: `cambios/` + `specs/`. Criterio de salida (`manager.md`): `C001` y
`C002` archivados con escenarios en verde, y el grupo usó el kit en al menos
un avance al profesor.

| ID | Cambio | Tarea | Dep. | Ses. | Escenarios que cierra | Leer | Tocar | Criterio de salida |
|---|---|---|---|---|---|---|---|---|
| ⬜ T1.1 🔒 | C001 | Propuesta del perfil MBA (P1) | T0.4 | 1 | — | `memoria.md §2.4`, `D3`, `D4` | `cambios/C001-*/propuesta.md` | Aprobada por el usuario |
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
| 1-3 | 2026-10-26 → 2026-11-15 | 0 | T0.1-T0.4 | 🏁 Arquitectura aprobada, datos del MBA |
| 4-7 | 2026-11-16 → 2026-12-13 | 1 | T1.1-T1.6 | 🏁 Perfil MBA archivado (C001) |
| 7-11 | 2026-12-07 → 2027-01-10 | 1 | T1.7-T1.12 | 🏁 Kit portable archivado (C002) |
| 11-13 | 2027-01-04 → 2027-01-24 | 1 | T1.13-T1.14 | 🏁 Piloto en uso |

**Ruta crítica:** `T0.2 → T0.4 → T1.1 → … → T1.12 → T1.13`. Todo retraso ahí
desplaza el piloto.

**Dónde se puede romper el plan (y qué hacer):**
1. **La entrega del MBA cae antes de la semana 11** (muy probable: "más de 6
   semanas" ≈ desde 2026-12-06). El plan base no llega a tiempo. Opciones, a
   decidir por el usuario en `Q7`:
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

## 7. Cómo se mantiene vivo este plan
- Al cerrar cada tarea: ✅ en §4 + fila en §6. 30 segundos.
- Al cerrar cada fase: recalcular §2 y §5 con las sesiones realmente gastadas.
- Si una tarea toma más de 2 sesiones: está mal partida → partirla con IDs
  nuevos y anotar por qué.
- Si aparece trabajo no previsto que sea comportamiento nuevo: primero un
  cambio nuevo (propuesta), nunca "de paso" dentro de otra tarea.
