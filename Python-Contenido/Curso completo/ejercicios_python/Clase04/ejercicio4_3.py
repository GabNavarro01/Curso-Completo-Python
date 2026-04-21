# -*- coding: utf-8 -*-

def buscar_u_elemento(lista, u):
    pos = -1
    i = 0
    while i < len(lista):
        if lista[i] == u:
            pos = i
        i += 1
    return pos

def buscar_n_elemento(lista, n):
    n_veces = 0
    i = 0
    while i < len(lista):
        if lista[i] == n:
            n_veces += 1 
        i += 1
    return n_veces