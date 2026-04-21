# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:26:44 2021

@author: Yamila
"""


def bbinaria_rec(lista, e):
    '''
    Precondición: recibe lista de números ordenados y un elemento e que se 
        desea buscar dentro de la lista.
    Devuelve: True si e fue hallado o False si no se encuentra.
    '''
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] == e:
            res = lista[medio] == e
        elif lista[medio] < e:
            res = bbinaria_rec(lista[medio+1:], e)
        elif lista[medio] > e:
            res = bbinaria_rec(lista[0:medio], e)

    return res
