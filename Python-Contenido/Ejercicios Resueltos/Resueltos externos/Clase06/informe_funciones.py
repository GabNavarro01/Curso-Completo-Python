# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:58:15 2021

@author: Yamila
"""

import fileparse

#%%
def leer_camion(nombre_archivo):
    camion = fileparse.parse_csv(nombre_archivo, types = [str, int, float])
    return camion

#%%

def leer_precios(nombre_archivo):
    precios = dict(fileparse.parse_csv(nombre_archivo, types = [str, float], has_headers = False))
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

#%%

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')