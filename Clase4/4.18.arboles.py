import csv

from pprint import pprint
from collections import Counter

# Recibe el nombre del archivo y un parque especifico del cual buscar los arboles
# Devuelve una lista de diccionarios con la informacion del paque
def leer_parque(nombre_archivo, nombre_parque):
    lista_arboles = []
    with open(nombre_archivo , 'rt', encoding = 'utf-8') as file_parque:
        
        parque = csv.reader(file_parque)
        headers = next(parque)

        for nArbol, arbol in enumerate(parque):
            try:
                registro = dict(zip(headers, arbol))
                if registro['espacio_ve'] == nombre_parque:
                    lista_arboles.append(registro)
            except ValueError:
                print(f'Hubo un problema con el arbol {nArbol}')
    return lista_arboles

# Devuelve un set de las especies de un parque especifico
def especies(lista_arboles):
    lista_especies = []
    for nArbol, arbol in enumerate(lista_arboles):
        try:
            lista_especies.append(arbol['nombre_com'])
        except ValueError:
            print(f'No se encontro la especie en la linea {nArbol}')
    
    return set(lista_especies)

# Devuelve un diccionario de manera { 'especieArbol' : cantidadArboles}
def contar_ejemplares(lista_arboles):
    contadorArboles = Counter()
    for nArbol, arbol in enumerate(lista_arboles):
        contadorArboles[arbol['nombre_com']] += 1

    return contadorArboles

def obtener_alturas(lista_arboles, especie):
    lista_alturas = []

    for nArbol, arbol in enumerate(lista_arboles):
        try:
            if arbol['nombre_com'] == especie:
                lista_alturas.append(float(arbol['altura_tot']))
        except ValueError:
            print(f'Hubo un error en la linea {nArbol}')
            
    return lista_alturas

def obtener_inclinaciones(lista_arboles, especie):
    lista_inclinaciones = []

    for nArbol, arbol in enumerate(lista_arboles):
        try:
            if arbol['nombre_com'] == especie:
                lista_inclinaciones.append(float(arbol['inclinacio']))
        except ValueError:
            print(f'Hubo un error en la linea {nArbol}')
            
    return lista_inclinaciones

def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    inclinacion_maxima = 0
    for especie in lista_especies:
        lista_inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        if max(lista_inclinaciones) >= inclinacion_maxima:
            especie_maxima = (especie, max(lista_inclinaciones))
            inclinacion_maxima = max(lista_inclinaciones)

    return especie_maxima

def especie_promedio_mas_inclinada(lista_arboles):
    lista_especies = especies(lista_arboles)
    inclinacion_promedio_maxima = 0
    for especie in lista_especies:
        lista_inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        promedio_inclinaciones = sum(lista_inclinaciones)/len(lista_inclinaciones)
        if promedio_inclinaciones >= inclinacion_promedio_maxima:
            especie_maxima = (especie, promedio_inclinaciones)
            inclinacion_promedio_maxima = promedio_inclinaciones

    return especie_maxima

def leer_arboles(nombre_archivo):
    arboleda = []
    with open(nombre_archivo , 'rt', encoding = 'utf-8') as fileArboles:
        arboles = csv.reader(fileArboles)
        headers = next(arboles)

        for nArbol, arbol in enumerate(arboles):
            try:
                registro = dict(zip(headers, arbol))
                arboleda.append(registro)
            except ValueError:
                print(f'Falta informacion en la linea {nArbol}')

    return arboleda

def medidas_de_especies(especies, arboleda):
    # { especie : [compresion de lista de alturas y diametros] for especie in especie}
    diccionario = { especie : [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies}
    return diccionario


arboleda = leer_arboles(r'C:\Users\Gabriel\Desktop\CursoPython\Data\arbolado-en-espacios-verdes.csv')

'''
[<expresión> for <variable> in <secuencia> if <condición>]
'''
alturas_jacarandas = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
alturas_y_diametros_jacarandas = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

especies_arboles = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

# {'especie' : (altura,diametro)}
medidas = medidas_de_especies(especies_arboles, arboleda)
cantidad_medidas_eucalipto = len(medidas[especies_arboles[0]])

nombre_general_paz = 'GENERAL PAZ'
nombre_los_andes = 'ANDES, LOS'
nombre_centenario = 'CENTENARIO'

parque_GENERAL_PAZ = leer_parque(r'C:\Users\Gabriel\Desktop\CursoPython\Data\arbolado-en-espacios-verdes.csv', nombre_general_paz)
parque_LOS_ANDES = leer_parque(r'C:\Users\Gabriel\Desktop\CursoPython\Data\arbolado-en-espacios-verdes.csv', nombre_los_andes)
parque_CENTENARIO = leer_parque(r'C:\Users\Gabriel\Desktop\CursoPython\Data\arbolado-en-espacios-verdes.csv', nombre_centenario)

ejemplares_GENERAL_PAZ = contar_ejemplares(parque_GENERAL_PAZ)
ejemplares_LOS_ANDES = contar_ejemplares(parque_LOS_ANDES)
ejemplares_CENTENARIO = contar_ejemplares(parque_CENTENARIO)

alturas_GENERAL_PAZ = obtener_alturas(parque_GENERAL_PAZ, 'Jacarandá')
alturas_LOS_ANDES = obtener_alturas(parque_LOS_ANDES, 'Jacarandá')
alturas_CENTENARIO = obtener_alturas(parque_CENTENARIO, 'Jacarandá')

inclinaciones_GENERAL_PAZ = obtener_inclinaciones(parque_GENERAL_PAZ, 'Jacarandá')
inclinaciones_LOS_ANDES = obtener_inclinaciones(parque_LOS_ANDES, 'Jacarandá')
inclinaciones_CENTENARIO = obtener_inclinaciones(parque_CENTENARIO, 'Falso Guayabo (Guayaba del Brasil)')
