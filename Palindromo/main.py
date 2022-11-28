from app import *

# Punto de entrada de la aplicación.
def main():
    while(True):
        header()
        word = receiveWord()
        print()
        result = calculator(word)
        results(result)
        print()
        footer()

if __name__ == "__main__":
    main()