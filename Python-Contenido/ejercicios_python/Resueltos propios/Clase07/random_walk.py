# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 07:28:58 2022

@author: Luciano
"""

import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

def random_caminata(N,caminatas):
    caminata_mas_lejana = [0]
    caminata_menos_lejana = [N]
    
    while caminatas > 0:
        caminata = randomwalk(N)
        plt.plot(caminata)
        
        if np.amax(np.absolute(caminata)) > np.amax(np.absolute
                                                    (caminata_mas_lejana)):
            caminata_mas_lejana = caminata
        
        if np.amax(np.absolute(caminata)) < np.amax(np.absolute
                                                    (caminata_menos_lejana)):
            caminata_menos_lejana = caminata
            
        caminatas -= 1
    return plt.plot(), caminata_mas_lejana, caminata_menos_lejana 

def f_principal(N, caminatas):
    plt.figure(figsize=(10,4.8))
    
    plt.subplot(2, 1, 1)    
    caminata = random_caminata(N,caminatas)
    plt.plot(caminata[0])
    plt.title('12 caminatas al azar')
    plt.xticks([]), plt.yticks([-500,0,500])
    plt.ylim([-1000,1000])

    plt.subplot(2, 2, 3)
    plt.plot(caminata[1])
    plt.title('La caminata que más se aleja')
    plt.xticks([]), plt.yticks([-500,0,500])
    plt.ylim([-1000,1000])
    
    plt.subplot(2, 2, 4)
    plt.plot(caminata[2])
    plt.title('La caminata que menos se aleja')
    plt.xticks([]), plt.yticks([])
    plt.ylim([-1000,1000])
    
    plt.show()


if __name__ == '__main__':
    N = 100000
    caminatas = 12
    f_principal(N, caminatas)