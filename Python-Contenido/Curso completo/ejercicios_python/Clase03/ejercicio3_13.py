# -*- coding: utf-8 -*-

import csv

#%% Precio pagado al productor

def leer_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        camion = []
        for row in rows:
            lote = {}
            lote['nombre'] = row[0]
            lote['cajones'] = int(row[1])
            lote['precio'] = float(row[2])
            camion.append(lote)
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
    costo_camion += cajones * costo
    
    precio_venta = precios[nombre]
    total_vendido += cajones * precio_venta
    
balance = total_vendido - costo_camion

print('*'*22)
print('*BALANCE DE VERDULERÍA*')
print('*'*22)
print(f'Costo del camión: {costo_camion:.2f}\nVenta: {total_vendido:.2f}\nBalance:{balance:.2f}')

#%% Ejercicio 3.13 y subsiguientes (tabla_informe.py)

def hacer_informe(cajon, precio):
    informe = []
    for i in cajon:
        diccionario_cajon = i
        if diccionario_cajon['nombre'] in precio.keys():
            tupla = (diccionario_cajon['nombre'], diccionario_cajon['cajones'], diccionario_cajon['precio'], precios[diccionario_cajon['nombre']] - diccionario_cajon['precio'])
            informe.append(tupla)
    return informe
    
informe = hacer_informe(camion, precios)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:
    precio_con_signo = '$' + str(round(precio, 2))
    print(f'{nombre:>10s} {cajones:>10d} {precio_con_signo:>10s} {cambio:>10.2f}')
