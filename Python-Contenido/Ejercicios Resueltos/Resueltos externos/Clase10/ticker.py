# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 14:01:48 2021

@author: Yamila
"""

from vigilante import vigilar
import csv
import informe_final
from formato_tabla import crear_formateador


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]    


def hace_dicts(rows, headers):      
    return (dict(zip(headers, row)) for row in rows)


def filtrar_datos(rows, nombres):
    return (row for row in rows if row['nombre'] in nombres)   


def imprimir_tabla(formateador, data):
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for linea in data:
        row = [linea['nombre'], str(linea['precio']), str(linea['volumen'])]
        formateador.fila(row)
        

def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    rows = parsear_datos(vigilar(log_file))
    datos = filtrar_datos(rows, camion)
    formateador = crear_formateador(fmt)
    imprimir_tabla(formateador, datos)


if __name__ == '__main__':
    # lines = vigilar('../Data/mercadolog.csv')
    # rows = parsear_datos(lines)
    # for row in rows:
    #     print(row)

    camion = informe_final.leer_camion('../Data/camion.csv')
    rows = parsear_datos(vigilar('../Data/mercadolog.csv'))
    rows = filtrar_datos(rows, camion)
    for row in rows:
        print(row)
