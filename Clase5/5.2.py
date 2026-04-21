import random

def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))

    return tirada


def es_generala(tirada):
    return len(tirada) == tirada.count(tirada[0])


N = 100000

G=sum([es_generala(tirar()) for i in range(N)])

probabilidad = G/N

def volver_a_tirar(tirada):
    repeticiones_mas_comun = 0
    for tiro in tirada:
        if tirada.count(tiro) >= repeticiones_mas_comun:
            repeticiones_mas_comun = tirada.count(tiro)
            tiro_mas_comun = tiro


    tirada = [tiro_mas_comun] * repeticiones_mas_comun
    for i in range( 6 - repeticiones_mas_comun):
        tirada.append(random.randint(1,6))

    return tirada


def prob_generala(N):
    contador = 0
    for j in range(N):
        tirada = tirar()
        if es_generala(tirada):
            contador += 1  
        for i in range(2):
            tiro_nuevo = volver_a_tirar(tirada)
            if es_generala(tiro_nuevo):
                contador += 1
    return contador/N

def prob_generala_estricta(N):
    contador = 0
    for j in range(N):
        tirada = tirar()
        if es_generala(tirada):
            contador += 1  
    return contador/N

prob = prob_generala(1000000)
prob_estricta = prob_generala_estricta(1000000)

print(f'La probabilidad de sacar generala de manera normal es de {prob}')
print(f'La probabilidad de sacar generala de manera estricta es de {prob_estricta}')

# print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
# print(f'Podemos estimar la probabilidad de sacar generala servida mediante {probabilidad:.6f}.')

