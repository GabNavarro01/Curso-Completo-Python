import pandas as pd
from matplotlib import pyplot as plt


''' Columnas:

Dato por hora -> Time (durante 4 anios) ->  01/01/2011 a 31/12/2014 -> formato -> 01/01/2011 a 12/31/2014
Altura del agua del puerto de San Fernando -> H_SF
Altura del agua del puerto de Buenos Aires -> H_BA

Existen datos faltantes
'''
# Parse dates: convierte la columna Time a formato datetime
# Index_col: establece la columna Time como índice del DataFrame
# Recordar que el formato de fecha es mes-dia-año

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col = ['Time'], parse_dates = True)

dh = df['12-15-2014':].copy()

delta_t = -1 # tiempo que tarda la marea entre ambos puertos
delta_h = 5.4 # diferencia de los ceros de escala entre ambos puertos
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h,     dh['H_BA']]).T.plot()
# T: Transpone el DataFrame (filas <-> columnas) 
plt.show()