from pprint import pprint
from collections import Counter
import csv
import os
import formato_tabla
import lote

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

def leer_camion(fileCamion):
    """
    Devuelve una Lista de Diccionarios
    """
    if isinstance(fileCamion, str):
        fileCamion = open(fileCamion, 'rt')
    
    camion = [] #Lista de diccionarios
    rows = csv.reader(fileCamion)
    headers = next(rows)
    totalCamion = 0
    for i, fila in enumerate(rows):
        try:
            fila = [func(val) for func, val in zip([str, int, float], fila) ]
            registro = lote.Lote(fila[0], fila[1], fila[2])
            camion.append(registro)
        except ValueError:
            print('Faltan datos en la línea', i, 'del archivo.')
    return camion

"""
Devuelve un diccionario de la forma { 'nombreFruta' : float(precio)}
"""
def leer_precios(filePrecios):
    diccionario = {}
    rows = csv.reader(filePrecios)
    totalCamion = 0
    for i, fila in enumerate(rows):
        try: 
            diccionario[fila[0]] = float(fila[1])
        except IndexError:
            print('Faltan datos en la línea', i, 'del archivo.')

    return diccionario



def balance_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    total_comprado = costo_camion(nombre_archivo_camion)
    total_vendido = 0
    for producto in camion:
        nombre = producto['nombre']
        cajones = int(producto['cajones'])
        costo = float(producto['precio'])
        
        precio_venta = precios[nombre] #Los precios ya estan en float
        total_vendido += cajones * precio_venta

    print(f'El costo del camion es de {total_comprado}')
    print(f'La venta es de {total_vendido}')
    print(f'Hay un balance de {round(total_vendido - total_comprado,2)}')



def hacer_informe(camion, precios):
    informe = []
    for row in camion:
        informe.append((row.nombre, row.cantidad, row.precio , precios[row.nombre] - float(row.precio)))
    return informe


def imprimir_informe(informe, formateador):
    formateador.encabezado(['Nombre', 'Cajones', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)   


def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt = 'txt'):
    with open(nombre_archivo_camion, 'rt') as fileCamion:
        camion = leer_camion(fileCamion)
    with open(nombre_archivo_precios, 'rt') as filePrecios:
        precios = leer_precios(filePrecios)
    informe = hacer_informe(camion, precios)
    # if fmt == 'txt':
    #     formateador = formato_tabla.FormatoTablaTXT()
    # elif fmt == 'csv':
    #     formateador = formato_tabla.FormatoTablaCSV()
    # elif fmt == 'html':
    #     formateador = formato_tabla.FormatoTablaHTML()
    # else:
    #     raise RuntimeError(f'Unknown format {fmt}')
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe, formateador)


def f_principal(camion, precios, fmt):
    informe_camion(camion,precios, fmt)
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
     raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion archivo_precios formato')
    archivo_camion = sys.argv[1]
    archivo_precios = sys.argv[2]
    fmt = sys.argv[3]
    f_principal(archivo_camion,archivo_precios, fmt)