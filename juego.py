import pygame
import random
import sys

pygame.init()
ANCHO=1000
ALTO=600
pantalla=pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("juego de cubos")
fondo=pygame.image.load("imagenes/ciudad.png")
FPS=60
relog=pygame.time.Clock()


class cubo1 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("imagenes/juegonave/cubo1.png")

        self.rect=self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.center=(ANCHO//2,ALTO-50)
        self.velocidad_x=10

    def update(self):
        self.rect.x = self.velocidad_x


        #teclas de movimiento
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_a]:
            self.velocidad_x-=10

        if teclas[pygame.K_d]:
            self.velocidad_x+=10

        #limite de margen
        if self.rect.right>ANCHO:
            self.velocidad_x -=10

        if self.rect.left<0:
            self.velocidad_x += 10





class cubo2 (pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_aleatoria = random.randrange(3)
        if self.image_aleatoria == 0:
            self.image = pygame.image.load("imagenes/juegonave/cubo2.png")
        if self.image_aleatoria == 1:
            self.image = pygame.image.load("imagenes/juegonave/cubo2.png")
        if self.image_aleatoria == 2:
            self.image = pygame.image.load("imagenes/juegonave/cubo2.png")

        self.image.set_colorkey((0, 0, 0))
        self.rect=self.image.get_rect()

        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = -self.rect.width
        self.velocidad_y = random.randrange(1,10)


    def update(self):
        self.rect.y += self.velocidad_y




        #actualizar sprites


        if self.rect.top-40>ALTO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y = -self.rect.width
            self.velocidad_y = random.randrange(1,10)


#GROUP SPRITES
sprites=pygame.sprite.Group()
enemigos=pygame.sprite.Group()

jugador=cubo1()
sprites.add(jugador)

for x in range(5):
    enemigo=cubo2()
    enemigos.add(enemigo)







while True:
    relog.tick(FPS)
    pantalla.blit(fondo,(0,0))



    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    jugador.update()
    enemigo.update()

    sprites.draw(pantalla)
    enemigos.draw(pantalla)







    pygame.display.flip()


