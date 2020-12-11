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
from FinalBoss import *
import time
ANCHO=1000
ALTO=568
#nuevo tamaño de fondo

if __name__ == '__main__': 
    
	pygame.init()
	clock = pygame.time.Clock()
	pantalla=pygame.display.set_mode([ANCHO,ALTO])
	fin=False
	fin_juego=False
	fin_inicio=False
	condicion3=False

	obj_lectura_mapa = LecturaSpriteMapa('info_mapa.txt')
	all_sprites, all_bloques, all_generadores_caracoles,all_plantas_enemies = obj_lectura_mapa.cargarObjetosMapa()

	fondo=pygame.image.load('./data/img/mapa3.png')
	tuberia=pygame.image.load('./data/img/tubo.png')
	mario_inicio=pygame.image.load('./data/img/inicio.jpg')
	mario_historia=pygame.image.load('./data/img/mario_historia.png')
	instrucciones=pygame.image.load('./data/img/instrucciones.png')
	instrucciones=pygame.transform.scale(instrucciones, (415,300))
	mario_historia=pygame.transform.scale(mario_historia, (200,340))
	inicio=pygame.transform.scale(mario_inicio, (415,205))
	fuente=pygame.font.Font(None,32)
	indicacion1='PRESIONA ENTER'
	indicacion2='PRESIONA ENTER PARA CONTINUAR'
	text_info=fuente.render(indicacion1,True, BLANCO)
	text_info2=fuente.render(indicacion2,True, BLANCO)
	info=fondo.get_rect()
	fondo_ancho=info[2]
	fondo_alto=info[3]
	f_x = 0
	f_y = 0

	pantalla.blit(fondo,[0,0])
	pantalla.blit(inicio,[300,200])
	pantalla.blit(text_info,[400,430])
	pygame.display.flip()

	while not fin_inicio:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin_inicio=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					musica_historia=pygame.mixer.Sound("./data/music/inicio.ogg")
					musica_historia.play()
					pantalla.blit(fondo,[0,0])
					pantalla.blit(mario_historia,[750,200])
					pantalla.blit(instrucciones,[300,180])
					pantalla.blit(text_info2,[300,500])
					pygame.display.flip()
					fin_inicio=True

	fin_inicio=False
	while not fin_inicio:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin_inicio=True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					pantalla.blit(fondo,[0,0])
					pygame.draw.rect(pantalla,NEGRO,(300,200,415,205))
					pygame.display.flip()
					time.sleep(3)
					fin_inicio=True
								
	musica_historia.set_volume(0)
			

	all_modificadores=pygame.sprite.Group()
	all_plantas=pygame.sprite.Group()
	all_enemies_caracol=pygame.sprite.Group()
	all_enemies=pygame.sprite.Group()
	balas_mario=pygame.sprite.Group()

	jugador = Jugador(all_bloques, all_enemies,all_enemies_caracol,all_plantas,all_plantas_enemies, [f_x, f_y], [ANCHO,ALTO],[fondo_ancho,fondo_alto])
	all_sprites.add(jugador)

	musica_fondo=pygame.mixer.Sound("./data/music/fondo.ogg")
	musica_fondo.set_volume(0)
	musica_fondo.play()
	tiempo=3600
	while not fin_juego and not fin:
		#gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin=True
			if event.type == pygame.KEYDOWN:
				tecla_presionada=pygame.key.get_pressed()
				if event.key == pygame.K_RIGHT:
					if jugador.estado==1 or jugador.estado==0:
						jugador.con_ini=14
						jugador.con_final=20
					else:
						jugador.con_ini=10
						jugador.con_final=12
					jugador.vel_x = 5
					jugador.dir=1
				if event.key == pygame.K_LEFT:
					if jugador.estado==1 or jugador.estado==0:
						jugador.con_ini=12
						jugador.con_final=7
					else:
						jugador.con_ini=6
						jugador.con_final=4
					jugador.vel_x = -5
					jugador.dir=2
				if event.key == pygame.K_UP:
					if not(jugador.saltar):
						jugador.vel_y = -14
						jugador.saltar=True
						jugador.sonidoSaltar()
				if event.key == pygame.K_x:
					if jugador.estado == 2:
						posicion=[(jugador.rect.x),jugador.rect.bottom-50]
						bala=Bala(posicion)
						if tecla_presionada[pygame.K_UP]:
							bala.vel_y=-8
						elif jugador.con_ini==10:
							bala.vel_x=4
						elif jugador.con_ini==6:
							bala.vel_x=-4
						balas_mario.add(bala)
						all_sprites.add(bala)
				if event.key == pygame.K_n:
					if tecla_presionada[pygame.K_s]:
						jugador.vida=10000
						
			if event.type == pygame.KEYUP:
				jugador.con_final=0
				if event.key == pygame.K_RIGHT and jugador.vel_x != 0 :
					jugador.vel_x = 0
					jugador.f_vel_x = 0
					if jugador.estado==1 or jugador.estado==0:
						jugador.con_ini=14
					else:
						jugador.con_ini=10
					jugador.con_final=0
				if event.key == pygame.K_LEFT and jugador.vel_x != 0 :
					jugador.vel_x = 0
					jugador.f_vel_x = 0
					if jugador.estado==1 or jugador.estado==0:
						jugador.con_ini=12
					else: 
						jugador.con_ini=6
					jugador.con_final=0
				if event.key != pygame.K_UP:
					jugador.vel_x=0
				if event.key == pygame.K_UP and jugador.vel_x>0:
					if jugador.estado==1 or jugador.estado==0:
						jugador.con_ini=14
						jugador.con_final=20
					else:
						jugador.con_ini=10
						jugador.con_final=12
					jugador.vel_y = 0
					jugador.f_vel_y = 0
				if event.key == pygame.K_UP and jugador.vel_x<0:
					if jugador.estado==1 or jugador.estado==0:
						jugador.con_ini=12
						jugador.con_final=7
					else:
						jugador.con_ini=6
						jugador.con_final=4
					jugador.vel_y = 0
					jugador.f_vel_y = 0

		for bloque_e in all_bloques:
			if bloque_e.tipo_b==1:
				if bloque_e.activa and bloque_e.golpeada:
					if bloque_e.tipo_m == 1 or bloque_e.tipo_m == 2:
						hongo=Hongo(all_bloques,[bloque_e.rect.x,bloque_e.rect.top-32],bloque_e.tipo_m)
						all_sprites.add(hongo)
						all_modificadores.add(hongo)
					else:
						planta=Planta([bloque_e.rect.x,bloque_e.rect.top-32])
						all_sprites.add(planta)
						all_modificadores.add(planta)
						all_plantas.add(planta)
					bloque_e.activa=False
			elif bloque_e.tipo_b==2:
				if bloque_e.temp<0:
					if bloque_e.cont<10:
						hongo=Hongo_enemigo(all_bloques,[bloque_e.rect.x,bloque_e.rect.y])   
						hongo.vel_x=2             
						all_enemies.add(hongo)
						all_sprites.add(hongo)
						bloque_e.temp=400
						bloque_e.cont+=1

		for enemigo_generador in all_generadores_caracoles:
			if enemigo_generador.temp<0:
				caracol=Caracol(all_bloques,[enemigo_generador.rect.x,enemigo_generador.rect.bottom])
				caracol.vel_x=2    
				all_enemies_caracol.add(caracol)
				all_sprites.add(caracol)
				enemigo_generador.temp=400

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
    			
		if jugador.vida<=0 or (jugador.rect.x>800 and jugador.f_x==-3680) or condicion3 or tiempo<=0:
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
		pygame.display.flip()
		time.sleep(2)
		jugador.rect.x=500
		jugador.rect.y=400
		for nube in all_generadores_caracoles:
			all_generadores_caracoles.remove(nube)
			all_sprites.remove(nube)
		for enemigo in all_enemies:
			all_enemies.remove(enemigo)
			all_sprites.remove(enemigo)
		for caracol in all_enemies_caracol:
			all_enemies_caracol.remove(caracol)
			all_sprites.remove(caracol)
		sonar_tuberia=True
		while jugador.f_x>-3690:
			if jugador.rect.x>870 and sonar_tuberia:
				ingresar=pygame.mixer.Sound("./data/music/tuberia.ogg")
				ingresar.play()
				sonar_tuberia=False
			jugador.vel_x=5
			jugador.limite_derecho=900
			pantalla.blit(fondo,[-4000, -708])
			all_sprites.update()
			all_sprites.draw(pantalla)
			pantalla.blit(tuberia,[870,380])
			pygame.display.flip()

			clock.tick(30)

	
	while not fin:
    	#gestion de eventos
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin=True
