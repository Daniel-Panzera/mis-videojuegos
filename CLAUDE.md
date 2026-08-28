# Proyecto: mis-videojuegos

Repositorio de la cursada de videojuegos con Python y Pygame. Cada actividad vive en su propia carpeta `clase_NN_*`.

## Archivos de respuestas: nunca se suben al repo

Los archivos de preguntas y respuestas de cada clase son **material de estudio personal**, no parte de la entrega.

Reglas obligatorias:

1. **Nombre:** cualquier archivo de este tipo debe contener la palabra `respuestas` en su nombre (por ejemplo `preguntas_y_respuestas.md`). Ese es el disparador del patrón `*respuestas*` del `.gitignore`.
2. **Ubicación:** dentro de la carpeta de la clase a la que corresponden.
3. **No versionar:** jamás agregarlos a git, ni con `git add -f`. Si alguno aparece en `git status` como archivo sin seguimiento, algo está mal en el patrón del `.gitignore`: corregir el patrón, no forzar el agregado.
4. **No mencionarlos en el `README.md`.** El README sí se sube, así que una referencia a un archivo ignorado sería un enlace roto para cualquiera que clone el repo.

Al crear un archivo de respuestas nuevo, verificar que quedó ignorado antes de commitear:

```powershell
git check-ignore -v clase_NN_lo_que_sea\preguntas_y_respuestas.md
```

Si el comando no imprime nada, el archivo **no** está siendo ignorado.

## Entorno

- **Python 3.14.7**, en `%LOCALAPPDATA%\Programs\Python\Python314`. En la máquina hay además un Python 3.14.2 del Install Manager que no se usa para este proyecto.
- **pygame-ce 2.5.8**, no el `pygame` clásico: este último no publica wheel para Python 3.14 e intentaría compilar desde C. Se importa igual, con `import pygame`.
- **Nunca ejecutar `pip install pygame`** (sin el `-ce`): los dos paquetes ocupan el mismo nombre y se rompen entre sí.

## Convenciones de código

- Comentarios en español, en el mismo tono que el material de la cátedra.
- Código simple y explícito por sobre lo ingenioso: es material didáctico y tiene que poder leerse en clase.
