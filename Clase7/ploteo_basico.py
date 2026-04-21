import numpy as np
import matplotlib.pyplot as plt



# Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada
plt.figure(figsize=(8, 6), dpi=80)

# Crea un nuevo subplot, en la fila 1, columna 1, y indice 1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plotea el coseno con una línea azul contínua de ancho 1 (en pixeles)
plt.plot(X, C, color="red", linewidth=2.0, linestyle="-", label = 'Coseno')

# Plotea el seno con una línea verde contínua de ancho 1 (en pixeles)
plt.plot(X, S, color="green", linewidth=2.0, linestyle="-.", label = 'Seno')

plt.legend(loc='upper left')


# Puntos donde queremos marcar intersecciones
xs = [-np.pi, -np.pi/2, np.pi/2, np.pi]

# Valores de cos y sin en esos puntos
cos_points = np.cos(xs)
sin_points = np.sin(xs)

# Dibujar los puntos
plt.scatter(xs, cos_points, color="red", zorder=5)
plt.scatter(xs, sin_points, color="green", zorder=5)

'''
Obtengo el eje
Borro el borde derecho
Borro el borde izquierdo
Pongo el eje de las x en el borde de abajo
Pongo el eje de las y en el borde izquierdo
Pongo los valores de las x en el borde de abajo
Pongo los valores de las y en el borde de la izquierda

____________
|<-borde   |
|          |
|          |
|__________| 
paso a ->
     y
     |<-sigue siendo el borde
     |
-----0------ x
     |
     |


'''
ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'

ax.spines['right'].set_color('none') #Saco los bordes
ax.spines['top'].set_color('none') #Saco los bordes
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0)) #Seteo en el centro
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0)) #Seteo en el centro

'''
Anoto los valores de los puntos importantes
'''
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ],[np.sin(t), ], 50, color='red')

plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

'''
Hago mas grandes los valores de los ejes
'''
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))





# Rango del eje x e y
plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)

# Ponemos marcas (ticks) en el eje x e y
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1, 0, +1])

# Podemos grabar el gráfico (con 72 dpi)
# plt.savefig("ejercicio_2.png)", dpi=72)

# Mostramos el resultado en pantalla
plt.show()