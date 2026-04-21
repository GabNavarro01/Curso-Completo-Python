import csv
from pprint import pprint

"""
Devuelve una Lista de Diccionarios
"""
def leer_camion(nombreArchivo):
    camion = [] #Lista de diccionarios
    with open(nombreArchivo , "rt") as fileCamion:

        rows = csv.reader(fileCamion)
        headers = next(rows)
        totalCamion = 0
        for i, fila in enumerate(rows):
            try: 
                registro = dict(zip(headers,fila))
                camion.append(registro)
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')
    return camion

"""
Devuelve un diccionario de la forma { 'nombreFruta' : float(precio)}
"""
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
camion = leer_camion('../Data/camion.csv')

costo_camion = 0
total_vendido = 0

for producto in camion:
    nombre = producto['nombre']
    cajones = int(producto['cajones'])
    costo = float(producto['precio'])
    costo_camion += cajones * costo
    
    precio_venta = precios[nombre] #Los precios ya estan en float
    total_vendido += cajones * precio_venta

print(f'El costo del camion es de {costo_camion}')
print(f'La venta es de {precio_venta}')
print(f'Hay un balance de {total_vendido - costo_camion}')