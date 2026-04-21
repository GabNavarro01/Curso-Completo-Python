# -*- coding: utf-8 -*-

#%% Ejercicio 2.3

f = open('..\Data\precios.csv', 'rt')

for line in f:
    row = line.split(',')
    if 'Naranja' in row:
        print(f'El precio de la naranja es: $ {row[1]}')
    else:
        pass

f.close()

#%% Ejercicio 2.7

def buscar_precio(fruta):
    with open('..\Data\precios.csv', 'rt') as f:
        listado_frutas = [ ]
        for line in f:
            row = line.split(',')
            listado_frutas.append(row[0])
            if row[0] == fruta:
                print(f'El precio de un cajón de {fruta} es $ {float(row[1])}')
        if fruta not in listado_frutas:
            print(f'{fruta} no figura en el listado de precios')