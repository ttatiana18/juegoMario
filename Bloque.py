import pygame
 
class Bloque(pygame.sprite.Sprite):
	"""docstring for Meteoro"""
	def __init__(self, b_sprite, pos):
		super().__init__()
		self.image = b_sprite.convert()
		self.image.set_colorkey( (0,0,0) )
		self.rect = self.image.get_rect()
		self.tipo_b=0
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.vel_y=0
		self.golpeada=False

	def gravedad(self,cte):
		if self.vel_y==0:
			self.vel_y=1
		else:
			self.vel_y+=cte

	def update(self, velocidad=0,velocidady=0):
		self.rect.x += velocidad
		if velocidady==0:
			self.rect.y += self.vel_y
		else:
			self.rect.y += velocidady
		if self.golpeada:
			self.gravedad(0.5)
			if self.vel_y>2.5:
				self.vel_y=0
				self.golpeada=False

	def golpear(self):
		self.vel_y=-2
		self.golpeada=True