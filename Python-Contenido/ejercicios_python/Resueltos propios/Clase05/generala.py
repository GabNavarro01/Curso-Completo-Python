# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 18:25:01 2022

@author: Luciano
"""

#%% Ejercicicio 5.2

from collections import Counter
import random

def tirar():
    tirada=[]
    for i in range (5):
        tirada.append(random.randint(1,6))
    return tirada

def mas_repetido1():
    
    tirada=tirar()
    counter= Counter(tirada)
    
    first =counter.most_common()
    num_repetido=[x[0] for x in first]
    cant_repeticiones=[x[1] for x in first]
    
    mas_repetido1=[num_repetido[0],cant_repeticiones[0]]
    return mas_repetido1 #te trae el más repetido con su cantidad

def tirada_2():
    mas_repetido_1=mas_repetido1()
    i=0
    tirada=[]
    while i<int(mas_repetido_1[1]): 
        tirada+=[int(mas_repetido_1[0])]
        i+=1
    tirada_2=tirada
    n=len(tirada_2)
    for i in range(5-n):
        tirada_2.append(random.randint(1,6))
    return tirada_2

def mas_repetido2():
    tirada2=tirada_2()
    counter= Counter(tirada2)
    
    second =counter.most_common()
    num_repetido=[x[0] for x in second]
    cant_repeticiones=[x[1] for x in second]
    
    mas_repetido2=[num_repetido[0],cant_repeticiones[0]]
    return mas_repetido2 #te trae el más repetido con su cantidad
    
def tirada_3():
    mas_repetido_2=mas_repetido2()
    i=0
    tirada=[]
    while i<int(mas_repetido_2[1]): 
        tirada+=[int(mas_repetido_2[0])]
        i+=1
    tirada_3=tirada
    n=len(tirada_3)
    for i in range(5-n):
        tirada_3.append(random.randint(1,6))
    return tirada_3

def es_generala():
         tirada_f=tirada_3()
          
         return max(tirada_f)==min(tirada_f)
 
N=100000
   
G= sum([es_generala() for i in range(N)])
prob=G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala .')
print(f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')     