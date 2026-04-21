import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]

cantidad_segun_nombre = df['nombre_cientifico'].value_counts()


print(f'Especies mas frecuentes: {cantidad_segun_nombre.head(10)}')

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]