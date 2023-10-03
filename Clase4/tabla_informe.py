# Ejercicio 4.4: La función zip()
# Ejercicio 4.8: Recolectar datos
# Ejercicio 4.9: Imprimir una tabla con formato
# Ejercicio 4.10: Agregar encabezados
# Ejercicio 4.11: Un desafío de formato

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


def hacer_informe(camion, precios):
    """
        Hace un informe de un listado de frutas que incluye: nombre, cantidad
        de cajones, precio de compra y variación con el precio de venta.
    """
    informe = []

    for fruta in camion:
        nombre = fruta['nombre']
        cajones = int(fruta['cajones'])
        precio_compra = float(fruta['precio'])
        precio_venta = float(buscar_precio(fruta['nombre'], '../Data/precios.csv'))
        diferencia = precio_venta - precio_compra

        lote = (nombre, cajones, precio_compra, diferencia)
        informe.append(lote)

    return informe


camion = leer_camion('../Data/camion.csv')

precios = leer_precios('../Data/precios.csv')

informe = hacer_informe(camion, precios)


headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

for header in headers:
    print(f'{header:>10}', end=' ')

print(f'\n---------- ---------- ---------- ----------')

for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {"$" + str(round(precio, 2)):>10s} {cambio:>10.2f}')
