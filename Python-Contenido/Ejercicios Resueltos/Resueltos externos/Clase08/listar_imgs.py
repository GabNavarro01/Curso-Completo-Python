# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:57:09 2021

@author: Yamila
"""
import os


def archivos_png(directorio):
    lista_archivos_png = []

    for root, dirs, files in os.walk(directorio):
        for name in files:
            path = name
            root2, extension = os.path.splitext(path)
            if extension == '.png':
                lista_archivos_png.append(name)

    return lista_archivos_png


if __name__ == '__main__':
    archivos_png('../Data/ordenar')
