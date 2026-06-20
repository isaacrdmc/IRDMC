
# ^^^^^^^^^^^^^^^^^^^^^^
# ? Funciones:
# ^^^^^^^^^^^^^^^^^^^^^^

"""
    * Las lsitas son:
"""


def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Isaac")


def sumar(a, b):
    return a+b

resultado = sumar(500, 1000)
print(resultado)




# ? FUnciones con parámetro por defecto:
def crear_usuario(nombre, rol="Lector"):
    return {
        "nombre": nombre,
        "rol": rol
    }

print(crear_usuario("Percy"))










# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# ? CON un solo '*' pueden enviar cuantos quiera valores del mismo tipo (Lista)
# ? CON dos '*' pueden enviar cuantos quiera valores de varios tipos (diccionario)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# ? Funciones con "args"
def sumar_todo(*numeros):
    total = 0

    for numero in numeros:
        total += numero

    return total

print(sumar_todo(13, 69, 66, 3, 1, 9))




# * 
def mostrar_datos(**datos):
    for clave, valor in datos.items():
        print(clave, ":", valor)


mostrar_datos(usernmae="Perro5466", contrasena="Perro5466")

