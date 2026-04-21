# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 10:35:22 2021

@author: Yamila
"""

import random
from collections import Counter

# Probabilidad que al menos dos personas cumplan el mismo día

def cocumpleaños(N): # N es el número de veces que hago el experimento
    cocumple = 0 # va a sumar las veces que se repiten cumpleaños
    i = N
    while i > 0:
        año = range(1, 366) # días del año
        cumpleaños = random.choices(año,k=30) # 30 personas al azar
        repe = [k for k,v in Counter(cumpleaños).items() if v>1] # verifico repetición de cumpleaños
        if len(repe) != 0:
            cocumple += 1
        i -= 1
    prob = cocumple/N
    return prob

# Probabilidad de que todos cumplan en distinto día

def cumpleaños_distintos(N): # N es el número de veces que hago el experimento
    cumple = 0 # va a sumar las veces que se repiten cumpleaños
    i = N
    while i > 0:
        dias = range(1, 366) # días del año
        cumples = random.choices(dias,k=30) # 30 personas al azar
        r = [k for k,v in Counter(cumples).items() if v>1] # verifico repetición de cumpleaños
        if len(r) == 0:
            cumple += 1
        i -= 1
    prob = cumple/N
    return prob
