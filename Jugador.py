import pygame
from lib_juegos import *

LIMITE_IZ = 90
LIMITE_DER = 850
class Jugador(pygame.sprite.Sprite):
	"""docstring for Nave"""
	def __init__(self, all_b_sprite, pos_fondo, info_ventana, info_fondo):
		super().__init__()
		self.m=Recorte("./data/img/mario.png",14,10)
		#self.direccion=0
		#self.con=7
		#self.image=self.m[self.direccion][self.con]
		#self.image = pygame.image.load("./data/img/sprite_mario_right.png").convert()
		#self.image.set_colorkey((0,0,0))
		self.image=pygame.Surface([32,32])
		self.image.fill([0,255,0])
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 50
		self.all_b_sprite = all_b_sprite
		self.ancho=info_ventana[0]
		self.f_ancho=info_fondo[0]
		self.vel_x = 0
		self.vel_y = 5
		self.f_vel_x = 0
		self.b_vel_x = 0
		self.f_x = pos_fondo[0]
		self.f_y = pos_fondo[1]
		self.saltar=False

	def gravedad(self,cte):
		if self.vel_y==0:
			self.vel_y=1
		else:
			self.vel_y+=cte

	def update(self):
    		
		#movimiento horizontal
		if self.rect.x < LIMITE_IZ:
			self.rect.x = LIMITE_IZ
			self.b_vel_x=(-self.vel_x)
			self.f_vel_x = -self.vel_x
		if self.rect.x > LIMITE_DER:
			self.rect.x = LIMITE_DER
			self.b_vel_x=(-self.vel_x)
			self.f_vel_x = -self.vel_x

		if self.vel_x!=0 and (self.rect.x==LIMITE_IZ or self.rect.x==LIMITE_DER):
			if ((self.f_x+self.f_vel_x) < 0) and  (self.f_x!=self.ancho-self.f_ancho): #condicion para que se muevan dentro del tamaño del fondo
				self.all_b_sprite.update(self.b_vel_x)
				self.f_x +=self.f_vel_x
			elif ((self.f_x+self.f_vel_x) >= (self.ancho-self.f_ancho)) and self.f_x!=0:
				self.all_b_sprite.update(self.b_vel_x)
				self.f_x +=self.f_vel_x
		
		self.rect.x += self.vel_x
		bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
		for bloque in bloque_hit_list:
			if self.vel_x > 0: 
				if self.rect.right > bloque.rect.left:
					self.rect.right = bloque.rect.left
					self.vel_x=0
			else: 
				if self.rect.left < bloque.rect.right:
					self.rect.left = bloque.rect.right
					self.vel_x=0

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
					bloque.golpear()

		self.gravedad(1)

