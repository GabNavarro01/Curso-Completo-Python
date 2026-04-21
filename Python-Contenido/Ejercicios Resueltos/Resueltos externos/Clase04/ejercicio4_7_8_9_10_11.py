# -*- coding: utf-8 -*-

#%% Ejercicio 4.7: Comprensión de listas

nums = [1,2,3,4]

cuadrados = [x*x for x in nums]

dobles = [2*x for x in nums if x>2]

#%% Ejercicio 4.8: Reducción de secuencias

# Se importa la función leer_camion de informe.py y se realizan distintas consultas desde ahí.

camion = leer_camion('../Data/camion.csv')

costo = sum( int([s['cajones']) * float(s['precio']) for s in camion] )

#%% Ejercicio 4.9: Consultas de datos

mas100 = [s for s in camion if int(s['cajones']) > 100]

myn = [s for s in camion if s['nombre'] in {'Mandarina','Naranja'}]

costo10k = [s for s in camion if int(s['cajones']) * float(s['precio']) > 10000]

#%% Ejercicio 4.10: Extracción de datos

# Comprensión de lista

nombre_cajones = [(s['nombre'], s['cajones']) for s in camion]

# Comprensión de conjuntos

nombre_cajones = {(s['nombre'], s['cajones']) for s in camion}

nombres = {s['nombre'] for s in camion}

# Diccionario

stock = {nombre: 0 for nombre in nombres}

for s in camion:
    stock[s['nombre']] += int(s['cajones'])
    
camion_precios = {nombre: precios[nombre] for nombre in nombres}

#%% Ejercicio 4.11: Extraer datos de un archivo CSV

import csv

f = open('../Data/fecha_camion.csv')
rows = csv.reader(f)
headers = next(rows)

select = ['nombre', 'cajones', 'precio']

indices = [headers.index(ncolumna) for ncolumna in select]

row = next(rows)

record = {ncolumna: row[index] for ncolumna, index in zip(select, indices)}

camion = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]