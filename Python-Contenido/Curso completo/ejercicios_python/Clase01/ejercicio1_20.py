nombre = 'Naranja'
cajones = 100
precio = 91.1
print(f'{cajones} cajones de {nombre} a ${precio:0.2f}')

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 0

while saldo >= 0:
    print(f'{mes}, {round(total_pagado)}, {round(saldo)}')
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra