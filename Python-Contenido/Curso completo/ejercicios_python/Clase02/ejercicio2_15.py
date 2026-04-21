# -*- coding: utf-8 -*-

#%% Función de referencia

# import csv

# def costo_camion(nombre_archivo):
#     # Computa el precio total del camión (cajones * precio) de un archivo.
#     total = 0.0

#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         next(rows)
#         for i, row in enumerate(rows):
#             try:
#                 ncajones = int(row[1])
#                 precio = float(row[2])
#                 total += ncajones * precio
#             except ValueError:
#                 print('Faltan datos en la línea', i, 'del archivo.')
#     return total

#%% informe.py

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
    return camion


camion = leer_camion('../Data/camion.csv')
total = 0.0

for nombre, cajones, precio in camion:
    total += cajones * precio
    
print(total)

pprint(camion)