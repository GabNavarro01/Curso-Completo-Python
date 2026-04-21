import csv

def costoCamion(nombreArchivo):
    
    
    with open(nombreArchivo , "rt") as fileCamion:

        rows = csv.reader(fileCamion)
        headers = next(rows)
        totalCamion = 0
        for i, fila in enumerate(rows):
            try: 
                # fila = row.split(',') # El csv reader ya me hace los split
                cantidades = float(fila[1])
                precios = float(fila[2])
                totalCamion += cantidades * precios
                print(f'Fruta: {fila[0]} - Cantidades: {cantidades} - Precio: {precios}')
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')

    return totalCamion

costo = costoCamion('../Data/camion.csv')
print( 'El precio total del camion es de ', costo)

def leer_camion(nombreArchivo):
    informacionCamion = []
    with open(nombreArchivo , "rt") as fileCamion:

        rows = csv.reader(fileCamion)
        headers = next(rows)
        totalCamion = 0
        for i, fila in enumerate(rows):
            try: 
                informacionCamion.append((fila[0],fila[1],fila[2]))
            except ValueError:
                print('Faltan datos en la línea', i, 'del archivo.')

    return informacionCamion