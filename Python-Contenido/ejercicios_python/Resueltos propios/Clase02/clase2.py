# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 07:26:58 2022

@author: Luciano
"""

#%%Ejercicios

# import os
# os.getcwd()

#Ejercicio 2.1

# with open('../Data/camion.csv','rt') as f:
#     data=f.read()
    
#     data

# print (data)

#%%Ejercicio 2.1.1

# with open ('../Data/camion.csv','rt') as f:
#     for line in f:
#         print(line,end='')
        
#%%Ejercicio 2.1.2 

# f=open('../Data/camion.csv','rt')
# headers=next(f)

# headers

# for line in f:
#     print (line, end ='')
    
# f.close()    

#%%Ejercicio 2.1.3 

# f=open('../Data/camion.csv','rt')
# headers= next(f).split(',')
# headers

# for line in f:
#     row=line.split(',')
#     print(row)
    
#     f.close()

#%%Ejercicio 2.2


# costo_total=0

# with open('../Data/camion.csv','rt') as f:
#     headers =next(f)
    
#     for line in f:
#         row=line.split(',')
#         costo_total= costo_total + float(row[1])*float(row[2])
        
# print('Costo total',costo_total)

#%%Ejercicio 2.3
# precio=0

# with open ('../Data/precios.csv','rt') as f:
#     for line in f:
#         row=line.split(',')
        
#     print(row)

#     for c in row:
#         if c=='Naranja':
#             precio= float(row[1])

# print('El preio de la naranja es',precio)
    
    
#%%Ejercicio 2.11

# import csv

# f = open('../Data/camion.csv')
# filas = csv.reader(f)
# next(filas)

# fila = next(filas)

# t = (fila[0], int(fila[1]), float(fila[2]))

# cost = t[1] * t[2]

# print(cost)
# print(f'{cost:0.2f}')

#%%Ejercicio 2.12

# import csv

# f = open('../Data/camion.csv')
# filas = csv.reader(f)
# next(filas)

# fila = next(filas)

# d={'nombre':fila[0], 'cajones': int(fila[1]), 'precio':float(fila[2])}

# costo= d['cajones']*d['precio']
# costo

# d['fecha']=(14,8,2020)
# d['cuenta']=12345

# d

#%%Ejercicio 2.12

# for k in d:
#     print('k=',k)
    
# for k in d:
#     print(k, '=', d[k])
    
# items=d.items()
# items

# # for k, v in d.items():
# #     print(k, '=',v)

# list(d)

#%%Ejercicio 2.15

# precios= {}

# with open ('../Data/precios.csv','rt') as f:
#     for line in f:
#         row=line.split(',')
#         precios[row[0]]=float(row[1])

# precios











