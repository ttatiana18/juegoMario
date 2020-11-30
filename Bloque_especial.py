import pygame
from lib_juegos import *
import random
 
class Bloque_especial(pygame.sprite.Sprite):
    """docstring for Meteoro"""
    def __init__(self, pos):
        super().__init__()
        self.m=Recorte("./data/img/elementos_mapa.png",33,28)
        self.con=24
        self.tipo_b=1#tipo bloque
        self.tipo_m=random.randrange(1,4)#tipo modificador
        self.image=self.m[0][self.con]
        self.image.set_colorkey( (0,0,0) )
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_y=0
        self.temp=0
        self.golpeada=False
        self.activa=True

    def gravedad(self,cte):
        if self.vel_y==0:
            self.vel_y=1
        else:
            self.vel_y+=cte

    def update(self, velocidad=0,velocidady=0):
        self.temp+=1
        self.rect.x += velocidad
        if velocidady==0:
            self.rect.y += self.vel_y
        else:
            self.rect.y += velocidady
        if self.golpeada:
            self.gravedad(0.5)
            if self.vel_y>2.5:
                self.vel_y=0
                self.golpeada=False
        
        if (self.temp%8)==0:
            if self.activa:
                self.image=self.m[0][self.con]
                if self.con<26:
                    self.con+=1
                else:
                    self.con=24
            else:
                self.image=self.m[0][27]

    def golpear(self):
        self.vel_y=-2
        self.golpeada=True

        