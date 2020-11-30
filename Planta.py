import pygame
from lib_juegos import *

class Planta(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.m=Recorte("./data/img/elementos2.png",36,15)
        self.image=self.m[2][0]
        self.tipo=3
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
