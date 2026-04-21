# -*- coding: utf-8 -*-

f = open('../Data/camion.csv', 'rt')
headers = next(f).split(',')

costo = float()

for line in f:
    row = line.split(',')
    costo = costo + (int(row[1]) * float(row[2]))
    
print(f'Costo total: $ {costo}')

f.close()