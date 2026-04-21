import numpy as np
import matplotlib.pyplot as plt

paquetes = np.load('../Data/paquetes.npy')

plt.hist(paquetes,bins=40)
plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.