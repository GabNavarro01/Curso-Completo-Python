

def buscar_u_elemento(lista, e):
    pos = -1

    for i, elemento in enumerate(lista):
        if elemento == e:
            pos = i
            break

    return pos

def buscar_n_elemento(lista, e):
    cantidad = 0

    for elemento in lista:
        if elemento == e:
            cantidad +=1
    return cantidad

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