

import csv
def leer_archivos(ruta):
    # ? Con la 'r' indicamos que e spara lectura, Tambien esta 'w', 
    with open(ruta, 'r', encoding='utf-8') as file:

        lector = csv.DictReader(file)

        return list[lector]
    

datos = leer_archivos('datos.csv')


print(datos)
