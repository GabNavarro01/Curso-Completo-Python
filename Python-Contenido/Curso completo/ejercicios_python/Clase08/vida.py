# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:59:08 2021

@author: Yamila
"""

from datetime import datetime, timedelta


def vida_en_segundos(fecha_nac):
    '''
    Pre: recibe una cadena en formato 'dd/mm/AAAA'.
    Pos: devuelve la cantidad de segundo que viviste, como nº flotante.
    '''
    fecha_actual = datetime.now()
    fecha_nacimiento = datetime.strptime(fecha_nac, '%d/%m/%Y')
    vida = fecha_actual - fecha_nacimiento
    vida_en_segundos = timedelta.total_seconds(vida)
    return vida_en_segundos
