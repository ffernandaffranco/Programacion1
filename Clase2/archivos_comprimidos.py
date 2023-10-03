# Clase 2 - Ejercicio 2.4: Archivos comprimidos

import gzip
with gzip.open('camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end = '')
