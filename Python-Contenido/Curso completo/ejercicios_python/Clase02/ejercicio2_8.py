# -*- coding: utf-8 -*-

def preguntar_edad(nombre):
    edad = int(input(f'Ingresá tu edad {nombre}: '))
    if edad<0:
        raise ValueError('La edad no puede ser negativa.')
    return edad

for nombre in ['Pedro','Juan','Caballero']:
        try:
            edad = preguntar_edad(nombre)
            print(f'{nombre} tiene {edad} años.')
        except ValueError:
            print(f'{nombre} no ingresó una edad válida.')
            
#%% Función costo_camion() del ejercicio 2.6

def costo_camion(nombre_archivo):
   with open('../Data/camion.csv', 'rt') as f:
       next(f).split(',')
       costo = float()
       for line in f:
           row = line.split(',')
           costo += (int(row[1]) * float(row[2]))
       return costo
    
costo = costo_camion('../Data/camion.csv')
print(f'Costo total: $ {costo}')

#%%

def costo_camion(nombre_archivo):
   with open('../Data/missing.csv', 'rt') as f:
       next(f).split(',')
       costo = float()
       try:
           for line in f:
               row = line.split(',')
               costo += (int(row[1]) * float(row[2]))
           return costo
       except ValueError:
           print('El archivo no contiene todos los datos, no es posible procesarlo.')
    
costo = costo_camion('../Data/missing.csv')
print(f'Costo total: $ {costo}')

