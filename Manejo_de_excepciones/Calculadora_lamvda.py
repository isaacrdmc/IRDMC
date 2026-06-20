



"""
? Las funciones "lambda" son funciones anonimas como las "ArrowFunctions" de Js "() => {}"
* La utilizamos para 
"""


def calcular(a, op, b):

    # ? Creamos un diccionario de funciones para cimplificar el sistema:
    operaciones = {
        '+': lambda x, y : x + y,
        '-': lambda x, y : x - y,
        '*': lambda x, y : x * y,
        '/': lambda x, y : x / y,
    }


    # * Validaciónes para el sistema:
    if op not in operaciones:
        print(f"El operador {op} no es reconocido dentro del sistema")


    
    # ? Atrapamos la expeción:
    try:
        return operaciones[op] (a,b)
    
    except TypeError as e:
        print(f"Tipo de dato incorrecto: {e}")
    
    except ZeroDivisionError as e:
        print(f"No se puede dividir entre cero")

    finally:
        print(f"Operación terminada")


    



# * 
def leer_numero(numero):
    while True:
        try:
            return float(input(numero))
        except ValueError:
            print("Ingresa un número válido")


def main():
    print("*** Calculadora ***")
    a = leer_numero("Ingres el valor de a: ")

    # * 



print(calcular(10, "-", 4))

