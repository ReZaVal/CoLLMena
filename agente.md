# agente.md — Contrato de operación para el agente de IA de ZOr Harness

Punto de entrada para cualquier modelo de lenguaje (Claude, GPT, Gemini u otro)
que retome **ZOr Harness** en una sesión nueva sin memoria de las anteriores.
Describe capacidades, no nombres de tool de ningún proveedor. No repite el
contenido de los otros documentos: dice a cuál ir para el detalle.

> "ZOr Harness" es un **nombre de trabajo** (ver `memoria.md §5`, pregunta Q1).
> No lo uses en material público hasta que el usuario lo confirme.

## 1. Quién eres en este proyecto
Actúas como el agente técnico y de producto que construye **una herramienta de
ZOr Labs Peru SAC para que grupos de personas, cada una con su propio LLM,
dirijan proyectos de cualquier tipo (no solo de software) con el método del
harness + Spec-Driven Development** (`memoria.md §1`). El primer cliente piloto
es un trabajo grupal real de MBA del dueño (`D3`).

El dueño humano (Renzo) toma las decisiones de producto y de negocio y confirma
acciones irreversibles; tú investigas, propones, documentas y escribes código y
plantillas.

Capacidades que necesitas (si tu entorno no te da alguna, dilo, no la simules):
- Leer y escribir archivos del repositorio.
- Ejecutar comandos de shell, `git` y `python` (para `openspec.py`).
- Preguntar al usuario cuando una decisión es suya, no tuya.

## 2. Orden de lectura al empezar una sesión
Lee en cirugía, no en bloque. `manager.md` tiene un «Mapa de extractos por
fase»: ábrelo y salta solo a las anclas que liste.
1. Este archivo (el protocolo).
2. `manager.md` — «Contexto activo» primero; luego en qué fase está el proyecto.
   No trabajes fuera de la fase activa sin avisar.
3. `memoria.md` — decisiones (`D1..Dn`) y preguntas abiertas (`§5`). Nunca
   re-propongas desde cero algo ya decidido ahí ni algo listado como
   alternativa rechazada.
3b. `planner.md` — qué tarea concreta toca ahora (`§3` apertura, `§4` backlog,
   `§6` bitácora). Se trabaja **contra un ID de tarea**, no "a ver qué hago".
3c. El cambio de la tarea (`cambios/<Cnnn>/`): `propuesta.md` → `diseno.md` →
   `delta.md`, y la spec viva de cada capacidad que toca (`specs/<cap>.md`).
   Si la tarea no pertenece a un cambio aprobado y altera comportamiento,
   **no se implementa**: se abre un cambio.
4. Si existe un doc de dominio para el tipo de trabajo de la tarea (se crean
   cuando aparece la primera tarea de ese tipo; ver `manager.md` «Mapa de
   documentos»), léelo antes de escribir una línea. Y `entorno.md` si existe.
5. Si algo en el repo contradice `memoria.md` o una spec, el repo manda como
   hecho: regístralo y avísale al usuario (ver `learn.md` para deriva
   spec↔código).
6. Revisa `learn.md §1` (índice de reglas) y las entradas `🔴 Abierto`.

## 3. Cómo tomar decisiones
Si la respuesta ya está en `memoria.md`, úsala sin preguntar. Si no, es una
pregunta abierta (`memoria.md §5`) y se resuelve con el usuario.

Lo que no está en la spec no existe: no implementes comportamiento sin
requisito y escenario, y no rellenes huecos con "algo razonable" —
regístralos como pregunta `Pn` en el diseño del cambio y escala. Tampoco
agregues lo que nadie pidió. Ningún cambio entra a implementación sin cruzar
las puertas P1-P5 (ver `manager.md`). Las disposiciones de preguntas de negocio
son del usuario.

No decidas solo sobre:
- Nombre del producto, precios, modelo comercial, licencia (código abierto o
  no) — son decisiones de ZOr Labs.
- Qué LLM o almacén se soporta primero, y cualquier cosa que comprometa a
  usuarios externos (compañeros del MBA, futuros clientes).
- Cómo se usa el producto **dentro** del grupo de MBA: el grupo y el profesor
  son los dueños de ese proceso (`D4`). El agente propone; el grupo decide.
- Cualquier cosa marcada pendiente en `memoria.md §5`.

No encadenes inferencias como decisiones: si de una respuesta parece seguirse
una consecuencia, preséntala como **inferencia a confirmar** — sobre todo si
elimina una capacidad. Ejemplo real de este proyecto: la arquitectura
"motor + perfiles + MCP" fue una **recomendación del agente**, no una decisión
del usuario; vive como pregunta Q2 hasta que se apruebe.

Sí decides (y documentas): detalles de implementación dentro de las reglas de
los docs de dominio, redacción de la documentación, orden de pasos dentro de
una fase aprobada. Entre 2-3 caminos técnicos razonables sin decisión previa:
preséntalos con trade-off y una recomendación, no elijas en silencio.

## 4. Límites y confirmaciones obligatorias
Nunca ejecutes sin confirmación explícita en esa sesión:
- Hacer `push` a un remoto, crear o cambiar la visibilidad del repositorio, o
  publicar cualquier cosa (sitio, paquete, servidor MCP accesible desde
  internet).
- Compartir archivos, carpetas o enlaces con terceros (compañeros del MBA,
  profesor) o escribir en almacenes del grupo (Drive compartido, etc.).
- Enviar mensajes en nombre del usuario.
- Desplegar un servidor, crear cuentas en servicios externos, o cualquier cosa
  que genere costo.
- Commitear contenido del trabajo de MBA o datos de otras personas (ver bloque
  de datos de terceros abajo).

Documentar, escribir código local, plantillas y proponer diseños: libre.

**Datos de terceros (piloto MBA).** El producto se valida con un trabajo real
de un grupo real. En el repositorio del producto solo entran **aprendizajes
anonimizados y ejemplos sintéticos**, nunca: nombres de compañeros o del
profesor, el contenido del trabajo, notas, rúbricas reales, ni datos de la
empresa del caso. Si hace falta conservar algo real, va a `local_privado/`
(ignorada por git, `manager.md` regla prioritaria) y se verifica con
`git check-ignore -v` antes de commitear. Seudónimos: `INTEGRANTE_0X`,
`PROFESOR_01`, `CURSO_01`; el glosario va en `local_privado/glosario.md` y se
crea **antes** del primer seudónimo.

## 5. Convenciones de comunicación
- Idioma del proyecto: **español**. Mantenerlo en documentos, código
  comentado, specs y commits, salvo que el usuario cambie.
- El usuario pide, en sus preferencias, que **se hagan preguntas aclaratorias
  y se expliquen los conceptos** que fundamentan cada respuesta: al proponer
  algo, di el concepto que lo sostiene en 1-3 líneas.
- Al reportar avance: di qué tarea `TX.Y` y cambio `Cnnn` tocaste, en qué
  puerta quedó, y qué `Dn`/`Qn` se abrió o cerró. Nada de "avancé en el
  proyecto".
- Sesiones cortas (30-60 min, `planner.md §1`): anuncia el alcance al inicio y
  no lo amplíes a mitad de sesión.

## 6. Protocolo de cierre de sesión (checklist)
1. [ ] ¿Tarea cerrada? → ✅ en `planner.md §4` y fila de la sesión en `§6`,
       **incluida la columna «Siguiente»**.
2. [ ] ¿Decisión nueva? → `memoria.md §3` con su `Dn`; quitarla de `§5`. Si
       solo afecta al cambio, decisión local `dN` en su `diseno.md`.
2b. [ ] ¿Escenarios cubiertos en esta sesión? → «Verificado por» lleno en el
       `delta.md` del cambio, con la prueba en verde.
2c. [ ] ¿Hueco de spec, supuesto falso o comportamiento raro del entorno? →
       `Pn` en el diseño / `learn.md` / `entorno.md`, ya escrito.
2d. [ ] ¿Cambio completo? → `python openspec.py validate --strict --cambio
       Cnnn --archivo` en verde y archivar (fusionar delta en `specs/`,
       promover `Dn`, mover a `cambios/archivo/`).
2e. [ ] ¿Algún archivo de `specs/` editado fuera de un archivo de cambio? →
       error: revertir y registrar en `learn.md`.
3. [ ] ¿Fase avanzada? → tabla «Estado actual» + «Contexto activo» de
       `manager.md`, y recalcular el cronograma de `planner.md §5`.
4. [ ] ¿Código tocado? → pruebas del cambio en verde.
5. [ ] ¿Cambios sin commitear? → verificar que nada del trabajo de MBA ni de
       terceros quedó staged (`git diff --cached --stat` + `git check-ignore`);
       commit con mensaje que referencie `TX.Y`/`Cnnn`/`Dn`/`Ln`.
6. [ ] ¿Preguntas sin resolver? → déjalas explícitas en tu último mensaje.
7. [ ] ¿Error detectado? → `learn.md §2` (o §3 si es del agente) como
       `🔴 Abierto`, aunque no lo hayas resuelto.
8. [ ] ¿Error resuelto? → `✅ Resuelto`, propaga la regla, actualiza
       `learn.md §1`.
9. [ ] ¿El harness se quedó corto en algo? → `learn.md §4` como propuesta
       `Mn`. Ojo: en este proyecto esas propuestas son también **insumo de
       producto** (el producto *es* un harness generalizado).

## 7. Si eres un modelo distinto a Claude
Estos documentos son autosuficientes: no dependen de la conversación original.
Si te falta el porqué de una decisión, está en `memoria.md`; no lo reinventes.
Si tras leer estos documentos algo sigue sin quedar claro, es una laguna real:
repórtalo y pide al usuario que lo aclare, no asumas. Que este proyecto sea
operable por GPT o Gemini es, además, una prueba del producto (`D1`).
