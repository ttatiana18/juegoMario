import pygame
from lib_juegos import *

LIMITE_IZ = 90
LIMITE_DER = 900
LIMITE_SUP = 100
LIMITE_INF = 484
class Hongo_enemigo(pygame.sprite.Sprite):
    def __init__(self,all_bloques, pos,color):
        super().__init__()
        self.m=Recorte("./data/img/enemies.png",16,12)
        self.con=0
        if color == 1:
            self.fila=0
        elif color == 2:
            self.fila=1
        self.image=self.m[self.fila][self.con]
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.all_b_sprite=all_bloques
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel_x = 2
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
        if not self.aplastado:

            bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
            for bloque in bloque_hit_list:
                if self.vel_y > 0: 
                    if (self.rect.bottom > (bloque.rect.top-10)) and (self.rect.bottom < (bloque.rect.top+10)):
                        self.rect.bottom=bloque.rect.top
                        self.vel_y=0

            self.rect.x += self.vel_x + velocidadx
            bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
            for bloque in bloque_hit_list:
                if self.vel_x > 0: 
                    if (self.rect.top<=bloque.rect.bottom)and (self.rect.right>=bloque.rect.left): 
                        self.rect.right = bloque.rect.left
                        self.vel_x=-self.vel_x
                elif self.vel_x<0: 
                    if (self.rect.top<=bloque.rect.bottom)and (self.rect.left<=bloque.rect.right):
                        self.rect.left = bloque.rect.right
                        self.vel_x=-self.vel_x

        #animacion del sprite en x
        if self.aplastado:
            self.image=self.m[self.fila][2]
            self.vel_x=0
            self.vel_y=10
        else:
            if (self.temp%6)==0 and self.vel_x!=0:
                self.image=self.m[self.fila][self.con]
                if self.con<1:
                    self.con+=1
                else:
                    self.con=0

            
        self.gravedad(0.5)
    
    def eliminar(self,grupo):
        self.remove(grupo)
    def parar(self):
        self.vel_x==0

