# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 08:24:31 2022

@author: Luciano
"""

import random
import math

def generar_punto():
    
        x=random.random()
        y=random.random()
        
        return x,y

def estimar_pi():
    M=0
    x,y=generar_punto()
    
    if (x*x + y*y) <1:
            M+=1
    return M

N=10000000
G=sum(estimar_pi() for i in range(N))

print(f'Lancé {N} veces el número pi se aproxima a {4*G/N}')
