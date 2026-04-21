# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 15:46:15 2021

@author: Yamila
"""
import random
from statistics import median

def medir_temp(n):
    medicion = []
    for i in range(n):
        t = round(random.normalvariate(37.5,0.2), 1)
        medicion.append(t)
    return medicion

def resumen_temp(n):
    mediciones = medir_temp(n)
    temp_max = max(mediciones)
    temp_min = min(mediciones)
    prom_temp = round((sum(mediciones)/n), 1)
    mediana_temp = median(mediciones)
    print(mediciones)
    return (temp_max, temp_min, prom_temp, mediana_temp)