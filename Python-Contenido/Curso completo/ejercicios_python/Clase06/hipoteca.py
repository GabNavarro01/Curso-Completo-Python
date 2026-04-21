# -*- coding: utf-8 -*-

#%% Ejercicio 1.7: La hipoteca de David

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))

#%% Ejercicio 1.8: Adelantos

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra = 1000
mes = 0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    if mes < 12:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra
    mes = mes + 1

print("Total pagado", round(total_pagado, 2))
print(mes)

#%% Ejercicio 1.9: Calculadora de adelantos

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 0

while saldo >= 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra

print('Total pagado', round(total_pagado, 2))
print(mes)

#%% Ejercicio1.10: Tablas

# No me imprime el mes 310 con el saldo negativo como muestra el ejemplo del enunciado.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 0

while saldo >= 0:
    print(mes, round(total_pagado, 2), round(saldo, 2))
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra
    
print(f'Total pagado: {round(total_pagado, 2)}')
print(f'Meses: {mes}')
    
#%% Ejercicio 1.11: Bonus

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 0

while saldo >= 0:
    print(mes, round(total_pagado, 2), round(saldo, 2))
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra

print(f'Total pagado: {round(total_pagado, 2)}')
print(f'Meses: {mes}')

#%% Ejercicio 1.20: f-strings

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 0

while saldo >= 0:
    print(f'{mes:>3d} {total_pagado:9.2f} {saldo:9.2f}')
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes = mes + 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra

print(f'Total pagado: {total_pagado:0.2f}')
print(f'Meses: {mes}')