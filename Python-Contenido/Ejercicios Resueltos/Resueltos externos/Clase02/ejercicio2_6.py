# -*- coding: utf-8 -*-

#%% Ejercicio 2.2 (costo_camion)

f = open('../Data/camion.csv', 'rt')
headers = next(f).split(',')

costo = float()

for line in f:
    row = line.split(',')
    costo = costo + (int(row[1]) * float(row[2]))
    
print(f'Costo total: $ {costo}')

f.close()

#%% Ejercicio 2.6 propiamente

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