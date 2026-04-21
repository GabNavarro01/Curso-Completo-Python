# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:37:19 2021

@author: Yamila
"""

import random
from matplotlib import pyplot as plt


def generar_lista(N):
    lista = [random.randint(1, 1000) for _ in range(N)]
    return lista


# %% Ordenamiento por selección

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: ordena la lista y devuelve la cantidad de comparaciones que 
           realiza para poder ordenar la lista."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    comparaciones = 0

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento

        p = buscar_max(lista, 0, n)

        comparaciones += p[1]

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p[0]], lista[n] = lista[n], lista[p[0]]

        # print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return comparaciones


def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    comparaciones = 0
    for i in range(a + 1, b + 1):
        comparaciones += 1
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max, comparaciones


# %% Ordenamiento por inserción


def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: ordena la lista y devuelve la cantidad de comparaciones que 
           realiza para poder ordenar la lista."""

    comparaciones = 0

    for i in range(len(lista) - 1):
        comparaciones += 1
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            a = reubicar(lista, i + 1)
            comparaciones += a[1]
        # print("DEBUG: ", lista)

    return comparaciones


def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]
    comparaciones = 1
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p

    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        comparaciones += 1
        j -= 1

    lista[j] = v
    return v, comparaciones


# %% Ordenamiento por burbujeo

def ord_burbujeo(lista):
    '''
    Pre: recibe como parámetro una lista cuyos elementos deben ser comparables.
    Post: ordena la lista y devuelve la cantidad de comparaciones que realiza 
        para poder ordenar la lista.
    '''
    n = len(lista) - 1
    comparaciones = 0
    while n > 0:
        for i in range(n):
            if lista[i] > lista[i+1]:
                e = lista[i]
                lista.pop(i)
                lista.insert(i+1, e)
            comparaciones += 1
        n -= 1
    return comparaciones


# %% Ordenamiento merge_sort

def merge_sort(lista):
    
    def merge_aux(lista, comparaciones):
        """
        Ordena lista mediante el método merge sort.
        Pre: lista debe contener elementos comparables.
        Devuelve: una nueva lista ordenada.
        """
        comparaciones += 1
        if len(lista) < 2:
            lista_nueva = lista
        else:
            medio = len(lista) // 2
            izq, comparaciones = merge_aux(lista[:medio], comparaciones)
            der, comparaciones = merge_aux(lista[medio:], comparaciones)
            lista_nueva, comparo = merge(izq, der)
            comparaciones += comparo
        return lista_nueva, comparaciones


    def merge(lista1, lista2):
        """
        Intercala los elementos de lista1 y lista2 de forma ordenada.
        Pre: lista1 y lista2 deben estar ordenadas.
        Devuelve: una lista con los elementos de lista1 y lista2.
        """
        i, j = 0, 0
        resultado = []
        comparaciones = 1
        while(i < len(lista1) and j < len(lista2)):
            comparaciones += 2
            if (lista1[i] < lista2[j]):
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista2[j])
                j += 1
    
        # Agregar lo que falta de una lista
        resultado += lista1[i:]
        resultado += lista2[j:]
    
        return resultado, comparaciones
    
    lista, comparaciones = merge_aux(lista, 0)
    return comparaciones

# %% Experimento

def experimento(N, k):
    '''
    Pre: recibe 2 parámetros. N que representa el largo de listas y k la 
        cantidad de veces que se repite el experimento.
    Post: devuelve una tupla con el promedio de comparaciones que se 
        realizaron para ordenar las listas por cada método 
        (selección, inserción, burbujeo).
    '''
    promedio_seleccion = 0
    promedio_insercion = 0
    promedio_burbujeo = 0
    promedio_merge = 0
    repes = k
    while repes > 0:
        lista = generar_lista(N)

        conteo_selección = ord_seleccion(lista.copy())
        promedio_seleccion += conteo_selección

        conteo_insercion = ord_insercion(lista.copy())
        promedio_insercion += conteo_insercion

        conteo_burbujeo = ord_burbujeo(lista.copy())
        promedio_burbujeo += conteo_burbujeo
        
        conteo_merge = merge_sort(lista.copy())
        promedio_merge += conteo_merge

        repes -= 1
    # print("(burbujeo, inserción, selección, merge_sort)")
    return promedio_burbujeo/k, promedio_insercion/k, promedio_seleccion/k, promedio_merge/k


# %% Ejercicio 12.5: comparar métodos gráficamente

def experimento_vectores(Nmax):
    '''
    Pre: recibe nº > 0
    Post: genera listas de largo desde 1 hasta el valor ingresado por 
        parámetro y devuelve una tupla de listas (vectores) que contienen las 
        cantidad de comparaciones que realiza para ordenar cada lista generada
        (método_burbujeo, método_inserción, método_selección, método_merge')
    '''

    n = 1
    comparaciones_burbujeo = []
    comparaciones_insercion = []
    comparaciones_seleccion = []
    comparaciones_merge = []
    while n <= Nmax:
        comparaciones = experimento(n, 1)
        comparaciones_burbujeo.append(comparaciones[0])
        comparaciones_insercion.append(comparaciones[1])
        comparaciones_seleccion.append(comparaciones[2])
        comparaciones_merge.append(comparaciones[3])
        n += 1
    return comparaciones_burbujeo, comparaciones_insercion, comparaciones_seleccion, comparaciones_merge


if __name__ == '__main__':

    vectores = experimento_vectores(250)

    comparaciones_burbujeo = vectores[0]
    comparaciones_insercion = vectores[1]
    comparaciones_seleccion = vectores[2]
    comparaciones_merge = vectores[3]
    largo_lista = [x for x in range(1, 251)]

    fig, ax = plt.subplots()
    ax.plot(largo_lista, comparaciones_burbujeo,
            dashes=[2], label='burbujeo', color='b')
    ax.plot(largo_lista, comparaciones_seleccion, label='selección', color='r')
    ax.plot(largo_lista, comparaciones_insercion, label='inserción', color='m')
    ax.plot(largo_lista, comparaciones_merge, label='merge_sort', color='c')
    ax.set(xlabel='largo de la lista', ylabel='cant. comparaciones')
    ax.legend()
    ax.set_title('Complejidad de ordenamiento')
    plt.show()
