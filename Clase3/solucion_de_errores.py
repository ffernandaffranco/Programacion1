# Ejercicios de errores en el código

#%%
# Ejercicio 3.5: Función tiene_a()


# def tiene_a(expresion):
#     n = len(expresion)
#     i = 0
#     while i < n:
#         if expresion[i] == 'a':
#             return True
#         else:
#             return False
#         i += 1
#
#
# tiene_a('UNSAM 2020')
# tiene_a('abracadabra')
# tiene_a('La novela 1984 de George Orwell')


# Comentario: Hay dos errores.
#
# El primero es de tipo semántico y se puede ver en el bloque if a partir de la línea 11.
# Si la primera letra de la expresión evaluada no es 'a', entonces la función devuelve false y el while no sigue
# ejecutándose. Lo corregí intercambiando el 'return false' y el contador i de lugar. De esta
# forma si el if encuentra una 'a' termina, y si no la encuentra aumenta el contador y se vuelve a repetir el while.
# Si aún después del while no encuentra una 'a', entonces devuelve False.
#
# El segundo es de tipo semántico y se puede ver en la línea 11.
# El bloque if solo está analizando si la expresión tiene la letra 'a', sin tener en cuenta la 'A'. Lo corregí
# analizando la expresion en minúsculas con un lower() (linea 41).
#
# Debajo está el código con las correcciones.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i].lower() == 'a':
            return True
        else:
            i += 1
    return False


tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
# Ejercicio 3.6: Función tiene_a()


# def tiene_a(expresion)
#     n = len(expresion)
#     i = 0
#     while i < n
#         if expresion[i] = 'a'
#             return True
#         i += 1
#     return Falso
#
# tiene_a('UNSAM 2020')
# tiene_a('La novela 1984 de George Orwell')


# Comentario: Hay múltiples errores de sintaxis, detallo a continuación:
# En la línea 56 falta un ':' al final del def
# En la linea 59 falta un ':' al final del while
# En la linea 60 falta un ':' al final, y además agregar otro '='
# En la línea 63 hay que cambiar 'Falso' por 'False'
#
# Debajo está el codigo con las correcciones.

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False


tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%

# Ejercicio 3.7: Función tiene_uno


# def tiene_uno(expresion):
#     n = len(expresion)
#     i = 0
#     tiene = False
#     while (i < n) and not tiene:
#         if expresion[i] == '1':
#             tiene = True
#         i += 1
#     return tiene
#
#
# tiene_a('UNSAM 2020')
# tiene_a('abracadabra')
# tiene_a('La novela 1984 de George Orwell')


# Comentario:
# Hay un error en tiempo de ejecución que ocurre al intentar llamar a la función con el argumento 1984.
# En la línea 96, la función no puede calcular el largo de un entero.
# En la línea 100, la función tampoco puede iterar sobre un número, ni verificar su igualdad con un string '1'.
# Para solucionarlo, pasé la expresión de int a string al principio de la función.
# No sé si es un error, porque el programa funcionaba y hacía lo que se suponia que hiciera, pero eliminé
# la variable 'tiene' completamente porque consideré su existencia redundante. En su lugar imité la sintaxis de los
# ejercicios anteriores.
#
# Debajo está el código con las correcciones.

def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0

    while i < n:
        if expresion[i] == '1':
            return True
        i += 1
    return False


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%

# Ejercicio 3.8: Función suma()


# def suma(a,b):
#     c = a + b
#
# a = 2
# b = 3
# c = suma(a,b)
# print(f"La suma da {a} + {b} = {c}")


# Comentario: El error es de tipo semántico. La función no tiene un valor de retorno especificado. Si no se le
# proporciona un return statement explícito con un valor de retorno explícito, entonces el valor de retorno es None.
#
# Debajo está el codigo con las correcciones.

def suma(a, b):
    c = a + b
    return c


a = 2
b = 3
c = suma(a, b)
print(f"La suma da {a} + {b} = {c}")

#%%

# Ejercicio 3.9: Función leer_camion()


# import csv
# from pprint import pprint
#
# def leer_camion(nombre_archivo):
#     camion=[]
#     registro={}
#     with open(nombre_archivo,"rt") as f:
#         filas = csv.reader(f)
#         encabezado = next(filas)
#         for fila in filas:
#             registro[encabezado[0]] = fila[0]
#             registro[encabezado[1]] = int(fila[1])
#             registro[encabezado[2]] = float(fila[2])
#             camion.append(registro)
#     return camion
#
# camion = leer_camion('../Data/camion.csv')
# pprint(camion)


# Comentario: Los errores en este programa son de tipo semántico. Para solucionar la información que se pisaba con cada
# iteración del for en la lista camion, moví el set registro adentro del for y lo cambié por una lista para conservar
# el orden que le dí a los objetos dentro de ella.
#
# Debajo está el código con las correcciones.

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)

        for fila in filas:
            nombre = fila[0]
            cajones = int(fila[1])
            precio = float(fila[2])

            registro = [nombre, cajones, precio]
            camion.append(registro)

    return camion


camion = leer_camion('../Data/camion.csv')
pprint(camion)
