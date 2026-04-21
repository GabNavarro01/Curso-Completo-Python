from datetime import datetime

def vida_en_segundos(fecha_nac : str) -> int:
    '''
        Retorna la cantidad de segundos vividos de una persona
        Se asume que nacio a las 00:00 hs
        Pre: dd/mm/yy        
    '''
    fecha = datetime.strptime(fecha_nac, '%d/%m/%Y')
    fecha_hoy = datetime.today()
    diferencia = fecha_hoy - fecha

    return diferencia.total_seconds()