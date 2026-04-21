fileCamion = open("../Data/camion.csv" , "rt")
filePrecios = open("../Data/precios.csv" , "rt")

headers = next(fileCamion)

totalCamion = 0


for fila in fileCamion:
    row = fila.split(',')
    cantidades = float(row[1])
    precios = float(row[2])
    totalCamion += cantidades * precios
    print(row)

print( 'El precio total del camion es de ', totalCamion)


costoNaranja = 0

for fila in filePrecios:
    row = fila.split(",")
    if row[0] == 'Naranja':
        costoNaranja = float(row[1])


print( 'El precio de la naranja es ', costoNaranja)

fileCamion.close()
filePrecios.close()