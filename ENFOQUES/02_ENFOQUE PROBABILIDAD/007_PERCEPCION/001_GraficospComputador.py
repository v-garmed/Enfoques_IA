import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Tamaño de la ventana
ancho, alto = 600, 400
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Gráficos por Computador - Círculo en movimiento")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Posición inicial del círculo
x, y = 300, 200
velocidad = 5

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Captura de teclas presionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Dibujar fondo y círculo
    pantalla.fill(BLANCO)
    pygame.draw.circle(pantalla, AZUL, (x, y), 30)

    # Actualizar pantalla
    pygame.display.flip()
    pygame.time.Clock().tick(60)
