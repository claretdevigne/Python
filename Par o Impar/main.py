from os import system
from app import *

# Función principal:
## 1.- Gestiona el borrado de la consola.
## 2.- Imprime los elementos necesarios.
## 3.- Llama a las funciones de la aplicación.

def main():
    while(True):
        system("clear")
        title()
        value = Input()
        
        if value == "S":
            break
        else:
            try:
                value = int(value)
                calculation(value)
            except:
                print("ERROR: Ha ingresado un número inválido.")
                print("Presione enter para continuar.")
                input()

if __name__ == "__main__":
    main()






