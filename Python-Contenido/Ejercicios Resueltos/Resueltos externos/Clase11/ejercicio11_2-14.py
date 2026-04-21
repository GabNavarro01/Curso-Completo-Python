# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 10:48:48 2021

@author: Yamila
"""
# %% Ejercicio 11.2: Números triangulares


import numpy as np
from matplotlib import pyplot as plt


def triangular(n):
    '''
    Precondición: n>= 0
    Devuelve: el n-ésimo número triangular 
        (es decir, el número 1 + 2 + 3 + ... + n).
    '''

    if n == 0 or n == 1:
        res = n
    else:
        res = n + triangular(n-1)

    return res

# %% Ejercicio 11.3: Dígitos


def cant_digitos(n):
    '''
    Precondición: n > 0; n debe ser un número entero.
    Devuelve: la cantidad de dígitos que tiene n.
    '''
    n_string = str(n)
    if len(n_string) == 1:
        res = 1
    else:
        res = 1 + cant_digitos(n_string[1:])
    return res

# %% Ejercicio 11.4: Potencias


def es_potencia(n, b):
    '''
    Precondición: recibe 2 enteros mayores que 0, n y b.
    Devuelve: True si n es potencia de b y False en caso contrario.
    '''
    if n == 1 or n == b:
        res = True
    elif n % b != 0:
        res = False
    else:
        n = n // b
        res = es_potencia(n, b)
    return res

# %% Ejercicio 11.5: Subcadenas


def posiciones(a, b):
    '''
    Precondición: recibe como parámetros dos cadenas a y b.
    Devuelve: una lista con las posiciones en donde se encuentra b dentro de a.
    '''
    res = []

    def posiciones_aux(a, b, res):
        if len(a) == 0 or len(b) == 0 or a.find(b) < 0:
            return res
        else:
            pos = a.rfind(b)
            res.insert(0, pos)
            posiciones_aux(a[:pos], b, res)
        return res

    lista = posiciones_aux(a, b, res)

    return lista

# %% Ejercicio 11.6: Paridad


def par(n):
    '''
    Precondición: recibe como parámetros un nº entero >= 0.
    Devuelve: True si es par o False si no lo es.
    '''
    if n == 1:
        res = False
    elif n == 0:
        res = True
    else:
        if impar(n-1):
            res = True
        else:
            res = False
    return res


def impar(n):
    '''
    Precondición: recibe como parámetros un nº entero >= 0.
    Devuelve: True si es impar o False si no lo es.
    '''
    if n == 1:
        res = True
    elif n == 0:
        res = False
    else:
        if par(n-1):
            res = True
        else:
            res = False
    return res

# %% Ejercicio 11.7: Máximo


def maximo(lista):
    '''
    Precondición: recibe como parámetros una lista.
    Devuelve: el mayor elemento de la lista.
    '''
    def max_aux(lista, res):
        if lista == []:
            maximo = res
        elif lista[-1] >= res:
            maximo = max_aux(lista[:-1], lista[-1])
        else:
            maximo = max_aux(lista[:-1], res)
        return maximo

    if len(lista) == 0:
        res = "No es posible indicar el elemento máximo, dado que la lista ingresada se encuentra vacía."
    elif len(lista) == 1:
        res = lista[0]
    else:
        res = max_aux(lista[:-1], lista[-1])

    return res


# %% Ejercicio 11.8: Replicar

def replicar(lista, n):
    '''
    Precondición: recibe como parámetros una lista y un número entero > 0.
    Devuelve: una lista con sus elementos replicados n veces.
    '''
    lista_replicada = []

    if len(lista) == 0:
        lista_replicada
    elif len(lista) == 1:
        lista_replicada = lista * n
    else:
        lista_replicada += [lista[0]] * n + replicar(lista[1:], n)

    return lista_replicada

# %% Ejercicio 11.9: Pascal


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

# %% Ejercicio 11.10: Combinatorios


def combinaciones(lista, k):
    '''
    Precondición: recibe como parámetros una lista de caracteres únicos, y 
        un número k entero > 0.
    Devuelve: una lista con todas las posibles cadenas de longitud k formadas 
        con los caracteres dados (permitiendo caracteres repetidos).
    '''
    if len(lista) == 0:
        res = 'No hay elelementos en la lista.'
    elif len(lista) != 0 and k == 1:
        res = lista
    else:
        res = []
        lista2 = combinaciones(lista, k-1)
        for i in range(0, len(lista)):
            for x in range(0, len(lista2)):
                res.append(lista[i] + lista2[x])
    return res

# %% Ejercicio 11.11: Búsqueda binaria


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

# %% Ejercicio 11.12: Envolviendo a Fibonacci


def fibonacci(n):
    '''
    Toma un entero positivo n y
    devuelve el n-ésimo número de Fibonacci
    donde F(0) = 0 y F(1) = 1.
    '''
    def fibonacci_aux(n, dict_fibo):
        '''
        Calcula el n-ésimo número de Fibonacci de forma recursiva
        utilizando un diccionario para almacenar los valores ya computados.
        dict_fibo es un diccionario que guarda en la clave 'k' el valor de F(k)
        '''
        if n in dict_fibo.keys():
            F = dict_fibo[n]
        else:
            dict_fibo[n] = (fibonacci(n-1) + fibonacci(n-2))
            F = dict_fibo[n]  # completar
        return F, dict_fibo  # completar

    dict_fibo = {0: 0, 1: 1}
    F, dict_fibo = fibonacci_aux(n, dict_fibo)
    return F

# %% Ejercicio 11.13: Hojas ISO y recursión


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

# %% Ejercicio 11.14: precio_alquiler ~ superficie


def ajuste_lineal_simple(x, y):
    a = sum(((x - x.mean())*(y-y.mean()))) / sum(((x-x.mean())**2))
    b = y.mean() - a*x.mean()
    return a, b


superficie = np.array([150.0, 120.0, 170.0, 80.0])
alquiler = np.array([35.0, 29.6, 37.4, 21.0])

a, b = ajuste_lineal_simple(superficie, alquiler)

errores = alquiler - (a*superficie + b)
print(errores)
print("ECM:", (errores**2).mean())
