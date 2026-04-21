# -*- coding: utf-8 -*-

#%% Ejercicio 2.9 (costo_camion con última modificación)

# import csv

# def costo_camion(nombre_archivo):
#    with open(nombre_archivo, 'rt') as f:
#        rows = csv.reader(f)
#        headers = next(rows)
#        headers
#        costo = float()
#        for row in rows:
#            costo += round(int(row[1]) * float(row[2]), 2)     
#        return costo
       
# costo = costo_camion('../Data/camion.csv')
# print(f'Costo total: $ {costo}')

#%% Ejercicio 2.10 (camion_commandline)

import csv
import sys

def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        costo = float()
        for row in rows:
            costo += round(int(row[1]) * float(row[2]), 2)     
        return costo
    
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/missing.csv'

costo = costo_camion(nombre_archivo)
print('Costo total: $', costo)