# Ejercicio 5.5: Invertir una lista


def invertir_lista(lista):
    """
    Recibe una lista y la devuelve invertida
    """
    invertida = []
    indice_ultimo = -1

    for e in lista:
        invertida.append(lista[indice_ultimo])
        indice_ultimo -= 1

    return invertida




