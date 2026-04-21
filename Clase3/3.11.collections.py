import csv
from pprint import pprint
from collections import Counter

"""
Devuelve un float (costo del camion)
"""
def costo_camion(nombreArchivo):
    with open (nombreArchivo , "rt") as fileCamion:

        rows = csv.reader(fileCamion)
        headers = next(rows)
        totalCamion = 0
        for i, fila in enumerate(rows):
            try: 
                cantidades = float(fila[1])
                precios = float(fila[2])
                totalCamion += cantidades * precios
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')

    return totalCamion

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
total_comprado = costo_camion('../Data/camion.csv')
total_vendido = 0

for producto in camion:
    nombre = producto['nombre']
    cajones = int(producto['cajones'])
    costo = float(producto['precio'])
    
    precio_venta = precios[nombre] #Los precios ya estan en float
    total_vendido += cajones * precio_venta

print(f'El costo del camion es de {total_comprado}')
print(f'La venta es de {total_vendido}')
print(f'Hay un balance de {total_vendido - total_comprado}')

# tenencias es un diccionario
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += float(s['cajones'])

print(tenencias.most_common(3))

camionDos = leer_camion("../Data/camion2.csv")
tenenciasDos = Counter()
for s in camionDos:
    tenenciasDos[s['nombre']] += float(s['cajones'])

print(tenenciasDos.most_common(3))

combinada = tenencias + tenenciasDos

