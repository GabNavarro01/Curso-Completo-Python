# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 22:26:03 2022

@author: Luciano
"""

import random
import statistics
import numpy as np
# for i in range(6):

#     print(f'{random.normalvariate(0,1):.2f}', end=', ')
    
    
def normalvariate():
    medicion= 37.2 + float(random.normalvariate(0,0.2))
    return medicion
    
def medir_temp(n):
    temperaturas=[]
    for _ in range(n):
        temp=normalvariate()
        temperaturas.append(temp)
        temperaturasnp=np.array(temperaturas)
    
    np.save('../Data/temperaturas.npy',temperaturasnp)
    return temperaturas

def resumen_temp(n):
    
    temperaturas=medir_temp(n)
    maximo=max(temperaturas)
    minimo=min(temperaturas)
    promedio=sum(temperaturas)/n
    mediana= statistics.median(temperaturas)    
    
    print(f' Máximo: {maximo}')
    print(f' Minimo: {minimo}')
    print(f' Promedio: {promedio}')
    print(f' Mediana: {mediana}')


      
    