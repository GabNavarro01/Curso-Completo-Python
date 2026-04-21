import matplotlib.pyplot as plt

fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba
plt.plot([0,1,2],[0,1,0]) # dibuja la curva
plt.xticks([]), plt.yticks([]) # saca las marcas
# define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x3
plt.subplot(2, 3, 4) 
plt.plot([0,1],[0,1])
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 5) # define la segunda de abajo, de la grilla 2x3
plt.plot([0,1],[1,1], color = 'green')
plt.xticks([]), plt.yticks([])

plt.subplot(2, 3, 6) # define la tercera de abajo, de la grilla 2x3
plt.plot([0,1],[1,0])
plt.xticks([]), plt.yticks([])


plt.show()