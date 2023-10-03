# Ejercicio 6.1: Generala servida
# Ejercicio 6.2: Generala no necesariamente servida

import random
from collections import Counter


def tirar():
    """
    Devuelve una lista con cinco números (entre 1 y 6) generados aleatoriamente
    """

    tirada = []

    for i in range(5):
        tirada.append(random.randint(1,6))
        
    return tirada


def es_generala(tirada):
    """
    Recibe una lista de números y devuelve True si son todos iguales
    """

    generala = False

    if min(tirada) == max(tirada):
        generala = True

    return generala


def se_repite(tirada):
    """
    Recibe una lista de números y devuelve True si un número se repite, y una
    lista con el número que se repite y cuantas veces lo hace.
    """

    serepite = False
    counter = Counter(tirada)

    max_value = max(counter.values())
    max_key = max(counter, key=counter.get)
    numero_maximo = [max_key, max_value]

    if max_value > 1:
        serepite = True

    return serepite, numero_maximo


def tirar_parcial(tirada):
    """
    Recibe una lista con números donde por lo menos uno se repite. Se queda con
    el número repetido y genera nuevos números buscando reemplazar los no
    repetidos
    """

    serepite, num = se_repite(tirada)
    quenum = num[0]
    cuantasveces = num[1]
    tirada_parcial1 = []

    if serepite:
        for i in range(cuantasveces):
            tirada_parcial1.append(quenum)

        for i in range(5 - cuantasveces):
            tirada_parcial1.append(random.randint(1,6))
            tirada_parcial = tirada_parcial1
    else:
        print("Error! Se necesita una tirada con repeticiones para hacer una"
              " tirada parcial")
        tirada_parcial = tirada

    return tirada_parcial


def prob_generala(N):
    """
    Realiza una simulación con N repeticiones para estimar la probabilidad de
    obtener una generala al finalizar una mano de tres tiradas, utilizando la
    estrategia de conservar los dados repetidos en un mismo juego
    """

    saquegenerala = 0

    for i in range(N):  # Por un numero N de juegos tira los dados
        tirada = tirar()

        for j in range(3):  # Por 3 tiradas
            serepite, num = se_repite(tirada)
            generala = es_generala(tirada)

            if not generala:  # Si no es generala...

                if serepite:  # ... y se repite, hace una tirada parcial
                    tirada = tirar_parcial(tirada)

                elif not serepite:  # ... y no se repite, tira todos de nuevo
                    tirada = tirar()

            generala = es_generala(tirada)

            # Si es generala aumenta el contador y termina el juego
            if generala:
                saquegenerala += 1
                break

    prob = saquegenerala / N

    return prob


def prob_generala_servida(N):

    saquegenerala = 0

    for i in range(N):
        tirada = tirar()
        generala = es_generala(tirada)
        if generala:
            saquegenerala += 1

    prob = saquegenerala / N

    return prob


# Para chequear si efectivamente la probabilidad de obtener una generala no
# servida es mayor a la de obtener una generala servida (en cien mil tiradas)
# ⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄⌄
# for i in range(10):
#     print(str(prob_generala(100000)) + ' NO SERVIDA')
#     print(str(prob_generala_servida(100000)) + ' SERVIDA\n')