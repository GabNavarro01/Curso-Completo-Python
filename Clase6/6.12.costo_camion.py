import csv
import informe_funciones

def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion(nombre_archivo)
    costo = sum((e['precio'])* (e['cajones']) for e in camion)
    return costo
