
#Ejercicio 1.8: Adelantos


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
pago_mensual_sumado = 3684.11
total_pagado = 0.0
contador = 0
meses = 0 

while saldo > 0:
    meses+=1
    while meses <= 12:
        meses+=1
        saldo = saldo * (1+tasa/12) - pago_mensual_sumado
        total_pagado = total_pagado + pago_mensual_sumado
        contador+=1
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))
print('Meses :', meses)