# Ejercicio 4.13: Lectura de los árboles de un parque
# Ejercicio 4.14: Determinar las especies en un parque
# Ejercicio 4.15: Contar ejemplares por especie
# Ejercicio 4.16: Alturas de una especie en una lista
# Ejercicio 4.17: Inclinaciones por especie de una lista
# Ejercicio 4.18: Especie con el ejemplar más inclinado
# Ejercicio 4.19: Especie más inclinada en promedio
# Ejercicio 5.15: Lectura de todos los árboles
# Ejercicio 5.16: Lista de altos de Jacarandá
# Ejercicio 5.17: Lista de altos y diámetros de Jacarandá
# Ejercicio 5.18: Diccionario con medidas

from collections import Counter
import csv
import statistics
from pprint import pprint


def leer_parque(nombre_archivo, parque):
    """
    recibe un archivo y un parque, y devuelve una lista de diccionarios con un
    diccionario por árbol
    """

    lista_parque = []
    arboles = []

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))

            if record['espacio_ve'] == parque:
                arboles.append(record)

    return arboles


def especies(lista_arboles):
    """
    toma una lista de árboles y devuelve el conjunto de especies
    """

    especies = set()

    for arbol in lista_arboles:
        especies.add(arbol['nombre_com'])

    return especies


def contar_ejemplares(lista_arboles):
    """
    toma una lista de árboles y devuelve un diccionario contador con la cantidad
    de ejemplares por especie
    """

    lista = []

    for arbol in lista_arboles:
        lista.append(arbol['nombre_com'])

    counter = Counter(lista)

    return counter


# parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
# frecuentes = {}
#
# for parque in parques:
#     arboles = leer_parque('../Data/arbolado.csv', parque)
#     cantidad = contar_ejemplares(arboles)
#     frecuentes[parque] = cantidad.most_common(5)


def obtener_alturas(lista_arboles, especie):
    """
    toma una lista de árboles y una especie y devuelve una lista con las alturas
    de los ejemplares de esa especie en la lista
    """

    alturas = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            altura = arbol['altura_tot']
            alturas.append(float(altura))

    return alturas


# parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
# jacarandas = {}
#
# for parque in parques:
#     arboles = leer_parque('../Data/arbolado.csv', parque)
#     alturas = obtener_alturas(arboles, 'Jacarandá')
#     jacarandas[parque] = {}
#     prom = round(statistics.mean(alturas), 2)
#     maximo = max(alturas)
#     jacarandas[parque]['promedio'] = prom
#     jacarandas[parque]['maximo'] = maximo
#
# pprint(jacarandas)


def obtener_inclinaciones(lista_arboles, especie):
    """
    toma una lista de árboles y una especie y devuelve una lista con las
    inclinaciones de los ejemplares de esa especie
    """

    inclinaciones = []

    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(int(arbol['inclinacio']))

    return inclinaciones


# parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']
# inclinacion_jacaranda = {}
#
# for parque in parques:
#     arboles = leer_parque('../Data/arbolado.csv', parque)
#     inclinaciones = obtener_inclinaciones(arboles, 'Jacarandá')
#     inclinacion_jacaranda[parque] = inclinaciones


def especimen_mas_inclinado(lista_arboles):
    """
    toma una lista de arboles y devuelve la especie que tiene el ejemplar más
    inclinado y su inclinación
    """

    lista_especies = especies(lista_arboles)
    maximo = {}

    for especie in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        maximo[especie] = max(inclinaciones)

    max_value = max(maximo.values())
    max_key = max(maximo, key=maximo.get)
    ejemplar_maximo = {max_key: max_value}

    return ejemplar_maximo


# Para General Paz = {'Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert)': 70
# Para Los Andes = {'Jacarandá': 30}
# Para Centenario = {'Falso Guayabo (Guayaba del Brasil)': 80}


def especie_promedio_mas_inclinada(lista_arboles):
    """
    toma una lista de árboles y devuelve la especie que en promedio tiene la
    mayor inclinación y el promedio calculado
    """

    promedio_inclinacion = {}

    lista_especies = especies(lista_arboles)

    for especie in lista_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        promedio_inclinacion[especie] = round(statistics.mean(inclinaciones), 2)

    max_value = max(promedio_inclinacion.values())
    max_key = max(promedio_inclinacion, key=promedio_inclinacion.get)
    max_inclinacion = {max_key: max_value}

    return max_inclinacion


# arboles = leer_parque('../Data/arbolado.csv', 'ANDES, LOS')
# a = especie_promedio_mas_inclinada(arboles)
# a = {'Álamo plateado': 25}


def leer_arboles(nombre_archivo):
    """
    Recibe un archivo de árboles y devuelve una lista de diccionarios con la
    información de todos los árboles en el archivo
    """
    arboleda = []

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            arboleda.append(record)

    return arboleda


# Ejercicio 5.16: Lista de altos de Jacarandá
arboleda = leer_arboles('../Data/arbolado.csv')
H = ([float(arbol['altura_tot'])
      for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá'])

# Ejercicio 5.17: Lista de altos y diámetros de Jacarandá
arboleda = leer_arboles('../Data/arbolado.csv')
A = ([(float(arbol['altura_tot']), float(arbol['diametro']))
      for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá'])


def medidas_de_especies(especies, arboleda):
    """
    Recibe una lista de especies y devuelve un diccionario cuyas claves son las
    especies y sus valores asociados son las medidas de cada árbol
    """

    medidas_especies = {}

    for especie in especies:
        medidas_especies[especie] = ([(float(arbol['altura_tot']), float(arbol['diametro']))
              for arbol in arboleda if arbol['nombre_com'] == especie])

    return medidas_especies


# especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
# arboleda = leer_arboles('../Data/arbolado.csv')
# medidas = medidas_de_especies(especies, arboleda)