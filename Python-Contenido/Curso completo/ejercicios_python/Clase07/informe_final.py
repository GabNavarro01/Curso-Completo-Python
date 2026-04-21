# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:58:15 2021

@author: Yamila
"""

import fileparse

#%%
def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        camion = fileparse.parse_csv(f, types = [str, int, float])
    return camion

#%%

def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = dict(fileparse.parse_csv(f, types = [str, float], has_headers = False))
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
        
#%% Ejercicio 7.4: Función principal

def f_principal(parametros):
    if len(sys.argv) != 3:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios')
    camion = leer_camion(sys.argv[1])
    precios = leer_precios(sys.argv[2])
    informe = hacer_informe(camion, precios)
    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    
    
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)