# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 11:40:59 2022

@author: Luciano
"""
# %% Ejercicio 5.1

from pprint import pprint
from collections import Counter
import random

# dado= random.randint(1,6)

# tirada=[]
# for i in range(5):
#     tirada.append(random.randint(1,6))

# print(tirada)


def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1, 6))
    return tirada


def es_generala(tirada):

    return max(tirada) == min(tirada)


N = 1000000

G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(
    f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')


# %% Ejercicicio 5.2


def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1, 6))
    return tirada


def mas_repetido1():

    tirada = tirar()
    counter = Counter(tirada)

    first = counter.most_common()
    num_repetido = [x[0] for x in first]
    cant_repeticiones = [x[1] for x in first]

    mas_repetido1 = [num_repetido[0], cant_repeticiones[0]]
    return mas_repetido1  # te trae el más repetido con su cantidad


def tirada_2():
    mas_repetido_1 = mas_repetido1()
    i = 0
    tirada = []
    while i < int(mas_repetido_1[1]):
        tirada += [int(mas_repetido_1[0])]
        i += 1
    tirada_2 = tirada
    n = len(tirada_2)
    for i in range(5-n):
        tirada_2.append(random.randint(1, 6))
    return tirada_2


def mas_repetido2():
    tirada2 = tirada_2()
    counter = Counter(tirada2)

    second = counter.most_common()
    num_repetido = [x[0] for x in second]
    cant_repeticiones = [x[1] for x in second]

    mas_repetido2 = [num_repetido[0], cant_repeticiones[0]]
    return mas_repetido2  # te trae el más repetido con su cantidad


def tirada_3():
    mas_repetido_2 = mas_repetido2()
    i = 0
    tirada = []
    while i < int(mas_repetido_2[1]):
        tirada += [int(mas_repetido_2[0])]
        i += 1
    tirada_3 = tirada
    n = len(tirada_3)
    for i in range(5-n):
        tirada_3.append(random.randint(1, 6))
    return tirada_3


def es_generala():
    tirada_f = tirada_3()

    return max(tirada_f) == min(tirada_f)


N = 1000

G = sum([es_generala() for i in range(N)])
prob = G/N

print(f'Tiré {N} veces, de las cuales {G} saqué generala .')
print(
    f'Podemos estimar la probabilidad de sacar generala mediante {prob:.6f}.')

# %%seeds


random.seed(31415)

tirada = []
for i in range(5):
    tirada.append(random.randint(1, 6))

print(tirada)

# %%

caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']

print(random.choice(caras))

# %%Ejercicio 5.3


def cumple():
    dia_de_cumpleaños = []
    for i in range(30):
        dia_de_cumpleaños.append(random.randint(1, 365))

    return dia_de_cumpleaños


def prob_cumple():

    cumple1 = cumple()
    counter = Counter(cumple1)
    repetido = counter.most_common()

    repeticiones = [x[1] for x in repetido]
    count = 0
    for repeticion in repeticiones:
        if repeticion > 1:
            count = 1

    return count


N = 10000

G = sum([prob_cumple() for i in range(N)])
prob = G/N

print(f'Probé {N} veces, de las cuales {G} coincidieron cumple.')
print(
    f'Podemos estimar la probabilidad de cumplir el mismo día mediante {prob:.6f}.')

# %%Ejercicio 5.4


# valores= [1,2,3,4,5,6,7,10,11,12]
# palos= ['basto', 'copa', 'espada', 'oro']
# naipes= [(valor,palo) for valor in valores for palo in palos]

# random.sample(naipes, k=3)

import random
# from collections import Counter

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(palo,valor) for valor in valores for palo in palos]
# mano = random.sample(naipes, k=3)

def envido(N): # N es el número de experimentos - manos de juego
    envido_31 = 0
    envido_32 = 0
    envido_33 = 0
    i = N
    while i > 0:
        mano = random.sample(naipes, k=3)
        mano.sort()
        
        puntos = 20

        if mano[0][0] == mano[1][0] and mano[0][0] != mano[2][0]:
            if mano[0][1] not in (10,11,12) and mano[1][1] not in (10,11,12):
                puntos += mano[0][1] + mano[1][1]
        
        if mano[0][0] == mano[2][0] and mano[0][0] != mano[1][0]:
            if mano[0][1] not in (10,11,12) and mano[2][1] not in (10,11,12):
                puntos += mano[0][1] + mano[2][1]
        
        if mano[1][0] == mano[2][0] and mano[1][0] != mano[0][0]:
            if mano[1][1] not in (10,11,12) and mano[2][1] not in (10,11,12):
                puntos += mano[1][1] + mano[2][1]
        
        if mano[0][0] == mano[1][0] and mano[0][0] == mano[2][0]:
            cartas = []
            for carta in mano:
                if carta[1] not in (10,11,12):
                    cartas.append(carta[1])
            
            if len(cartas) < 3:
                puntos += sum(cartas)
            if len(cartas) == 3:
                carta_mayor = max(cartas)
                cartas.remove(max(cartas))
                puntos  += max(cartas) + carta_mayor
                
        if puntos == 31:
            envido_31 += 1
        elif puntos == 32:
            envido_32 += 1
        elif puntos == 33:
            envido_33 += 1
                
        i -= 1
    
    prob_31 = envido_31/N
    prob_32 = envido_32/N
    prob_33 = envido_33/N
    print(f'La probabilidad de tener envido con 31 puntos es de {prob_31}')
    print(f'La probabilidad de tener envido con 32 puntos es de {prob_32}')
    print(f'La probabilidad de tener envido con 33 puntos es de {prob_33}')    
            
#%%
import numpy as np

a=np.array([1,2,3])

a

np.zeros(2)

np.ones(2)

np.empty(2)

np.arange(4)

np.arange(2,9,2)

np.linspace(0,10, num=5)

#%%Ejercicio 5.7

v=np.arange(1,19,2)
v
i=np.linspace(1,19,num=9)
i

arr=np.array([2,1,5,3,7,4,6,8])

np.sort(arr)
arr

a=np.array([1,2,3,4])
b=np.array([5,6,7,8])

np.concatenate((a,b))

csv_arr=np.array([1,2,3,4,5,6,7,8])
np.savetxt('new_file.csv', csv_arr)

np.loadtxt('new_file.csv')


#%%Ejercicio 5.8

import numpy as np
import random

def normalvariate():
    medicion= 37.2 + float(random.normalvariate(0,0.2))
    return medicion
    
def medir_temp(n):
    temperaturas=[]
    for _ in range(n):
        temp=normalvariate()
        temperaturas.append(temp)
        temperaturasnp=np.array(temperaturas)
    
    np.save('../Data/temperatuas.npy',temperaturasnp)
    return temperaturas,temperaturasnp



    



            
        
        
    




    
         
    
    
    




    
    
    
    
    
    





