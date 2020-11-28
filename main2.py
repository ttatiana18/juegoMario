import configparser
import pygame
import random
from lib_juegos import *

f_x = 0
f_y = -132

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

class Jugador(pygame.sprite.Sprite):
    """docstring for Nave"""
    def __init__(self, all_b_sprite):
        super().__init__()
        self.image = pygame.image.load("C:/Users/ttati/Desktop/Mapa-v4/Mapa/img/sprite_mario_right.png").convert()
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.all_b_sprite = all_b_sprite
        self.vel_x = 0
        self.vel_y = 5

    def gravedad(self,cte):
        if self.vel_y==0:
            self.vel_y=1
        else:
            self.vel_y+=cte

    def update(self):
        global f_x
        if self.rect.x < 10:
            self.rect.x = 10
        if self.rect.x > 850:
            self.rect.x = 850
        if self.rect.y > 600:
            self.rect.y = -64

        self.rect.x += self.vel_x
        if self.vel_x!=0 and (self.rect.x<150 or self.rect.x>850):
            print("Reajuste Bloques: ",self.all_b_sprite)
            self.all_b_sprite.update(-self.vel_x)
            f_x += -self.vel_x

        self.rect.y += self.vel_y
        bloque_hit_list = pygame.sprite.spritecollide(self, self.all_b_sprite, False)	
        for bloque in bloque_hit_list:
            if self.vel_y > 0: 
                if self.rect.bottom > bloque.rect.top:
                    self.rect.bottom = bloque.rect.top
                    self.vely=0
            else: 
                if self.rect.top < bloque.rect.bottom:
                    self.rect.top = bloque.rect.bottom
                    self.vel_y=0
                    
        self.gravedad(0.5)
        '''		
        if bloque.rect.y < (self.rect.y+64):
            self.rect.y = bloque.rect.y-64
        '''

ANCHO=992
ALTO=600

if __name__ == '__main__': 
    # Cargando datos del archivo
    archivo=configparser.ConfigParser()
    archivo.read('info_mapa.txt')
    name_archivo = archivo.get('info','imagen')
    mapa = archivo.get('info','mapa')
    filas_mapa = mapa.split('/n')
    name_sprites = archivo.sections()
    name_sprites.remove('info')

    print("name_archivo: ", name_archivo)
    print("name_sprites: ", name_sprites)

    # Iniciando Libreria Grafica
    pygame.init()

    fondo=pygame.image.load('C:/Users/ttati/Desktop/Mapa-v4/Mapa/img/mapa2.png')
    info=fondo.get_rect()
    fondo_ancho=info[2]
    fondo_alto=info[3]

    plantilla_sprite=pygame.image.load('C:/Users/ttati/Desktop/Mapa-v4/Mapa/img/'+name_archivo)
    info=plantilla_sprite.get_rect()
    print("Shape plantilla: ",info)
    #parametros: posicion x, posicion y, ancho corte, alto corte
    an_plantilla=info[2]
    al_plantilla=info[3]

    cant_obj_ancho = archivo.get('info','can_ancho')
    cant_obj_alto = archivo.get('info','can_alto')

    an_sprites = an_plantilla / int(cant_obj_ancho)
    al_sprites = al_plantilla / int(cant_obj_alto)
    print('ancho sprite: ', an_sprites)
    print('alto sprite: ', al_sprites)
    
    lista_obj_sprite = {}
    for objeto in name_sprites:
        columna = int(archivo.get(objeto,'col'))
        fila = int(archivo.get(objeto,'fil'))
        lista_obj_sprite[objeto] = plantilla_sprite.subsurface(columna*an_sprites,fila*al_sprites,an_sprites,al_sprites)

    indice_col = 0
    indice_fil = 0
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    all_bloque_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    for fil_m in filas_mapa:
        for dato in fil_m:
            if dato=="#":
                bloque = Bloque(lista_obj_sprite[dato], [indice_col*an_sprites, indice_fil*al_sprites])
                all_bloque_sprites.add(bloque)
                all_sprites.add(bloque)
            elif dato=="a":
                pass
            # else:
            # 	pantalla.blit( lista_obj_sprite[dato] ,[indice_col*an_sprites, indice_fil*al_sprites])
            indice_col += 1
        indice_fil += 1
        indice_col = 0

    jugador = Jugador(all_bloque_sprites)
    jugador.rect.x = 800
    jugador.rect.y = 200
    all_sprites.add(jugador)

    clock = pygame.time.Clock()
    fin=False
    while not fin :
        #gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True


            if event.type == pygame.KEYDOWN:
                print("Evento key Down: ",event.key)
                if event.key == pygame.K_RIGHT:
                    jugador.image = pygame.image.load("C:/Users/ttati/Desktop/Mapa-v4/Mapa/img/sprite_mario_right.png").convert()
                    jugador.vel_x = 5
                if event.key == pygame.K_LEFT:
                    jugador.image = pygame.image.load("C:/Users/ttati/Desktop/Mapa-v4/Mapa/img/sprite_mario_left.png").convert()
                    jugador.vel_x = -5
                if event.key == pygame.K_UP:
                    jugador.vel_y=-10

            if event.type == pygame.KEYUP:
                print("Evento key UP: ",event.key)
                if event.key != pygame.K_UP:
                    jugador.velx=0
                if event.key == pygame.K_RIGHT and jugador.vel_x != 0 :
                    jugador.vel_x = 0
                if event.key == pygame.K_LEFT and jugador.vel_x != 0 :
                    jugador.vel_x = 0

        pantalla.fill( (0,0,0) )
        pantalla.blit(fondo,[f_x ,f_y])

        all_sprites.update()
        all_sprites.draw(pantalla)
        pygame.display.flip()

        clock.tick(60)