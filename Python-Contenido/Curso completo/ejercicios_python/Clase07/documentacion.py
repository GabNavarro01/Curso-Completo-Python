# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:06:14 2021

@author: Yamila
"""

def valor_absoluto(n):
    '''
    Pre: n debe ser un número
    Pos: devuelve el valor absoluto de n.
    '''
    
    if n >= 0:
        return n
    else:
        return -n
    
#%%

def suma_pares(l):
    '''
    Pre: l debe ser una lista de números
    Pos: devuelve la suma de los nº pares que están en l. Si l es vacía
        devuelve 0.
    '''
    
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

# El invariante del ciclo es res

#%%

def veces(a, b):
    '''
    Pre: a y b deben ser números. Con b>=0
    Pos: devuelve la suma de 'a' por sí misma,tantas veces como lo indique 'b'
        (a*b)
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1

    return res

# El invariante del ciclo es res

#%%

def collatz(n):
    ''' Recibe un número y calcula la Conjetura de Collatz.
    
    Pre: n debe ser un número
    pos: devuelve la cantidad de iteraciones requeridas para alcanzar la unidad
    '''
    
    res = 1

    while n!=1:
        # Si el número es par, se divide entre 2.    
        if n % 2 == 0:
            n = n//2
        else: # Si el número es impar, se multiplica por 3 y se suma 1.
            n = 3 * n + 1
        res += 1

    return res

# El invariante del ciclo es res