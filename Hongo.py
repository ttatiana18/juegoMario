import pygame
from lib_juegos import *

LIMITE_IZ = 90
LIMITE_DER = 900
LIMITE_SUP = 100
LIMITE_INF = 484
class Hongo(pygame.sprite.Sprite):
    def __init__(self,all_bloques, pos, tipo):
        super().__init__()
        self.m=Recorte("./data/img/elementos2.png",36,15)
        if tipo==1:
            self.image=self.m[0][0]
        else:
            self.image=self.m[0][1]
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.all_b_sprite=all_bloques
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_x = 5
        self.vel_y = 0
        self.tipo = tipo

    def gravedad(self,cte):
        if self.vel_y==0:
            self.vel_y=1
        else:
            self.vel_y+=cte

    def update(self):
                        
        self.rect.x += self.vel_x
        bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
        for bloque in bloque_hit_list:
            if self.vel_x > 0: 
                print('aqui entro el hongo')
                if self.rect.right > bloque.rect.left and (self.rect.top<bloque.rect.bottom and self.rect.top>bloque.rect.top):
                    print('por aqui',self.rect.bottom,'--',self.rect.top,'--',bloque.rect.bottom,'--',bloque.rect.top)
                    self.rect.right = bloque.rect.left
                    self.vel_x=-5
            elif self.vel_x<0: 
                if self.rect.left < bloque.rect.right:
                    self.rect.left = bloque.rect.right
                    self.vel_x=5

        self.rect.y += self.vel_y
        bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
        for bloque in bloque_hit_list:
            if self.vel_y > 0: 
                if self.rect.bottom > bloque.rect.top:
                    self.rect.bottom=bloque.rect.top
                    self.vel_y=0
                    self.saltar=False
            elif self.vel_y < 0:
                if self.rect.top < bloque.rect.bottom:
                    self.rect.top = bloque.rect.bottom
                    self.vel_y=0
            
        self.gravedad(1)
