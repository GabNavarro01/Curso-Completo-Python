# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 09:55:27 2021

@author: Yamila
"""


def medidas_hoja_A(N):
    '''
    Precondición: recibe un parámetro N mayor que cero.
    Devuelve: el ancho y el largo en mm de la hoja A(N) en una tupla.
    '''
    if N < 0:
        res = f"No existe el tamaño de hoja A{N}"
    elif N == 0:
        res = (841, 1189)
    else:
        res = (medidas_hoja_A(N-1)[1] // 2, medidas_hoja_A(N-1)[0])
    return res
