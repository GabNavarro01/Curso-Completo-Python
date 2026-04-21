
import csv

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

costo = costo_camion('../Data/camion.csv')
print( 'El precio total del camion es de ', costo)
