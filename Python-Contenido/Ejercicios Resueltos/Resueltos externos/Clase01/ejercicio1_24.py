frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'

lista_frutas = frutas.split(',')

lista_frutas[2] = 'Granada'

compra = []

compra.append('Pera')

lista_frutas[-2:] = compra

print('Granada' in lista_frutas)

print('Lima' in lista_frutas)

print('Limon' not in lista_frutas)