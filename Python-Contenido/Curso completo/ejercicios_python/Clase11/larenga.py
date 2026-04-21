# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 21:37:06 2021

@author: Yamila
"""


def pascal(n, k):
    '''
    Precondición: recibe como parámetros dos nº enteros > 0.
    Devuelve: calcula el valor que se encuentra en la fila n y la columna k, 
        según el triángulo de Pascal.
    '''
    if n == 0 and k != 0:
        res = "k fuera de rango. Con n = 0 ; k debe ser 0."
    elif k == 0 or k == n:
        res = 1
    else:
        res = pascal(n-1, k-1) + pascal(n-1, k)

    return res
