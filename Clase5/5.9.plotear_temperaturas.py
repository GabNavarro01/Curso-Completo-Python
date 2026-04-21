import numpy as np
import matplotlib.pyplot as plt

temperaturas = np.load('../Data/temperaturas.npy')

plt.hist(temperaturas,bins=25)
plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.