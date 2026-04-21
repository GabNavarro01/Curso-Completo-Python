
#%% Ejercicio 2.2 / costo_camión


costo_total=0

with open('../Data/camion.csv','rt') as f:
    headers =next(f)
    
    for line in f:
        row=line.split(',')
        costo_total= costo_total + float(row[1])*float(row[2])
    
print('Costo total',costo_total)

#%%Ejercicio 2.6

def costo_camion (nombre_archivo):
    
    costo_total=0
    
    with open(nombre_archivo,'rt') as f:
        headers =next(f)
        headers
        
        for line in f:
            row=line.split(',')
            costo_total= costo_total + float(row[1])*float(row[2])
    
    return costo_total
    
costo= costo_camion('../Data/camion.csv')

#%%Ejercicio 2.8

def costo_camion (nombre_archivo):
   
    costo_total=0
   
    with open(nombre_archivo,'rt') as f:
        next(f).split(',')
        costo=float()
       
        try:
            
            for line in f:
                row=line.split(',')
                costo_total= costo_total + int(row[1])*float(row[2])
            return costo
            print(f'Costo total:${costo}')
        except ValueError:
            print('El archivo no contiene todos los datos, no es posible procesarlo.')
            next(f)
   
costo= costo_camion('../Data/missing.csv')

#%%Ejercicio 2.9

import csv

def costo_camion (nombre_archivo):
   
   
    with open(nombre_archivo,'rt') as f:
        rows=csv.reader(f)
        headers=next(rows)
        headers
        costo=float()
             
        for row in rows:
                       costo= costo + int(row[1])*float(row[2])
        return costo
       
   
costo= costo_camion('../Data/camion.csv')
print(f'Costo total:${costo}')















