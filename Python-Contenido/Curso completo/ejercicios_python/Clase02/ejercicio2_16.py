# -*- coding: utf-8 -*-

#%% Ejercicio 2.15 (informe.py)

# import csv

# def leer_camion(nombre_archivo):
#     camion = []
#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         next(rows)
#         for row in rows:
#             lote = (row[0], int(row[1]), float(row[2]))
#             camion.append(lote)
#     return camion


# camion = leer_camion('../Data/camion.csv')
# print(camion)

# total = 0.0

# for nombre, cajones, precio in camion:
#     total += cajones * precio
    
# print(total)

# from pprint import pprint

# pprint(camion)

#%%

import csv

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            lote = {}
            lote['Fruta'] = row[0]
            lote['Cajones'] = int(row[1])
            lote['Precio'] = float(row[2])
            camion.append(lote)
        return camion
    
camion = leer_camion('../Data/camion.csv')
print(camion)

print(camion[0])
print(camion[1])
print(camion[1]['Cajones'])

total = 0.0

for s in camion:
    total += s['Cajones'] * s['Precio']
    
print(total)

from pprint import pprint
pprint(camion)