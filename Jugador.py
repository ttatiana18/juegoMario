import pygame
from lib_juegos import *

LIMITE_IZ = 90
LIMITE_DER = 900
LIMITE_SUP = 100
LIMITE_INF = 484
class Jugador(pygame.sprite.Sprite):
	"""docstring for Nave"""
	def __init__(self, all_b_sprite, pos_fondo, info_ventana, info_fondo):
		super().__init__()
		self.m=Recorte("./data/img/mario.png",26,12)
		self.con_ini=14
		self.con_final=0
		self.dir=1
		self.image=self.m[0][self.con_ini]
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 400
		self.all_b_sprite = all_b_sprite
		self.ancho=info_ventana[0]
		self.alto=info_ventana[1]
		self.f_ancho=info_fondo[0]
		self.f_alto=info_fondo[1]
		self.vel_x = 0
		self.vel_y = 5
		self.f_vel_x = 0
		self.b_vel_x = 0
		self.f_vel_y = 0
		self.b_vel_y = 0
		self.f_x = pos_fondo[0]
		self.f_y = pos_fondo[1]
		self.saltar=False
		self.vidas=3
		self.estado=0

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
			if ((self.f_x+self.f_vel_x) < 0) and  (self.f_x+self.f_vel_x>self.ancho-self.f_ancho): #condicion para que se muevan dentro del tamaño del fondo
				self.all_b_sprite.update(self.b_vel_x)
				self.f_x +=self.f_vel_x
			elif ((self.f_x+self.f_vel_x) >= (self.ancho-self.f_ancho)) and self.f_x!=0:
				self.all_b_sprite.update(self.b_vel_x)
				self.f_x +=self.f_vel_x

		#movimiento vertical
		if self.rect.y < LIMITE_SUP:
			self.rect.y = LIMITE_SUP
			self.b_vel_y=-self.vel_y
			self.f_vel_y = -self.vel_y
		if self.rect.y > LIMITE_INF:
			self.rect.y = LIMITE_INF
			self.b_vel_y=-self.vel_y
			self.f_vel_y =-self.vel_y

		if self.vel_y!=0 and (self.rect.y==LIMITE_SUP or self.rect.y==LIMITE_INF):
			if ((self.f_y+self.f_vel_y) > self.alto-self.f_alto) and self.f_y<=0: #condicion para que se muevan dentro del tamaño del fondo
				self.all_b_sprite.update(0,self.b_vel_y)
				self.f_y +=self.f_vel_y
			elif ((self.f_y+self.f_vel_y) < 0) and (self.f_y>self.alto-self.f_alto):
				self.all_b_sprite.update(0,self.b_vel_y)
				self.f_y +=self.f_vel_y
		
		self.rect.x += self.vel_x
		bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
		for bloque in bloque_hit_list:
			if self.vel_x > 0 and self.vel_y==0: 
				if self.rect.right > bloque.rect.left:
					self.rect.right = bloque.rect.left
					self.vel_x=0
			elif self.vel_x<0: 
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

		self.image=self.m[0][self.con_ini] #aqui se cambia el sprite
		#animacion del sprite en x
		if self.vel_x !=0 :
			if self.con_ini<self.con_final:
				self.con_ini+=2
			else:
				self.con_ini-=2
		else:
			if self.dir==1:
				self.con_ini=14
			else: 
				self.con_ini=12

		#animacion del sprite en y
		if self.vel_y !=0:
			if self.dir==1:
				self.image=self.m[0][24]
			elif self.dir==2:
				self.image=self.m[0][2]
			


		self.gravedad(1)

