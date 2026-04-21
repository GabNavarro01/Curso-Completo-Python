# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 22:37:20 2022

@author: Luciano
"""

costo_camion=0

with open ('../Data/camion.csv', 'rt') as f:   
    headers= next(f)
    headers
    
    for i in f:
        row= i.split(',')
        costo_camion += int(row[1]) * float (row[2])   


print("Costo total ", costo_camion)
    

    
    