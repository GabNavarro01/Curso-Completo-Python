

#%%Ejercicio 2.15

# import csv

# def leer_camion(nombre_archivo):
#     camion = []

#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         next(rows)
#         for row in rows:
            
#             lote= (row[0], int(row[1]), float(row[2]))
#             camion.append(lote)
        
#         return camion
     
# camion = leer_camion('../Data/camion.csv')
    
# total= 0.0

# for s in camion:
#     total += s[1]*s[2]
    
# print(total)


#%%Ejercicio 2.16

# import csv

# from pprint import pprint

# def leer_camion(nombre_archivo):
#     camion = []

#     with open(nombre_archivo, 'rt') as f:
#         rows = csv.reader(f)
#         next(rows)
#         for row in rows:
            
#             lote= {}
#             lote['Nombre']=row[0]
#             lote['Cajon']=int(row[1])
#             lote['Precio']=float(row[2])
            
#             camion.append(lote)
        
#         return camion
     
# camion = leer_camion('../Data/camion.csv')

# pprint(camion)

# print(camion[0])
# print(camion[1])
# print(camion[1]['Cajon'])
    
# total= 0.0

# for s in camion:
#     total += s['Cajon']*s['Precio']
    
# print(total)

#%%Ejercicio 2.17

# import csv

# def leer_precio(fruta):
#     f = open('../Data/precios.csv', 'r')
#     rows=csv.reader(f)
#     precios = {}
    
#     try:
#         for row in rows:            
                
#                 precios[row[0]]=float(row[1])
                
#     except IndexError:
                 
    
#      return precios
        
# precios= leer_precio('../Data/precios.csv')

# precios

# precios['Naranja']
# precios['Mandarina']

#%%Ejercicio 2.18

#%%Precio de venta
import csv

def leer_precio(fruta):
    f = open('../Data/precios.csv', 'r')
    rows=csv.reader(f)
    precios = {}
    
    try:
        for row in rows:            
                
                precios[row[0]]=float(row[1])
                
    except IndexError:
                 
    
      return precios
  
precios=leer_precio('../Data/precios.csv')


#%%Precio de Compra

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            
            lote= {}
            lote['Nombre']=row[0]
            lote['Cajon']=int(row[1])
            lote['Precio']=float(row[2])
            
            camion.append(lote)
        
        return camion
     
# camion= leer_camion('../Data/camion.csv')
# camion

# costo_total=0.0

# for s in camion:
#         costo_total += s['Cajon'] * s['Precio']


#%%Balance

archivo_camion='../Data/camion.csv'
archivo_precios='../Data/precios.csv'

camion= leer_camion(archivo_camion)
precios= leer_precio(archivo_precios)

costo_camion= 0
total_vendido= 0

for producto in camion:
    nombre=producto['Nombre']
    cajones=producto['Cajon']
    precio=producto['Precio']
    costo_camion += cajones * precio
    
    precio_venta= precios[nombre]
    total_vendido+= precio_venta * cajones
    
balance = total_vendido - costo_camion

print(f'La empresa ganó ${round(balance,2)}')

print(f'La mercadería costó ${costo_camion}')

print(f'Se vendió un total de ${total_vendido}')

# 




