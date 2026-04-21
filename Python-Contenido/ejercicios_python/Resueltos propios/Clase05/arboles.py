# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 13:24:23 2022

@author: Luciano
"""

#%%Ejercicio 4.5
import csv

def leer_arboles (nombre_archivo):
    arboleda=[]
    f=open(nombre_archivo, 'rt', encoding='utf8')
    rows=csv.reader(f)
    headers=next(rows)
    
    types=[float, float, int, float, float, float, int, str, str, str, str, str, str, str, str, float, float]
    arboleda=[{name: func(val) for name, func, val in zip(headers, types, row)} for row in rows]
    return arboleda

arboleda=leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
arboleda
    
#%%Ejercicio 4.16

H= [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']== 'Jacarandá']
H

#%%Ejercicio 4.17

H= [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']== 'Jacarandá']
H

#%%Ejercicio 4.18

especies= ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies, arboleda):
    medidas={especie: [(arbol['altura_tot'], arbol['diametro']) for arbol in arboleda if arbol['nombre_com']==especie] for especie in especies}
    return medidas

medidas= medidas_de_especies(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'], arboleda)
medidas

#%%Ejercicio 5.25

import os
import matplotlib.pyplot as plt
import numpy as np

def h_jacaranda(nombre_archivo):
    os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    
    arboleda=leer_arboles(nombre_archivo)
    altos=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']== 'Jacarandá']
    plt.hist(altos,bins=100)

#%%Ejercicio 5.26

def diametro_jacaranda():
    
    H= [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']== 'Jacarandá']
    H
    d=np.array(H)[:,0]
    h=np.array(H)[:,1]
    
    
    plt.xlabel('diametro (cm)')
    plt.ylabel('diametro (m)')
    plt.title('Relación diámetro-alto para Jacarandás')
    plt.scatter(d,h, c='orange')
    
#%%Ejercicio 5.27


import os
import matplotlib.pyplot as plt

def medidas_de_especiesplt():
    
    nombre_archivo=os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda= leer_arboles(nombre_archivo)
    especies=['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas= medidas_de_especies(especies, arboleda)
    med_eu=medidas['Eucalipto']
    med_palo=medidas['Palo borracho rosado']
    med_jaca=medidas['Jacarandá']
    
    d_eucalipto=np.array(med_eu)[:,0]
    h_eucalipto=np.array(med_eu)[:,1]
    
    plt.xlabel('diametro (cm)')
    plt.ylabel('diametro (m)')
    plt.title('Relación diámetro-alto para Eucaliptos')
    plt.scatter(d_eucalipto,h_eucalipto, c="orange")
    
    d_palo=np.array(med_palo)[:,0]
    h_palo=np.array(med_palo)[:,1]
    
    plt.xlabel('diametro (cm)')
    plt.ylabel('diametro (m)')
    plt.title('Relación diámetro-alto para Jacarandá')
    plt.scatter(d_palo,h_palo, c="blue")
    
    d_jaca=np.array(med_jaca)[:,0]
    h_jaca=np.array(med_jaca)[:,1]
    
    plt.xlabel('diametro (cm)')
    plt.ylabel('diametro (m)')
    plt.title('Relación diámetro-alto para Jacarandá')
    plt.scatter(d_jaca,h_jaca, c="red")


