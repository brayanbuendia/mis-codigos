import pygame,sys
from pygame.locals import *
from random import randint

#variables globales
ANCHO=800
ALTO=480

class NaveEspacial(pygame.sprite.Sprite):
    #clase para nuestra nave
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagennave=pygame.image.load("imagenes/nave.png")
        self.rect=self.imagennave.get_rect()
        self.rect.centerx= ANCHO/2
        self.rect.centery= ALTO-60

        self.ListaDisparos=[]
        self.vida=True
        self.velocidad=20
        


    def movimiento(self):
        if self.vida==True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>820:
                self.rect.right=800

        

    def disparar(self,x,y):
        miProyectil=Proyectil(x,y)
        self.ListaDisparos.append(miProyectil)

    def dibujar(self,superficie):
        superficie.blit(self.imagennave,self.rect)   

class Proyectil(pygame.sprite.Sprite):
    #sprite para que la clase tengo acceso a los sprites
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenDisparo=pygame.image.load("imagenes/disparo.png")
        #rect para convertirlo en rectangulo para usar la funcion de colision
        self.rect=self.imagenDisparo.get_rect()
        self.velocidadDisparo=9
        self.rect.top=posY
        self.rect.left=posX

    def trayectoria(self):
        self.rect.top= self.rect.top-self.velocidadDisparo

    def dibujar(self,superficie):
        superficie.blit(self.imagenDisparo,self.rect)



class Invasor (pygame.sprite.Sprite):
    #sprite para que la clase tengo acceso a los sprites
    def __init__(self,posX,posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA=pygame.image.load("imagenes/enemigo1.png")
        self.imagenB=pygame.image.load("imagenes/enemigo1B.png")

        #lista para concadenar las imagenes
        self.ListaImagenes= [self.imagenA,self.imagenB]
        self.posImagen=0

        self.ImagenInvasor=self.ListaImagenes[self.posImagen]

        #rect para convertirlo en rectangulo para usar la funcion de colision
        self.rect=self.ImagenInvasor.get_rect()
        self.ListaDisparos=[]
        self.velocidad=20
        self.rect.top=posY
        self.rect.left=posX

        self.tiempoCambio= 1

    def trayectoria(self):
        self.rect.top= self.rect.top-self.velocidadDisparo

    def dibujar(self,superficie):
        self.ImagenInvasor=self.ListaImagenes[self.posImagen]
        superficie.blit(self.ImagenInvasor,self.rect)

    def comportamiento(self,tiempo):
        if self.tiempoCambio==tiempo:
            self.posImagen+=1
            self.tiempoCambio+=1

        if self.posImagen>len(self.ListaImagenes)-1:
            self.posImagen=0
        

def SpaceInvader():
    pygame.init()
    ventana=pygame.display.set_mode((ANCHO,ALTO))
    pygame.display.set_caption("Space Invader")
    Imagenfondo=pygame.image.load("imagenes/fondonegro.jpg")
    fondo=pygame.image.load("imagenes/planeta rojo2.png")

    demoProyectil=Proyectil(ANCHO/2,ALTO-60)
    enemigo=Invasor(100,100)

    
    
    reloj=pygame.time.Clock()
    jugador=NaveEspacial()

    
    tiempo=pygame.time.get_ticks()/1000

    enjuego=True
    while True:
        reloj=pygame.time.Clock()
        demoProyectil.trayectoria()
        reloj.tick(60)
        jugador.movimiento()
        ventana.blit(Imagenfondo,(0,0))
        
        
        for evento in pygame.event.get():
            if evento.type== QUIT:
                pygame.quit()
                sys.exit()
            if enjuego== True:
                if evento.type==pygame.KEYDOWN:

                    if evento.key==K_LEFT:
                        jugador.rect.left-=jugador.velocidad
                    elif evento.key==K_RIGHT:
                        jugador.rect.right+=jugador.velocidad
                    elif evento.key==K_UP:
                        jugador.rect.top-=jugador.velocidad
                    elif evento.key==K_DOWN:
                        jugador.rect.top+=jugador.velocidad
                    elif evento.key==K_s:
                        x,y=jugador.rect.center
                        jugador.disparar(x,y)
            
                    
                            
                    
            
        
        
        
        ventana.blit(fondo,(500,0))
        enemigo.comportamiento(tiempo)
        jugador.dibujar(ventana)
        enemigo.dibujar(ventana)
        
        if len(jugador.ListaDisparos)>0:
            for x in jugador.ListaDisparos:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top<0:
                    jugador.ListaDisparos.remove(x)
        pygame.display.update()

SpaceInvader()