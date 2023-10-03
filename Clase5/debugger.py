# Ejercicio 5.1: Debugger
# Ejercicio 5.2: Más debugger

#%%
def invertir_lista(lista):
    '''Recibe una lista L y la devuelve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento
        i = i-1
        invertida.append(lista[i])
    return invertida

l = [1, 2, 3, 4, 5]
m = invertir_lista(l)
print(f'Entrada {l}, Salida: {m}')

#%%
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

# camion = leer_camion('../Data/camion.csv')
# pprint(camion)

#%%

def busqueda_con_index(lista, e):
    """
    Busca un elemento 'e' en la lista. Si e está en la lista devuelve el índice,
    de lo contrario devuelve -1.
    """

    if e in lista:
        pos = lista.index(e)
    else:
        pos = -1

    return pos


def busqueda_lineal(lista, e):
    """
    Si e está en la lista devuelve su posición, de lo contrario devuelve -1.
    """

    pos = -1  # comenzamos suponiendo que e no está
    i = 0  # variable iteradora

    for z in lista:  # recorremos la lista
        if z == e:  # si encontramos e
            pos = i  # guardamos su posición
            break  # y salimos del ciclo
        i += 1

    return pos


def busqueda_lineal(lista, e):
    """
    Si e está en la lista devuelve su posición, de lo contrario devuelve -1.
    """

    pos = -1

    for i, z in enumerate(lista):
        if z == e:
            pos = i
            break

    return pos
