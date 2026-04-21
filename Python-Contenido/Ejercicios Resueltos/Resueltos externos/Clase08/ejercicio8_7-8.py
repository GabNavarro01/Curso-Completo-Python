# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:23:29 2021

@author: Yamila
"""

import pandas as pd
import os

# %% Ejercicio 8.7: Lectura y selección

directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio, archivo)
df_lineal = pd.read_csv(fname)

cols_sel = df_lineal[['nombre_cientifico', 'ancho_acera',
                      'diametro_altura_pecho', 'altura_arbol']]

cant_ejemplares = df_lineal['nombre_cientifico'].value_counts()
cant_ejemplares.head(10)

especies_seleccionadas = ['Tilia x moltkei',
                          'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(
    especies_seleccionadas)]

# %% Ejercicio 8.8: Boxplots

df_lineal_seleccion.boxplot('diametro_altura_pecho', by='nombre_cientifico')

df_lineal_seleccion.boxplot('altura_arbol', by='nombre_cientifico')
