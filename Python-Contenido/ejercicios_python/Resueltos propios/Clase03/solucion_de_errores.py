

#%%
# Ejercicio 3.1
# Comentario: El error era de tipo semantico y estaba en el buble
    # Lo corregí haciendo que lea mayúsculas tmb y sacando el bucle.
    # El codigo corregido es:
        

def tiene_a(expresion):
       
    if 'a' in expresion or 'A' in expresion: 
        return True
    else:
        return False
        

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')


#%%
# Ejercicio 3.2
# Comentario: El error era de tipo sintáctico y estaba en los ":", "=" y "False"
    # Lo corregí poniendo los simbolos faltantes y escribiendo bien.
    # El codigo corregido es:
        
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.3
# Comentario: El error era de tipo Type y estaba en que el programa no podía trabajar con int, asi que lo convertí a str.
    # Lo corregí haciendo una nueva variable que trasforme lo ingresado en str.
    # El codigo corregido es:
        
def tiene_uno(expresion):
    transformar_str= str(expresion)
    n = len(transformar_str)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if transformar_str[i] == '1' :
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
# Ejercicio 3.3
# Comentario: El error era de tipo semantico
    # Lo corregí haciendo que la función devolviera el valor de c para poder ser utilizado en el print
    # El codigo corregido es:
        
def suma(a,b):
    c = int(a) + int(b)
    return c

a = 2
b = 4
c = suma(a,b)
print(f'La suma da {a} + {b} = {c}')

#%%
# Ejercicio 3.4
# Comentario: El error era de tipo semantico
    # Lo corregí haciendo que el diccionario se vacíe cada vez que entra en el bucle y que se almacene en la lista el correcto.
    # El codigo corregido es:

        
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)