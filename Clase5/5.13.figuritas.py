import random
import numpy as np

def crear_album(figus_total):
    A = np.zeros(figus_total, dtype = np.int64)
    return A


def album_incompleto(A):
    return min(A) == 0

def comprar_figu(figus_total):
    return random.randint(0,figus_total - 1)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] +=1

    return sum(album)