# Clase 2 - Ejercicio 2.3: Precio de la naranja

with open('precios.csv', 'rt') as f:
    for line in f:
        row = line.split(',')

        if row[0] == 'Naranja':
            precio_naranja = float(row[1])

print(f"El precio de la naranja es: {precio_naranja}")
