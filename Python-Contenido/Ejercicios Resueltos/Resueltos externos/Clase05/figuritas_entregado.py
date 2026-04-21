# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:37:23 2021

@author: Yamila
"""

import random
import numpy as np

#%% Ejercicio 5.10

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=int)
    return album

#%% Ejercicio 5.11

def album_incompleto(A):
    if min(A) == 0:
        return True
    else:
        return False
    
#%% Ejercicio 5.12

def comprar_figu(figus_total):
    figuritas = random.randint(0,figus_total - 1)
    return figuritas

#%% Ejercicio 5.13

def cuantas_figus(figus_total):
    figuritas = 0
    album = crear_album(figus_total)
    seguir_comprando = True
    while seguir_comprando:
        compra = comprar_figu(figus_total)
        figuritas += 1
        album[compra] += 1
        if album_incompleto(album) == False:
            seguir_comprando = False
    return figuritas

#%% Ejercicio 5.14

# n_repeticiones = 1000
# figus_total = 6

def repeticiones(n_repeticiones, figus_total):
    compras = [ ]
    while n_repeticiones > 0:
        compro = cuantas_figus(figus_total)
        compras.append(compro)
        n_repeticiones -= 1
    promedio = np.mean(compras)
    return promedio

#%% ejercicio 5.15

def experimento_figus(n_repeticiones, figus_total):
    compras = [ ]
    while n_repeticiones > 0:
        compro = cuantas_figus(figus_total)
        compras.append(compro)
        n_repeticiones -= 1
    promedio = np.mean(compras)
    return promedio