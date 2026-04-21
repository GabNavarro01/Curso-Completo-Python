from datetime import datetime, timedelta

def fecha_reincorporacion(fecha_arranque : str) -> datetime:
    fecha = datetime.strptime(fecha_arranque , '%d/%m/%Y')
    fecha_reinc = fecha + timedelta(days = 200)
    return fecha_reinc