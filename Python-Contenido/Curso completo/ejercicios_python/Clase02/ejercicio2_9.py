# -*- coding: utf-8 -*-

#%% Ejercicio 2.6 (costo_camion mdificado)

def costo_camion(nombre_archivo):
   with open('../Data/camion.csv', 'rt') as f:
       next(f).split(',')
       costo = float()
       for line in f:
           row = line.split(',')
           costo += (int(row[1]) * float(row[2]))
       return costo
    
costo = costo_camion('../Data/camion.csv')
print(f'Costo total: $ {costo}')

#%% Ejercicio 2.9

# import csv

# f = open('../Data/missing.csv')
# rows = csv.reader(f)
# headers = next(rows)
# print(headers)

# for row in rows:
#     print(row)

# f.close()

#%%
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