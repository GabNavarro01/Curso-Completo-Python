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



parque_GENERAL_PAZ = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')
parque_LOS_ANDES = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')
parque_CENTENARIO = leer_parque('../Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')
# pprint(len(arboles))

# arboles_especies = especies(parque)
# print(arboles_especies)

ejemplares_GENERAL_PAZ = contar_ejemplares(parque_GENERAL_PAZ)
ejemplares_LOS_ANDES = contar_ejemplares(parque_LOS_ANDES)
ejemplares_CENTENARIO = contar_ejemplares(parque_CENTENARIO)

# print(f'Los tres ejemplares mas comunes en el parque GENERAL PAZ son {ejemplares_GENERAL_PAZ.most_common(5)}')
# print(f'Los tres ejemplares mas comunes en el parque LOS ANDES son {ejemplares_LOS_ANDES.most_common(5)}')
# print(f'Los tres ejemplares mas comunes en el parque CENTENARIO son {ejemplares_CENTENARIO.most_common(5)}')

alturas_GENERAL_PAZ = obtener_alturas(parque_GENERAL_PAZ, 'Jacarandá')
alturas_LOS_ANDES = obtener_alturas(parque_LOS_ANDES, 'Jacarandá')
alturas_CENTENARIO = obtener_alturas(parque_CENTENARIO, 'Jacarandá')


print(f'El maximo de los Jacarandá en GENERAL PAZ es de {max(alturas_GENERAL_PAZ)} con promedio de {sum(alturas_GENERAL_PAZ)/len(alturas_GENERAL_PAZ):0.2f}')
print(f'El maximo de los Jacarandá en LOS ANDES es de {max(alturas_LOS_ANDES)} con promedio de {sum(alturas_LOS_ANDES)/len(alturas_LOS_ANDES):0.2f}')
print(f'El maximo de los Jacarandá en CENTENARIO es de {max(alturas_CENTENARIO)} con promedio de {sum(alturas_CENTENARIO)/len(alturas_CENTENARIO):0.2f}')