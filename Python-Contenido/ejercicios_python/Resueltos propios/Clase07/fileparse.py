# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 08:43:43 2022

@author: Luciano
"""
import csv
#%%fileparse.py
#%%Ejercicio 6.6
# import csv

# def parse_csv(nombre_archivo):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows=csv.reader(f)
#         headers=next(rows)
#         registros=[]
#         for row in rows:
#             if not row:
#                 continue
#             registro=dict(zip(headers,row))
#             registros.append(registro)
            
#         return registros
    
    
#%%Ejercicio 6.7

# import csv

# def parse_csv(nombre_archivo, select=None):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows=csv.reader(f)
#         headers=next(rows)
        
#         if select:
#             indices=[headers.index(nombre_columna) for nombre_columna in select]
#             headers=select
            
#         else:
#             indices=[]
            
            
#         registros=[]
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row=[row[index] for index in indices]
           
#             registro=dict(zip(headers,row))
#             registros.append(registro)
            
#         return registros
    
#%%Ejercicio 6.8


# def parse_csv(nombre_archivo, select=None, types=None):
#     '''
#     Parsea un archivo CSV en una lista de registros
#     '''
#     with open(nombre_archivo) as f:
#         rows=csv.reader(f)
#         headers=next(rows)
        
#         if select:
#             indices=[headers.index(nombre_columna) for nombre_columna in select]
#             headers=select
            
#         else:
#             indices=[]
       
            
#         registros=[]
#         for row in rows:
#             if not row:
#                 continue
#             if indices:
#                 row=[row[index] for index in indices]
#             if types:
#                 row= [func(val) for func, val in zip(types, row)]
#             registro=dict(zip(headers,row))
#             registros.append(registro)
                
#         return registros


# camion = parse_csv('../Data/camion.csv', select=None, types=[str, int, float])
# camion

#%%Ejercicio 6.9

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True, silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        if has_headers == True:
            # Lee los encabezados del archivo
            encabezados = next(filas)
    
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
            if select:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
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
                        
            return registros
    
    if select != None and has_headers == False:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
    return registros
# camion = parse_csv('../Data/camion.csv', select=['nombre','cajones'])




















    