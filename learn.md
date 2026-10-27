# learn.md — Bitácora de errores y aprendizaje de CoLLMena

Registro de errores detectados (de diseño, código, plantillas, o del propio
agente que dirige el proyecto) y de la regla que queda una vez resueltos. Es
el mecanismo por el que el harness "aprende". No reemplaza a `memoria.md`
(decisiones): esto registra errores.

En este proyecto la §4 tiene doble valor: las carencias del harness que
aparezcan aquí, o en el piloto MBA, son **requisitos candidatos del producto**.

## Protocolo
1. Al detectar un error: entrada nueva en §2 con estado `🔴 Abierto` (no hace
   falta tener la solución).
2. Al resolverlo: completar causa raíz + solución + regla derivada, cambiar a
   `✅ Resuelto`, y propagar la regla al documento que corresponda. Anotar
   dónde quedó la regla.
3. Antes de repetir un análisis o diseño, revisar el índice de §1.
4. Un error que se repite dos veces a pesar de tener regla escrita → la regla
   está mal ubicada o redactada; arreglar la regla, no solo el síntoma.
5. Hallazgos del piloto MBA: **siempre anonimizados** (`agente.md §4`).

Campos de cada entrada: Estado · Detectado en (sesión, tarea `TX.Y`, cambio
`Cnnn`) · **Tipo** (supuesto falso `Cnnn Sn` / hueco de spec / deriva
spec↔código / bug / proceso del agente / entorno / piloto) · Síntoma · Causa
raíz · Solución · Regla derivada → dónde vive.

## 1. Índice de reglas ya incorporadas
| ID | Resumen del error | Regla derivada | Dónde vive ahora |
|----|-------------------|----------------|-------------------|
| — | (sin entradas aún) | | |

## 2. Log de errores
### L1 — `local_privado/` no viaja con el repo y el glosario se perdió
- **Estado:** 🔴 Abierto (se resuelve al recrear el glosario en `T1.15`).
- **Detectado en:** S-16, al cerrar `T0.4`.
- **Tipo:** entorno.
- **Síntoma:** `local_privado/glosario.md`, creado en S-02 en otra carpeta de
  trabajo, no existe en el clon de S-15 y el dueño no encuentra el original.
- **Causa raíz:** `local_privado/` está ignorada por git (a propósito) y nada
  del harness pide respaldarla ni llevarla a un clon nuevo; el protocolo de
  inicio de S-15 no comprobó que existiera.
- **Solución:** el dueño dicta de nuevo los seudónimos y el agente recrea el
  glosario en `T1.15`.
- **Regla derivada → dónde vive:** pendiente (candidata: al clonar o cambiar
  de máquina, comprobar `local_privado/` como paso del protocolo de inicio,
  y que el dueño guarde una copia fuera del repo). Ver `M5`.

## 3. Errores de comportamiento del agente
(sin entradas aún)

## 4. Propuestas de mejora al harness (para evaluar con el usuario)
**NO se aplican al skill sin visto bueno del usuario.**

### M1 — El skill base asume un operador, git y Python
- **Observación:** al plantear este producto (S-01) se vio que tres supuestos
  del skill no valen para grupos no técnicos (`memoria.md §2.1`).
- **Propuesta:** es el objeto mismo del producto; se resuelve vía los cambios
  de las Fases 1-2, no parcheando el skill base.
- **Estado:** 🟡 propuesta

### M2 — `planner.md` no modela responsables ni fechas externas
- **Observación:** en un grupo la unidad de plan es **persona + fecha de
  avance**, no solo la sesión de un agente (`memoria.md §2.4`).
- **Propuesta:** columnas «Responsable» y «Fecha límite» opcionales por
  perfil; lo decide el diseño de `C001`.
- **Estado:** 🟡 propuesta

### M3 — El validador no distingue un cambio en borrador
- **Observación:** en S-01, al crear la propuesta de `C001` en borrador,
  `openspec.py validate --strict` (sin `--cambio`) pasó de verde a rojo por
  "falta aprobación / diseño / delta". Es correcto bloquear `C001`, pero el
  estado global del repo queda en rojo mientras exista cualquier borrador.
- **Propuesta:** que el validador trate los cambios con `Estado: 🟡 borrador`
  como aviso informativo en la validación global, y como error solo con
  `--cambio Cnnn`. Para el producto: "¿está sano el proyecto?" y "¿está listo
  este cambio?" son dos preguntas distintas que un grupo no técnico necesita
  ver separadas.
- **Estado:** 🟡 propuesta (no se parchea `openspec.py` sin visto bueno)

### M4 — El harness no dice cómo conviven las skills externas ni el flujo de ramas y PR
- **Observación:** en S-15, al instalar superpowers (`D33`) y adoptar ramas y PR
  (`D35`), `agente.md` no tenía regla sobre skills de terceros (quién manda, en
  qué fase se usan, qué hacer con las que despachan subagentes) y no menciona
  ramas ni PR. Se resolvió con decisiones en `memoria.md` (`D34`-`D36`), que un
  agente nuevo solo lee en el paso 3 del orden de lectura.
- **Propuesta:** una sección corta en `agente.md` («Skills externas y ramas»)
  que remita a `D34`-`D36` y `Q21`. Para el producto: un harness generalizado
  necesita una política sobre herramientas externas y sobre el flujo de
  revisión del grupo.
- **Estado:** ✅ aplicada en S-15 con visto bueno del dueño: `agente.md §8`

### M5 — Los datos privados del proyecto no tienen dónde sobrevivir
- **Origen:** `L1` (S-16).
- **Problema:** lo que no entra al repo (`local_privado/`) vive en una sola
  carpeta local: se pierde al clonar, cambiar de máquina o de entorno.
- **Propuesta:** que el harness indique dónde se respalda lo privado (p. ej.
  el almacén del grupo o una carpeta personal del dueño) y que el protocolo de
  inicio compruebe que está. Para el producto: decidir dónde vive el material
  privado de cada panal.
- **Estado:** propuesta, sin visto bueno.

### M6 — El skill base asume que el agente escribe los archivos
- **Origen:** `T1.15` (S-17), al armar el kit del piloto manual.
- **Problema:** el harness supone que el agente lee y escribe los documentos
  de control. En un chat de ChatGPT o Claude sin conector que escriba en
  Drive (y el de Claude no lista .txt, `memoria.md §2.6`), el agente solo
  puede devolver texto: la persona lo copia y lo sube a mano. El cierre de
  sesión pasa a depender de un paso manual que se puede olvidar.
- **Propuesta:** que el skill contemple un modo «sin escritura»: el agente
  entrega al cerrar, listo para copiar, la entrada de la bitácora y el texto
  completo de cada archivo que cambió. Para el producto: el piloto mide si
  este paso es tolerable; es insumo para `C002` y `Q17`.
- **Estado:** propuesta, sin visto bueno; aplicada a prueba en el kit del
  piloto (`local_privado/piloto/`).
