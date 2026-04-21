def buscar_precio(nombreFruta):
    filePrecios = open("../Data/precios.csv" , "rt")
    costoFruta = 0
    listadoFrutas = []
    for fila in filePrecios:
        row = fila.split(",")
        listadoFrutas.append(row[0])
        if row[0] == nombreFruta:
            print( 'El precio de la', nombreFruta, 'es', float(row[1]))
    if nombreFruta not in listadoFrutas:
        print("El nombre no esta en el listado")

costoFruta = buscar_precio(input("Ingrese el nombre de la fruta a buscar : "))