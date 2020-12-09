import pygame
from lib_juegos import *

class Generador_caracol(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.m=Recorte("./data/img/nube.png",3,1)
        self.con_ini=1
        self.image=self.m[0][self.con_ini]
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.temp=300
        self.cont=0
        self.vel_x=5
        self.limiteD=self.rect.right + 200
        self.limiteI=self.rect.left - 200
        self.salud=200

    def update(self):
        self.rect.x += self.vel_x
        if(self.rect.left<=self.limiteI):
            self.vel_x=5
        elif self.rect.right>=self.limiteD:
            self.vel_x=-5
        
        self.temp-=1

        self.image=self.m[0][self.con_ini]
        if (self.temp%50)==0 and self.vel_x !=0 :
            if self.vel_x >0:
                if self.con_ini<2:
                    self.con_ini+=1
                else:
                    self.con_ini=1
            else:
                if self.con_ini<1:
                    self.con_ini+=1
                else:
                    self.con_ini=0