# Clase 1 - Ejercicio 1.13: El volumen de una esfera

# Este programa le pide al usuario que ingrese el radio 'r'  de una esfera y calcula e imprime en pantalla el volumen de la misma.

radio = float(input("Radio: "))
valor_pi = 3.141592653589793

volumen = (4/3) * valor_pi * radio ** 3

print(f"Volumen: {volumen}")

# Input: r = 6
# Output: Volumen: 904.7786842338603
