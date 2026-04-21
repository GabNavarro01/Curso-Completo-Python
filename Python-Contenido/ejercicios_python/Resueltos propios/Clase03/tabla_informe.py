

#%%Costo_camion

import csv

def costo_camion (nombre_archivo):
     
   
    with open(nombre_archivo,'rt') as f:
        filas=csv.reader(f)
        encabezados=next(filas)        
        costo_total=float()
       
        for n_fila, fila in enumerate (filas, start=1):
            record= dict(zip(encabezados, fila))
            
            try:
                ncajones= int(record['cajones'])
                precio= float(record['precio'])
                costo_total+= ncajones * precio
                
            except ValueError:
                print(f' Fila {n_fila}: No pude interpretar: {fila}')
        
       
        return costo_total
        
   
#%%Precio de venta


def leer_precio(fruta):
    f = open('../Data/precios.csv', 'r')
    rows=csv.reader(f)
    precios = {}
    
    try:
        for row in rows:            
                
                precios[row[0]]=float(row[1])
                
    except IndexError:
           print(f'Ups! no logro entender la línea:{row}')
    
    return precios
  
precios=leer_precio('../Data/precios.csv')


#%%Precio de Compra

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers=next(rows)
        for n_row, row in enumerate(rows, start=1):
            record=dict(zip(headers,row))

            try:
             
               camion.append(record)
               
            except ValueError:
                print(f'Fila {n_row}: No pude interpretar: {row}')
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
    nombre=producto['nombre']
    cajones=producto['cajones']
    precio=producto['precio']
    costo_camion += int(cajones) * float(precio)
    
    precio_venta= precios[nombre]
    total_vendido+= float((precio_venta)) * int(cajones)
    
balance = total_vendido - costo_camion

print(f'La empresa ganó ${round(balance,2)}')

print(f'La mercadería costó ${costo_camion}')

print(f'Se vendió un total de ${total_vendido}')

#%% INFORME

def hacer_informe(cajones,precios):
    
    informe=[]
    
    for i in cajones:
        if i['nombre'] in precio.keys():
            tupla= (i['nombre'], i['cajones'], i['precio'], precios[i['nombre']]-i['precio'] )
            informe.append(tupla)
        return informe
    
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')


print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
print('    ------     ------     ------     ------')
for nombre, cajones, precio, cambio in informe:
    precio_sig= '$' + str(round(precio, 2))
    
    print(f'{nombre:>10s} {cajones:>10d} {precio_sig:>10s} {cambio:>10.2f}')
    
        
        
        
        
    
    
    
