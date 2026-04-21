import csv

def costoCamion(nombreArchivo):
    fileCamion = open(nombreArchivo , "rt")

    rows = csv.reader(fileCamion)
    headers = next(rows)
    totalCamion = 0
    for i, fila in enumerate(rows):
        try: 
            # fila = row.split(',') # El csv reader ya me hace los split
            cantidades = float(fila[1])
            precios = float(fila[2])
            totalCamion += cantidades * precios
            # print(f'Fruta: {fila[0]} - Cantidades: {cantidades} - Precio: {precios}')
        except ValueError:
            print(f'Fila {i} del archivo. No se puede interpretar {fila}')
    fileCamion.close()

    return totalCamion

costo = costoCamion('../Data/missing.csv')
print( 'El precio total del camion es de ', costo)
