import random
from os import system

# Clase que genera y modifica el contador de intentos.
class Attemps:

    counter = 0

    def increase(self):
        self.counter += 1

# Instancia del contador de intentos
playing = Attemps()

# Genera el título de la aplicación
def title():
    system("clear")
    print(" ADIVINA EL NÚMERO ".center(80, "="))
    print()

# Genera un menu de pie de página para el usuario.
def footer(value):
    if value == "win":
        print()
        print("S para salir, cualquier tecla para jugar de nuevo.")
        option = input()
        if option == "S" or option == "s":
            system("clear")
            title()
            print("Muchas gracias por jugar.")
            print()
            exit()
        else:
            return "new game"
    else:
        print()
        print("S para salir o enter para intentarlo de nuevo")
        option = input()
        if option == "S" or option == "s":
            system("clear")
            title()
            print("Muchas gracias por jugar.")
            print()
            exit()


# Genera el número secreto que debe ser adivinado.
def generateSecretNumber():
    secretNumber = random.randint(1, 50)
    return secretNumber

# Pide el número al usuario y gestiona la respuesta y los posibles errores.
def userMove():
    print("Por favor, ingrese un número entre el 1 y el 50")
    try:
        userChoice = int(input())
        print()
    except:
        print("ERROR: Debe colocar un número del 1 al 50.")
        return "error"
    
    if userChoice < 1 or userChoice > 50:
        print("ERROR: Número fuera del rango. Debe escoger un número entre 1 y 50.")
        return "error"
    else:
        return userChoice

# Compara el número ingresado por el usuario con el número secreto y en base a eso devuelve un mensaje 
# por consola. Ejecuta el método para aumentar el contador.
def play(secretNumber, userChoice):
    if secretNumber == userChoice:
        playing.increase()
        print("¡Felicidades has acertado el número!")
        print(f"Número de intentos: {playing.counter}")
        footer("win")
    elif userChoice == "error":
        footer(None)
    else:
        playing.increase()
        print("No has acertado.")
        footer(None)
        