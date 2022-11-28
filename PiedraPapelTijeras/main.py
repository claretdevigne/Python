from app import *

# Instancia el contador
counter = Counter()

# Imprime la cabezera: nombre del programa y contador.
def header():
    title()
    counter.showCounter()
    print()

# Imprime el footer, tiene el menu para salir o resetear el contador.
def footer():
    print()
    print("Escribe S para salir, enter para continuar.".center(80))
    option = input()
    print()
    if option == "S" or option == "s":
        exit()
    else:
        counter.reset()

# Punto de entrada de la aplicación.
def main():
    # Bucle que permite que la aplicación no se cierre
    while(True):
        header()

        # try-except: Permite que el mensaje no apareza la primera vez, cuando aún no existen jugadas
        # se usa el try para evitar el error de que aún las variables user y pc, no existen.
        try:
            message(user, pc)
            result(user, pc)
        except:
            pass
        user = userMoves()
        pc = pcMoves()
        pointer = play(user, pc)

        # Aumenta el contador del usuario o de la pc.
        if pointer == 0:
            counter.pcWin()
        elif pointer == 1:
            counter.userWin()

        # Imprime el nombre del ganador al terminar la partida
        if counter.endGame() == "user":
            header()
            print("TÚ GANAS".center(80))
            footer()
        elif counter.endGame() == "pc":
            header()
            print("GAME OVER".center(80))
            footer()

if __name__ == "__main__":
    main()