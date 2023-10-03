# Clase 2 - Ejercicio 2.7: Buscar precios

def buscar_precio(fruta, imprimir=True):
    """
    Busca el precio de la fruta deseada dentro del listado de precios
    """
    precio = None
    with open('precios.csv', 'rt', encoding='utf-8') as file:
        for line in file:
            if line:
                row = line.split(',')
                if row[0] == fruta:  # row = [fruta, precio]
                    precio = float(row[1])
                    break

    if imprimir:
        if precio:
            print(f"El precio de un cajón de {fruta} es: {precio}")
        else:
            print(f"{fruta} no figura en el listado de precios.")

    return precio


buscar_precio('Ciruela')

# buscar_precio('Frambuesa') == El precio de un cajón de Frambuesa es: 34.35.
# buscar_precio('Ananá') == Ananá no figura en el listado de precios.
