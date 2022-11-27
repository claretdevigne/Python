# Función que imprime el título de la aplicación.
def title():
    print("PROGRAMA PAR O IMPAR")
    print()

# Función encargada de imprimir las instrucciones, recibir y retornar el número ingresado.
def Input():
    print("Piensa en un número del 1 al 1000 y escribelo:")    
    print("Escribe S para salir")
    number = input()
    return number

# Función que se encarga de realizar los calculos necesarios para que:
# 1.- Se cumplan las condiciones.
# 2.- Calcular si el número es par o impar.
def calculation(value):

    if value < 1 or value > 1000:
        print("Error: El número debe estar entre 1 y 1000.")
        print("Presione enter para continuar.")
        input()
    elif value % 2 == 0:
        print("¡Es un número PAR!")
        print("Presione enter para continuar.")
        input()
    else:
        print("¡Es un número IMPAR!")
        print("Presione enter para continuar.")
        input()
