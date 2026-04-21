# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:50:16 2021

@author: Yamila
"""

import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True,
              silence_errors = False):
       
    filas = csv.reader(nombre_archivo)
    if has_headers == True:
        # Lee los encabezados del archivo
        encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # En ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for 
                       nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for i,fila in enumerate(filas):
            try:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                # Convierte los tipos de datos
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
            except ValueError as e:
                if not silence_errors:
                    print(f'Fila {i+1}: no pude convertir  {fila}')
                    print(f'Fila {i+1}: {e}')
    if has_headers == False:
        registros = [ ]
        for fila in filas:
            if not fila:
                continue
            if types:
                fila = [func(val) for func, val in zip(types, fila)]
            registro = tuple(fila)
            registros.append(registro)
    
    if select != None and has_headers == False:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
    return registros

# camion = parse_csv('../Data/camion.csv', select=['nombre','cajones'])