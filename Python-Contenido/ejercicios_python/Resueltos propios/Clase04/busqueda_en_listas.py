# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 08:32:08 2022

@author: Luciano
"""

#%% Ejercicio 4.2

def buswueda_con_index (lista, e):
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