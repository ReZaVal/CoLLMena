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
(sin entradas aún)

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
