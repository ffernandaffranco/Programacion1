# Ejercicio 6.5: Calcular pi
import random


def generar_punto():
    """
    Genera coordenadas x e y entre 0 y 1 aleatorias para un punto
    """
    x = random.random()
    y = random.random()
    return x,y



def estimar_pi():
    """
    Da una aproximación del valor pi
    """
    M = 0
    N = 100000

    for i in range(N):
        x, y = generar_punto()
        if x ** 2 + y ** 2 < 1:
            M += 1

    valor_pi = 4 * M / N

    return valor_pi