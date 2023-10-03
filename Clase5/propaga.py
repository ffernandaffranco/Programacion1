# Ejercicio 5.5: Invertir una lista
# Ejercicio 5.6: Propagación


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

def propagar(lista):
    """
    Recibe un vector con 0's, 1's y -1's y devuelve un vector en el que los 1's
    se propagaron a sus vecinos con 0.
    """
    nuevo = 0
    prendido = 1

    for i in range(2):
        for indice, fosforo in enumerate(lista):
            if indice < len(lista) - 1 and fosforo == prendido:
                if lista[indice + 1] == nuevo:
                    lista[indice + 1] = prendido

        lista = invertir_lista(lista)

    return lista
