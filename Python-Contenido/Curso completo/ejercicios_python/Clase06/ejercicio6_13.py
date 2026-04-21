# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:22:13 2021

@author: Yamila
"""
#%% Función original de la sección 4.2
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

#%% Ejercicio 6.13

def busqueda_lineal_lordenada(lista,e):
    '''Recibe una lista ordenada y devuelve la posición del 1ª elemento
    mayor que e. Sino, devuelve -1.'''
    pos = -1
    for i, element in enumerate(lista):
        if element > e:
            pos = i
            break
    return pos