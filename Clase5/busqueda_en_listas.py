# Ejercicio 5.3: Búsquedas de un elemento
# Ejercicio 5.4: Búsqueda de máximo y mínimo


def buscar_u_elemento(lista, u):
    """
    Recibe una lista y un elemento y devuelve la posición de la última aparición
    de ese elemento en la lista, o -1 si el elemento no está en la lista.
    """
    pos = -1

    for indice, z in enumerate(lista):
        if z == u:
            pos = indice
        else:
            pass

    return pos


def buscar_n_elemento(lista, n):
    """
    Recibe una lista y un elemento y devuelve la cantidad de veces que aparece
    el elemento en la lista.
    """
    aparece = 0

    for z in lista:
        if z == n:
            aparece += 1
        else:
            pass

    return aparece


def maximo(lista):
    """
    Devuelve el máximo de los elementos de una lista
    """
    for indice, e in enumerate(lista):
        if indice == 0:
            m = e
        else:
            if e > m:
                m = e
            else:
                pass

    return m


def minimo(lista):
    """
    Devuelve el mínimo de los elementos de una lista
    """
    for indice, e in enumerate(lista):
        if indice == 0:
            m = e
        else:
            if e < m:
                m = e
            else:
                pass

    return m



