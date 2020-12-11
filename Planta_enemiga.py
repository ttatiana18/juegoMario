import pygame
from lib_juegos import *

class Planta_enemiga(pygame.sprite.Sprite):
    def __init__(self, pos,color):
        super().__init__()
        self.color=color
        self.m=Recorte("./data/img/enemies.png",15,8)
        if color == 1:
            self.fila=1
            self.con=13
            self.m=Recorte("./data/img/enemies.png",15,8)
        elif color == 2:
            self.fila=0
            self.con=0
            self.m=Recorte("./data/img/planta.png",2,1)
        self.temp=0
        self.image=self.m[self.fila][self.con]
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
            self.image=self.m[self.fila][self.con]
            if self.color==1:
                if self.con<14:
                    self.con+=1
                else:
                    self.con=13
            else:
                if self.con<1:
                    self.con+=1
                else:
                    self.con=0

        self.temp+=1