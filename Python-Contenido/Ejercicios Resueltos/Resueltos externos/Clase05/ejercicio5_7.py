# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:51:52 2021

@author: Yamila
"""

import numpy as np

#%% Ejercicio 5.7

a = np.arange(1,20,2) # Genera el array con datos de tipo int
b = np.linspace(1, 19, num=10) # Genera el array con datos de tipo float
c = np.linspace(1, 19, num=10, dtype=(np.int64)) # Crea el mismo array que b pero con datos de tipo int

#%%

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)