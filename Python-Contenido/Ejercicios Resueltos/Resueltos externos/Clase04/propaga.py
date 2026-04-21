def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    return invertida

def encender_fosforos(lista_fosforos):
    l = len(lista_fosforos) - 1
    for n, f in enumerate(lista_fosforos):
        if f == 1 and n < l:
            if lista_fosforos[n+1] == 0:
                lista_fosforos[n+1] = 1
    return lista_fosforos

def propagar(fosforos):
    propagacion = fosforos.copy()
    iniciar_propagacion = encender_fosforos(propagacion)          
    invertir_propagacion = invertir_lista(iniciar_propagacion)
    finalizar_propagacion = encender_fosforos(invertir_propagacion)
    propagacion_completada = invertir_lista(finalizar_propagacion)
    return propagacion_completada
