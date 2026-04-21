# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 10:09:42 2022

@author: Luciano
"""
#%% Ejercicio 7.8
def sumar_enteros(desde, hasta):
   suma=0
   for i in range (desde,hasta):
       suma+=i
  
   return suma      

#%%
def sumar_enterosT(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    
    suma = 0
    if hasta >= desde:
        suma = ((hasta * (hasta + 1)) / 2) - ((desde * (desde - 1)) / 2)
    return int(suma)

#%%

import matplotlib.pyplot as plt
import numpy as np


X = np.linspace(-np.pi, np.pi, 256)
C, S= np.cos(X), np.sin(X)

plt.plot(X,C, color = 'blue',linewidth=2.5, linestyle="-")
plt.plot(X,S, color = 'red')
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
           [r'$-\pi$', r'$-\pi2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])

plt.show()

#%% Ejercicio 7.11

fig = plt.figure()
fig = plt.figure()

plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas

plt.subplot(2, 3, 4)
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5)
plt.plot([1,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6)
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])

plt.show()









