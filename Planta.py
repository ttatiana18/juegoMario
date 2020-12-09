import pygame
from lib_juegos import *

class Planta(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.m=Recorte("./data/img/elementos2.png",36,15)
        self.image=self.m[2][0]
        self.sonido= pygame.mixer.Sound("./data/music/crecer.ogg")
        self.tipo=3
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

    def sonar(self):
        self.sonido.play()


