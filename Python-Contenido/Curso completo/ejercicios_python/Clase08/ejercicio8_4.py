# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 15:05:58 2021

@author: Yamila
"""

from datetime import datetime, timedelta


def dias_habiles(inicio, fin, feriados):
    '''
    Pre: inicio y fin son las fechas que demarcan el período de analisis.
        Ambas fechas deben ser en formato texto ("dd/mm/aaaa")
        El argumento feriado deberá ser la lista con las fechas
        correspondientes a feriados dentro del período.
    Pos: devuelve una lista con las fechas de días hábiles comprendidos en el
        perído. Se considera día hábil a un día que no es feriado ni sábado 
        ni domingo.'''
    
    
    
