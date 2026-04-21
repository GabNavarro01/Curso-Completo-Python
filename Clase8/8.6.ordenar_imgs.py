import os
from datetime import datetime
from pprint import pprint


# obtener nuevo_nombre , fecha
def procesar_nombre(nombre_archivo):
    fecha_string = nombre_archivo[-12:-4]
    nuevo_nombre = nombre_archivo[:-13]
    fecha = datetime.strptime(fecha_string, '%Y%m%d')
    return nuevo_nombre, fecha


def procesar(directorio, debug = False):

    destino = "../Data/imgs_procesadas"
    os.makedirs(destino, exist_ok=True)

    dir_pngs = []

    for dirpath, dirnames, filenames in os.walk(directorio):
        for file in filenames:
            if file.lower().endswith(".png"):
                dir_pngs.append(os.path.join(dirpath, file))


    for png in dir_pngs:
            
        nombre_archivo = os.path.basename(png)
        if debug:
            print(f'Transformando el archivo : {nombre_archivo}')
        # Obtener fecha
        nuevo_nombre, nueva_fecha = procesar_nombre(nombre_archivo)
        if debug:
            print(f'Nuevo nombre : {nuevo_nombre}, Nueva fecha: {nueva_fecha}')
        # Cambiar fecha
        timestamp = nueva_fecha.timestamp()
        os.utime(png, (timestamp, timestamp))

        # Nuevo nombre
        nuevo_archivo = nuevo_nombre + ".png"
        if debug:
            print(f'Nueva ruta: {destino + nuevo_archivo}')
        # Ruta final
        destino_final = os.path.join(destino, nuevo_archivo)

        # Mover + renombrar
        os.replace(png, destino_final)

    # Borrar carpetas vacías
    for dirpath, dirnames, filenames in os.walk(directorio, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print(f'Se necesita: {sys.argv[0]} nombre_directorio debug(opcional)')
        sys.exit(1)
    if len(sys.argv) == 2:
        procesar(sys.argv[1])
    else:
        procesar(sys.argv[1], True)