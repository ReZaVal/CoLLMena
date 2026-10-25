# Prompt para Claude Design — Prototipo del landing de coLLMena

Versión 1 · 2026-10-25 · Decisiones de origen: `memoria.md D8-D17`

Copia todo lo que está dentro del bloque y pégalo en Claude Design.

---

```
Diseña el prototipo de una landing page (una sola página web, adaptable a celular y escritorio) para coLLMena, un producto de la empresa peruana ZOr Labs. Todo el texto de la página va en español neutro latinoamericano, tuteando al lector.

## Qué es el producto
coLLMena es el espacio de trabajo ordenado para que un grupo de personas trabaje con inteligencia artificial. Está pensado para gente que NO es técnica: estudiantes de MBA haciendo su tesis en grupo, equipos de investigación, equipos de trabajo. El nombre es un juego entre "colmena" y "LLM" (modelo de lenguaje): muchas abejas, cada una con su rol, trabajando en el mismo panal ordenado.

El problema que resuelve: hoy los grupos usan la IA en un solo chat donde mezclan documentos, ideas y correcciones. El chat se vuelve lento y caro (la IA relee todo en cada pregunta), nadie encuentra la última versión de nada y no se sabe quién cambió qué.

Cómo lo resuelve (estas son las funcionalidades, úsalas como contenido):
1. Tu panal en Google Drive: los documentos viven en una carpeta compartida del grupo, en los formatos de siempre (Word, PowerPoint, Excel).
2. Cada uno con su IA favorita: cada integrante usa el asistente que prefiera y todos trabajan sobre los mismos documentos.
3. Una colmena con memoria: el proyecto guarda qué decidió el grupo, qué tareas faltan y qué dijo el profesor en cada avance. La IA lo lee al empezar y no hay que explicarle todo otra vez. Gasta menos y responde mejor.
4. Cuaderno de cambios: cada modificación queda anotada (quién, cuándo, qué y por qué), como un historial de trabajo del equipo. Si alguien edita a mano, la IA lo detecta y pregunta qué se hizo.
5. Tú decides: la IA lee todo, pero solo edita un documento cuando tú se lo pides.

## Estructura de la página
1. Barra superior: logotipo "coLLMena" (texto, con "LLM" en amarillo), enlaces "Cómo funciona", "Funciones", "Preguntas", y un botón "Únete al piloto".
2. Hero (fondo negro): titular grande "Tu grupo y su IA, trabajando como una colmena." Subtítulo: "Un solo espacio en Google Drive donde cada integrante usa la IA que prefiera, con memoria del proyecto y registro de cada cambio. Sin saber de tecnología." Botón principal amarillo "Únete al piloto" y botón secundario de contorno "Ver cómo funciona". Al lado o detrás, una ilustración de abejas robot sobre un panal hexagonal.
3. El problema: comparación visual "Antes: un chat desordenado" vs "Con coLLMena: un panal ordenado". A la izquierda un chat caótico con mensajes y archivos amontonados; a la derecha celdas hexagonales ordenadas (Documentos, Decisiones, Tareas, Cambios).
4. Cómo funciona, en 3 pasos numerados: (1) Conecta la carpeta de Drive de tu grupo. (2) Cada integrante abre su IA favorita. (3) Trabajen: la colmena recuerda las decisiones y anota cada cambio.
5. Funciones: una cuadrícula de 5 tarjetas, una por cada funcionalidad de arriba, cada una con un ícono hexagonal simple.
6. "Funciona con la IA que ya usas": una fila de insignias de texto (sin logotipos de otras marcas) con estos nombres y su estado:
   - Claude — "En piloto"
   - ChatGPT — "En piloto"
   - Gemini, DeepSeek, Grok, Perplexity, Microsoft Copilot — "Próximamente"
   Las insignias "En piloto" van con borde amarillo; las "Próximamente" en gris.
7. Vista previa del "Cuaderno de cambios": una tarjeta con tipografía monoespaciada que muestre 3 entradas de ejemplo con este formato:
   [0012] 03 nov 2026 · Integrante 2 · ChatGPT
   Documento: Capítulo 3 - Análisis de mercado.docx
   Cambio: Se agregó la sección 3.2 con el tamaño de mercado.
   Motivo: Observación del profesor en el avance.
   Usa nombres genéricos ("Integrante 1, 2, 3"), nunca nombres de personas reales.
8. Caso de uso: "Hecho para trabajos en grupo largos" — tesis de MBA, investigaciones en equipo, proyectos de consultoría. Sin testimonios inventados: no pongas citas ni opiniones atribuidas a personas, porque aún no hay clientes.
9. Preguntas frecuentes (4-5, en acordeón): ¿Necesito saber programar? (No.) ¿Dónde quedan mis documentos? (En tu Google Drive, no en el nuestro.) ¿La IA cambia cosas sin permiso? (No.) ¿Puedo usar una IA distinta a la de mis compañeros? (Sí.) ¿Cuánto cuesta? (Estamos en piloto; únete a la lista.)
10. Llamado final: fondo amarillo, titular "Lleva a tu grupo a la colmena", campo de correo + botón negro "Únete al piloto" (solo visual, no tiene que enviar nada).
11. Pie de página: "coLLMena es un producto de ZOr Labs Peru SAC", año 2026, enlaces de contacto y privacidad como marcadores.

## Estilo visual
- Inspirado en la estética de Vercel: minimalista, alto contraste, mucho espacio en blanco, líneas de cuadrícula finas de 1 px, bordes sutiles, esquinas levemente redondeadas (8 px), sombras casi invisibles, animaciones discretas. Inspirado, no copiado: no uses el logotipo ni el triángulo de Vercel ni su marca.
- Tipografía: Geist Sans para todo el texto y Geist Mono para etiquetas, números de paso, insignias y el cuaderno de cambios (ambas son libres, de Google Fonts). Titulares grandes, peso semibold, interletrado ligeramente negativo.
- Colores, solo estos tres más grises neutros:
  - Negro #0A0A0A (fondos del hero y secciones oscuras, texto principal)
  - Blanco #FFFFFF (fondos claros, texto sobre negro)
  - Amarillo abeja #FFC21A como acento (botones principales, "LLM" del logotipo, insignias activas, detalles de las abejas); tono miel #E5A100 para estados hover
  - Grises para bordes y texto secundario: #EAEAEA, #A1A1A1, #666666
  - Accesibilidad: nunca texto amarillo sobre fondo blanco (no tiene contraste suficiente). El amarillo va como fondo con texto negro, o como acento sobre negro.
- Motivo gráfico: hexágonos de panal, usados con sutileza (patrón de fondo tenue en el hero, íconos dentro de hexágonos, celdas en la comparación).
- Ilustraciones: abejas robot amigables, geométricas y minimalistas, en negro y amarillo: cuerpo con franjas, ojos tipo LED, antenas de robot, alas como paneles translúcidos. Úsalas en 3 o 4 lugares: el hero (varias abejas volando hacia el panal), la sección "Cómo funciona" (una abeja por paso) y el llamado final. Deben transmitir "tecnología e IA" sin dejar de ser simpáticas. No las uses en todas las secciones.
- Tono de los textos: cercano, claro y sin jerga técnica. No uses palabras como "LLM", "API", "repositorio", "commit" o "markdown" en el texto visible (solo el guiño del nombre del producto).
- Diseño adaptable: en celular, una sola columna, menú plegable y el botón "Únete al piloto" siempre visible.
```

---

## Notas para quien use este prompt
- **Estado real del producto:** el landing es un prototipo. Ninguna IA está
  integrada todavía; "En piloto" = objetivo de la Fase 1 (`memoria.md D1`,
  `D16`). No publicar sin revisar que cada afirmación sea cierta en ese
  momento.
- **Marcas de terceros:** se nombran como texto para indicar compatibilidad,
  sin usar sus logotipos. Antes de publicar, revisar las pautas de marca de
  cada empresa.
- **Nombre y marca:** pendiente la revisión en INDECOPI y de dominios
  (`memoria.md Q10`).
