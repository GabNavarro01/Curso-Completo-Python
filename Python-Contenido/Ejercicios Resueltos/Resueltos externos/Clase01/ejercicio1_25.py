frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'

lista_frutas = frutas.split(',')

lista_frutas[2] = 'Granada'

compra = []

compra.append('Pera')

lista_frutas[-2:] = compra

lista_frutas.append('Mango')

print(lista_frutas)

lista_frutas.insert(1, 'Lima')

print(lista_frutas)

lista_frutas.remove('Mandarina')

print(lista_frutas)

lista_frutas.append('Banana')

print(lista_frutas)

print(lista_frutas.index('Banana'))

print(lista_frutas[4])

print(lista_frutas.count('Banana'))

lista_frutas.remove('Banana')

print(lista_frutas)