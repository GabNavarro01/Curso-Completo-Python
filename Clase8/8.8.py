import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../Data/arbolado-publico-lineal-2017-2018.csv')
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]

cantidad_segun_nombre = df['nombre_cientifico'].value_counts()


print(f'Especies mas frecuentes: \n {cantidad_segun_nombre.head(10)}')

especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]


def boxplot():
    fig, (ax1, ax2) = plt.subplots(2,1)
    df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico', ax = ax1)
    ax1.legend()
    df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico', ax = ax2)
    ax2.legend()
    plt.show()

def pairplot():
    sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
    plt.show()


