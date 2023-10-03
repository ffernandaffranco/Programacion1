# Ejercicio 4.3: Un ejemplo práctico de enumerate()
# Ejercicio 4.4: La función zip()

import csv


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


costo_final = costo_camion('../Data/missing.csv')
print(f'El costo del camión es de ${costo_final}.')
