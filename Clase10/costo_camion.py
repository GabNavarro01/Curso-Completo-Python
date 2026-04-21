import csv
import informe_final

def costo_camion(nombre_archivo):
    camion = informe_final.leer_camion(nombre_archivo)
    return camion.costo_total()

def f_principal(archivo_camion):
    costo = costo_camion(archivo_camion)
    print(f'El costo del camion es de {costo}')
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
     raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    archivo_camion = sys.argv[1]
    f_principal(archivo_camion)


archivo_camion = '../Data/camion.csv'
archivo_precios = '../Data/precios.csv'