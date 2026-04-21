# -*- coding: utf-8 -*-

import csv
from collections import Counter

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
print(cantidad_ejemplares)
print(cantidad_ejemplares.most_common(5))

#%% most_common()

# def contar_ejemplares(lista_arboles):
#     ejemplares = Counter()
#     for k in lista_arboles:
#         ejemplares[k['nombre_com']] += 1
#     print(cantidad_ejemplares.most_common(5))

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

def especie_promedio_mas_inclinada(lista_arboles):
    cantidad_por_ejemplar = contar_ejemplares(lista_arboles)
    for arbol in lista_arboles:
        inclinaciones = obtener_alturas(lista_arboles, arbol)
        
            
    return inclinaciones

mas_inclinado = especie_promedio_mas_inclinada(info_parque)


def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles) #obtengo todas las especies de la lista
    maximo = 0.0
    for row in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles,row)
        if maximo <= max(inclinaciones):
            maximo = max(inclinaciones)
            especie = row
    return especie, maximo





