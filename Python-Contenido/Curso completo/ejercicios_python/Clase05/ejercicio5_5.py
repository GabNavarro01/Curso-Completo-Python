# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:44:07 2021

@author: Yamila
"""

import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

N = 100000
M = 0
for i in range(N):
    x, y = generar_punto()
    if (x**2 + y**2) < 1:
        M += 1
print(f'pi ~ {4*M/N:.5f}')
