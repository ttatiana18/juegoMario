import pygame
from lib_juegos import *

LIMITE_IZ = 90
LIMITE_DER = 900
LIMITE_SUP = 100
LIMITE_INF = 484
class Caracol(pygame.sprite.Sprite):
    def __init__(self,all_bloques, pos):
        super().__init__()
        self.m=Recorte("./data/img/enemies.png",15,12)
        self.con_ini=7
        self.con_final=0
        self.image=self.m[7][self.con_ini]
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.all_b_sprite=all_bloques
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_x = 0
        self.vel_y = 0
        self.temp=0
        self.aplastado=False

    def gravedad(self,cte):
        if self.vel_y==0:
            self.vel_y=1
        else:
            self.vel_y+=cte

    def update(self,velocidadx=0,velocidady=0):
        self.temp+=1

        self.rect.y += self.vel_y+ velocidady
        bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
        for bloque in bloque_hit_list:
            if self.vel_y > 0: 
                if (self.rect.bottom > (bloque.rect.top-20)) and (self.rect.bottom < (bloque.rect.top+20)):
                    self.rect.bottom=bloque.rect.top
                    self.vel_y=0
        self.rect.x += self.vel_x + velocidadx
        bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
        for bloque in bloque_hit_list:
            if self.vel_x==0:
                if (self.rect.top<=bloque.rect.bottom) and (self.rect.left<=bloque.rect.right) and self.rect.x>bloque.rect.x:
                    self.rect.left=bloque.rect.right
                    self.vel_x+=2
                elif (self.rect.top<=bloque.rect.bottom)and (self.rect.right>=bloque.rect.left):
                    self.rect.right=bloque.rect.left
            elif self.vel_x > 0: 
                if (self.rect.top<=bloque.rect.bottom)and (self.rect.right>=bloque.rect.left): 
                    self.rect.right = bloque.rect.left
                    self.vel_x=-self.vel_x
            elif self.vel_x<0: 
                if (self.rect.top<=bloque.rect.bottom)and (self.rect.left<=bloque.rect.right):
                    self.rect.left = bloque.rect.right
                    self.vel_x=-self.vel_x

        self.image=self.m[7][self.con_ini] #aqui se cambia el sprite
        #animacion del sprite en x
        if (self.temp%2)==0 and self.vel_x !=0 :
            if self.vel_x >0:
                if self.con_ini<6:
                    self.con_ini+=1
                else:
                    self.con_ini=5
            else:
                if self.con_ini<4:
                    self.con_ini+=1
                else:
                    self.con_ini=3

        #animacion del sprite en y
        if self.vel_y !=0:
            self.con_ini=7

            
        self.gravedad(0.5)
    
    def eliminar(self,grupo):
        self.remove(grupo)
    def parar(self):
        self.vel_x==0
