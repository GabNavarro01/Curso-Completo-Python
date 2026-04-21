# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:49:07 2021

@author: Yamila Bruzzone
"""

import random
from collections import Counter

def tirar(d = 5): # lanza los dados
    tirada = [random.randint(1,6) for _ in range(d)]
    return tirada 

def es_generala(tirada): # verifica si los 5 dados son = o no
    if tirada.count(tirada[0]) == 5:
        return True
    else:
        return False

"""La siguiente función separa los dados iguales en una lista
y genera otra lista con los dados no repetidos.
Si todos los dados son iguales guarda al menos 1, siendo la siguiente 
tirada 4 dados."""

def nuevo(tiro):  
    conteo = Counter(tiro)
    r = max(conteo)
    separo = [ ]
    nuevo_tiro = int()
    for i, x in enumerate(tiro):
        if x == r:
            separo.append(r)
        else:
            nuevo_tiro += 1
    return separo, nuevo_tiro

def actualizacion_reserva(cantidad, numero):
    nueva_reserva = []
    while cantidad > 0:
        nueva_reserva.append(numero)
        cantidad -= 1
    return nueva_reserva
    
def prob_generala(N):
    generala = int() # contabilizo las veces que se hace generala
    for _ in range(N): 
        tirada_inicial = tirar() # invoco a la función que tira los dados
        reserva = [ ] # va a guardar los dados que ya no tiro
        if es_generala(tirada_inicial) == True:
           generala += 1 # si al 1º tiro ya tengo generala
        else:
# genero la reserva a partir de la función nuevo(tiro)
            reserva.extend(nuevo(tirada_inicial)[0])
# invoco a la función que tira los dados a partir de los dados no reservados
            segundo_tiro = tirar(nuevo(tirada_inicial)[1])
            if es_generala(reserva + segundo_tiro) == True:
# generala a partir de los dados reservados y los que provienen del 2º tiro
                generala += 1 
            else:
# verifico si a pesar de no tener generala tengo dados iguales que la reserva
                if reserva[0] in segundo_tiro:
# si hay alguno igual lo separo y hago el 3º tiro por la diferencia de dados
                    cantidad_dados_repetidos = segundo_tiro.count(reserva[0])
                    numero_dado = reserva[0]
                    tiro_tres = len(segundo_tiro) - cantidad_dados_repetidos
                    reserva.extend(actualizacion_reserva(cantidad_dados_repetidos, numero_dado))
                    ultimo_tiro = tirar(tiro_tres)
                    if es_generala(reserva + ultimo_tiro) == True:
# generala a partir de los dados reservados y los que provienen del 3º tiro
                        generala += 1 
                else:
# los dados de la 2º tirada no tienen a la reserva. Vuelvo a repetir tirada.
                    tercer_tiro = tirar(nuevo(tirada_inicial)[1])
                    if es_generala(reserva + tercer_tiro) == True:
# generala a partir de los dados reservados y los que provienen del 3º tiro
                        generala += 1
    probabilidad = generala/N

    return probabilidad