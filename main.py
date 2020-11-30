import configparser
import pygame
import random
from Bloque import Bloque
from Jugador import Jugador
from LecturaSpriteMapa import LecturaSpriteMapa

ANCHO=1000
ALTO=568

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
	f_y = 0

	jugador = Jugador(all_bloques, [f_x, f_y], [ANCHO,ALTO],[fondo_ancho,fondo_alto])
	all_sprites.add(jugador)

	while not fin :
		#gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin=True
			if event.type == pygame.KEYDOWN:
				print("Evento key Down: ",event.key)
				if event.key == pygame.K_RIGHT:
					if jugador.estado==0:
						jugador.con_ini=14
						jugador.con_final=20
					jugador.vel_x = 5
					jugador.dir=1
				if event.key == pygame.K_LEFT:
					if jugador.estado==0:
						jugador.con_ini=12
						jugador.con_final=7
					jugador.vel_x = -5
					jugador.dir=2
				if event.key == pygame.K_UP:
					if not(jugador.saltar):
						jugador.vel_y = -14
						jugador.saltar=True

			if event.type == pygame.KEYUP:
				print("Evento key UP: ",event.key)
				jugador.con_final=0
				if event.key == pygame.K_RIGHT and jugador.vel_x != 0 :
					jugador.vel_x = 0
					jugador.f_vel_x = 0
					if jugador.estado==0:
						jugador.con_ini=14
				if event.key == pygame.K_LEFT and jugador.vel_x != 0 :
					jugador.vel_x = 0
					jugador.f_vel_x = 0
					if jugador.estado==0:
						jugador.con_ini=12
				if event.key != pygame.K_UP:
					jugador.vel_x=0
				if event.key == pygame.K_UP and jugador.vel_x>0:
					if jugador.estado==0:
						jugador.con_ini=14
						jugador.con_final=20
					jugador.vel_y = 0
					jugador.f_vel_y = 0
				if event.key == pygame.K_UP and jugador.vel_x<0:
					if jugador.estado==0:
						jugador.con_ini=12
						jugador.con_final=7
					jugador.vel_y = 0
					jugador.f_vel_y = 0

		pantalla.blit(fondo,[ jugador.f_x , jugador.f_y])
		all_sprites.update()
		all_sprites.draw(pantalla)
		pygame.display.flip()

		clock.tick(30)
