import random

def lista_cumpleanios(cant_alumnos):
    lista = []
    for i in range(cant_alumnos):
        lista.append(random.randint(1,365))
    return lista


def cocumpleanios(cant_personas):
    lista = lista_cumpleanios(cant_personas)
    return len(lista) != len(set(lista))

N = 10000
cant_personas = 30
for personas in range(1,100):
    prob = sum(cocumpleanios(personas) for _ in range(N)) / N
    
    if prob > 0.5:
        print(f"Con {personas} personas la probabilidad supera 0.5")
        break





