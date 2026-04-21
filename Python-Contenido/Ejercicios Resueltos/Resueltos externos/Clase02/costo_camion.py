# -*- coding: utf-8 -*-

#%% Ejercicio 2.2: Lectura de un archivo de datos

f = open('../Data/camion.csv', 'rt')
headers = next(f).split(',')

costo = float()

for line in f:
    row = line.split(',')
    costo = costo + (int(row[1]) * float(row[2]))
    
print(f'Costo total: $ {costo}')

f.close()

#%% Ejercicio 2.6: Transformar un script en una función

def costo_camion(nombre_archivo):
   with open(nombre_archivo, 'rt') as f:
       next(f).split(',')
       costo = float()
       for line in f:
           row = line.split(',')
           costo += (int(row[1]) * float(row[2]))
       return costo
    
costo = costo_camion('../Data/camion.csv')
print(f'Costo total: $ {costo}')

#%% Ejercicio 2.8: Administración de errores

def costo_camion(nombre_archivo):
   with open(nombre_archivo, 'rt') as f:
       next(f).split(',')
       costo = float()
       try:
           for line in f:
               row = line.split(',')
               costo += (int(row[1]) * float(row[2]))
           return costo
           print(f'Costo total: $ {costo}')
       except ValueError:
           print('El archivo no contiene todos los datos, no es posible procesarlo.')
    
costo = costo_camion('../Data/missing.csv')

#%% Ejercicio 2.9: Funciones de la biblioteca

import csv

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