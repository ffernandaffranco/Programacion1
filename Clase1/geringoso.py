# Clase 1 - Ejercicio 1.18: Geringoso rústico

# Este programa recibe y traduce una cadena a geringoso.

cadena = str(input("Decí algo! ").lower())  # Recibe una cadena en minúsculas

tabla = str.maketrans('áéíóú', 'aeiou')
cadena = cadena.translate(tabla)  # Reemplaza las tildes

capadepenapa = ''

for letra in cadena:
    capadepenapa += letra
    if letra in 'aeiou':
        capadepenapa += 'p' + letra

print(f"Geringoso: '{capadepenapa.capitalize()}'.")  # Imprime el resultado

# Input: BOLIGOMA
# Output: Geringoso: 'Bopolipigopomapa'.
