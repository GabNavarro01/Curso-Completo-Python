# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 13:24:23 2022

@author: Luciano
"""

#%%Ejercicio 4.5
import csv

def leer_arboles (nombre_archivo):
    arboleda=[]
    f=open(nombre_archivo, 'rt', encoding='utf8')
    rows=csv.reader(f)
    headers=next(rows)
    
    types=[float, float, int, float, float, float, int, str, str, str, str, str, str, str, str, float, float]
    arboleda=[{name: func(val) for name, func, val in zip(headers, types, row)} for row in rows]
    return arboleda

arboleda=leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
arboleda
    
#%%Ejercicio 4.16

H= [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']== 'Jacarandá']
H

#%%Ejercicio 4.17

H= [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']== 'Jacarandá']
H

#%%Ejercicio 4.18

especies= ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    medidas={especie: [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==especie] for especie in especies}
    return medidas

medidas= medidas_de_especies(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'], arboleda)
medidas




