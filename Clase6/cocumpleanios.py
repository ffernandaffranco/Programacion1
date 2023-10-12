# Ejercicio 6.3: Cocumpleanios

import random


def generar_fecha():
    """
    Genera una fecha de un año no bisiesto y la devuelve en una tupla con el
    formato (dia, mes)
    """
    mes = random.randint(1,12)
    if mes == 2:
        dia = random.randint(1, 28)
    elif mes in {4, 6, 9, 11}:
        dia = random.randint(1, 30)
    else:
        dia = random.randint(1, 31)

    fecha = (dia, mes)

    return fecha


def prob_cumpleanios(N, K):
    """
    Estima la probabilidad de que en un grupo de N personas cumplan años el
    mismo día en un año no bisiesto, para una cantidad K de simulaciones
    """

    mismodia = 0

    for simulacion in range(K):
        personas = set()

        for persona in range(N):
            cumple = generar_fecha()

            if cumple in personas:
                mismodia += 1
                break
            else:
                personas.add(cumple)

    prob = mismodia / K

    return prob
