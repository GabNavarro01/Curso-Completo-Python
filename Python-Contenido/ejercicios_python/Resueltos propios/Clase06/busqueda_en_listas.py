# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 08:32:08 2022

@author: Luciano
"""

#%% Ejercicio 4.2

def busqueda_con_index (lista, e):
    if e in lista:
        pos=lista.index(e)
    else:
        pos=-1
        
    return pos

#%% Ejercicio 4.2.1

def busqueda_lineal(lista,e):
    pos=-1 
    
    for i, z in enumerate(lista):
        if z==e:
            pos= i
            break        
    return pos

#%% Ejercicio 4.3

def buscar_u_elemento(lista,e):
    pos=-1 
    
    for i, z in enumerate(lista):
        if z==e:
            pos= i
                   
    return pos

#%%

def buscar_n_elemento(lista,e):
    
    cant=0
    for i,z in enumerate(lista):
        if z==e:
            cant+=1
    
    return cant

#%% Ejercicio 4.4

def maximo(lista):
    m=-999
    for e in lista:
        if m<e:
            m=e
    return m

def min(lista):
    m=999
    for e in lista:
        if m>e:
            m=e
    return m

#%% Ejercicio 6.13

def busqueda_lineal_lordenada(lista,e):
    pos=-1 
    
    for i, z in enumerate(lista):
        if z>e:
            break
        if z==e:
            pos= i
            break        
    return pos

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



