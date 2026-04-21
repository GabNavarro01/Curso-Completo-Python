# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:41:43 2021

@author: Yamila
"""

import random
# from collections import Counter

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(palo,valor) for valor in valores for palo in palos]
# mano = random.sample(naipes, k=3)

def envido(N): # N es el número de experimentos - manos de juego
    envido_31 = 0
    envido_32 = 0
    envido_33 = 0
    i = N
    while i > 0:
        mano = random.sample(naipes, k=3)
        mano.sort()
        print(mano)
        puntos = 20

        if mano[0][0] == mano[1][0] and mano[0][0] != mano[2][0]:
            if mano[0][1] not in (10,11,12) and mano[1][1] not in (10,11,12):
                puntos += mano[0][1] + mano[1][1]
        
        if mano[0][0] == mano[2][0] and mano[0][0] != mano[1][0]:
            if mano[0][1] not in (10,11,12) and mano[2][1] not in (10,11,12):
                puntos += mano[0][1] + mano[2][1]
        
        if mano[1][0] == mano[2][0] and mano[1][0] != mano[0][0]:
            if mano[1][1] not in (10,11,12) and mano[2][1] not in (10,11,12):
                puntos += mano[1][1] + mano[2][1]
        
        if mano[0][0] == mano[1][0] and mano[0][0] == mano[2][0]:
            cartas = []
            for carta in mano:
                if carta[1] not in (10,11,12):
                    cartas.append(carta[1])
            
            if len(cartas) < 3:
                puntos += sum(cartas)
            if len(cartas) == 3:
                carta_mayor = max(cartas)
                cartas.remove(max(cartas))
                puntos  += max(cartas) + carta_mayor
                
        if puntos == 31:
            envido_31 += 1
        elif puntos == 32:
            envido_32 += 1
        elif puntos == 33:
            envido_33 += 1
                
        i -= 1
    
    prob_31 = envido_31/N
    prob_32 = envido_32/N
    prob_33 = envido_33/N
    print(f'La probabilidad de tener envido con 31 puntos es de {prob_31}')
    print(f'La probabilidad de tener envido con 32 puntos es de {prob_32}')
    print(f'La probabilidad de tener envido con 33 puntos es de {prob_33}')    