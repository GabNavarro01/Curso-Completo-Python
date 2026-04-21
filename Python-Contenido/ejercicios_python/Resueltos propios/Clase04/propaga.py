# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 07:09:51 2022

@author: Luciano
"""
#%%Manera fácil

def propagar(lis):
    for i,f in enumerate(lis):
        if i-1>=0:
            if f==0 and lis[i-1]==1:
                lis[i]=1
                
    for i in range(len(lis)-1,-1,-1):
        if i +1 < len(lis):
            if lis[i]==0 and lis [i+1]==1:
                lis[i]=1
                
    return lis


#%% Manera dificil
def invertir_lista(lista):
    invertida = []
    for e in lista:
        invertida.insert(0, e)
    return invertida

def encender_fosforos(lista_fosforos):
    l = len(lista_fosforos) - 1
    for n, f in enumerate(lista_fosforos):
        if f == 1 and n < l:
            if lista_fosforos[n+1] == 0:
                lista_fosforos[n+1] = 1
    return lista_fosforos

def propagar(fosforos):
    propagacion = fosforos.copy()
    iniciar_propagacion = encender_fosforos(propagacion)          
    invertir_propagacion = invertir_lista(iniciar_propagacion)
    finalizar_propagacion = encender_fosforos(invertir_propagacion)
    propagacion_completada = invertir_lista(finalizar_propagacion)
    return propagacion_completada