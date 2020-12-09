import pygame
import random
class Generador_hongos(pygame.sprite.Sprite):
    def __init__(self, b_sprite, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=b_sprite
        self.image.set_colorkey((0,0,0))
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.temp=400
        self.cont=0
        self.vel_y=0
        self.vel_x=0
        self.tipo_b=2

    def update(self, velocidad=0,velocidady=0):
        self.vel_x=velocidad
        self.rect.x += velocidad
        if velocidady==0:
            self.rect.y += self.vel_y
        else:
            self.rect.y += velocidady

        self.temp-=1

    def golpear(self):
        pass