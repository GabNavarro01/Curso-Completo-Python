# -*- coding: utf-8 -*-

#%% Ejercicio 2.7

# def buscar_precio(fruta):
#     with open('..\Data\precios.csv', 'rt') as f:
#         listado_frutas = [ ]
#         for line in f:
#             row = line.split(',')
#             listado_frutas.append(row[0])
#             if row[0] == fruta:
#                 print(f'El precio de un cajón de {fruta} es $ {float(row[1])}')
#         if fruta not in listado_frutas:
#             print(f'{fruta} no figura en el listado de precios')
            
#%% Ejercicio 2.17

import csv

def leer_precio(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        precios = {}
       
        try:
            
           for row in rows:
                #print(row)
                precios[row[0]] = float(row[1])
     
        except TypeError:
        except IndexError:
        
            return precios
        
precios = leer_precio('../Data/precios.csv')
print(precios['Naranja'])
print(precios['Mandarina'])
