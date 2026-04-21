import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    #Da pasos entre -1, 0 y 1 (retrocedo, quieto, avanzo) n veces (largo)
    return pasos.cumsum() #Retorna las posiciones en cada paso
'''
pasos = [1, -1, 0, 1, 1, -1]

La suma acumulada sería:

[1,
 1-1 = 0,
 0+0 = 0,
 0+1 = 1,
 1+1 = 2,
 2-1 = 1]

'''
N = 100000

cantidad = 12
r = np.random.rand(cantidad)
b = np.random.rand(cantidad)
g = np.random.rand(cantidad)
colors = zip(r,g,b)
minimo = 100
maximo = 0
for c in colors:
    plt.subplot(2,1,1)
    plt.title(f'{cantidad} Caminatas al azar', fontsize=10)
    plt.ylim(-700,700)
    plt.yticks([-500, 0, 500])
    plt.xticks([])



    walk = randomwalk(N)
    if abs(walk[-1]) > maximo:
        maximo = abs(walk[-1])
        caminata_mas_leja = walk

    if abs(walk[-1]) < minimo:
        minimo = abs(walk[-1])
        caminata_mas_cerca = walk

    plt.plot(randomwalk(N), color = c)

#------------------------
plt.subplot(2,2,3)
plt.title("La caminata que mas se aleja", fontsize=10)
plt.ylim(-700,700)
plt.yticks([-500, 0, 500])
plt.xticks([])

plt.plot(caminata_mas_leja)

#------------------------
plt.subplot(2,2,4)
plt.title("La caminata que menos se aleja", fontsize=10)
plt.ylim(-700,700)
plt.yticks([-500, 0, 500])
plt.xticks([])

plt.plot(caminata_mas_cerca)

plt.show()