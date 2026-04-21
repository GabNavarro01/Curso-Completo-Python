import csv
from pprint import pprint

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

arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
# pprint(len(arboles))
