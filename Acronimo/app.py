from os import system

# Función que limpia la consola e imprime el titulo del programa.
def title():
    system("clear")
    print(" CREADOR DE ACRONIMOS ".center(80, "="))
    print()

# Función que recibe y gestiona el texto introducido por el usuario, y pasandolo a través de un array
# y un bucle for generá el acronimo en mayusculas.
def creator():
    name = input("Ingrese el nombre de una organización:\n")
    nameList = name.split(" ")
    acronimo = ""
    for i in nameList:
        acronimo += i[0]
    return print(acronimo.upper())

# Función que imprime la despedida del programa.
def end():
    print()
    print("Gracias por usar nuestro programa.")
    print()