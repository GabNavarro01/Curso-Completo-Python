# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:57:55 2021

@author: Yamila
"""

#%% Función de la sección 6.5

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

#%% Ejercicio 6.14: Búsqueda binaria

def donde_insertar(lista, x, verbose = False):
    '''Recibe una lista ordenada y un elemento.
    Devuelve la posición de ese elemento en la lista (si se encuentra) o la
    posición donde se podrá insertar, manteniendo ordenada la lista.'''
    pos = -1
    izq = 0
    der = len(lista) - 1
    if verbose:
        print('[DEBUG] izq |der |medio')
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio # elemento encontrado!
            break
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        if izq == der:
            if lista[der] > x:
                pos = der
            if lista[der] < x:
                pos = der + 1
        if izq == medio:
            if lista[izq] > x:
                pos = izq
            if lista[izq] < x:
                pos = izq + 1
    return pos

#%% Ejercicio 6.15: Insertar un elemento en una lista

def insertar(lista, x):
    '''Recibe una lista ordenada y un elemento. Si el elemento se encuentra en
    la lista solamente devuelve su posición; si no se encuentra, lo inserta en
    la posición correcta para mantener el orden.
    En este segundo caso, también devuelve su posición.'''
    pos = donde_insertar(lista, x)
    if x not in lista:
        lista.insert(pos,x)
        # print(lista)
    return pos
    
# lista = [0,2,4,6,8,10]
# lista_nueva = insertar(lista,3)
    
    
    
    
    