# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:37:19 2021

@author: Yamila
"""

import random
from matplotlib import pyplot as plt
import numpy as np
import timeit as tt


def generar_lista(N):
    lista = [random.randint(1, 1000) for _ in range(N)]
    return lista


# %% Ordenamiento por selección


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return lista


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


# %% Ordenamiento por inserción


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        # print("DEBUG: ", lista)

    return lista


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v


# %% Ordenamiento por burbujeo

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


# %% Ordenamiento merge_sort

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


# %% Experimento timeit


# def experimento_timeit_seleccion(listas, num):
#     """
#     Realiza un experimento usando timeit para evaluar el método
#     de selección para ordenamiento de listas
#     con las listas pasadas como entrada
#     y devuelve los tiempos de ejecución para cada lista
#     en un vector.
#     El parámetro 'listas' debe ser una lista de listas.
#     El parámetro 'num' indica el número de veces que repite el ordenamiento
#     para cada lista.
#     """
#     tiempos_seleccion = []

#     global lista

#     for lista in listas:

#         # evalúo el método de selección
#         # en una copia nueva para cada iteración
#         tiempo_seleccion = tt.timeit(
#             'ord_seleccion(lista.copy())', number=num, globals=globals())

#         # guardo el resultado
#         tiempos_seleccion.append(tiempo_seleccion)

#     # paso los tiempos a arrays
#     tiempos_seleccion = np.array(tiempos_seleccion)

#     return tiempos_seleccion


# %% Ejercicio 12.8: timeit()


def experimento_timeit(Nmax):
    '''
    Pre: recibe nº > 0
    Post: genera listas de largo desde 1 hasta el valor ingresado por 
        parámetro y devuelve una tupla de listas (vectores) que contienen los 
        tiempos que tarda en realizar cada ordenamiento paracada lista generada
        (método_burbujeo, método_inserción, método_selección, método_merge')
    '''

    listas = []
    tiempos_burbujeo = []
    tiempos_insercion = []
    tiempos_seleccion = []
    tiempos_merge = []

    for N in range(1, Nmax+1):
        listas.append(generar_lista(N))

    global lista

    for lista in listas:
        tiempo_burbujeo = tt.timeit(
            'ord_burbujeo(lista.copy())', number=10, globals=globals())
        tiempos_burbujeo.append(tiempo_burbujeo)

        tiempo_insercion = tt.timeit(
            'ord_insercion(lista.copy())', number=10, globals=globals())
        tiempos_insercion.append(tiempo_insercion)

        tiempo_seleccion = tt.timeit(
            'ord_seleccion(lista.copy())', number=10, globals=globals())
        tiempos_seleccion.append(tiempo_seleccion)

        tiempo_merge = tt.timeit(
            'merge_sort(lista.copy())', number=10, globals=globals())
        tiempos_merge.append(tiempo_merge)

    return tiempos_burbujeo, tiempos_insercion, tiempos_seleccion, tiempos_merge


if __name__ == '__main__':

    vectores = experimento_timeit(500)

    tiempos_burbujeo = vectores[0]
    tiempos_insercion = vectores[1]
    tiempos_seleccion = vectores[2]
    tiempos_merge = vectores[3]
    largo_lista = [x for x in range(1, 501)]

    fig, ax = plt.subplots()
    ax.plot(largo_lista, tiempos_burbujeo, label='burbujeo', color='b')
    ax.plot(largo_lista, tiempos_insercion, label='inserción', color='m')
    ax.plot(largo_lista, tiempos_seleccion, label='selección', color='r')
    ax.plot(largo_lista, tiempos_merge, label='merge_sort', color='c')
    ax.set(xlabel='Largo de la lista', ylabel='Tiempos de ordenamiento')
    ax.legend()
    ax.set_title('Tiempos de ordenamiento')
    plt.show()
