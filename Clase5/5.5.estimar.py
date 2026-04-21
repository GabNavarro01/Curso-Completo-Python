import random

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y


def cae_dentro_del_circulo(x,y):
    return (x ** 2 + y ** 2) < 1

N = 1000000 
M = 0
for i in range(N):
    x , y = generar_punto()
    M += cae_dentro_del_circulo(x,y)

print(4 * M / N)