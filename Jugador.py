import pygame
from lib_juegos import *

LIMITE_IZ = 90
LIMITE_DER = 850
LIMITE_SUP = 50
LIMITE_INF = 484
class Jugador(pygame.sprite.Sprite):
	"""docstring for Nave"""
	def __init__(self, all_b_sprite, all_enemies,all_enemies_caracol,all_plantas,all_plantas_enemies, pos_fondo, info_ventana, info_fondo):
		super().__init__()
		self.m=Recorte("./data/img/mario_1.png",26,5)
		self.m2=Recorte("./data/img/mario_2.png",26,1)
		self.m3=Recorte("./data/img/mario_3.png",17,1)
		self.sonido_saltar = pygame.mixer.Sound("./data/music/salto.ogg")
		self.sonido_herido = pygame.mixer.Sound("./data/music/herido.ogg")
		self.sonido_matar_enemigo = pygame.mixer.Sound("./data/music/matar.ogg")
		self.sabana=self.m
		self.con_ini=14
		self.con_final=0
		self.num_sprites=2
		self.dir=1
		self.fila=0
		self.image=self.sabana[self.fila][self.con_ini]
		self.image.set_colorkey((0,0,0))
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 400
		self.all_b_sprite = all_b_sprite
		self.all_enemies=all_enemies
		self.all_plantas=all_plantas
		self.all_plantas_enemies=all_plantas_enemies
		self.all_enemies_caracol=all_enemies_caracol
		self.all_modificadores=[]
		self.ancho=info_ventana[0]
		self.alto=info_ventana[1]
		self.f_ancho=info_fondo[0]
		self.f_alto=info_fondo[1]
		self.vel_x = 0
		self.vel_y = 5
		self.f_vel_x = 0 #velocidad del fondo
		self.b_vel_x = 0 #velocidad de los bloques que sirven para todos los sprites
		self.f_vel_y = 0
		self.b_vel_y = 0
		self.f_x = pos_fondo[0]
		self.f_y = pos_fondo[1]
		self.saltar=False
		self.vida=500
		self.estado=0
		self.muerto=False
		self.colisionando_v=False 
		self.cambio=False
		self.limite_derecho=850

	def gravedad(self,cte):
		if self.vel_y==0:
			self.vel_y=1
		else:
			self.vel_y+=cte

	def update(self):
    		

		if self.vida<=0 and not self.muerto:
			self.image=pygame.image.load("./data/img/marioMuerto.png")
			self.image.set_colorkey((0,0,0))
			self.rect.y-=30
			self.muerto=True
			self.vida-=1
    		    		
		#movimiento horizontal
		if self.rect.x < LIMITE_IZ:
			self.rect.x = LIMITE_IZ
			self.b_vel_x=(-self.vel_x)
			self.f_vel_x = -self.vel_x
		if self.rect.x > self.limite_derecho:
			self.rect.x = self.limite_derecho
			self.b_vel_x=(-self.vel_x)
			self.f_vel_x = -self.vel_x

		if self.vel_x!=0 and (self.rect.x==LIMITE_IZ or self.rect.x==self.limite_derecho):
			if ((self.f_x+self.f_vel_x) < 0) and  (self.f_x+self.f_vel_x>self.ancho-self.f_ancho): #condicion para que se muevan dentro del tamaño del fondo
				self.all_b_sprite.update(self.b_vel_x)
				self.f_x +=self.f_vel_x
				self.all_enemies.update(self.b_vel_x)
				self.all_enemies_caracol.update(self.b_vel_x)
				self.all_plantas.update(self.b_vel_x)
				self.all_plantas_enemies.update(self.b_vel_x)
			elif ((self.f_x+self.f_vel_x) >= (self.ancho-self.f_ancho)) and self.f_x!=0:
				self.all_b_sprite.update(self.b_vel_x)
				self.f_x +=self.f_vel_x
				self.all_enemies.update(self.b_vel_x)
				self.all_enemies_caracol.update(self.b_vel_x)
				self.all_plantas.update(self.b_vel_x)
				self.all_plantas_enemies.update(self.b_vel_x)

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
				self.all_enemies.update(0,self.b_vel_y)
				self.all_enemies_caracol.update(0,self.b_vel_y)
				self.all_plantas.update(0,self.b_vel_y)
				self.all_plantas_enemies.update(0,self.b_vel_y)
			elif ((self.f_y+self.f_vel_y) < 0) and (self.f_y>self.alto-self.f_alto):
				self.all_b_sprite.update(0,self.b_vel_y)
				self.f_y +=self.f_vel_y
				self.all_enemies.update(0,self.b_vel_y)
				self.all_enemies_caracol.update(0,self.b_vel_y)
				self.all_plantas.update(0,self.b_vel_y)
				self.all_plantas_enemies.update(0,self.b_vel_y)
		

		self.rect.y += self.vel_y
		bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
		for bloque in bloque_hit_list:
			if bloque.tipo_b==3:
				self.vida-=5
				self.sonido_herido.play()
			if bloque.tipo_b==4:
				self.vida=0
				self.sonido_herido.play()
			if self.vel_y > 0: 
				if ((self.rect.bottom > (bloque.rect.top-20)) and (self.rect.bottom < (bloque.rect.top+20))) or (self.rect.bottom > (bloque.rect.top-40)) and (self.rect.bottom < (bloque.rect.top+40)):
					self.rect.bottom=bloque.rect.top
					self.vel_y=0
					self.saltar=False
			elif self.vel_y < 0:
				if self.rect.top < bloque.rect.bottom:
					self.rect.top = bloque.rect.bottom
					self.vel_y=0
					bloque.golpear()

		if not self.muerto:
			self.rect.x += self.vel_x
			bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)
			for bloque in bloque_hit_list:
				if self.vel_x==0:
					if (self.rect.top<=bloque.rect.bottom) and (self.rect.left<=bloque.rect.right) and self.rect.x>bloque.rect.x:
						self.rect.left=bloque.rect.right
						self.colisionando_v=True
					elif (self.rect.top<=bloque.rect.bottom)and (self.rect.right>=bloque.rect.left):
						self.rect.right=bloque.rect.left
						self.colisionando_v=True
				elif self.vel_x >0: 
					if (self.rect.top<=bloque.rect.bottom)and (self.rect.right>=bloque.rect.left):
						self.rect.right = bloque.rect.left
						self.vel_x=0
				elif self.vel_x<0: 
					if (self.rect.top<=bloque.rect.bottom)and (self.rect.left<=bloque.rect.right):
						self.rect.left = bloque.rect.right
						self.vel_x=0

		modificador_hit_list = pygame.sprite.spritecollide(self, self.all_modificadores, True)
		for modificador in modificador_hit_list:
			self.cambio=True
			if modificador.tipo==1:
				self.fila=0
				self.estado=1
				modificador.sonar()
			elif modificador.tipo==2:
				self.vida+=100
				modificador.sonar()
			elif modificador.tipo==3:
				self.fila=0
				if self.dir==1:
					self.con_ini=10
				else:
					self.con_ini=6
				self.con_final=0
				self.estado=2
				self.rect.bottom=modificador.rect.top
				modificador.sonar()

		enemies_hit_list = pygame.sprite.spritecollide(self, self.all_enemies, False)
		for enemigo in enemies_hit_list:
			if (self.rect.bottom<enemigo.rect.top+10) and not self.muerto:
				enemigo.aplastado=True
				self.sonido_matar_enemigo.play()
			elif (self.rect.right >= enemigo.rect.left or self.rect.left <= enemigo.rect.right) and not self.muerto:
				self.sonido_herido.play()
				if(self.rect.right >= enemigo.rect.left and self.rect.x<enemigo.rect.x):
					self.rect.right = enemigo.rect.left
					self.vel_x = 0
					if self.colisionando_v:
						enemigo.rect.left=self.rect.right
						enemigo.vel_x=2
						self.colisionando_v=False
				elif (self.rect.left <= enemigo.rect.right and self.rect.x>enemigo.rect.x):
					self.rect.left = enemigo.rect.right
					self.vel_x = 0
					if self.colisionando_v:
						enemigo.rect.right=self.rect.left
						enemigo.vel_x=-2
						self.colisionando_v=False
				if self.estado==0:
					self.vida-=10
				elif self.estado==1:
					self.estado=0
					self.vida-=5
				elif self.estado==2:
					self.estado=1
					self.vida-=2

		enemies_caracoles_hit_list = pygame.sprite.spritecollide(self, self.all_enemies_caracol, False)
		for enemigo in enemies_caracoles_hit_list:
			if not self.muerto:
				self.sonido_herido.play()
				if(self.rect.right >= enemigo.rect.left and self.rect.x<enemigo.rect.x):
					self.rect.right = enemigo.rect.left
					self.vel_x = 0
					if self.colisionando_v:
						enemigo.rect.left=self.rect.right
						enemigo.vel_x=2
						self.colisionando_v=False
				elif (self.rect.left <= enemigo.rect.right and self.rect.x>enemigo.rect.x):
					self.rect.left = enemigo.rect.right
					self.vel_x = 0
					if self.colisionando_v:
						enemigo.rect.right=self.rect.left
						enemigo.vel_x=-2
						self.colisionando_v=False
				elif(self.rect.top>=enemigo.rect.bottom and (self.rect.x==enemigo.rect.x)):
					enemigo.rect.bottom=self.rect.top
				if self.estado==0:
					self.vida-=10
				elif self.estado==1:
					self.estado=0
					self.vida-=5
				elif self.estado==2:
					self.estado=1
					self.vida-=2
		

		enemies_plantas_hit_list = pygame.sprite.spritecollide(self, self.all_plantas_enemies, False)
		for enemigo in enemies_plantas_hit_list:
			if not self.muerto:
				self.sonido_herido.play()
				if(self.rect.right >= enemigo.rect.left and self.rect.x<enemigo.rect.x):
					self.rect.right = enemigo.rect.left
					self.vel_x = 0
				elif (self.rect.left <= enemigo.rect.right and self.rect.x>enemigo.rect.x):
					self.rect.left = enemigo.rect.right
					self.vel_x = 0
				elif(self.rect.top>=enemigo.rect.bottom and (self.rect.x==enemigo.rect.x)):
					enemigo.rect.bottom=self.rect.top
				if self.estado==0:
					self.vida-=10
				elif self.estado==1:
					self.estado=0
					self.vida-=5
				elif self.estado==2:
					self.estado=1
					self.vida-=2

		
		
		if self.estado==0:
			self.sabana=self.m
			self.rect[2]=24
			self.rect[3]=27
			self.num_sprites=2
			self.cambio=False
		elif self.estado==1:
			self.sabana=self.m2
			self.rect[2]=24
			self.rect[3]=51
			self.num_sprites=2
			if self.cambio:
				self.rect.y-=50
			self.cambio=False
		else:
			self.sabana=self.m3
			self.rect[2]=38
			self.rect[3]=56
			self.num_sprites=1
			self.cambio=False
    		

		if not self.muerto:		
			self.image=self.sabana[self.fila][self.con_ini] #aqui se cambia el sprite
			#animacion del sprite en x
			if self.vel_x !=0 :
				if self.con_ini<self.con_final:
					self.con_ini+=self.num_sprites
				else:
					self.con_ini-=self.num_sprites
			else:
				if self.dir==1:
					if self.estado==1 or self.estado==0:
						self.con_ini=14
					else:
						self.con_ini=10
				else: 
					if self.estado==1 or self.estado==0:
						self.con_ini=12
					else:
						self.con_ini=6

			#animacion del sprite en y
			if self.vel_y !=0:
				if self.dir==1:
					if self.estado==1 or self.estado==0:
						self.image=self.sabana[self.fila][24]
					else:
						self.image=self.sabana[self.fila][15]
				elif self.dir==2:
					if self.estado==1 or self.estado==0:
						self.image=self.sabana[self.fila][2]
					else:
						self.image=self.sabana[self.fila][1]


		self.gravedad(1)

	def sonidoSaltar(self):
		self.sonido_saltar.set_volume(0.3)
		self.sonido_saltar.play()

