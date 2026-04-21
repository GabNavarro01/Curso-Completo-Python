# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 08:36:08 2022

@author: Luciano
"""
import csv
import informe_funciones

f= open ('../Data/missing.csv', 'rt')
filas= csv.reader(f)
encabezados=next(filas)
encabezados

fila=next(filas)
fila

list(zip(encabezados, fila))

record=dict(zip(encabezados, fila))
record

import csv

def costo_camion (nombre_archivo):
     
   
        costo_total= informe_funciones.leer_camion(nombre_archivo)
        
       
        return costo_total
        
   
