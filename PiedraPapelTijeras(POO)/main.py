from app import *

# Punto de entrada de la aplicación.
def main():
    screen = Main()
    screen.userNameScreen()

    while(True):
        userMove = screen.userMoveScreen()
        if userMove == "error":
            continue
        screen.pcMoveScreen()
        screen.gameScreen()

if __name__ == "__main__":
    main()