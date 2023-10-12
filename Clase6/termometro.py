# Ejercicio 6.6: Gaussiana
import random


def medir_temp(n):
    """
    Simula n valores medidos por el termómetro y devuelve una lista con ellos
    """
    mu = 0
    sigma = 0.2
    temperatura_real = 37.5
    lista_temp = []

    for i in range(n):
        temp = temperatura_real + random.normalvariate(mu, sigma)
        lista_temp.append(round(temp,2))

    return lista_temp


def calcular_mediana(lista):
    """
    Calcula la mediana de una lista de valores
    """
    lista.sort()
    largo = len(lista)

    if largo % 2 == 0:
        num1 = lista[largo//2]
        num2 = lista[largo//2 - 1]
        mediana = round(((num1 + num2)/2),2)
    else:
        mediana = round(lista[n//2],2)

    return mediana

def resumen_temp(n):
    """
    Realiza una simulación de n temperaturas y devuelve una tupla con el valor
    máximo, el mínimo, el promedio y la mediana de estas n mediciones.
    """
    lista_temp = medir_temp(n)

    maximo = max(lista_temp)
    minimo = min(lista_temp)
    promedio = round((sum(lista_temp) / len(lista_temp)),2)
    mediana = calcular_mediana(lista_temp)

    resumen = (maximo, minimo, promedio, mediana)

    return resumen


