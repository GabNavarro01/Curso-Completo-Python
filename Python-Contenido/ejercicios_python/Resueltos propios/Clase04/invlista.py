# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 08:32:43 2022

@author: Luciano
"""

#%% Ejercicio 4.5

def invertir_lista(lista):
    invertida=[]
    i_max=len(lista)
    i=i_max
    for e in lista:    
        invertida.append(lista[i-1])
        i=i-1
    return invertida

invertir= invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
invertir

#%% Ejercicio 4.6


            