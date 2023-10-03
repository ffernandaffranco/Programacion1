import sys


if len(sys.argv) == 1:
    altura = 100
else:
    altura = int(sys.argv[1])

desgaste = 3/5
rebote = 0
cant_rebotes = 10

while rebote < cant_rebotes:
    altura = altura * desgaste
    rebote += 1
    print(rebote, round(altura, 4))