from app import *
from screen import *

# Punto de entrada de la aplicación.
def main():
    # Instancia de la clase screen que imprime los mensajes por consola.
    screen = Screen()

    while(True):
        screen.emailCacher()
        email = emailCatcher()
        response = emailVerificator(email)
        status = screen.emailVerificator(response)
        if status == "error":
            continue
        provider = providerVerificator(response)
        name = nameVerificator(response[0])
        screen.emailProcessed(name, provider)

if __name__ == "__main__":
    main()