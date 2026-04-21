# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:23:56 2021

@author: Yamila
"""
import os

def procesar_nombre(fname):
    
    
    
    
    
    
def procesar(fname):
    lista_archivos_png = []

    for root, dirs, files in os.walk(directorio):
        for name in files:
            path = name
            root2, extension = os.path.splitext(path)
            if extension == '.png':
