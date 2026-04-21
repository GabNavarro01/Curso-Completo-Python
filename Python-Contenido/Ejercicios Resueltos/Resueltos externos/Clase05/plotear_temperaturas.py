# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:29:14 2021

@author: Yamila
"""
import matplotlib.pyplot as plt
import numpy as np

def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=10)
    plt.show()
    return