import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_veredas = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')
df_parques = pd.read_csv('../Data/arbolado-en-espacios-verdes.csv')


cols_parque = [ 'altura_tot', 'diametro', 'nombre_cie']
cols_veredas = ['altura_arbol', 'diametro_altura_pecho', 'nombre_cientifico'] # Luego no voy a necesitar esto
nombres_parques = ['Tipuana Tipu', 'Jacarandá mimosifolia']
nombres_veredas = ['Tipuana tipu', 'Jacaranda mimosifolia']
# Hago replace y rename al dataframe de veredas para que tengan los mismos nombres de columnas que el de parques, y así poder comparar las especies entre ambos dataframes

df_veredas = df_veredas.rename(columns={cols_veredas[0]: cols_parque[0], cols_veredas[1]: cols_parque[1], cols_veredas[2]: cols_parque[2]})
df_veredas['nombre_cie'] = df_veredas['nombre_cie'].replace(nombres_veredas[0], nombres_parques[0])
df_veredas['nombre_cie'] = df_veredas['nombre_cie'].replace(nombres_veredas[1], nombres_parques[1])

df_tipas_parques = df_parques[df_parques['nombre_cie'] == nombres_parques[0]][cols_parque]
df_tipas_veredas = df_veredas[df_veredas['nombre_cie'] == nombres_parques[0]][cols_parque]

df_jacaranda_parque = df_parques[df_parques['nombre_cie'] == nombres_parques[1]][cols_parque].copy()
df_jacaranda_veredas = df_veredas[df_veredas['nombre_cie'] == nombres_parques[1]][cols_parque].copy()

df_tipas_parques['ambiente'] = 'parque'
df_tipas_veredas['ambiente'] = 'vereda'

df_jacaranda_parque['ambiente'] = 'parque'
df_jacaranda_veredas['ambiente'] = 'vereda'

df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
df_jacaranda = pd.concat([df_jacaranda_veredas, df_jacaranda_parque])


fig, (ax1, ax2, ax3, ax4) = plt.subplots(2,2)
df_tipas.boxplot('diametro', by='ambiente', ax = ax1)
df_tipas.boxplot('altura_tot', by='ambiente', ax = ax2)

df_jacaranda.boxplot('diametro_altura_pecho', by='ambiente', ax = ax3)
df_jacaranda.boxplot('altura_tot', by='ambiente', ax = ax4)
plt.show()

'''
Esto convendria hacerlo con una funcion que reciba el nombre cientifico de la especie, y el dataframe, y que haga el boxplot de esa especie en ambos ambientes. 
De esta forma, se podria comparar cualquier especie entre ambos ambientes.

Pre: Ambos dataframes
     El nombre del campo a buscar, en caso de que el nombre cientifico no sea el mismo en ambos dataframes, se podria pasar una tupla con ambos nombres, y la funcion se encargaria de hacer el replace correspondiente.
Post: El ploteo
    '''