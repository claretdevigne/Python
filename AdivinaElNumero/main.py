from app import *

# Punto de entrada de la aplicación.
def main():
    while(True):
        secretNumber = generateSecretNumber()
        while (True):
            title()
            userChoice = userMove()
            result = play(secretNumber, userChoice)
            if result == "new game":
                break

if __name__ == "__main__":
    main()        

