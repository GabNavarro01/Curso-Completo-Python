import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    A = np.zeros(figus_total, dtype = np.int64)
    return A


def album_incompleto(A):
    return min(A) == 0

def comprar_figu(figus_total):
    return random.randint(0,figus_total - 1)

def comprar_paquete(figus_total, figus_paquete):
    return [comprar_figu(figus_total) for i in range(figus_paquete)]

def comprar_paquete_sin_repetir(figus_total, figus_paquete):
    return random.sample(range(0,figus_total - 1), figus_paquete)

def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu] +=1
    return sum(album)

def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)

    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for figu in paquete:
            album[figu] +=1

    return np.sum(album) / figus_paquete

def experimento_figus(n_repeticiones, figus_total):
    resultados = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    return np.mean(resultados)

def experimento_paquetes(n_repeticiones, figus_total, figus_paquete):
    resultados = [cuantos_paquetes(figus_total,figus_paquete) for i in range(n_repeticiones)]
    np.save('../Data/paquetes.npy', resultados)
    return np.mean(resultados)

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete: #voy vaciando el paquete, y coloco un uno en dicha pos
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum() #Cantidad de posiciones que son mayores a cero, sumadas
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

def probabilidad_menos_de_n_paquetes(n_repeticiones,figus_total,figus_paquete, cant_paquetes):
    resultados = [cuantos_paquetes(figus_total,figus_paquete) for i in range(n_repeticiones)]
    
    return sum((r < cant_paquetes) for r in resultados) / n_repeticiones

def probabilidad_mayor_a(n_repeticiones,figus_total,figus_paquete):

    for i in range(800,2000):
        if probabilidad_menos_de_n_paquetes(n_repeticiones, figus_total, figus_paquete , i) >= 0.90:
            return i

n_repeticiones = 1000
figus_total = 670
figus_paquete = 5

# plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
# plt.xlabel("Cantidad de paquetes comprados.")
# plt.ylabel("Cantidad de figuritas pegadas.")
# plt.title("La curva de llenado se desacelera al final")
# plt.show()

experimento_p = experimento_paquetes(n_repeticiones, figus_total , figus_paquete)


