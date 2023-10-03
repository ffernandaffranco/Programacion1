# Clase 2 - Ejercicio 2.13 - Diccionario geringoso

def geringoso(lista):
    """"
    Traduce una lista a geringoso e introduce los resultados en un diccionario
    """
    diccionario_geringoso = {}

    for objeto in lista:
        capadepenapa = ''
        for letra in objeto:
            capadepenapa += letra
            if letra in 'aeiou':
                capadepenapa += 'p' + letra

        diccionario_geringoso[objeto] = capadepenapa

    print(diccionario_geringoso)


frutas = ['banana', 'manzana', 'mandarina']
geringoso(frutas)
