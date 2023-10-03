# Clase 1 - Ejercicio 1.5: La pelota que rebota

# Una pelota es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó.
# Este programa imprime en pantalla las alturas que alcanza en sus primeros diez rebotes.

altura = 100
desgaste = 3/5
rebote = 0
cant_rebotes = 10

while rebote < cant_rebotes:
    altura = altura * desgaste
    rebote += 1
    print(rebote, round(altura, 4))
