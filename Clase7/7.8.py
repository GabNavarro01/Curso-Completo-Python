def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    suma = 0
    for i in range(hasta, start = desde):
        suma+= i

    return suma

def sumar_enteros_triangular(desde, hasta):
    return hasta*(hasta+1)//2 - (desde-1)*desde//2