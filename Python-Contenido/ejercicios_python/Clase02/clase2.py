
f = open ('../Data/camion.csv', 'rt')
headers = next(f).split (',')
headers
for line in f:
    row =line.split (',')
    print (row)
    
#%%

with open ('../Data/precios.csv', 'rt') as f:
    
    
    for i in f:
        row= i.split(',')
        if row[0]=='Naranja':
           
            print(f'El precio de la Naranja es {row[1]}')

#%%

import gzip

with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print (line, end = '')
        
#%%

x





        