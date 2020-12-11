import configparser
import pygame
import random
from Bloque import Bloque
from Jugador import Jugador
from LecturaSpriteMapa import LecturaSpriteMapa
from Hongo import Hongo
from Planta import Planta
from Caracol import Caracol
from Bala import Bala
from Hongo_enemigo import Hongo_enemigo
from lib_juegos import *
import time
ANCHO=1000
ALTO=568

if __name__ == '__main__': 
    
	pygame.init()
	clock = pygame.time.Clock()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	fin=False
	fin_juego=False
	condicion3=False


	"""Cargar el archivo tmx del directorio señalado,
	crea el objeto tilerender y carga el archivo .tmx."""
	tmx_file = "data/img/mapa2.tmx"
	tile_renderer = tilerd.Renderer(tmx_file)


	"""Crea el mapa usando el metodo make_map().
	  Para ser usado en la pantalla."""
	map_surface = tile_renderer.make_map()
	fondo_alto = map_surface.get_rect()[2]
	fondo_ancho = map_surface.get_rect()[3]
	f_x = 0
	f_y = 0


	"""Creacion de los colliders. almacenados en "blockers"."""
	blockers = []
	triggers = []
	tilewidth = tile_renderer.tmx_data.tilewidth
	for tile_object in tile_renderer.tmx_data.objects:
	    properties = tile_object.__dict__
	    #print(properties)
	    #print(properties['x'], properties['x'])
	    if(properties['type'] == 'choza' or properties['type'] == 'chocita'):
	    	x = properties['x']
	    	y = properties['y']
	    	width = properties['width']
	    	height = properties['height']
	    	new_rect = pg.Rect(x, y, width, height)
	    	triggers.append(new_rect)

	    else:
	    	x = properties['x']
	    	y = properties['y']
	    	width = properties['width']
	    	height = properties['height']
	    	new_rect = pg.Rect(x, y, width, height)
	    	blockers.append(new_rect)


	fuente=pygame.font.Font(None,32)
	
	musica_fondo=pygame.mixer.Sound("./data/music/fondo.ogg")
	musica_fondo.set_volume(0.2)
	musica_fondo.play()
	tiempo=3600
	while not fin_juego and not fin:
		#gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin=True
			


		for bala in balas_mario:
			balas_hit_enemies=pygame.sprite.spritecollide(bala,all_enemies,True)
			balas_hit_generador=pygame.sprite.spritecollide(bala,all_generadores_caracoles,False)
			bloques_hit_balas=pygame.sprite.spritecollide(bala,all_bloques,False)
			for bloque_rebote in bloques_hit_balas:
				if bala.rect.right>=bloque_rebote.rect.left and bala.rect.left<=bloque_rebote.rect.right and  bala.rect.top <= bloque_rebote.rect.top:
					bala.vel_y=-bala.vel_y
					bala.contador_up=0
				if (bala.rect.right >= bloque_rebote.rect.left) and bala.rect.y>=bloque_rebote.rect.y:
					bala.vel_x=-bala.vel_x
					bala.contador_up=0
				elif (bala.rect.left <= bloque_rebote.rect.right) and bala.rect.y>=bloque_rebote.rect.y:
					bala.vel_x=-bala.vel_x
					bala.contador_up=0

			if bala.temp>=300:
				balas_mario.remove(bala)
				all_sprites.remove(bala)
			else:
				if len(balas_hit_enemies)>0 or len(balas_hit_generador)>0:
					balas_mario.remove(bala)
					all_sprites.remove(bala)
					if len(balas_hit_generador)>0:
						for generador in all_generadores_caracoles:
							if generador.salud<=0:
								all_generadores_caracoles.remove(generador)
								all_sprites.remove(generador)
							else:
								generador.salud-=20
				if bala.rect.bottom < 0 or bala.rect.bottom>568:
					balas_mario.remove(bala)
					all_sprites.remove(bala)

		temp=pygame.sprite.Group()
		for enemigo in all_enemies:
			if not enemigo.aplastado:
				temp.add(enemigo)
				
		all_enemies=temp
    	
		jugador.all_enemies=all_enemies
		jugador.all_modificadores=all_modificadores
		jugador.all_plantas=all_plantas
		
		#condiciones de fin de juego
		if jugador.f_y<-131 and jugador.vel_y>0 and (jugador.f_x<-100 and jugador.f_x>-1000):
			jugador.vida=0
			condicion3=True
		elif jugador.f_y<-500 and jugador.vel_y>0 and (jugador.f_x<-1254 and jugador.f_x>-2160):
			jugador.vida=0
			condicion3=True
		elif jugador.f_y<-745 and jugador.vel_y>0 and (jugador.f_x<-2405 and jugador.f_x>-2790):
			jugador.vida=0
			condicion3=True
    			
		if jugador.vida<=0 or (jugador.rect.x>800 and jugador.f_x==-3000) or condicion3 or tiempo<=0:
			fin_juego=True
		
		if tiempo<=0:
			jugador.vida=0

		#informacion del jugador
		info_salud='Vidas :'+str(jugador.vida)
		texto=fuente.render(info_salud,True, BLANCO)

		#informacion del tiempo
		info_tiempo='Tiempo :'+str(tiempo)
		texto2=fuente.render(info_tiempo,True, BLANCO)
		if(tiempo==500):
			musica_fondo.set_volume(0)
			alerta=pygame.mixer.Sound("./data/music/tiempo.ogg")
			alerta.play()
			musica_fondo.set_volume(0.2)

		tiempo-=1
		
		pantalla.blit(fondo,[ jugador.f_x , jugador.f_y])
		pantalla.blit(texto,[450,50])
		pantalla.blit(texto2,[800,50])
		all_sprites.update()
		all_sprites.draw(pantalla)
		pygame.display.flip()

		clock.tick(30)

	#pantalla de fin de juego
	if (jugador.vida<=0 or condicion3) or (tiempo<=0):
		musica_fondo.set_volume(0)
		jugador.sonido_herido.set_volume(0)
		perder=pygame.mixer.Sound("./data/music/perder.ogg")
		perder.play()
		time.sleep(4)
		pantalla.fill(NEGRO)
		texto=fuente.render('GAME OVER',True, ROJO)
		pantalla.blit(texto,[400,300])
		pygame.display.flip()
		hmm=pygame.mixer.Sound("./data/music/mmm.ogg")
		hmm.play()
		time.sleep(1)
	elif fin:
		pantalla.fill(NEGRO)
		pygame.display.flip()
		musica_fondo.set_volume(0)
		adios=pygame.mixer.Sound("./data/music/mama-mia.ogg")
		adios.play()
		time.sleep(2)
	else:
		musica_fondo.set_volume(0)
		musica_ganar=pygame.mixer.Sound("./data/music/ganar.ogg")
		musica_ganar.play()
		time.sleep(7)
		fuego=pygame.mixer.Sound("./data/music/fuegos.ogg")
		for i in range(3):
			fuego.play()
			time.sleep(0.55)
		pantalla.fill(NEGRO)
		texto=fuente.render('YOU WIN',True, VERDE)
		pantalla.blit(texto,[450,300])
		pygame.display.flip()
		adios_g=pygame.mixer.Sound("./data/music/yes.ogg")
		adios_g.play()
		time.sleep(1)
	
	while not fin:
    	#gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin=True
