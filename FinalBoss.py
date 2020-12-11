import pygame
from lib_juegos import *

class FinalEnemy(pygame.sprite.Sprite):
	"""docstring for Nave"""
	def __init__(self, all_bloques, pos):
		super().__init__()
		self.m=Recorte("./data/img/bowser.png",8,1)
		self.con=0
		self.dir = 0
		self.image=self.m[0][self.con]
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		self.all_b_sprite=all_bloques
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.vel_x = 2
		self.vel_y = 0
		self.temp = 0
		self.vivo = False
		self.limiteD=self.rect.right + 50
		self.limiteI=self.rect.left - 50

	def gravedad(self,cte):
		if self.vel_y==0:
			self.vel_y=1
		else:
			self.vel_y+=cte

	def update(self):

		if(self.rect.left<=self.limiteI):
			self.vel_x=2
		elif self.rect.right>=self.limiteD:
			self.vel_x=-2

		self.rect.x += self.vel_x
		
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

		if(self.vel_x > 0):
			self.dir = 0

		else:
			self.dir = 1


		if(self.vel_x != 0 or self.vel_y != 0):
			if self.con < 3 and (self.dir == 0):
				self.image = self.m[0][self.con+4]
				self.con += 1
			elif self.con < 3 and (self.dir == 1):
				self.image = self.m[0][self.con]
				self.con += 1

			else:
				self.con = 0


		self.gravedad(1)

	def sonidoSaltar(self):
		self.sonido_saltar.set_volume(0.3)
		self.sonido_saltar.play()

