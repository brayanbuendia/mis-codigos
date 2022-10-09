import pygame
import random

#Tamaño de pantalla
ANCHO = 1000
ALTO = 600
#FPS
FPS = 60
# Paleta de colores
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)
H_FA2F2F = (250,47,47)
VERDE= (0,255,0)
AZUL = (0,0,255)
H_50D2FE = (94,210,254)
Fondo=pygame.image.load("imagenes/ciudad.png")

class Jugador(pygame.sprite.Sprite):
    # Sprite del jugador
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.image.load("imagenes/juegonave/nave.png").convert()      
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (ANCHO // 2, ALTO)
        self.image.set_colorkey(NEGRO)
        
        self.rect.center=(200,200)
        
    def update(self):
        
          
        #velocidad inicial del jugador
        self.velocidad_x=0
        self.velocidad_y=0

        #get the modules pressed
        teclas=pygame.key.get_pressed()

        #izquierda
        if teclas[pygame.K_a]:
            self.velocidad_x = -20
        # derecha
        if teclas[pygame.K_d]:
            self.velocidad_x = +20
        
        #disparo
        if teclas[pygame.K_SPACE]:
            jugador.disparo()
        
        #arriba
        elif teclas[pygame.K_w]:
            self.velocidad_y = -20
        
        elif teclas[pygame.K_s]:
            self.velocidad_y = +20

        #Actualiza la velocidad del personaje
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        #limita el marge izquiero
        if self.rect.left < -20:
           self.rect.left=-20

        #limite derecho
        if self.rect.right > ANCHO+15:
           self.rect.right=ANCHO+15

        #limite arriba
        if self.rect.top<-35:
            self.rect.top= -35

        #limite abajo
        if self.rect.bottom> ALTO:
            self.rect.bottom= ALTO
    
    def disparo(self):
        bala= Disparo(self.rect.centerx,self.rect.top+50)
        balas.add(bala)


class Disparo(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("imagenes/disparo.png").convert(),(10,20))
        self.image.set_colorkey(NEGRO)
        self.rect= self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x

    def update(self):
        self.rect.y-=20
        if self.rect.bottom <0:
            self.kill()

class Meteoritos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_aleatoria= random.randrange(3)
        if self.image_aleatoria==0:
            self.image=pygame.transform.scale(pygame.image.load("imagenes/meteoritos.png").convert(),(100,80))
        if self.image_aleatoria==1:
            self.image=pygame.transform.scale(pygame.image.load("imagenes/meteoritos.png").convert(),(100,200))
        if self.image_aleatoria==2:
            self.image=pygame.transform.scale(pygame.image.load("imagenes/meteoritos.png").convert(),(150,90))
        self.image.set_colorkey((255,255,255))
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(ANCHO-self.rect.width)
        self.rect.y=-self.rect.width
        self.velocidad_y=random.randrange(1,10)

    def update(self):
        self.rect.y+= self.velocidad_y
        if self.rect.top > ALTO:
            self.rect.x = random.randrange(ANCHO - self.rect.width)
            self.rect.y =-self.rect.width
            self.velocidad_y = random.randrange(1, 10)


class nave2(pygame.sprite.Sprite):
    # Sprite del enemigo
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.image.load("imagenes/juegonave/personaje2.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (200, 200)
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        self.image.set_colorkey((255,255,255))
        # velocidad de los enemigos
        self.velocidad_x = random.randrange(5, 10)
        self.velocidad_y = random.randrange(5, 10)

    def update(self):

        # Actualiza la velocidad del personaje

        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        # limita el marge izquiero
        if self.rect.left < 0:
            self.velocidad_x += 1

        # limite derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1

        # limite arriba
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        # limite abajo
        if self.rect.top < 0:
            self.velocidad_y += 1


class nave3(pygame.sprite.Sprite):
    # Sprite del enemigo
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.image.load("imagenes/juegonave/personaje3.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (200, 200)
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        self.image.set_colorkey((255,255,255))
        # velocidad de los enemigos
        self.velocidad_x = random.randrange(1, 10)
        self.velocidad_y = random.randrange(1, 10)

    def update(self):

        # Actualiza la velocidad del personaje

        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        # limita el marge izquiero
        if self.rect.left < 0:
            self.velocidad_x += 1

        # limite derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1

        # limite arriba
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        # limite abajo
        if self.rect.top < 0:
            self.velocidad_y += 1


class nave4(pygame.sprite.Sprite):
    # Sprite del enemigo
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.image.load("imagenes/juegonave/personaje 4.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (200, 200)
        self.rect.x = random.randrange(ANCHO - self.rect.width)
        self.rect.y = random.randrange(ALTO - self.rect.height)
        self.image.set_colorkey((255,255,255))
        # velocidad de los enemigos
        self.velocidad_x = random.randrange(10, 20)
        self.velocidad_y = random.randrange(10, 20)

    def update(self):

        # Actualiza la velocidad del personaje

        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        # limita el marge izquiero
        if self.rect.left < 0:
            self.velocidad_x += 1

        # limite derecho
        if self.rect.right > ANCHO:
            self.velocidad_x -= 1

        # limite arriba
        if self.rect.bottom > ALTO:
            self.velocidad_y -= 1
        # limite abajo
        if self.rect.top < 0:
            self.velocidad_y += 1



class Enemigos(pygame.sprite.Sprite):
    # Sprite del enemigo
    def __init__(self):
        # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        # Rectángulo (jugador)
        self.image = pygame.image.load("imagenes/juegonave/personaje1.png").convert()
        # Obtiene el rectángulo (sprite)
        self.rect = self.image.get_rect()
        # Centra el rectángulo (sprite)
        self.rect.center = (200,200)
        self.rect.x=random.randrange(ANCHO- self.rect.width)
        self.rect.y=random.randrange(ALTO- self.rect.height)
        self.image.set_colorkey(NEGRO)
        #velocidad de los enemigos
        self.velocidad_x=random.randrange(1,15)
        self.velocidad_y=random.randrange(1,15)
        




    def update(self):
        
        
        
        #Actualiza la velocidad del personaje
        
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x

        #limita el marge izquiero
        if self.rect.left < 0:
            self.velocidad_x+=1

        #limite derecho
        if self.rect.right > ANCHO:
            self.velocidad_x-=1
           

        #limite arriba
        if self.rect.bottom>ALTO:
            self.velocidad_y-=1
        #limite abajo
        if self.rect.top< 0:
            self.velocidad_y+=1
            

# Inicialización de Pygame, creación de la ventana, título y control de reloj.
pygame.init()
#sistema de puntuacion
puntuacion=0
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Trabajando con sprites")
clock = pygame.time.Clock()
#Grupo de sprites, instanciación del objeto jugador.
sprites = pygame.sprite.Group()
enemigos = pygame.sprite.Group()
balas = pygame.sprite.Group()
meteoros= pygame.sprite.Group()
nave_enemiga2=pygame.sprite.Group()
nave_enemiga3=pygame.sprite.Group()
nave_enemiga4=pygame.sprite.Group()

enemigo2=nave2()
nave_enemiga2.add(enemigo2)

enemigo3=nave3()
nave_enemiga3.add(enemigo3)

enemigo4=nave4()
nave_enemiga4.add(enemigo4)



enemigo=Enemigos()
enemigos.add(enemigo)


for x in range(5):
    meteoro=Meteoritos()
    meteoros.add(meteoro)



jugador = Jugador()
sprites.add(jugador)

# Bucle de juego

ejecutando = True
while ejecutando:
    
    # Es lo que especifica la velocidad del bucle de juego
    clock.tick(FPS)
    # Eventos
    pantalla.blit(Fondo,(0,0))
    for event in pygame.event.get():
        # Se cierra y termina el bucle
        if event.type == pygame.QUIT:
            ejecutando = False

    #colision
    #colision_nave = pygame.sprite.spritecollide(jugador, enemigos, False,pygame.sprite.collide_circle)
    #colision_meteorito = pygame.sprite.spritecollide(jugador, meteoros, False, pygame.sprite.collide_circle)
     #colision bala
    #colision_disparo= pygame.sprite.groupcollide(meteoros, balas,False,False)
    



    #colision= pygame.sprite.groupcollide(enemigos, balas,False,False)




    # Actualización de sprites
    sprites.update()
    enemigos.update()
    balas.update()
    meteoros.update()
    nave_enemiga2.update()
    nave_enemiga3.update()
    nave_enemiga4.update()
    # Fondo de pantalla, dibujo de sprites y formas geométricas.
    
    sprites.draw(pantalla)
    enemigos.draw(pantalla)
    balas.draw(pantalla)
    meteoros.draw(pantalla)
    nave_enemiga2.draw(pantalla)
    nave_enemiga3.draw(pantalla)
    nave_enemiga4.draw(pantalla)

    # Actualiza el contenido de la pantalla.
    pygame.display.flip()
pygame.quit() 
pygame.quit()