
# ^^^^^^^^^^^^^^^^^^^^^^
# ? Diccionarios
# ^^^^^^^^^^^^^^^^^^^^^^

"""
    * Las lsitas son:
"""


empleado = {
    "nombre": "Pedro",
    "edad": 28,
    "activo": True
}


# * Obtenemos los datos del diccionario:
print(empleado.get("nombre"), empleado.get("edad"))

for clave, valor in empleado.items():
    print(clave,":",valor)


# ? MOstramos solo las calves del diccionario
print(empleado.keys())


# ? Par obtener solo los valores del diccionario
print(empleado.values())