import csv
from pprint import pprint

def leer_precios(nombreArchivo):
    with open(nombreArchivo, 'rt') as filePrecios:
        diccionario = {}
        rows = csv.reader(filePrecios)
        totalCamion = 0
        for i, fila in enumerate(rows):
            try: 
                diccionario[fila[0]] = float(fila[1])
            except IndexError:
                print('Faltan datos en la línea', i, 'del archivo.')

    return diccionario

precios = leer_precios('../Data/precios.csv')
pprint(precios)