from datetime import datetime

def cuanto_falta(fecha_futuro : str):
    fecha = datetime.strptime(fecha_futuro, '%d/%m/%Y')
    diferencia = fecha - datetime.today()

    return abs(diferencia.days)
