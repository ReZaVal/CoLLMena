# C001 — Crear el perfil "Trabajo grupal de MBA"

- **Estado:** 🟡 borrador (preparado por el agente en S-01; se revisa en `T1.1`)
- **Tipo:** normal
- **Fase (`manager.md`):** 1

> Borrador anticipado para que el usuario vea a dónde va la Fase 1. Puede
> cambiar según `memoria.md Q2` (arquitectura) y `Q7` (cómo llegar a tiempo
> al MBA). No se aprueba antes de cerrar la Fase 0.

## Por qué
Dolor observado en el grupo piloto (`memoria.md D8`): trabajan con LLMs en
un solo chat que mezcla documentos y anotaciones, con alto consumo de tokens,
sin repositorio ubicable y sin versiones de los documentos.

El método del harness resuelve un problema que un grupo de MBA también tiene:
cada integrante abre su LLM sin memoria del trabajo, se re-discuten
decisiones ya tomadas, se repite el error que el profesor ya señaló y nadie
sabe si una sección "está lista". Pero el harness actual habla en lenguaje de
software y supone una sola persona (`memoria.md §2.1`), así que un grupo de
MBA no puede usarlo tal cual.

## Qué cambia
- Existe un perfil de proyecto "Trabajo grupal de MBA" que genera los
  documentos del proyecto del grupo con vocabulario de MBA: entregables en
  lugar de capacidades, iniciativas en lugar de cambios, criterios de
  aceptación derivados de la rúbrica en lugar de escenarios de software.
- Los tipos de verificación del perfil son propios del trabajo académico
  (fuente citada, revisión por un par, cálculo reproducible, cumple rúbrica).
- Las puertas 🔒 del perfil corresponden a los avances presentados al
  profesor y a los acuerdos del grupo (`memoria.md D4`).
- El plan del grupo registra responsable y fecha por tarea (`learn.md M2`).

## Fuera de alcance
- Servidor MCP, almacenamiento automático y validación del lado del servidor
  (Fase 2).
- Instrucciones específicas por LLM (eso es `C002`).
- Otros perfiles (investigación académica, consultoría, software).
- El contenido del trabajo de MBA del grupo: el perfil da la estructura, no
  escribe el trabajo.

## Capacidades afectadas
| Capacidad | Tipo | Delta |
|---|---|---|
| `PERFIL` | modificada (primeros requisitos) | `delta.md §PERFIL` |
| `COLAB` | modificada (primeros requisitos, modo manual) | `delta.md §COLAB` |

## Impacto
Ningún sistema de producción. Afecta a personas: los compañeros del grupo
usarán lo que salga de aquí en un trabajo con nota. Cualquier cosa que se
comparta con ellos requiere confirmación (`agente.md §4`).

## Criterio de éxito
Todos los escenarios del delta en verde **y** un integrante que no participó
en el diseño puede, con solo los documentos generados, decir qué entregable
está en curso, qué decidió el grupo y qué falta para el próximo avance.

## Aprobación (P1)
- [ ] Aprobada por el usuario el <fecha> — <comentario>
