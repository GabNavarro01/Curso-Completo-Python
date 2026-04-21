# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 07:15:41 2022

@author: Luciano
"""

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        i += 1
        if expresion[i] == 'a':
            return True
        else:
            return False
            

rta = tiene_a ('palabra')
# print(rta)

#%% Ejercicio 4.1

def invertir_lista(lista):
    
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        # invertida.append (lista.pop(i))  #####Paso clave ja
    return invertida

l = [1, 2, 3, 4, 5]    
m = invertir_lista(l)
# print(f'Entrada {l}, Salida: {m}')

#%% Ejercicio 4.1

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
# pprint(camion)

#%% Ejercicio 4.2

def buswueda_con_index (lista, e):
    if e in lista:
        pos=lista.index(e)
    else:
        pos=-1
        
    return pos

#%% Ejercicio 4.2.1

def busqueda_lineal(lista,e):
    pos=-1 
    
    for i, z in enumerate(lista):
        if z==e:
            pos= i
            break        
    return pos

#%% Ejercicio 4.3

def buscar_u_elemento(lista,e):
    pos=-1 
    
    for i, z in enumerate(lista):
        if z==e:
            pos= i
                   
    return pos

#%%

def buscar_n_elemento(lista,e):
    
    cant=0
    for i,z in enumerate(lista):
        if z==e:
            cant+=1
    
    return cant

#%% Ejercicio 4.4

def maximo(lista):
    m=-999
    for e in lista:
        if m<e:
            m=e
    return m

def min(lista):
    m=999
    for e in lista:
        if m>e:
            m=e
    return m

#%% Ejercicios al 4.11

#%% Informe

#%%Costo_camion

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
        
   
#%%Precio de venta


def leer_precio(fruta):
    f = open('../Data/precios.csv', 'r')
    rows=csv.reader(f)
    precios = {}
    
    try:
        for row in rows:            
                
                precios[row[0]]=float(row[1])
                
    except IndexError:
           print(f'Ups! no logro entender la línea:{row}')
    
    return precios
  
precios=leer_precio('../Data/precios.csv')


#%%Precio de Compra

from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers=next(rows)
        for n_row, row in enumerate(rows, start=1):
            record=dict(zip(headers,row))

            try:
             
               camion.append(record)
               
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
    return camion
     
camion= leer_camion('../Data/camion.csv')

pprint(camion)

# costo_total=0.0

# for s in camion:
#         costo_total += s['Cajon'] * s['Precio']


#%%Balance

archivo_camion='../Data/camion.csv'
archivo_precios='../Data/precios.csv'

camion= leer_camion(archivo_camion)
precios= leer_precio(archivo_precios)

costo_camion= 0
total_vendido= 0

for producto in camion:
    nombre=producto['nombre']
    cajones=producto['cajones']
    precio=producto['precio']
    costo_camion += int(cajones) * float(precio)
    
    precio_venta= precios[nombre]
    total_vendido+= float(precio_venta) * int(cajones)
    
balance = total_vendido - costo_camion

print(f'La empresa ganó ${round(balance,2)}')

print(f'La mercadería costó ${costo_camion}')

print(f'Se vendió un total de ${total_vendido}')




















#%% Ejercicio 4.7

nums= [1,2,3,4]
cuadrados=[x*x for x in nums]
cuadrados

dobles= [2*x for x in nums]
dobles

#%% Ejercicio 4.8

camion= leer_camion('../Data/camion.csv')
costo= [sum(int(s['cajones'])*float(s['precio']) for s in camion)]
costo

precios= leer_precio('../Data/precios.csv')
valor= sum([int(s['cajones'])*float(precios[s['nombre']]) for s in camion])
valor

#%% Ejercicio 4.9

mas100=[fruta for fruta in camion if int(fruta['cajones'])>100]
mas100

myn=[s for s in camion if s['nombre'] in {'Mandarina', 'Naranja'}]
myn

mas10000=[fruta for fruta in camion if float(fruta['precio'])*int(fruta['cajones'])>10000]
mas10000

#%% Ejercicio 4.10

nombre_cajones= [(s['nombre'], s['cajones']) for s in camion]
nombre_cajones

nombres= {s['nombre'] for s in camion}
nombres

stock={nombre: 0 for nombre in nombres}
stock

camion_precios= {nombre: precios[nombre] for nombre in nombres}
camion_precios

#%% Ejercicios 4.11

import csv
f=open('../Data/camion.csv')
rows=csv.reader(f)
headers=next(f)

headers

select= ['nombre', 'cajones', 'precio']
select

indices =[headers.index(ncolumna) for ncolumna in select]
indices

rows= next(row)
record= {ncolumna: row[index] for ncolumna, index in zip(select, indices)}
record

#%%Ejercicios 4.12

types = [str, int, float]

import csv

f=open('../Data/camion.csv')
rows=csv.reader(f)
headers=next(rows)
row=next(rows)
row

types[2](row[2])

r=list(zip(types,row))
r

converted= []
for func, val in zip(types, row):
    converted.append(func(val)) 

converted   

converted[1]*converted[2]    

converted= [func(val) for func, val in zip(types,row)]
converted

#%%Ejercicios 4.13

headers
converted

dict(zip(headers, converted))

#%%Ejercicios 4.14

## Era un ejemplo




