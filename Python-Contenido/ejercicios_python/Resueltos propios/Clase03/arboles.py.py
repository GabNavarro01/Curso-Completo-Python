
#%%Ejercicio 3.18


import csv

def leer_parque(nombre_archivo, parque):
    info=[]
    
    with open (nombre_archivo, 'rt', encoding='utf8') as data:
        datos= csv.reader(data)
        headers=next(datos)
        
                
        for i, dato in enumerate(datos):
            if dato[10] == parque :
            
                record=dict(zip(headers,dato))
                info.append(record)
                    
        return info


arboles=leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')

#%%Ejercicio 3.19

def especies (lista_arboles):
    especies=set()
  
    for i in lista_arboles:
        especies.add(i['nombre_com'])
    return especies

conjunto_especies= especies(arboles)

conjunto_especies
        
#%%Ejercicio 3.20

from collections import Counter

def contar_ejemplares (lista_arboles):
    ejemplares=Counter()
    for i in lista_arboles:
        ejemplares[i['nombre_com']]+= 1
    
    return ejemplares


lista_arboles1= leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
contar_ejemplares (lista_arboles1)
   
lista_arboles2= leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
contar_ejemplares (lista_arboles2)
    
lista_arboles3= leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
contar_ejemplares (lista_arboles3)
    
recuento1=contar_ejemplares (lista_arboles1)
recuento2=contar_ejemplares (lista_arboles2)
recuento3=contar_ejemplares (lista_arboles3)

# print(recuento1.most_common(5)) 
# print(recuento2.most_common(5))     
# print(recuento3.most_common(5))     

#%%Ejercicio 3.21

import statistics

def obtener_alturas (lista_arboles, especie):
    alturas=[]
    for k in lista_arboles:
        if k['nombre_com']== especie:
            alturas.append(float(k['altura_tot']))
    return alturas            

alturas_especie= obtener_alturas(lista_arboles3, 'Jacarandá')
altura_máxima=max(alturas_especie)
altura_prom= statistics.mean(alturas_especie)
    
# print(alturas_especie)
# print (altura_máxima)
# print(altura_prom)    

#%%Ejercicio 3.22

def obtener_inclinaciones (lista_arboles, especie):
    inclinaciones=[]
    for k in lista_arboles:
        if k['nombre_com']== especie:
            inclinaciones.append(float(k['inclinacio']))
    return inclinaciones            

inclinacio_especie= obtener_inclinaciones(lista_arboles1, 'Jacarandá')

# print(inclinacio_especie)

#%%Ejercicio 3.23

import statistics

def especimen_mas_inclinado (lista_arboles):
    especie_inclinacion = ['', 0.0]
    for arbol in lista_arboles:
        if float(arbol['inclinacio'])> especie_inclinacion[1]:
            arbol_inclinado= [arbol['nombre_com'], float(arbol['inclinacio'])]
            especie_inclinacion = arbol_inclinado
    return especie_inclinacion

e= especimen_mas_inclinado (arboles)

# print (e)

#%%Ejercicio 3.24

def especie_promedio_mas_inclinada(lista_arboles):
    
    cantidad_por_ejemplar = contar_ejemplares(lista_arboles)
    for arbol in lista_arboles:
        inclinaciones = obtener_alturas(lista_arboles, arbol)
        
            
    return inclinaciones

mas_inclinado = especie_promedio_mas_inclinada(arboles)


def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles) #obtengo todas las especies de la lista
    maximo = 0.0
    for row in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles,row)
        if maximo <= max(inclinaciones):
            maximo = max(inclinaciones)
            especie = row
    return especie, maximo
