
lista_frutas= ['banana', 'manzana', 'mandarina']

def diccionario_geringoso(lista_frutas):
    
    lista_geringoso= []
    palabra_geringoso=''
    
    for fruta in lista_frutas:
        for c in fruta:
            palabra_geringoso= fruta.lower().replace('a', 'apa').replace('e', 'epe').replace('i', 'ipi').replace('o', 'opo').replace('u', 'upu')
    
        lista_geringoso.append(palabra_geringoso)
        
    diccionario= dict(zip(lista_frutas, lista_geringoso))
    print(diccionario)
        

