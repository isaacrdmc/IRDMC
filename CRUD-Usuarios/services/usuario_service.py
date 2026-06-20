

from ..models.usuario import crear_usuario

# * 
usuario = []


def registrar_usuario(nombre, edad):
    usuario = crear_usuario(nombre, edad)
    usuario.append(usuario)

    return usuario



def buscar_usuario(nombre):
    for usuarios in usuario:
        if usuarios["nombre"] == nombre:
            return usuario

print("Usuario Service")

