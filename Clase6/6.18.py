from pprint import pprint

def incrementar(s):
    carry = 1
    l = len(s)
    
    for i in range(l-1,-1,-1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


def listar_secuencias(n):
    lista = [0] * n
    lista_nueva = lista.copy()
    lista_de_secuencias = [lista_nueva]
    for i in range(2 ** n - 1):
        incrementar(lista)
        lista_nueva = lista.copy()
        lista_de_secuencias.append(lista_nueva)
    return lista_de_secuencias


lista = listar_secuencias(20)
pprint(lista)