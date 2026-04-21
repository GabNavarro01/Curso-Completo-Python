# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 23:38:38 2022

@author: Luciano
"""
import os 
import pandas as pd


directorio= '../Data'
archivo1= 'arbolado-en-espacios-verdes.csv'
archivo2= 'arbolado-publico-lineal-2017-2018.csv'

espacios_verdes= os.path.join(directorio,archivo1)
publico=os.path.join(directorio,archivo2)

df_parques= pd.read_csv(espacios_verdes)
df_veredas= pd.read_csv(publico)

cols_parques=['diametro', 'altura_tot']
cols_veredas=['diametro_altura_pecho', 'altura_arbol']

df_tipas_parques= df_parques[df_parques['nombre_cie']
                              == 'Tipuana Tipu'][cols_parques].copy()

df_tipas_veredas= df_veredas[df_veredas['nombre_cientifico']
                              == 'Tipuana Tipu'][cols_veredas].copy()

parques=df_tipas_parques.rename(columns={'altura_tot': 'altura'})
veredas=df_tipas_veredas.rename(columns={'altura_arbol': 'altura'})

tipas_parques = parques.assign(ambiente='parque')
tipas_veredas = veredas.assign(ambiente='vereda')

df_tipas = pd.concat([tipas_veredas, tipas_parques])

df_tipas.boxplot('diametro', by = 'ambiente')

df_tipas.boxplot('altura', by = 'ambiente')


