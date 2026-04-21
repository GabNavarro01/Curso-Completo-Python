# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 08:36:08 2022

@author: Luciano
"""
import csv
import informe_final

import informe_final as info

def costo_camion(nombre_archivo):
    camion = info.leer_camion(nombre_archivo)
    costo_total = float()
    for cajon in camion:
        n_cajones = cajon['cajones']
        precio = cajon['precio']
        costo_total += n_cajones * precio
    return costo_total

#%% Ejercicio 7.4

def f_principal(parametros):
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    camion = info.leer_camion(sys.argv[1])
    costo_total = float()
    for cajon in camion:
        n_cajones = cajon['cajones']
        precio = cajon['precio']
        costo_total += n_cajones * precio
    print(costo_total)
    

if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
        
   
