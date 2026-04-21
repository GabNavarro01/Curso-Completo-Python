import matplotlib.pyplot as plt
import numpy as np
from numpy import pi

# Fourier approximation
def fourier_x2(x, N):
    s = np.zeros_like(x)
    for n in range(1, N + 1):
        s += (1/n**2) * np.cos(n*x) - (pi/n) * np.sin(n*x)
    return (4/3)*(pi**2) + 4*s

# periodic extension of x^2
def f_periodic(x):
    x_mod = np.mod(x, 2*pi)
    return x_mod**2


N = 5

x = np.linspace(-4*pi, 4*pi, 2000)

y_fourier = fourier_x2(x, N)
y_original = f_periodic(x)

plt.plot(x, y_fourier, label=f'Fourier approximation (N={N})')
plt.plot(x, y_original, '--', label='Periodic $x^2$')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Fourier Approximation vs Periodic Extension of $x^2$')
plt.grid()
plt.legend()
plt.show()