# -*- coding: utf-8 -*-

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    registro = {} # al estar el dict afuera del for se pisan los datos y todas las líneas se modifican con los valores último agregados.
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)