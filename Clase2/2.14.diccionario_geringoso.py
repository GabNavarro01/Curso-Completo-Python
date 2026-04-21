# Diccionario Geringoso
def palabraGeringosa(palabra):
    geringoso = ''
    for c in palabra:
        if c in ['a','e','i','o','u']:
            geringoso = geringoso + c + 'p' + c
        else:
            geringoso = geringoso + c
    return geringoso

def diccionarioGeringoso(listaDePalabras):
    #(palabras,geringoso)
    listaTuplaGeringosa = []
    
    for item in listaDePalabras:
        listaTuplaGeringosa.append((item,palabraGeringosa(item)))

    diccionario = dict(listaTuplaGeringosa)
    return diccionario

d = diccionarioGeringoso(['banana', 'manzana', 'mandarina'])
print(d)