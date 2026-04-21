# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:52:19 2021

@author: Yamila
"""

from datetime import datetime, timedelta


def reincorporacion(fecha_inicio, duracion):
    '''
    Pre: fecha_inicio es la fecha de inicio de la licencia con formato "dd/mm/aaaa"
        duracion son los días que dura la licencia
    Pos: devuelve la fecha en la que hay que volver a trabajar.
    '''
    fecha = datetime.strptime(fecha_inicio, '%d/%m/%Y')
    
    plazo = timedelta(days=duracion)
    reincorporacion = fecha + plazo

    return reincorporacion
