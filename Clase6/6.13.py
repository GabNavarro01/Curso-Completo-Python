

def buscar_u_elemento(lista, e):
    pos = -1

    for i, elemento in enumerate(lista):
        if elemento == e:
            pos = i
            break

    return pos

def maximo(lista_numeros_positivos):
    max = lista_numeros_positivos[0]
    for elemento in lista_numeros_positivos:
        if(elemento > max):
            max = elemento
    return max

def minimo(lista_numeros_positivos):
    min = lista_numeros_positivos[0]
    for elemento in lista_numeros_positivos:
        if(elemento < min):
            min = elemento

    return min

def buscar_n_elemento(lista, e):
    cantidad = 0
    for elemento in sorted(lista):
        if elemento == e:
            cantidad +=1
    return cantidad

def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def busqueda_lineal_ordenada(lista, e):
    '''Devuelve su posición en una lista ordenada, de lo contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(sorted(lista)): # recorremos la lista
        if z >= e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos