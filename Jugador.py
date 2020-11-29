import pygame

class Jugador(pygame.sprite.Sprite):
	"""docstring for Nave"""
	def __init__(self, all_b_sprite, pos_fondo):
		super().__init__()
		self.image = pygame.image.load("./data/img/sprite_mario_right.png").convert()
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 50
		self.all_b_sprite = all_b_sprite
		self.vel_x = 0
		self.vel_y = 5
		self.f_x = pos_fondo[0]
		self.f_y = pos_fondo[1]

	def update(self):
		
		if self.rect.x < 10:
			self.rect.x = 10
		if self.rect.x > 850:
			self.rect.x = 850
		if self.rect.y > 600:
			self.rect.y = -64

		self.rect.x += self.vel_x
		self.rect.y += self.vel_y
		if self.vel_x!=0 and (self.rect.x<150 or self.rect.x>850):
			print("Reajuste Bloques: ",self.all_b_sprite)
			self.all_b_sprite.update(-self.vel_x)
			self.f_x += -self.vel_x


		bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)	
		for bloque in bloque_hit_list:
			if bloque.rect.y < (self.rect.y+64):
				self.rect.y = bloque.rect.y-64
