import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w).mean()

df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()

plt.show()


