import pygame 

class Bala(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("./data/img/fuego.png")
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vel_x=0
        self.vel_y=0
        self.temp=0
        self.contador_up=0

    def gravedad(self,cte):
        if self.vel_y==0:
            self.vel_y=1
        else:
            self.vel_y+=cte

    def update(self):
        self.temp+=1
        if self.vel_y==-1:
            self.contador_up+=1
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        if self.vel_y==-1 and (self.contador_up%30==0):
            self.vel_y=1
        if self.vel_y == 0 and self.vel_x!=0:
            self.gravedad(0.5)