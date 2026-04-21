# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 21:50:39 2022

@author: Luciano
"""

from datetime import datetime, timedelta

def dias_primavera():
    
    fecha_actual=datetime.now()
    fecha_primavera=datetime.strptime('21/09/2022', '%d/%m/%Y')
    delta=abs(fecha_actual-fecha_primavera)
    dias=timedelta.total_seconds(delta)/60/60/24
    
    print( f'Faltan {round(dias, 2)} para la primavera.')
    
    return 


#%% Ejercicio 8.3


def reincorporacion(duracion):
    
    fecha_i= datetime.strptime('26/09/2020', '%d/%m/%Y')
    plazo = timedelta(days=duracion)
    
    reincorporacion= fecha_i + plazo


    return print(reincorporacion)

#%% Ejercicio 8.5

import pandas as pd
import os
import seaborn as sns



directorio = '../Data'
archivo= 'arbolado-en-espacios-verdes.csv'
fname= os.path.join(directorio, archivo)
df= pd.read_csv(fname)

cols= ['altura_tot' , 'diametro' , 'inclinacio']

df_jacarandas= df[df['nombre_com'] == 'Jacarandá'][cols].copy()


df_jacarandas.plot.scatter(x= 'diametro', y = 'altura_tot')
sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')


# %%

import numpy as np

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()

# s2.plot()

s3 = s2.rolling(5).mean()
# s3.plot()

df_series_23 = pd.DataFrame([s2, s3]).T  
df_series_23.plot()

#%%

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()


df_walk_suav.to_csv('caminata_apostolica.csv')

#%% Ejercicio 8.7

cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']

directorio= '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'

f_lineal= os.path.join(directorio,archivo)
df= pd.read_csv(f_lineal)
df_lineal= df[cols_sel]

mas_frec= df['nombre_cientifico'].value_counts()
print(mas_frec.head(10))



#%% Ejercicio 8.8
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]


df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')


#%% Ejercicio 8.9







