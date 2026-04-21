# -*- coding: utf-8 -*-

import csv

#%% Función costo_camion

def costo_camion(nombre_archivo):
   with open(nombre_archivo, 'rt') as f:
       rows = csv.reader(f)
       headers = next(rows)
       headers
       costo = float()
       for row in rows:
           costo += round(int(row[1]) * float(row[2]), 2)     
       return costo
       
costo = costo_camion('../Data/camion.csv')
print(f'Costo total: $ {costo}')

#%% Ejercicio 3.8: Un ejemplo práctico de enumerate()

def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        headers = next(filas)
        headers
        costo = float()
        for n_fila, fila in enumerate(filas, start=1):
            try:
                costo += round(int(fila[1]) * float(fila[2]), 2) 
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        return costo

costo = costo_camion('../Data/missing.csv')
