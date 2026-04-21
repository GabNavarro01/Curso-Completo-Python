import csv
import sys
def costoCamion(nombreArchivo):
    fileCamion = open(nombreArchivo , "rt")

    rows = csv.reader(fileCamion)
    headers = next(rows)
    totalCamion = 0
    for fila in rows:
        try: 
            # fila = row.split(',') # El csv reader ya me hace los split
            cantidades = float(fila[1])
            precios = float(fila[2])
            totalCamion += cantidades * precios
            print(f'Fruta: {fila[0]} - Cantidades: {cantidades} - Precio: {precios}')
        except ValueError:
            print("No se encuentra valor deseado")
    fileCamion.close()

    return totalCamion


if len(sys.argv) == 2:
    nombreArchivo = sys.argv[1]    #El parametro del archivo, el [0] es el .py en si
else:
    nombreArchivo = '../Data/camion.csv'

costo = costoCamion(nombreArchivo)
print( 'El precio total del camion es de ', costo)