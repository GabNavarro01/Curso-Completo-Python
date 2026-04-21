

def buscar_u_elemento(lista, e):
    pos = -1

    for i, elemento in enumerate(lista):
        if elemento == e:
            pos = i
            break

    return pos

def buscar_n_elemento(lista, e):
    cantidad = 0

    for i, elemento in enumerate(lista):
        if elemento == e:
            cantidad +=1
    return cantidad