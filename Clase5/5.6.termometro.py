import random

def medir_temp(N):
    lista_temp = []

    for i in range(N):
        lista_temp.append(round(37.5 + random.normalvariate(0,0.2),2))

    return lista_temp


def resumen_temp(N):
    lista_temp = medir_temp(N)
    maximo = max(lista_temp)
    minimo = min(lista_temp)
    promedio = round(sum(lista_temp) / N , 2)
    lista_temp.sort()
    if(N % 2 != 0):
        mediana = lista_temp[(int(N + 1)/2)]
    else:
        mediana = (lista_temp[int((N)/2)] + lista_temp[int((N + 1)/2)]) / 2
        
    return (maximo,minimo,promedio,mediana)
            


resumen = resumen_temp(100)