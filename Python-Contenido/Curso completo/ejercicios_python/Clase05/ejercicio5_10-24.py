# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 11:37:23 2021

@author: Yamila
"""

import random
import numpy as np
import matplotlib.pyplot as plt

#%% Ejercicio 5.10

# Crea un álbum vacío con la cant. de figuritas indicadas como parámetro.

def crear_album(figus_total):
    album = np.zeros(figus_total, dtype=int)
    return album

#%% Ejercicio 5.11

"""Verifica si un álbum tiene o no todas sus figuritas pegadas.
# El álbum vacío es un arreglo de 0, cuando se va completando cambian los 0
por la cantidad de veces que se obtuvo la figu.
Si se verifica que el arreglo (álbum) aún tiene 0, entonces,
sigue incompleto"""

def album_incompleto(A):
    if min(A) == 0:
        return True
    else:
        return False
    
#%% Ejercicio 5.12

# Simula la compra de 1 figurita del álbum al azar.

def comprar_figu(figus_total):
    figuritas = random.randint(0,figus_total - 1)
    return figuritas

#%% Ejercicio 5.13

"""Estima la cant. de figus que hay que comprar para llenar el álbum,
teniendo la posibilidad de comprar repetidas."""

def cuantas_figus(figus_total):
    figuritas = 0 # Acumula las commpras de figus, inicializado en 0.
    album = crear_album(figus_total) # Crea el álbum de figus
    seguir_comprando = True
    """Iicio un ciclo que simula la compra de figus hasta completar el álbum
    el álbum se completa cuando deja de tener 0 en todas sus posiciones."""
    while seguir_comprando:
        compra = comprar_figu(figus_total) # compro figuritas
        figuritas += 1 # agrego la compra al contador
        album[compra] += 1 # pego figurita o sumo como repe
        if album_incompleto(album) == False:
            seguir_comprando = False # si el álbum se lleno finalizo ciclo.
    return figuritas # retorno el contador

#%% Ejercicio 5.14

# n_repeticiones = 1000
# figus_total = 6

# Calculo el promedio de figus que se deben comprar, probando n veces el exp.

def repeticiones(n_repeticiones, figus_total):
    compras = [ ] # acumula el total de compras para cada vuelta.
    while n_repeticiones > 0:
        compro = cuantas_figus(figus_total)
        compras.append(compro)
        n_repeticiones -= 1
    promedio = np.mean(compras)
    
    """La siguiente línea descomentada, me permite guardar la lista de compras
    en un archivo npy en la carpeta Data, si se trabaja con el directorio
    propuesto en clase"""
    
    # np.save('../Data/compras_figus.npy', compras)
    
    return promedio

#%% ejercicio 5.15

# Ídem al ejercicio anterior, no encontré diferencias para cambiar...

def experimento_figus(n_repeticiones, figus_total):
    compras = [ ]
    while n_repeticiones > 0:
        compro = cuantas_figus(figus_total)
        compras.append(compro)
        n_repeticiones -= 1
    promedio = np.mean(compras)
    return promedio

#%% Ejercicio 5.16

# unifiqué todo en la función siguiente

#%% Ejercicio 5.17

"""Simula la compra de 1 paquete de figus según tamaño del álbum y cant. de
figus por paquete"""

def comprar_paquete(figus_total, figus_paquete):
    paquete = random.choices(range(figus_total), k=figus_paquete)
    return paquete

#%% Ejercicio 5.18

# ¿Cuántos paquetes debo comprar para completar el álbum?

def cuantos_paquetes(figus_total, figus_paquete):
    paquetes = 0 # contador de paquetes comprados
    album = crear_album(figus_total) # Creación del álbum vacío
    seguir_comprando = True
    """Genero un ciclo while que va a simular la compra de paquetes de figus, 
    mientras tenga el álbum incompleto. Dentro del while hay un for que 
    mete en el álbúm las figus compradas. El if revisa si el álbum
    se completó"""
    while seguir_comprando:
        compra = comprar_paquete(figus_total, figus_paquete)
        paquetes += 1
        for x in compra:
            album[x] += 1
        if album_incompleto(album) == False:
            seguir_comprando = False
    return paquetes

#%% Ejercicio 5.19

"""Promedio de paquetes que se deben comprar para llenar un álbum de figus.
Se calcula en base a n repeticiones.
La línea comentada se puede descomentar para generar un archivo npy que se 
almacena en la carpeta data con el total de compra de paquetes por cada álbum
que se generó a lo largo de las n repeticiones. (utilizo la ruta de directorio
propuesta en clase)"""

def repeticiones_paquetes(n_repeticiones, figus_total, figus_paquete):
    compras_paquetes = [ ]
    while n_repeticiones > 0:
        compro = cuantos_paquetes(figus_total, figus_paquete)
        compras_paquetes.append(compro)
        n_repeticiones -= 1
    promedio = np.mean(compras_paquetes)
    # np.save('../Data/compras_paquetes.npy', compras_paquetes)
    return promedio

#%% Graficar el llenado del álbum

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

# figus_total = 670
# figus_paquete = 5

# plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
# plt.xlabel("Cantidad de paquetes comprados.")
# plt.ylabel("Cantidad de figuritas pegadas.")
# plt.title("La curva de llenado se desacelera al final")
# plt.show()

#%% Ejercicio 5.20

"""Probabilidad de completar el álbúm habiendo comprado 850 paquetes de figus
o menos."""

def probabilidad(n_repeticiones, figus_total, figus_paquete):
    compras_paquetes = [ ]
    repes = n_repeticiones
    while n_repeticiones > 0:
        compro = cuantos_paquetes(figus_total, figus_paquete)
        compras_paquetes.append(compro)
        n_repeticiones -= 1
    n_paquetes_hasta_llenar = np.array(compras_paquetes)
    prob = (n_paquetes_hasta_llenar <= 850).sum() / repes
    return prob

#%% Ejercicio 5.21

""""Los datos obtenidos en el ejercicio 5.19, almacenados en un archivo npy,
serán graficados en un histograma. Para ello hay que ingresar a la función como
parámetro la ruta de acceso al archivo."""

def plotear_paquetes(archivo):
    paquetes = np.load(archivo)
    plt.hist(paquetes,bins=50)
    plt.show()
    return

#%% Ejercicio 5.22

""""Utilizando la función del ejercicio 5.20 fui tanteando cuántos paquetes de
figus debía comprar para alcanzar una probabilidad del 90% para completar el
álbum. Varía un poco de los valores ingresados por páramentro. Pero para 1000
repeticiones, 670 figus totale y 5 por paquete, se necesita comprar aprox.
1150 paquetes"""

def probab(n_repeticiones, figus_total, figus_paquete):
    compras_paquetes = [ ]
    repes = n_repeticiones
    while n_repeticiones > 0:
        compro = cuantos_paquetes(figus_total, figus_paquete)
        compras_paquetes.append(compro)
        n_repeticiones -= 1
    n_paquetes_hasta_llenar = np.array(compras_paquetes)
    prob = (n_paquetes_hasta_llenar <= 1150).sum() / repes
    return prob

#%% Ejercicio 5.23

"""Solicita que no haya repes en el paquete. Entonces reutilizo las funciones
de los ejercicios 17, 18 y 21. Cambiando el random.choices en la compra del 
paquete por random.sample.
El resultado obtenido es muy similar, porque si bien no retito figus dentro del
mismo paqute, si puede suceder repes de una compra a otra."""

def comprar_paquete_sin_repe(figus_total, figus_paquete):
    paquete = random.sample(range(figus_total), k=figus_paquete)
    return paquete

def cuantos_paquetes2(figus_total, figus_paquete):
    paquetes = 0 # contador de paquetes comprados
    album = crear_album(figus_total) # Creación del álbum vacío
    seguir_comprando = True
    """Genero un ciclo while que va a simular la compra de paquetes de figus, 
    mientras tenga el álbum incompleto. Dentro del while hay un for que 
    mete en el álbúm las figus compradas. El if revisa si el álbum
    se completó"""
    while seguir_comprando:
        compra = comprar_paquete_sin_repe(figus_total, figus_paquete)
        paquetes += 1
        for x in compra:
            album[x] += 1
        if album_incompleto(album) == False:
            seguir_comprando = False
    return paquetes

def probabilidad2(n_repeticiones, figus_total, figus_paquete):
    compras_paquetes = [ ]
    repes = n_repeticiones
    while n_repeticiones > 0:
        compro = cuantos_paquetes2(figus_total, figus_paquete)
        compras_paquetes.append(compro)
        n_repeticiones -= 1
    n_paquetes_hasta_llenar = np.array(compras_paquetes)
    prob = (n_paquetes_hasta_llenar <= 850).sum() / repes
    return prob

#%% Ejercicio 5.24

"""Si entre amigos comparten las figuritas, ¿cuántos paquetes deben comprar
para que todos completen su álbum?

En la 1ª función se crea un array con los álbumes de cada amigo con todos 0
para simular que está vacío. La variable 'amigo' es la cantidad de amigos que
participan y 'figus_total' la cantidad de figuritas de cada álbum.
"""

def conjunto_albumes(amigos, figus_total):
    conj_albumes = np.zeros((amigos,figus_total), dtype=int)
    return conj_albumes

"""Esta función permite determinar cuántos paquetes fueron necesarios comprar
para que todos logren llenar su álbum, compartiendo figus.
Reutilicé la función 'comprar_paquete' del ejercicio 5.17"""

def compartiendo(figus_total,figus_paquete,amigos):
    albumes = conjunto_albumes(amigos, figus_total) # creo el álbum de álbumes
    compras = 0 # contador de compras de paquetes
    seguir_comprando = True
    # Inicio un bucle que correrá mientras halla algún álbum sin completar.
    while seguir_comprando:
        compra = comprar_paquete(figus_total, figus_paquete) # genera la compra
        compras += 1 # suma al contador
        """El siguiente bucle for intenta simular que como se van pegando
        figus en los álbumes. La variable 'compra' es una lista con los nª de 
        figus recién compradas."""
        for x in compra:
            """Si en alguno de los álubemes en la posición de la figurita es 0,
            voy a sumarle 1 para indicar que ya la tengo."""
            if 0 in albumes[0:len(albumes),x]:
                lista_figus = list(albumes[0:len(albumes),x])
                primer_0 = lista_figus.index(0)
                albumes[0:len(albumes),x][primer_0] += 1
        """Confirmo si hay aún algún 0 en los álbumes, si no hay termina el 
        ciclo while y retorna el total de compras efectuadas."""
        if np.amin(albumes) != 0:
            seguir_comprando = False
    return compras

"""La siguiente función calcula el promedio de compras de paquetes que
deben realizar el grupo de amigos para que todos completen su álbum.
Es similar a la propuesta para el ejercicio 5.19, pero asociada a las funciones
de este bloque."""

def promedio(n_repeticiones,figus_total,figus_paquete,amigos):
    compras_paquetes = [ ]
    while n_repeticiones > 0:
        compro = compartiendo(figus_total,figus_paquete,amigos)
        compras_paquetes.append(compro)
        n_repeticiones -= 1
    promedio = np.mean(compras_paquetes)
    # np.save('../Data/compras_paquetes.npy', compras_paquetes)
    return promedio
