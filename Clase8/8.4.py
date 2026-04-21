from datetime import datetime, timedelta

def dias_habiles(inicio: str, fin: str, feriados: list[str]) -> list[str]:

    lista_dias_habiles = []

    fecha_inicio = datetime.strptime(inicio, '%d/%m/%Y')
    fecha_fin = datetime.strptime(fin, '%d/%m/%Y')

    # convertir feriados a datetime para compararlos fácilmente
    feriados_dt = {
        datetime.strptime(f, '%d/%m/%Y').date()
        for f in feriados
    }

    fecha_actual = fecha_inicio

    while fecha_actual <= fecha_fin:
        es_fin_de_semana = fecha_actual.weekday() >= 5  # 5=sábado, 6=domingo
        es_feriado = fecha_actual.date() in feriados_dt

        if not es_fin_de_semana and not es_feriado:
            lista_dias_habiles.append(fecha_actual )

        fecha_actual += timedelta(days=1)

    lista = [f.strftime('%d/%m/%Y') for f in lista_dias_habiles]
    return lista