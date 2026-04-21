# -*- coding: utf-8 -*-

with open('../Data/camion.csv', 'rt') as f:
    data = f.read()

print(data)

#%%

with open('../Data/camion.csv', 'rt') as f:
    for line in f:
        print(line, end = '')

#%%

f = open('../Data/camion.csv', 'rt')
headers = next(f)

for line in f:
    print(line, end = '')
    
f.close()

#%%

f = open('../Data/camion.csv', 'rt')
headers = next(f).split(',')

for line in f:
    row = line.split(',')
    print(row)
    
f.close()