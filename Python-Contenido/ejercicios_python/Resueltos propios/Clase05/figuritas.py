# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:12:40 2022

@author: Luciano
"""
#%%Ejercicio 5.10

import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    
    album=np.zeros(figus_total,dtype=int)
    
    return album

#%%Ejercicio 5.11

def album_incompleto(album):
        if min(album)==0:
            return True
        else:
            return False
        
#%%Ejercicio 5.12

def comprar_figu(figus_total):
    figurita=random.randint(0,figus_total-1)
    
    return figurita

#%%Ejercicio 5.13

def cuantas_figus(figus_total):
    figuritas=0
    album=crear_album(figus_total)
    seguir_comprando=True
    
    while seguir_comprando:
        compra=comprar_figu(figus_total)
        figuritas+=1
        album[compra]+=1
        if album_incompleto(album)==False:
            seguir_comprando=False
    return figuritas
        
#%%Ejercicio 5.14

n_repeticiones=1000
figus_compl=[]
for i in range(n_repeticiones):
    figuritas=cuantas_figus(6)
    figus_compl.append(figuritas)
    
promedio=np.mean(figus_compl)

# print(f'Se necesitan en promdio {promedio} compras de 1 figurita para completar el album de 6')

#%%Ejercicio 5.15

def experimento_figus(n_repeticiones, figus_total):
    figus_compl=[]
    for i in range(n_repeticiones):
        figuritas=cuantas_figus(figus_total)
        figus_compl.append(figuritas)
        
    promedio=np.mean(figus_compl)

    print(f'Se necesitan en promdio {promedio} compras de 1 figurita para completar el album de 6')

#%%Ejercicio 5.16 y 5.17 (paquetes)


def comprar_paquete(figus_total):
    paquete=[random.randint(0,figus_total-1) for i in range (5)]
    
    return paquete

#%%Ejercicio 5.18

def cuantos_paquetes(figus_total):
    paquetes=0
    album=crear_album(figus_total)
    seguir_comprando=True
    
    while seguir_comprando:
        compra=comprar_paquete(figus_total)
        paquetes+=1
        for x in compra:
            album[x]+=1
        if album_incompleto(album)==False:
            seguir_comprando=False
    return paquetes

#%%Ejercicio 5.19

def experimento_paq(n_repeticiones, figus_total):
    paquetes_compl=[]
    for i in range(n_repeticiones):
        paquetes=cuantos_paquetes(figus_total)
        paquetes_compl.append(paquetes)
        
    promedio=np.mean(paquetes_compl)

    print(f'Se necesitan en promdio {promedio} compras de paquetes para completar el album')
    
    
#%%Ejercicio 5.19.1

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total)
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

#%%Ejercicio 5.20


def probabilidad(n_repeticiones, figus_total):
    compras_paquetes = [ ]
    repes = n_repeticiones
    while n_repeticiones > 0:
        compro = cuantos_paquetes(figus_total)
        compras_paquetes.append(compro)
        n_repeticiones -= 1
    n_paquetes_hasta_llenar = np.array(compras_paquetes)
    prob = (n_paquetes_hasta_llenar <= 850).sum() / repes
    return prob
    


#%%Ejercicio 5.21
paq=[]
for i in range (100):
    paquetes=cuantos_paquetes(670)
    paq.append(paquetes)
# plt.hist(paq, bins=25)
# plt.show()

#%%Ejercicio 5.22

# def proba90(n_repeticiones, figus_total):
#     compras_paquetes = [ ]
#     repes = n_repeticiones
#     while n_repeticiones > 0:
#         compro = cuantos_paquetes(figus_total)
#         compras_paquetes.append(compro)
#         n_repeticiones -= 1
#     n_paquetes_hasta_llenar = np.array(compras_paquetes)
#     prob = (n_paquetes_hasta_llenar <= 1150).sum() / repes
#     return prob

    np.percentile(paq, 90)


#%%Ejercicio 5.23

def comprar_paquetenp(figus_total):
    paquetes=random.sample(range(figus_total), k=5)
    
    return paquetes

def cuantos_paquetesnp(figus_total):
    paquetes=0
    album=crear_album(figus_total)
    seguir_comprando=True
    
    while seguir_comprando:
        compra=comprar_paquetenp(figus_total)
        paquetes+=1
        for x in compra:
            album[x]+=1
        if album_incompleto(album)==False:
            seguir_comprando=False
    return paquetes

def probabilidadnp(n_repeticiones, figus_total):
    compras_paquetes = [ ]
    repes = n_repeticiones
    while n_repeticiones > 0:
        compro = cuantos_paquetesnp(figus_total)
        compras_paquetes.append(compro)
        n_repeticiones -= 1
    n_paquetes_hasta_llenar = np.array(compras_paquetes)
    prob = (n_paquetes_hasta_llenar <= 850).sum() / repes
    return prob


