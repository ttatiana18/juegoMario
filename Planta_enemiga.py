import pygame
from lib_juegos import *

class Planta_enemiga(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.m=Recorte("./data/img/enemies.png",15,8)
        self.con=13
        self.temp=0
        self.image=self.m[1][self.con]
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_y=0
        self.vel_x=0


    def update(self, velocidad=0,velocidady=0):
        self.vel_x=velocidad
        self.rect.x += velocidad
        if velocidady==0:
            self.rect.y += self.vel_y
        else:
            self.rect.y += velocidady

        #animacion del sprite en x
        if (self.temp%15)==0 :
            self.image=self.m[1][self.con]
            if self.con<14:
                self.con+=1
            else:
                self.con=13

        self.temp+=1