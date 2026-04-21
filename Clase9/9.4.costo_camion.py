import csv
import informe_final

def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo)
    costo = sum(e.costo() for e in camion)
    return costo

def f_principal(archivo_camion):
    print(costo_camion(archivo_camion))
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
     raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    archivo_camion = sys.argv[1]
    f_principal(archivo_camion)