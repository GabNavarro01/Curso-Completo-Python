


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

def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    return invertida
    

'''
0: apagado
1: encendido
-1: carbonizado (no se propaga)
'''

def propagar(lista):
    apagado = 0
    encendido = 1
    carbonizado = -1

    for i in range(2):
        for nFosforo, fosforo in enumerate(lista):
            if nFosforo == len(lista) - 1: #Si llego a la ultima posicion, corto para no pasarme en el nFosforo + 1 y salirme de la lista
                break
            if fosforo == 0:
                continue
            elif fosforo == 1:
                if lista[nFosforo + 1] == 0: #Si el siguiente no esta encendido
                    lista[nFosforo + 1] = 1 #Lo propago
                if (lista[nFosforo + 1] == -1 or lista[nFosforo + 1] == 1):
                    continue
            else:
                continue
        lista_invertida = invertir_lista(lista)
        lista = lista_invertida
    
    return lista


print(propagar([0, 0, 1, 0]))

