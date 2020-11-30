import pygame

VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
AMARILLO=[255,255,0]
AZUL_2=[0,255,255]
NEGRO=[0,0,0]
BLANCO=[255,255,255]

def Recorte(nom_img,ob_an,ob_al):
    terreno=pygame.image.load(nom_img)
    info=terreno.get_rect()
    print(info)
    #parametros: posicion x, posicion y, ancho corte, alto corte
    an_t=info[2] #ancho de la imagen
    al_t=info[3] #alto de la imagen
    ancho_sp=int(an_t/ob_an)
    alto_sp=int(al_t/ob_al)
    
    ls_t=[]
    for fila in range(ob_al):
        ls_fila=[]
        for col in range(ob_an):
            cuadro=terreno.subsurface(col*ancho_sp,fila*alto_sp,ancho_sp,alto_sp)
            ls_fila.append(cuadro)
        ls_t.append(ls_fila)
    
    return ls_t
