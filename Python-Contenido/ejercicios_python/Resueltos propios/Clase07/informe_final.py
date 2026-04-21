# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 08:16:44 2022

@author: Luciano
"""

# tabla_informe.py

from fileparse import parse_csv
import sys
import csv
#%%

def leer_camion(nombre_archivo):
    camion= parse_csv(nombre_archivo,types= [str, int, float])
    return camion

#%%

def leer_precios(nombre_archivo):
    precios=dict(parse_csv(nombre_archivo, types = [str, float], has_headers = False))
    return precios


#%%
def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista

        
#%% Ejercicio 6.5

def informe_camion (nombre_archivo_camion,nombre_archivo_precios):

    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
        
#%% Ejercicio 7.4

def f_principal(parametros):
    if len (sys.argv)!=3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    camion=leer_camion[sys.argv[1]]
    precios=leer_precios[sys.argv[2]]
    informe=hacer_informe(camion,precios)
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')        
        
if __name__=='__main__':
  
    f_principal(sys.argv)
    
camion = parse_csv('../Data/camion.csv', types=[str,int,float])
camion
