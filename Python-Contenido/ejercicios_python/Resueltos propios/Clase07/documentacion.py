# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 08:28:11 2022

@author: Luciano
"""
#%%
def valor_absoluto(n):
    
    '''Precondición: n es un número real
    Postcondición= obtiene el valor absoluto de n
    '''
    if n >= 0:
        return n
    else:
        return -n
    
#%%

def suma_pares(l):
    
    '''Pre= l es una lista numerica
       Pos= devuelve la suma de los numeros pares.
    '''
    
    res = 0
    for e in l:
        if e % 2 == 0:
            res += e
        else:
            res += 0

    return res

# El invariante es res

#%%

def veces(a, b):
    
    '''Pre: a y b deben ser números y b debe ser >=0
       Pos: devuelve la suma de a tantas veces como indique b
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res

# El invariante es res

#%%
def collatz(n):
    
    '''Pre: n debe ser un numero
       Pos: Si n es par realiza la división por 2 y devuelve la cantidad de iteraciones para acanzar la unidad.
    '''
    res = 1
    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res

# El invariante del ciclo es res
