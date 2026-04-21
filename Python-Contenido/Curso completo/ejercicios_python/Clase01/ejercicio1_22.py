frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'

lista_frutas = frutas.split(',')

print(lista_frutas)

print(lista_frutas[0])

print(lista_frutas[1])

print(lista_frutas[-1])

print(lista_frutas[-2])

lista_frutas[2] = 'Granada'

print(lista_frutas)

print(lista_frutas[0:3])

print(lista_frutas[-2:])

compra = []

compra.append('Pera')

print(compra)

lista_frutas[-2:] = compra

print(lista_frutas)