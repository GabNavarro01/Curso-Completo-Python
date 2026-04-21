
#Ejercicio 1.9


saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
meses = 0

while saldo > 0:
    if  saldo < pago_mensual:
        total_pagado += saldo
        saldo = 0
        meses+=1
        # print((meses), round(total_pagado,2), round(saldo,2))
        print(f'En el mes {meses}, pago acumulado de {round(total_pagado,2)} , queda {round(saldo,2)} por pagar')
        break
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    meses+=1
    
    print(f'En el mes {meses}, pago acumulado de {round(total_pagado,2)} , queda por pagar {round(saldo,2)}')
    # print((meses), round(total_pagado,2), round(saldo,2))
    if pago_extra_mes_comienzo  <= meses <= pago_extra_mes_fin :
        saldo -= pago_extra
        total_pagado += pago_extra 
    # if saldo == 0:
    #     print((meses), round(total_pagado,2), round(saldo,2))


# 878.203
    
print('Total pagado', round(total_pagado, 2))
print('Meses :', meses)