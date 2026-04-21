import random
import numpy as np

def medir_temp(N):
    # Genera N temperaturas con distribución normal
                                        #var normal, var estandar, cantidad
    temps = np.round(37.5 + np.random.normal(0, 0.2, N), 2)
    return temps


def resumen_temp(N):
    temps = medir_temp(N)

    maximo = np.max(temps)
    minimo = np.min(temps)
    promedio = np.round(np.mean(temps), 2)
    mediana = np.median(temps)

    return (maximo, minimo, promedio, mediana)
            

N = 999

temperaturas = medir_temp(N)
np.save('../Data/temperaturas',temperaturas)

resumen = resumen_temp(N)
