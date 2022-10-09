import pygame,sys
from pygame.locals import *

ANCHO=600
ALTO=450

clock=pygame.time.Clock()
FPS=60



class nave(pygame.sprite.Sprite):
    #atributos
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.jugador=pygame.image.load("imagenes/sprite/ninja definitivo.png")
        self.rect=self.jugador.get_rect()
        self.rect.centerx=ANCHO/2
        self.rect.centery=ALTO-60

    def dibujar(self,superficie):
        superficie.blit(self.jugador,self.rect)









personaje=nave()
fondo=pygame.image.load("imagenes/fondoblanco.jpg")

def Mariobros():
    pygame.init()
    ventana=pygame.display.set_mode((ANCHO,ALTO))
    pygame.display.set_caption("mario bros")
    ventana.blit(fondo,(0,0))
    clock.tick(FPS)
    print(clock)

    while True:
        for evento in pygame.event.get():
                if evento.type== QUIT:
                    pygame.quit()
                    sys.exit()
        
        personaje.dibujar(ventana)
        pygame.display.update()

Mariobros()




