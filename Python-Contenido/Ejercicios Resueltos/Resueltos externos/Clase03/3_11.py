# -*- coding: utf-8 -*-

import csv

# def costo_camion(nombre_archivo):
#     with open(nombre_archivo, 'rt') as f:
#         filas = csv.reader(f)
#         encabezados = next(filas)
#         costo_total = float()
#         for n_fila, fila in enumerate(filas, start=1):
#             record = dict(zip(encabezados, fila))
#             try:
#                 ncajones = int(record['cajones'])
#                 precio = float(record['precio'])
#                 costo_total += ncajones * precio
#             # Esto atrapa errores en los int() y float() de arriba.
#             except ValueError:
#                 print(f'Fila {n_fila}: No pude interpretar: {fila}')
#         return costo_total
    
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
    
print(tenencias)
print(tenencias.most_common(3))


camion2 = leer_camion('../Data/camion2.csv')
tenencias2 = Counter()
for s in camion2:
    tenencias2[s['nombre']] += int(s['cajones'])
    
print(tenencias2)

combinada = tenencias + tenencias2
print(combinada)