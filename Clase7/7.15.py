import matplotlib.pyplot as plt
import numpy as np

n = 2048
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

# ángulo del vector (X,Y)
theta = np.arctan2(Y, X)

# normalizar a [0,1] para usar como color

C = (theta + np.pi) / (2*np.pi)
plt.scatter(X,Y, c= C, alpha = 0.3, s = 100)


plt.xlim([-1,1])
plt.ylim([-1,1])

plt.show()