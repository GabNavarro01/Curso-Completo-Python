# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:58:15 2021

@author: Yamila
"""

import fileparse
import lote
import formato_tabla

# %%


def leer_camion(nombre_archivo):
    with open(nombre_archivo) as f:
        camion_dicts = fileparse.parse_csv(
            f, select=['nombre', 'cajones', 'precio'], types=[str, int, float])
        camion = [lote.Lote(d['nombre'], d['cajones'], d['precio'])
                  for d in camion_dicts]
    return camion

# %%


def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = dict(fileparse.parse_csv(
            f, types=[str, float], has_headers=False))
    return precios

# %%


def hacer_informe(camion, precios):
    lista = []
    for item in camion:
        precio_venta = precios[item.nombre]
        cambio = precio_venta - item.precio
        t = (item.nombre, item.cajones, precio_venta, cambio)
        lista.append(t)
    return lista

# %%


def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv (fmt = 'csv') o .html (fmt = 'html').
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)

# %%


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

# %% Ejercicio 7.4: Función principal


def f_principal(parametros):
    if len(sys.argv) > 4:
        raise SystemExit(
            f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios fmt (opcional, por defecto el formato es .txt')
    
    try:
        informe_camion(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        informe_camion(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
