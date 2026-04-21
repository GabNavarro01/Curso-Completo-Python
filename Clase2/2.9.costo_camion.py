import csv

def costoCamion(nombreArchivo):
    fileCamion = open(nombreArchivo , "rt")

    rows = csv.reader(fileCamion)
    headers = next(rows)
    print(headers)
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
    fileCamion.close()

    return totalCamion

costo = costoCamion('../Data/camion.csv')
print( 'El precio total del camion es de ', costo)
