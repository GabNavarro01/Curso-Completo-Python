# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 07:36:15 2022

@author: Luciano
"""

#%% EJercicio 6.19

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    comp=0
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
            comp+=1
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
            comp+=1
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            comp+=1
    return pos,comp

lista=[x for x in range(98)]




