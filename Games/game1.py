import pygame
import sys
import random

pygame.init()

# Pantalla y reloj
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Supervivencia")
reloj = pygame.time.Clock()
FPS = 60

# Jugador
jugador = pygame.Rect(100, 100, 40, 40)
velocidad = 5

# Recursos
class Recurso:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 20, 20)
        self.tipo = random.choice(["madera", "comida", "piedra"])
        self.color = {"madera": (139,69,19), "comida": (255,0,0), "piedra": (128,128,128)}[self.tipo]

recursos = [Recurso(random.randint(0, ANCHO-20), random.randint(0, ALTO-20)) for _ in range(15)]
inventario = {"madera": 0, "comida": 0, "piedra": 0}

# Tiempo máximo (en segundos)
TIEMPO_LIMITE = 180
tiempo_juego = 0  # en frames

def mostrar_pantalla_final(texto):
    pantalla.fill((0, 0, 0))
    mensaje = fuente.render(texto, True, (255, 255, 255))
    pantalla.blit(mensaje, (ANCHO//2 - mensaje.get_width()//2, ALTO//2 - 10))
    pygame.display.flip()
    pygame.time.wait(4000)
    pygame.quit()
    sys.exit()

# Estado
salud = 100
energia = 100
temporizador_energia = 0
hogueras = []

# Fuente
fuente = pygame.font.SysFont(None, 36)

# Misión
mision_completa = False

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador con bordes conectados
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]: 
        jugador.x = (jugador.x - velocidad) % ANCHO
    if teclas[pygame.K_RIGHT]: 
        jugador.x = (jugador.x + velocidad) % ANCHO
    if teclas[pygame.K_UP]: 
        jugador.y = (jugador.y - velocidad) % ALTO
    if teclas[pygame.K_DOWN]: 
        jugador.y = (jugador.y + velocidad) % ALTO

    # Usar comida
    if teclas[pygame.K_SPACE] and inventario["comida"] > 0 and energia < 100:
        inventario["comida"] -= 1
        energia = min(100, energia + 20)

    # Construir hoguera
    if teclas[pygame.K_b] and all(inventario[t] >= 3 for t in ["madera", "piedra"]):
        hogueras.append(pygame.Rect(jugador.x + 50, jugador.y, 20, 20))
        inventario["madera"] -= 3
        inventario["piedra"] -= 3

    # Recolectar recursos
    for recurso in recursos[:]:
        if jugador.colliderect(recurso.rect):
            inventario[recurso.tipo] += 1
            recursos.remove(recurso)
            # Añadir nuevo recurso para mantener el conteo
            recursos.append(Recurso(random.randint(0, ANCHO-20), random.randint(0, ALTO-20)))

    # Energía y salud
    temporizador_energia += 1
    if temporizador_energia >= FPS * 5:
        energia = max(0, energia - 5)
        if energia == 0:
            salud = max(0, salud - 10)
        temporizador_energia = 0

    # Verificar misión
    if not mision_completa and len(hogueras) > 0 and inventario["comida"] >= 3:
        mision_completa = True

    # Actualizar tiempo
    tiempo_juego += 1
    segundos_restantes = max(0, TIEMPO_LIMITE - tiempo_juego // FPS)

    # Dibujar
    pantalla.fill((0, 100, 0))
    pygame.draw.rect(pantalla, (0, 255, 0), jugador)

    for recurso in recursos:
        pygame.draw.rect(pantalla, recurso.color, recurso.rect)

    for h in hogueras:
        pygame.draw.rect(pantalla, (255, 140, 0), h)

    # Mostrar HUD
    texto_inv = fuente.render(f'M: {inventario["madera"]} C: {inventario["comida"]} P: {inventario["piedra"]}', True, (255,255,255))
    pantalla.blit(texto_inv, (10, 10))

    pygame.draw.rect(pantalla, (255, 0, 0), pygame.Rect(10, 40, salud * 2, 20))
    pygame.draw.rect(pantalla, (0, 0, 255), pygame.Rect(10, 70, energia * 2, 20))

    texto_tiempo = fuente.render(f"Tiempo: {segundos_restantes}s", True, (255, 255, 255))
    pantalla.blit(texto_tiempo, (10, 100))

    # Verificar condiciones de fin de juego
    if salud <= 0:
        mostrar_pantalla_final("HAS MUERTO")
    elif segundos_restantes <= 0:
        mostrar_pantalla_final("¡Tiempo agotado!")
    elif mision_completa:
        mostrar_pantalla_final("¡Misión completada! Has sobrevivido")

    if mision_completa:
        pantalla.blit(fuente.render("¡MISIÓN CUMPLIDA!", True, (255, 255, 0)), (ANCHO//2 - 100, 20))

    pygame.display.flip()
    reloj.tick(FPS)