# -*- coding: utf-8 -*-

import csv

#%% Ejercicio 3.1 - Semántica

#Enunciado del ejercicio

# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i<n:
#         if expresion[i] == 'a':
#             return True
#         else:
#             return False
#         i += 1

# tiene_a('UNSAM 2020')
# tiene_a('abracadabra')
# tiene_a('La novela 1984 de George Orwell')

#RESOLUCIÓN

#El error era que sólo verificaba la última 'a'
#Lo resolví sacando el bucle.
#Incorporé la a la verificación tanto la 'a' mayúscula como con tilde, para que sea más complea.
#A continuación va el código corregido:
    
def tiene_a(expresion):
    if 'a' in expresion.lower() or 'á' in expresion.lower():
        return True
    else:
        return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%% Ejercicio 3.2 - Sintaxis

#Enunciado del ejercicio

# def tiene_a(expresion)
#     n = len(expresion)
#     i = 0
#     while i<n
#         if expresion[i] = 'a'
#             return True
#         i += 1
#     return Falso

# tiene_a('UNSAM 2020')
# tiene_a('La novela 1984 de George Orwell')

#RESOLUCIÓN

#Faltan los dos puntos (:) al final de varias líneas
#La expresión de igualdad en la condición del if que falta un signo =
#return Falso es incorrecto. Debería ser: return False
#Corrigiendo los errores de sintaxis no es suficiente para que funcione en todos los casos.
#No contempla 'a' mayúsculas o con tilde.
#A continuación el código corregido:

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] in 'aAáÁ':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%% Ejercicio 3.2 - Tipos

#Enunciado del ejercicio

# def tiene_uno(expresion):
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i<n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#         i += 1
#     return tiene

# tiene_uno('UNSAM 2020')
# tiene_uno('La novela 1984 de George Orwell')
# tiene_uno(1984)

#RESOLUCIÓN

#La función len() no se puede aplicar a números enteros (int).
#Los números no admiten ser leídos por su índice (expresion[i]).
#Lo resolví atrapando la expresión ingresada en una variable que la convierte a string y esa es la que luego aplica a la función.
#A continuación el código corregido:
    
def tiene_uno(expresion):
    string_expresion = str(expresion)
    n = len(string_expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if string_expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%% Ejercicio 3.4 - Alcances

#Enunciado del ejercicio

# def suma(a,b):
#     c = a + b

# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")

#RESOLUCIÓN

#La variable c en la función no está siendo utilizada, retornada
#Lo resolví ingresando a la función el return c.
#A continuación el código corregido:
    
def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%% Ejercicio 3.5 - Pisando memoria

#Enunciado del ejercicio

# import csv
# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion

# camion = leer_camion('../Data/camion.csv')
# pprint(camion)

#RESOLUCIÓN

#Al quedar el diccionario fuera del bucle for, el siguiente ingreso pisa la información.
#Así se agrega la siguiente entrada pero cambiando la anterior también.
#Si ingresamos el diccionario vacío al bucle se limpia su memoria, solo almacena el último dato.
#Y antes de borrar el dato se ingresa a la lista camion.
#A continuación el código corregido:
    
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, 'rt') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
        return camion
    
camion = leer_camion('../Data/camion.csv')
#print(camion)
pprint(camion)