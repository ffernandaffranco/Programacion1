# Clase 2 - Ejercicio 2.2: Lectura de un archivo de datos
# Clase 2 - Ejercicio 2.6: Transformar  un script en una función

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


costo = costo_camion('../Data/camion.csv')
print(f"Costo total: {costo}")
