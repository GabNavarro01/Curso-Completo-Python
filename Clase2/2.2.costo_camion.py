file = open("../Data/camion.csv" , "rt")

headers = next(file)

totalCamion = 0


for fila in file:
    row = fila.split(',')
    cantidades = float(row[1])
    precios = float(row[2])
    totalCamion += cantidades * precios
    # print(row)

print( 'El precio total del camion es de ', totalCamion)

file.close()