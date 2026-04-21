import gzip
import os
from pprint import pprint
def archivos_png(directorio):
    pngs = []
    for dirpath, dirnames, filenames in os.walk(directorio): 
        for file in filenames:
            if(file[-4:] == '.png'):
                pngs.append(file)
    return pngs

def f_principal(nombre_directorio):
    pprint(archivos_png(nombre_directorio))


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print(f'Se necesita: {sys.argv[0]} nombre_directorio')
    f_principal(sys.argv[1])