import pygame

class Bloque(pygame.sprite.Sprite):
	"""docstring for Meteoro"""
	def __init__(self, b_sprite, pos):
		super().__init__()
		self.image = b_sprite.convert()
		self.image.set_colorkey( (0,0,0) )
		self.rect = self.image.get_rect()
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def update(self, velocidad=0):
		self.rect.x += velocidad