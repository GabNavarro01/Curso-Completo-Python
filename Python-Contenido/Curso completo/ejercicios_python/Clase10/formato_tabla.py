# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 21:57:39 2021

@author: Yamila
"""


class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

# %% Tabla TXT


class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''

    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()

# %% Tabla CSV


class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''

    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

# %% Tabla HTML


class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''

    def encabezado(self, headers):
        print('<tr>', end="")
        for h in headers:
            print(f'<th>{h}</th>', end="")
        print('</tr>')

    def fila(self, data_fila):
        print('<tr>', end="")
        for d in data_fila:
            print(f'<td>{d}</td>', end="")
        print('</tr>')

# %%


def crear_formateador(nombre):
    if nombre == 'txt':
        formateador = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador = FormatoTablaCSV()
    elif nombre == 'html':
        formateador = FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {nombre}')
    return formateador

#%%

def imprimir_tabla(lista_1, lista_2, formateador):
   formateador.encabezado(lista_2)
   for obj in lista_1:
       data = []
       for colname in lista_2:
           data.append(str(getattr(obj, colname)))
       formateador.fila(data)