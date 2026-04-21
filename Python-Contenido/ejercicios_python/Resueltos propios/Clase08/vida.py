# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:57:08 2022

@author: Luciano
"""

from datetime import datetime, timedelta

def vida_en_segundos(fecha_nac):
    
    fecha_actual=datetime.now()
    fecha_nac=datetime.strptime(fecha_nac, '%d/%m/%Y')
    delta=fecha_actual-fecha_nac
    segundos=timedelta.total_seconds(delta)
    
    print( f'Hasta ahora viviste {round(segundos, 2)} segundos.')
    
    return 


