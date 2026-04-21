import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']
pocos_nombres = nombres[:3]
df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,3]).cumsum(axis=0), index = idx, columns = pocos_nombres)

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['Suave_' + n for n in pocos_nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados

fig, (ax1, ax2) = plt.subplots(2, 1)
df_walks.plot(ax=ax1, alpha=0.3, label='Original')
ax1.legend()
df_walk_suav.plot(ax=ax2, label='Smoothed')
ax2.legend()

plt.show()

