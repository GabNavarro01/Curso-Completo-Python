# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:15:40 2021

@author: Yamila
"""


def ord_burbujeo(lista):
    '''
    Pre: recibe como parámetro una lista cuyos elementos deben ser comparables.
    Post: devuelve la lista está ordenada.
    '''
    n = len(lista) - 1
    while n > 0:
        for i in range(n):
            if lista[i] > lista[i+1]:
                e = lista[i]
                lista.pop(i)
                lista.insert(i+1, e)
        n -= 1
    return lista
