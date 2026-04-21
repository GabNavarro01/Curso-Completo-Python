# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:05:03 2022

@author: Luciano
"""

#%%Ejercicio 5.9

import random
import numpy as np
import matplotlib.pyplot as plt

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

def plotear_temperaturas(n):
    
    temperaturas_plot=medir_temp(n)
    plt.hist(temperaturas_plot,bins=25)
    plt.show()
    
    
    