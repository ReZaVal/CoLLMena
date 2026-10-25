# coLLMena

**El espacio de trabajo ordenado para tu grupo y su inteligencia artificial.**

Un producto de ZOr Labs Peru SAC · En desarrollo (fase de piloto)

---

## ¿Qué problema resuelve?

Imagina que tu grupo está haciendo un trabajo largo, como una tesis, y todos
usan inteligencia artificial: unos ChatGPT, otros Claude. Lo normal hoy es
tener todo metido en **un solo chat**: documentos, ideas, correcciones, todo
mezclado. Con el tiempo pasa esto:

- El chat se vuelve lento y caro, porque la IA tiene que releer todo cada vez
  que le preguntas algo.
- Nadie encuentra nada: ¿dónde quedó la última versión del capítulo 2?
- Cada uno trabaja por su lado y no se sabe quién cambió qué.

## ¿Qué es coLLMena?

Piensa en una **colmena**: muchas abejas, cada una haciendo lo suyo, pero
todas trabajan en el mismo panal, donde cada cosa tiene su lugar.

- **El panal es una carpeta en Google Drive** que comparte el grupo. Ahí
  están los documentos de siempre: el Word de la tesis, la presentación en
  PowerPoint, los cálculos en Excel.
- **Cada abeja es un integrante con su propia IA.** No importa si usas
  ChatGPT o Claude: todos trabajan sobre los mismos documentos.
- **La colmena tiene memoria.** Guarda en un archivo sencillo qué decidió el
  grupo, qué tareas faltan y qué dijo el profesor en cada avance. Cuando
  alguien abre su IA, esta lee primero ese resumen y ya sabe en qué va el
  trabajo. No hay que explicarle todo de nuevo.
- **Hay un cuaderno de cambios.** Cada vez que alguien modifica un documento,
  queda anotado quién lo hizo, cuándo, qué cambió y por qué. Si alguien edita
  a mano, la IA lo nota al empezar y pregunta qué se hizo.
- **Tú mandas.** La IA puede leer todo, pero solo modifica un documento si tú
  se lo pides.

**En una frase:** coLLMena hace que tu grupo trabaje con inteligencia
artificial como un equipo ordenado, y no como un chat desordenado, sin que
nadie tenga que saber de tecnología.

## Con qué IA funciona

| Asistente | Estado |
|---|---|
| Claude, ChatGPT | En piloto |
| Gemini, DeepSeek, Grok, Perplexity, Microsoft Copilot | Planificados (por verificar cómo se conectan) |

---

## Para quien desarrolla coLLMena

Este repositorio se dirige con un *harness* de documentación + Spec-Driven
Development, para que cualquier agente de IA retome el trabajo sin memoria de
sesiones anteriores. **Empieza siempre por [`agente.md`](agente.md).**

| Documento | Para qué sirve |
|---|---|
| `agente.md` | Contrato de operación del agente (punto de entrada) |
| `manager.md` | Fases, estado actual y «Contexto activo» |
| `memoria.md` | Decisiones del producto y preguntas abiertas |
| `planner.md` | Tareas, sesiones y cronograma |
| `learn.md` | Errores, reglas aprendidas y mejoras al harness |
| `specs/` · `cambios/` | Qué hace el producto y cómo cambia |
| `openspec.py` | Validador: `python openspec.py validate --strict` |
| `marketing/` | Material de comunicación (prompts de diseño, textos) |
