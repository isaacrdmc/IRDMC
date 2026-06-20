from services.usuario_service import registrar_usuario
from services.usuario_service import buscar_usuario
from utils.helpers import imprimir_titulo_sistema


imprimir_titulo_sistema("Sistema Usuarios")

registrar_usuario("Isaac", 25)

print(buscar_usuario("Isaac"))
