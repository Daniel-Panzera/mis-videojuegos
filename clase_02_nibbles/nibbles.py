import random
import sys
from pathlib import Path

import pygame

pygame.init()

ANCHO, ALTO = 600, 600
CELDA = 30
COLUMNAS = ANCHO // CELDA
FILAS = ALTO // CELDA

# La manzana dorada vale más, pero aparece poco y no espera para siempre.
PUNTOS_DORADA = 5
PROBABILIDAD_DORADA = 0.2   # 1 de cada 5 manzanas comunes invoca una dorada
DURACION_DORADA = 50        # cuadros que se queda en pantalla (5 s a 10 FPS)

# El récord se guarda al lado del script, no en la carpeta desde donde se ejecuta.
ARCHIVO_RECORD = Path(__file__).parent / "record.txt"

pantalla = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()

# El cuerpo: lista de (columna, fila). La cabeza es el primer elemento.
serpiente = [(5, 5)]
direccion = (1, 0)  # (dx, dy) -> derecha


def celda_libre(ocupadas):
    """Sortea una celda del tablero que no esté ya ocupada."""
    while True:
        c = (random.randint(0, COLUMNAS - 1), random.randint(0, FILAS - 1))
        if c not in ocupadas:
            return c


manzana = celda_libre(serpiente)
manzana_dorada = None       # None = ahora mismo no hay dorada en pantalla
tiempo_dorada = 0           # cuadros que le quedan antes de desvanecerse
puntos = 0

# Récord de partidas anteriores. Si el archivo no existe o está corrupto, arranca en 0.
try:
    record = int(ARCHIVO_RECORD.read_text())
except (FileNotFoundError, ValueError):
    record = 0


def dibujar_celda(pos, color):
    pygame.draw.rect(pantalla, color,
                     (pos[0] * CELDA, pos[1] * CELDA, CELDA - 2, CELDA - 2))


ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            # No dejar que gire 180 grados (no puede ir para atrás)
            if evento.key == pygame.K_UP and direccion != (0, 1):
                direccion = (0, -1)
            elif evento.key == pygame.K_DOWN and direccion != (0, -1):
                direccion = (0, 1)
            elif evento.key == pygame.K_LEFT and direccion != (1, 0):
                direccion = (-1, 0)
            elif evento.key == pygame.K_RIGHT and direccion != (-1, 0):
                direccion = (1, 0)

    # 1) Nueva cabeza
    cabeza = (serpiente[0][0] + direccion[0], serpiente[0][1] + direccion[1])
    serpiente.insert(0, cabeza)

    # 2) ¿Comió?
    if cabeza == manzana:
        puntos += 1
        manzana = celda_libre(serpiente)
        # Cada tanto, además de la común, aparece una dorada.
        if manzana_dorada is None and random.random() < PROBABILIDAD_DORADA:
            manzana_dorada = celda_libre(serpiente + [manzana])
            tiempo_dorada = DURACION_DORADA
    elif cabeza == manzana_dorada:
        puntos += PUNTOS_DORADA
        manzana_dorada = None
    else:
        serpiente.pop()  # no comió -> se achica por el final

    # La dorada se desvanece sola si no llegás a tiempo.
    if manzana_dorada is not None:
        tiempo_dorada -= 1
        if tiempo_dorada <= 0:
            manzana_dorada = None

    # 3) ¿Chocó con el borde o consigo misma?
    if (cabeza[0] < 0 or cabeza[0] >= COLUMNAS or
            cabeza[1] < 0 or cabeza[1] >= FILAS or
            cabeza in serpiente[1:]):
        ejecutando = False

    # 4) Dibujar
    pantalla.fill((10, 10, 15))
    for segmento in serpiente:
        dibujar_celda(segmento, (0, 220, 60))
    dibujar_celda(manzana, (230, 40, 40))
    if manzana_dorada is not None:
        dibujar_celda(manzana_dorada, (255, 200, 0))
    pygame.display.set_caption(f"Puntos: {puntos}  |  Récord: {record}")
    pygame.display.flip()
    reloj.tick(10)  # 10 FPS: velocidad clásica

pygame.quit()

# Guardar el récord solo si esta partida lo superó.
if puntos > record:
    record = puntos
    ARCHIVO_RECORD.write_text(str(record))
    print(f"Fin del juego. ¡Nuevo récord: {record} puntos!")
else:
    print(f"Fin del juego. Puntos: {puntos} (récord: {record})")

sys.exit()
