import configparser
import pygame
from Bloque import Bloque
from Bloque_especial import Bloque_especial
from Generador_hongos import Generador_hongos
from Generador_caracol import Generador_caracol

class LecturaSpriteMapa():

	def __init__(self, nombre_archivo):
		# Cargando datos del archivo
		archivo=configparser.ConfigParser()
		archivo.read('./data/img/'+nombre_archivo)
		name_archivo = archivo.get('info','imagen')
		mapa = archivo.get('info','mapa')
		self.filas_mapa = mapa.split('\n')
		name_sprites = archivo.sections()
		name_sprites.remove('info')

		print("name_archivo: ", name_archivo)
		print("name_sprites: ", name_sprites)

		# Iniciando Libreria Grafica
		pygame.init()

		plantilla_sprite=pygame.image.load('./data/img/'+name_archivo)
		info=plantilla_sprite.get_rect()
		print("Shape plantilla: ",info)

		#parametros: posicion x, posicion y, ancho corte, alto corte
		an_plantilla=info[2]
		al_plantilla=info[3]

		cant_obj_ancho = archivo.get('info','can_ancho')
		cant_obj_alto = archivo.get('info','can_alto')

		self.an_sprites = an_plantilla / int(cant_obj_ancho)
		self.al_sprites = al_plantilla / int(cant_obj_alto)
		print('ancho sprite: ', self.an_sprites)
		print('alto sprite: ', self.al_sprites)

		self.lista_obj_sprite = {}
		for objeto in name_sprites:
			fila = int(archivo.get(objeto,'fil'))
			columna = int(archivo.get(objeto,'col'))
			ancho = int(archivo.get(objeto,'ancho'))
			alto = int(archivo.get(objeto,'alto'))
			self.lista_obj_sprite[objeto] = plantilla_sprite.subsurface(columna*self.an_sprites,fila*self.al_sprites,ancho*self.an_sprites,alto*self.al_sprites)

	def cargarObjetosMapa(self):
		indice_col = 0
		indice_fil = 0
		all_bloque_sprites = pygame.sprite.Group()
		all_sprites = pygame.sprite.Group()
		all_generadores_caracoles = pygame.sprite.Group()
		for fil_m in self.filas_mapa:
			for dato in fil_m:
				if dato=="b" or dato=="T" or dato=="a": # Condicion para definir los elementos Bloque (piedas, palmas, tubos)
					bloque = Bloque(self.lista_obj_sprite[dato], [indice_col*self.an_sprites, indice_fil*self.al_sprites])
					all_bloque_sprites.add(bloque)
					all_sprites.add(bloque)
				if dato=="e": # bloque especial con los 3 modificadores
					bloque_e= Bloque_especial([indice_col*self.an_sprites, indice_fil*self.al_sprites])
					all_bloque_sprites.add(bloque_e)
					all_sprites.add(bloque_e)
				if dato=="G": # generador de hongos
					generador= Generador_hongos(self.lista_obj_sprite[dato],[indice_col*self.an_sprites, indice_fil*self.al_sprites])
					all_bloque_sprites.add(generador)
					all_sprites.add(generador)
				if dato=="C": # generador de caracoles
					generador2= Generador_caracol([600,100])
					all_generadores_caracoles.add(generador2)
					all_sprites.add(generador2)
				indice_col += 1
			indice_fil += 1
			indice_col = 0

		return all_sprites, all_bloque_sprites, all_generadores_caracoles