# -*- coding: utf-8 -*-
import random

def tirar():
    tirada = [random.randint(1,6) for _ in range(5)]
    return tirada 

def es_generala(tirada):
    if tirada.count(tirada[0]) == 5:
        return True
    else:
        return False

N = 20
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
