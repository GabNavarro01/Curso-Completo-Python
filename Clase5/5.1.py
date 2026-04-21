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

print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {probabilidad:.6f}.')

