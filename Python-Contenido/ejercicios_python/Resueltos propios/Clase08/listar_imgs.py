# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 22:27:12 2022

@author: Luciano
"""

import os

def archivos_png(directorio):
    lista_png=[]
    for root, dirs, files in os.walk(directorio):
        for name in files:
            path=name
            root2, extention= os.path.splitext(path)
            if extention =='.png':
                lista_png.append(name)
    return lista_png


if __name__ == '__main__':
    archivos_png('../Data/ordenar')
    
    