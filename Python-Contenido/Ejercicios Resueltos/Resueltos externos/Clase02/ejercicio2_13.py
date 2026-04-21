# -*- coding: utf-8 -*-

#%% Ejercicio 2.12

import csv

f = open('../Data/missing.csv')
filas = csv.reader(f)
next(filas)

fila = next(filas)

# Creación de tupla

t = (fila[0], int(fila[1]), float(fila[2]))

cost = t[1] * t[2]

print(fila)
print(cost)
print(f'{cost:0.2f}')

# Creación de diccionario

d = {
     'nombre' : fila[0],
     'cajones' : int(fila[1]),
     'precio'  : float(fila[2])
     }

print(d)

cost = d['cajones'] * d['precio']
print(cost)

# Cambiando el número de cajones

d['cajones'] = 75
print(d)

# Agregando atributos

d['fecha'] = (14, 8, 2020)
d['cuenta'] = 12345

print(d)

#%% Ejercicio 2.12

for k in d:
    print('k =', k)
    
for k in d:
    print(k, '=', d[k])
    
print(list(d))

claves = d.keys()
print(claves)

nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
print(nuevos_items)

d = dict(nuevos_items)
print(d)