
#%%Ejercicio 2.10

import csv
import sys

def costo_camion (nombre_archivo):
   
   
    with open(nombre_archivo,'rt') as f:
        rows=csv.reader(f)
        headers=next(rows)
        headers
        costo=float()
             
        for row in rows:
                       costo= costo + int(row[1])*float(row[2])
        return costo
       
if len(sys.argv)==2:
    nombre_archivo= sys.argv[1]
   
else:
    nombre_archivo = '../Data/camion.csv'
    
costo= costo_camion('../Data/camion.csv')
print(f'Costo total:${costo}')