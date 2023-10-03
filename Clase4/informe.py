# Ejercicio 4.4: La función zip()

import csv


def leer_camion(nombre_archivo):
    """
        Recolecta la información de las frutas en un camión.
    """

    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row_n, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                camion.append(record)
            except ValueError:
                pass

    return camion


def leer_precios(nombre_archivo):
    """
        Lee un listado de precios.
    """
    precios = {}

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)

        for row in rows:
            if row:
                try:
                    nombre = row[0]
                    precio = row[1]
                    precios[nombre] = float(precio)
                except ValueError:
                    pass
    return precios


def costo_camion(nombre_archivo):
    """
        Calcula el costo total de un camión.
    """
    with (open(nombre_archivo, 'rt') as file):
        rows = csv.reader(file)
        headers = next(rows)
        costo = 0

        for row_n, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                cajones = int(record['cajones'])
                precio = float(record['precio'])

                costo += cajones * precio
            except ValueError:
                print(f'Fila {row_n}: No puede interpretar: {row}')

    return costo


def buscar_precio(fruta, nombre_archivo):
    """
    Busca el precio de la fruta deseada dentro de un listado de precios.
    """
    precio = None
    with open(nombre_archivo, 'rt') as file:
        rows = csv.reader(file)

        for row in rows:
            if row[0] == fruta:
                precio = row[1]
                break

    return precio


camion_csv = '../Data/camion.csv'
precios_csv = '../Data/precios.csv'

precios = leer_precios(precios_csv)
camion = leer_camion(camion_csv)
costo = costo_camion(camion_csv)
venta = 0.0


for fruta in camion:
    cajones = int(fruta['cajones'])
    precio_venta = float(buscar_precio(fruta['nombre'], precios_csv))

    venta += cajones * precio_venta


ganancia = venta - costo

print(f"El costo total del camión es ${round(costo, 2)}")
print(f"La venta total es ${round(venta, 2)}")
print(f"La ganancia total es ${round(ganancia, 2)}")



