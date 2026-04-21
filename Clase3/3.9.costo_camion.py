import csv

def costoCamion(nombreArchivo):
    with open(nombreArchivo , "rt") as fileCamion:

        rows = csv.reader(fileCamion)
        headers = next(rows)
        totalCamion = 0

        for nFila, fila in enumerate(rows , start = 1):
            record = dict(zip(headers,fila))
            try: 
                ncajones = int(record['cajones'])
                precios = float(record['precio'])
                totalCamion += ncajones * precios
                # print(f'Fruta: {record['nombre']} - Cantidades: {ncajones} - Precio: {precios}')
            except ValueError:
                print(f'Fila {nFila} del archivo. No se puede interpretar {fila}')

    return totalCamion

costo = costoCamion('../Data/fecha_camion.csv')
print( 'El precio total del camion es de ', costo)
