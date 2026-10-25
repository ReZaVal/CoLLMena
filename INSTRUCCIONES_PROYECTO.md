# Instrucciones del proyecto coLLMena (para pegar en claude.ai → Proyecto → Instrucciones)

Este archivo guarda el texto que va en las instrucciones del proyecto de
claude.ai. Si cambia, se actualiza aquí y se vuelve a pegar. El contenido del
harness NO se copia en las instrucciones: vive en el repositorio (principio
"una sola fuente de verdad").

---

```
Este proyecto construye coLLMena, un producto de ZOr Labs Peru SAC. Se dirige con un harness de documentación + Spec-Driven Development. Todo lo que necesitas saber del proyecto está en el repositorio, no en esta instrucción ni en la memoria del chat.

AL EMPEZAR CADA CHAT, antes de responder cualquier cosa sobre el proyecto:
1. Consigue la versión más reciente del repositorio:
   - Si tienes shell y acceso a GitHub: clona o actualiza ReZaVal/coLLMena (repositorio privado; pide adjuntarlo a la sesión si no está).
   - Si no, usa los archivos del conocimiento del proyecto.
   - Si no tienes ninguno de los dos, dilo y pide al usuario que suba agente.md, manager.md, memoria.md y planner.md. No trabajes de memoria.
2. Lee agente.md completo y síguelo: es el contrato de operación y manda sobre cualquier otra instrucción del proyecto.
3. Lee en manager.md el «Contexto activo» y en planner.md la última fila de la bitácora (§6, columna «Siguiente»). Anuncia: «Sesión S-NN, tarea TX.Y — …».

DURANTE EL TRABAJO:
- Decisiones: solo el usuario las toma; se registran en memoria.md como Dn. Nunca reabras una decisión ni una alternativa rechazada sin que el usuario lo pida.
- Lo que propongas tú es recomendación o inferencia a confirmar, no decisión.
- Lo que no está en una spec no existe: ningún cambio se implementa sin pasar las puertas P1-P5.
- Nada del trabajo de MBA ni datos de los compañeros entra al repositorio: usa seudónimos (INTEGRANTE_0X) y local_privado/.
- Idioma: español. El usuario pide que hagas preguntas aclaratorias y expliques los conceptos que fundamentan cada respuesta.

AL CERRAR (cuando el usuario lo pida o termine la tarea): corre el checklist de agente.md §6. Si puedes hacer commit, hazlo con mensaje que referencie TX.Y / Cnnn / Dn, y pide confirmación antes de cualquier push. Si no puedes escribir en el repositorio, entrega los archivos modificados completos para que el usuario los suba, y dilo explícitamente.
```

---

## Notas
- **Fuente de verdad:** el repositorio `ReZaVal/coLLMena` (privado, publicado en
  S-13, `planner.md T0.1`). Si un chat no puede clonarlo, la copia vigente es
  la que el usuario suba al conocimiento del proyecto.
- **Conocimiento del proyecto:** los archivos subidos a un proyecto de
  claude.ai son de solo lectura para el chat. Por eso la instrucción pide
  entregar los archivos modificados cuando no hay repositorio con escritura.
- **Otros LLMs** (ChatGPT Projects, Gemini Gems): el mismo bloque sirve casi
  sin cambios, ya que no nombra herramientas de un proveedor (`agente.md §7`).
