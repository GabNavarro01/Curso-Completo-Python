# -*- coding: utf-8 -*-

#%% Ejercicio 4.12: Datos de primera clase

import csv

types = [str, int, float]

f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)

r = list(zip(types, row))

#%%
converted = []

for func, val in zip(types, row):
          converted.append(func(val))
          
#%%
#El código del bloque anterior se puede comprimir usando comprensión de listas:
    
converted = [func(val) for func, val in zip(types, row)]

#%% Ejercicio 4.13: Diccionarios

# Armo un diccionarios desde 2 listas (headers y converted)
dict(zip(headers, converted))

# Resumo el proceso del diccionario anterior en 1 línea

{ name: func(val) for name, func, val in zip(headers, types, row) }

#%% Ejercicio 4.14: Fijando ideas

f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
headers

types = [str, float, str, str, float, float, float, float, int]

converted = [func(val) for func, val in zip(types, row)]

record = dict(zip(headers, converted))
