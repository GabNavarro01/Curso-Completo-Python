# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 21:07:01 2022

@author: Luciano
"""

#%% Ejercicio 3.6

for n in range(10):
    print(n, end='')
    
for n in range (10,0,-1):
    print(n,end='')
    
for n in range (0,10,2):
    print (n, end='')
    
    
#%% Ejercicio 3.7

data =[4,9,1,25,16,10,49]

min(data)
max(data)
sum(data)

for x in data:
    print(x, end=' ')
    
for n, x in enumerate(data):
    if n==2 or n==4 or n==6:
        continue
    print(n,x)
    
    
for n in range(len(data)):
    print(data[n])


#%% Ejercicio 3.8

import csv

def costo_camion (nombre_archivo):
    fila=0   
   
    with open(nombre_archivo,'rt') as f:
        rows=csv.reader(f)
        headers=next(rows)
        headers
        costo=float()
        try:
            
            for row in rows:
                           costo= costo + int(row[1])*float(row[2])
                           fila+=1
            return costo
        except ValueError:
            print(f'Fila {fila}: No pude interpretar: {row}')
   
costo= costo_camion('../Data/missing.csv')
print(f'Costo total: ${costo}')

#%% Ejercicio 3.9

f= open ('../Data/missing.csv', 'rt')
filas= csv.reader(f)
encabezados=next(filas)
encabezados

fila=next(filas)
fila

list(zip(encabezados, fila))

record=dict(zip(encabezados, fila))
record


import csv

def costo_camion (nombre_archivo):
     
   
    with open(nombre_archivo,'rt') as f:
        filas=csv.reader(f)
        encabezados=next(filas)        
        costo_total=float()
       
        for n_fila, fila in enumerate (filas, start=1):
            record= dict(zip(encabezados, fila))
            
            try:
                ncajones= int(record['cajones'])
                precio= float(record['precio'])
                costo_total+= ncajones * precio
                
            except ValueError:
                print(f' Fila {n_fila}: No pude interpretar: {fila}')
        
       
        return costo_total
        
   
costo_total= costo_camion('../Data/fecha_camion.csv')
print(f'Costo total: ${round(costo_total,2)}')

#%% Ejercicio 3.10

precios = {
       'Pera' : 490.1,
       'Lima' : 23.45,
       'Naranja' : 91.1,
       'Mandarina' : 34.23
}

precios.items()

lista_precios= list(zip(precios.values(),precios.keys()))
lista_precios

#%%Ejercicio 3.11

#%% Precio pagado al productor

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        camion = []
        for i,row in enumerate(rows, start=1):
            record = dict(zip(encabezados, row))
            try:
                camion.append(record)
            except ValueError:
                print(f'Fila {i}: No pude interpretar: {row}')
        return camion
    
#%% Precio de venta

def leer_precio(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        precios = {}
        for i,row in enumerate(rows):
            try:
                precios[row[0]] = float(row[1])
            except IndexError:
                print(f'Ups! no logro entender la línea {i+1}:{row}')
        return precios

#%% Balance

archivo_camion = '../Data/camion.csv'
archivo_precios ='../Data/precios.csv'

camion = leer_camion(archivo_camion)
precios = leer_precio(archivo_precios)

costo_camion = 0
total_vendido = 0

for producto in camion:
    nombre = producto['nombre']
    cajones = producto['cajones']
    costo = producto['precio']
    costo_camion += int(cajones) * float(costo)
    
    precio_venta = precios[nombre]
    total_vendido += int(cajones) * float(precio_venta)
    
balance = total_vendido - costo_camion

print('*'*22)
print('*BALANCE DE VERDULERÍA*')
print('*'*22)
print(f'Costo del camión: {costo_camion:.2f}\nVenta: {total_vendido:.2f}\nBalance:{balance:.2f}')

#%% Ejercicio 3.11

from collections import Counter
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += int(s['cajones'])
    
tenencias
tenencias.most_common(3)    

camion2= leer_camion('../Data/camion2.csv')
tenencias2= Counter ()
for s in camion2:
    tenencias2[s['nombre']]+= int(s['cajones'])
    
tenencias2

tenencia_combinada= tenencias + tenencias2

tenencia_combinada

#%% Ejercicio 3.12

value = 42863.1
print(value)

print (f'{value:>16.2f}')

#%% Ejercicio 3.13















    
