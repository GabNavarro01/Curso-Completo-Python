import random
import numpy as np

def crear_album(figus_total):
    A = np.zeros(figus_total, dtype = np.int64)
    return A


def album_incompleto(A):
    return min(A) == 0

def comprar_figu(figus_total):
    return random.randint(0,figus_total - 1)

def comprar_paquete(figus_total, figus_paquete):
    return [comprar_figu(figus_total) for i in range(figus_paquete)]

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] +=1
    return sum(album)


def experimento_figus(n_repeticiones, figus_total):
    resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    return np.mean(resultados)



n_repeticiones = 1000
figus_total = 6



