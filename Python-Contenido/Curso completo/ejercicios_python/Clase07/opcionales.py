# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:49:17 2021

@author: Yamila
"""

import numpy as np
import matplotlib.pyplot as plt

#%% Ejercicio 7.13

n = 12 
X = np.arange(n)

Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='right', va='bottom')


for x, y in zip(X, Y2):
    plt.text(x + 0.4, -y - 0.2, '%.2f' % y, ha='right', va='bottom')

plt.xlim(-.5, n)
plt.xticks([])
plt.ylim(-1.25, +1.25)
plt.yticks([])

plt.show()

#%% Ejercicio 7.14

ax = plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)    

N = 20
theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)
bars = plt.bar(theta, radii, width=width, bottom=0.0)

for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.jet(r / 10.))
    bar.set_alpha(0.5)
    
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()

#%% Ejercicio 7.15

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks([])
plt.ylim(-1.5, 1.5)
plt.yticks([])

plt.show()