# -*- coding: utf-8 -*-

import csv
from collections import Counter
import os
import matplotlib.pyplot as plt
import numpy as np

#%% Ejercicio 3.18: Lectura de los árboles de un parque

def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, encoding="utf8") as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        arboles = []
        for i,row in enumerate(rows, start=1):
            if row[10] == parque:
                record = dict(zip(encabezados, row))
                arboles.append(record)
        return arboles

info_parque = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')

#%% Ejercicio 3.19: Determinar las especies en un parque

def especies(lista_arboles):
    especies = set()
    for i in lista_arboles:
        especies.add(i['nombre_com'])
    return especies

conjunto_especies = especies(info_parque)

#%% Ejercicio 3.20: Contar ejemplares por especie

def contar_ejemplares(lista_arboles):
    ejemplares = Counter()
    for k in lista_arboles:
        ejemplares[k['nombre_com']] += 1
    return ejemplares
    
cantidad_ejemplares = contar_ejemplares(info_parque)
# print(cantidad_ejemplares.most_common(5))

#%% most_common()

def contar_ejemplares(lista_arboles):
    ejemplares = Counter()
    for k in lista_arboles:
        ejemplares[k['nombre_com']] += 1
    print(cantidad_ejemplares.most_common(5))

#%% Ejercicio 3.21: Alturas de una especie en una lista

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for k in lista_arboles:
        if k['nombre_com'] == especie:
            alturas.append(float(k['altura_tot']))
    return alturas

alturas_especie = obtener_alturas(info_parque, 'Jacarandá')
altura_máxima = max(alturas_especie)
promedio_altura = round(sum(alturas_especie) / len(alturas_especie), 2)

# print(altura_máxima)
# print(promedio_altura)

#%% Ejercicio 3.22: Inclinaciones por especie de una lista

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for k in lista_arboles:
        if k['nombre_com'] == especie:
            inclinaciones.append(float(k['inclinacio']))
    return inclinaciones

inclinaciones_especie = obtener_inclinaciones(info_parque, 'Palo borracho rosado')

#%% Ejercicio 3.23: Especie con el ejemplar más inclinado

def especimen_mas_inclinado(lista_arboles):
    especie_inclinacion = ['', 0.0]
    for arbol in lista_arboles:
        if float(arbol['inclinacio']) > especie_inclinacion[1]:
            arbol_inclinado = [arbol['nombre_com'], float(arbol['inclinacio'])]
            especie_inclinacion = arbol_inclinado
    return especie_inclinacion
    # print(f'La especie más inclinada es: {especie_inclinacion[0]} y su inclinación es de: {especie_inclinacion[1]}')

especie_mas_inclinada = especimen_mas_inclinado(info_parque)

#%% Ejercicio 3.24: Especie más inclinada en promedio

#%% Ejercicio 4.15: Lectura de todos los árboles

def leer_arboles(nombre_archivo):
    with open(nombre_archivo, encoding="utf8") as f:
        rows = csv.reader(f)
        encabezados = next(rows)
        types = [float, float, int, float, float, float, int, str, str, str, str, str, str, str, str, float, float]
        arboleda = [{ name: func(val) for name, func, val in zip(encabezados, types, row)} for row in rows]
    return arboleda

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')

#%% Ejercicio 4.16: Lista de altos de Jacarandá

H = [float(arbol['altura_tot']) for arbol in arboleda]

h_jacaranda = [h['altura_tot'] for h in arboleda if h['nombre_com'] == 'Jacarandá']

#%% Ejercicio 4.17: Lista de altos y diámetros de Jacarandá

h_d_jacaranda = [(hd['altura_tot'], hd['diametro']) for hd in arboleda if hd['nombre_com'] == 'Jacarandá']

#%% Ejercicio 4.18: Diccionario con medidas

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies,arboleda):
    diccionario = {clave: [(hd['altura_tot'], hd['diametro']) for hd in arboleda if hd['nombre_com'] == clave] for clave in especies}
    return diccionario

#%% Ejercicio 5.25: Histograma de altos de Jacarandás

def histograma_altos_jacaranda():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = [h['altura_tot'] for h in arboleda if h['nombre_com'] == 'Jacarandá']
    plt.hist(altos,bins=25)

#%% Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás

def scatter_hd(lista_de_pares):
    pares = np.array(lista_de_pares)
    h = np.array(pares)[:,0]
    d = np.array(pares)[:,1]
    
    plt.scatter(d, h, c = d*h, alpha = .5)
    plt.xlim(0,150)
    plt.ylim(0,40)
    plt.xlabel('diámetro (cm)')
    plt.ylabel('alto (m)')
    
#%% Ejercicio 5.27: Scatterplot para diferentes especies

'''Está mal este ejercicio, no salen 3 gráficos separados, sino todo en uno'''

def scater_distintas_especies():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    
    scatter_hd(medidas['Eucalipto'])
    scatter_hd(medidas['Palo borracho rosado'])
    scatter_hd(medidas['Jacarandá'])
