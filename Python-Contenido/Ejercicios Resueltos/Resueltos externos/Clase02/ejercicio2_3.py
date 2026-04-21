# -*- coding: utf-8 -*-

f = open('../Data/precios.csv', 'rt')

for line in f:
    row = line.split(',')
    if 'Naranja' in row:
        print(f'El precio de la naranja es: $ {row[1]}')
    else:
        pass

f.close()
