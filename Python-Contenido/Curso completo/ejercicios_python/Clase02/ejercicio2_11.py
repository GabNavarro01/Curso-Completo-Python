# -*- coding: utf-8 -*-

import csv

f = open('../Data/missing.csv')
filas = csv.reader(f)
next(filas)

fila = next(filas)

t = (fila[0], int(fila[1]), float(fila[2]))

cost = t[1] * t[2]

print(cost)
print(f'{cost:0.2f}')

# Asignación de nueva tupla

t = (t[0], 75, t[2])
print(t)

# Desempaquetar valores en tuplas

nombre, cajones, precio = t
print(nombre)
print(cajones)
print(precio)

# Empaquetar valores en una tupla

t = (nombre, 2*cajones, precio)
print(t)