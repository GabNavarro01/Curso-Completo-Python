# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:49:19 2021

@author: Yamila
"""
import informe_funciones as info

def costo_camion(nombre_archivo):
    camion = info.leer_camion(nombre_archivo)
    costo_total = float()
    for cajon in camion:
        n_cajones = cajon['cajones']
        precio = cajon['precio']
        costo_total += n_cajones * precio
    return costo_total