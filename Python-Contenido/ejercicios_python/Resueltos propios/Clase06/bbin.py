# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:32:05 2022

@author: Luciano
"""

#%% Ejercicio 6.14

def donde_insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            break
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        if lista[medio]< x:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        if izq==der:
            if lista[der]>x:
                pos=der
            if lista[der]<x:
                pos=der+1
                
        if izq == medio:
            if lista[izq] > x:
                pos = izq
            if lista[izq] < x:
                pos = izq + 1
        
    
    return pos

#%%

def insertar(lista,x):
    
    pos=donde_insertar(lista,x)
    
    if x not in lista:
        lista.insert(pos,x)
    return pos

lista= [1,2,9,12,14,16,17]
