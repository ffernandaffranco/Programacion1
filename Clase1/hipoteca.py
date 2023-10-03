# Clase 1 - Ejercicio 1.11: Hipoteca ajustado

# Este programa calcula e imprime el monto total de la hipoteca de David y el tiempo que le tomará pagarla.

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo > 0:
    mes += 1
    if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
        pago_extra = 1000
    else:
        pago_extra = 0

    saldo = saldo * (1 + tasa / 12) - pago_mensual - pago_extra
    total_pagado = total_pagado + pago_mensual + pago_extra

    if saldo < 0:
        total_pagado = total_pagado + saldo
        saldo -= saldo

    print(mes, round(total_pagado, 2), round(saldo, 2))

print(f"Total pagado: {round(total_pagado, 2)}\nMeses: {mes}")
