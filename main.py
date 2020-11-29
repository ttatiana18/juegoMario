import configparser
import pygame
import random
from Bloque import Bloque
from Jugador import Jugador
from LecturaSpriteMapa import LecturaSpriteMapa

ANCHO=992
ALTO=600

if __name__ == '__main__': 
    
	pygame.init()
	clock = pygame.time.Clock()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	fin=False

	obj_lectura_mapa = LecturaSpriteMapa('info_mapa.txt')
	all_sprites, all_bloques = obj_lectura_mapa.cargarObjetosMapa()

	fondo=pygame.image.load('./data/img/mapa2.png')
	info=fondo.get_rect()
	fondo_ancho=info[2]
	fondo_alto=info[3]
	f_x = 0
	f_y = -129

	jugador = Jugador(all_bloques, [f_x, f_y] )
	all_sprites.add(jugador)

	while not fin :
	    #gestion de eventos
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            fin=True

	        if event.type == pygame.KEYDOWN:
	        	print("Evento key Down: ",event.key)
	        	if event.key == pygame.K_RIGHT:
	        		jugador.image = pygame.image.load("./data/img/sprite_mario_right.png").convert()
	        		jugador.image.set_colorkey((0,0,0))
	        		jugador.vel_x = 5
	        	if event.key == pygame.K_LEFT:
	        		jugador.image = pygame.image.load("./data/img/sprite_mario_left.png").convert()
	        		jugador.image.set_colorkey((0,0,0))
	        		jugador.vel_x = -5

	        if event.type == pygame.KEYUP:
	        	print("Evento key UP: ",event.key)
	        	if event.key == pygame.K_RIGHT and jugador.vel_x != 0 :
	        		jugador.vel_x = 0
	        	if event.key == pygame.K_LEFT and jugador.vel_x != 0 :
	        		jugador.vel_x = 0

	    pantalla.blit(fondo,[ jugador.f_x , jugador.f_y])

	    all_sprites.update()
	    all_sprites.draw(pantalla)
	    pygame.display.flip()

	    clock.tick(60)
