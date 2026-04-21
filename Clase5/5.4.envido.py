import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]


mano = random.sample(naipes,k=3)

def convertir_valor(carta):
    if carta[0] <= 7:
        return carta[0]
    else:
        return 0

def envido(mano):
    valores = [convertir_valor(carta) for carta in mano]
    palos = [carta[1] for carta in mano]
    mejor = max(valores)  # caso sin palos iguales

    if palos[0] == palos[1]:
        mejor = max(mejor, valores[0] + valores[1] + 20)

    if palos[0] == palos[2]:
        mejor = max(mejor, valores[0] + valores[2] + 20)

    if palos[1] == palos[2]:
        mejor = max(mejor, valores[1] + valores[2] + 20)

    return mejor

env = envido(mano)