# Ejercicio 2.7: Buscar precios
# Ejercicio 3.1: Lista de tuplas
# Ejercicio 3.2: Lista de diccionarios
# Ejercicio 3.3: Diccionarios como contenedores
# Ejercicio 3.4: Balances

import csv


def leer_camion(nombre_archivo):
    camion = []

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)

        for row in rows:
            try:
                nombre = row[0]
                cajones = int(row[1])
                precio = float(row[2])

                lote = {
                    'nombre': nombre,
                    'cajones': cajones,
                    'precio': precio
                }
                camion.append(lote)
            except ValueError:
                pass

    return camion


def leer_precios(nombre_archivo):
    precios = {}

    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)

        for row in rows:
            try:
                [nombre, precio] = row
                precios[nombre] = float(precio)
            except ValueError:
                pass
    return precios


def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        next(f)
        costo = 0

        for line in f:
            line = line.split(',')
            cajones = int(line[1])
            precio = float(line[2])

            costo += cajones * precio

    return costo


def buscar_precio(fruta, nombre_archivo):
    """
    Busca el precio de la fruta deseada dentro del listado de precios
    """
    precio = None
    with open(nombre_archivo, 'rt') as file:
        for line in file:
            if line:
                row = line.split(',')
                if row[0] == fruta:  # row = [fruta, precio]
                    precio = float(row[1])
                    break

    return precio


camion_csv = '../Data/camion.csv'
precios_csv = '../Data/camion.csv'

precios = leer_precios(precios_csv)
camion = leer_camion(camion_csv)
costo = costo_camion(camion_csv)
venta = 0.0

for fruta in camion:
    precio_venta = buscar_precio(fruta['nombre'], precios_csv)
    venta += precio_venta * fruta.get('cajones')

ganancia = venta - costo

print(f"El costo total del camión es ${round(costo, 2)}")
print(f"La venta total es ${round(venta, 2)}")
print(f"La ganancia total es ${round(ganancia, 2)}")

