# Ejercicio 4.12: Tablas de multiplicar

tabla = list(range(0, 10))

# encabezado de la tabla
print('    ', end='')
for numero in tabla:
    print(f'{numero:>4d}', end='')
print('\n---------------------------------------------')

# tabla
for n in range(0, 10):
    print(f'{" " + str(n) + ":"}', end=' ')  # índice
    for numero in tabla:
        print(f'{numero * n:>4d}', end='')  # productos
    print()  # salto de línea
