# Ejercicio 6.4: Envido

import random


def generar_mazo():
    """
    Genera un mazo de naipes teniendo en cuenta las reglas del Truco, donde las
    cartas de número 8 y 9 no forman parte del mazo
    """

    valores = [1,2,3,4,5,6,7,10,11,12]
    palos = ['oro', 'basto', 'espada', 'copa']
    mazo = [(valor, palo) for valor in valores for palo in palos]

    return mazo


def prob_envido(N):
    """
    Estima la probabilidad de obtener 31, 32 o 33 puntos de envido en una mano
    de Truco para una cantidad N de simulaciones
    """

    mazo = generar_mazo()
    tengobuenas = 0

    for n in range(N):  # Para una N cantidad de simulaciones
        mano = random.sample(mazo, k=3)
        envido = False
        se_repite = []
        numeros_envido = []

        for carta in mano:  # Por cada carta...
            if carta[1] in se_repite:  #... si el palo se repite, hay posible envido
                envido = True
                basto_envido = carta[1]
                break
            else:
                se_repite.append(carta[1])

        if envido:  # Si hay dos o más cartas del mismo palo
            for carta in mano:
                if carta[1] == basto_envido and carta[0] < 8:  # Descarta las figuras
                    numeros_envido.append(carta[0])

            numeros_envido = sorted(numeros_envido, reverse = True)
            if len(numeros_envido) > 1 and sum(numeros_envido[:2]) > 10:  # Si el envido es mayor a 30...
                    tengobuenas += 1  # ... tengo buenas.

    prob = tengobuenas / N

    return prob
