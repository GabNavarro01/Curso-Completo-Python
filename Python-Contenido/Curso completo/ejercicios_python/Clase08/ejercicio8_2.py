# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 12:57:58 2021

@author: Yamila
"""

from datetime import datetime, date, timedelta


def dias_para_primavera(fecha):
    '''
    Pre: recibe una cadena en formato 'dd/mm/AAAA'.
    Pos: devuelve la cantidad de días que faltan para la primavera.
    '''
    fecha_inicio = datetime.strptime(fecha, '%d/%m/%Y')
    data_fecha = date(year=fecha_inicio.year,
                      month=fecha_inicio.month, day=fecha_inicio.day)

    if (fecha_inicio.month == 9 and fecha_inicio.day < 21) or fecha_inicio.month < 9:
        proxima_primavera = date(year=fecha_inicio.year, month=9, day=21)
    elif fecha_inicio.day == 21 and fecha_inicio.month == 9:
        proxima_primavera = fecha_inicio
    else:
        proxima_primavera = date(year=fecha_inicio.year+1, month=9, day=21)

    falta = proxima_primavera - data_fecha
    dias = int(timedelta.total_seconds(falta) // 86400)
    return dias
