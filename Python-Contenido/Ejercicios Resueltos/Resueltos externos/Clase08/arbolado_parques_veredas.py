# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 18:46:42 2021

@author: Yamila
"""

import pandas as pd
import os


directorio = '../Data'
archivo_parques = 'arbolado-en-espacios-verdes.csv'
fname_parques = os.path.join(directorio, archivo_parques)
archivo_veredas = 'arbolado-publico-lineal-2017-2018.csv'
fname_veredas = os.path.join(directorio, archivo_veredas)

df_parques = pd.read_csv(fname_parques)
df_veredas = pd.read_csv(fname_veredas)

cols_parques = ['altura_tot', 'diametro']
cols_veredas = ['altura_arbol', 'diametro_altura_pecho']

df_tipas_parques = df_parques[df_parques['nombre_cie']
                              == 'Tipuana Tipu'][cols_parques].copy()
df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico']
                              == 'Tipuana tipu'][cols_veredas].copy()

parques = df_tipas_parques.rename(columns={'altura_tot': 'altura'})
veredas = df_tipas_veredas.rename(
    columns={'altura_arbol': 'altura', 'diametro_altura_pecho': 'diametro'})

tipas_parques = parques.assign(ambiente='parque')
tipas_veredas = veredas.assign(ambiente='vereda')

df_tipas = pd.concat([tipas_veredas, tipas_parques])

df_tipas.boxplot('diametro', by = 'ambiente')

df_tipas.boxplot('altura', by = 'ambiente')



