# Ejercicio 3.11: Ejecución desde la línea de comandos con parámetros
import csv
import sys

def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as file:
        headers = next(file).split(',')  # Headers: nombre, cajones, precio
        costo = 0

        for line in file:
            line = line.split(',')
            cajones = int(line[1])
            precio = float(line[2])

            costo += cajones * precio

    return costo


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'


costo = costo_camion(nombre_archivo)
print(f"Costo total: {costo}")
