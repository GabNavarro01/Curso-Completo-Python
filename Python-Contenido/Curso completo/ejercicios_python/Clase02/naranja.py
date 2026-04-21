f= open ('C:/Users/Luciano/Desktop/Python/ejercicios_python/Data/precios.csv', 'rt')
for line in f:
    lista= line.split(',')

    
    if lista[0]=='Naranja':
        print( 'El precio de la naranja es:', lista[1])