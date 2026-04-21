frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'

lista_frutas = frutas.split(',')

lista_frutas[2] = 'Granada'

compra = []

compra.append('Pera')
lista_frutas[-2:] = compra

lista_frutas.append('Mango')

lista_frutas.insert(1, 'Lima')

lista_frutas.remove('Mandarina')

lista_frutas.append('Banana')

lista_frutas.remove('Banana')

lista_frutas.sort()

print(lista_frutas)

lista_frutas.sort(reverse=True)

print(lista_frutas)