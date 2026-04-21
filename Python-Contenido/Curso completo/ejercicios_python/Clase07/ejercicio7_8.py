# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 17:06:28 2021

@author: Yamila
"""

#%% Implementación con un ciclo

def sumar_enteros_con_ciclos(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    
    suma = 0
    while desde <= hasta:
        suma += desde
        desde += 1
    return suma

#%% Implementación sin un ciclo (número triangular)

def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    
    suma = 0
    if hasta >= desde:
        suma = ((hasta * (hasta + 1)) / 2) - ((desde * (desde - 1)) / 2)
    return int(suma)