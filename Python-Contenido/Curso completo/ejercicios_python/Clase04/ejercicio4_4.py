# -*- coding: utf-8 -*-

#%% Ejercicio 4.3: Búsquedas de un elemento
    
def buscar_u_elemento(lista, u):
    # Devuelve la posición del último elemento u que encuentre 
    pos = -1
    i = 0
    while i < len(lista):
        if lista[i] == u:
            pos = i
        i += 1
    return pos

def buscar_n_elemento(lista, n):
    # Devuelve la cantidad de veces que encuentra al elemento n
    n_veces = 0
    i = 0
    while i < len(lista):
        if lista[i] == n:
            n_veces += 1 
        i += 1
    return n_veces

#%% Búsqueda de máximo y mínimo

# def maximo(lista):
#     '''Devuelve el máximo de una lista, 
#     la lista debe ser no vacía y de números positivos.
#     '''
#     # m guarda el máximo de los elementos a medida que recorro la lista. 
    
#     m = 0 # Lo inicializo en 0
    
#     for e in lista: # Recorro la lista y voy guardando el mayor
#         if e > m:
#             m = e
#     return m

def maximo(lista):
    #Versión mejorada
    m = lista[0]
        
    for e in lista:
        if e > m:
            m = e
    return m

def minimo(lista):
    m = lista[0]
    
    for e in lista:
        if e < m:
            m = e
    return m