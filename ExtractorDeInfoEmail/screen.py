from os import system

# Clase que crea un objeto Screen con los mensajes de pantalla.
class Screen():

    # Limpia la consola e imprime el nombre de la aplicación.
    def title(self):
        system("clear")
        print(" Extractor de Email ".center(80, "="))
        print()

    # Imprime un menú con la opción de resetear o salir de la aplicación.
    def footer(self):
        print("S para salir | Enter para introducir otro email.")
        option = input()
        if option == "s" or option == "S":
            self.title()
            print("Gracias por usar nuestro programa.".center(80))
            print()
            exit()

    # Imprime un mensaje pidiendo el correo.
    def emailCacher(self):
        self.title()
        print("Por favor ingrese su correo electrónico: ")

    # Imprime un mensaje de error, si existe, y retorna un mensaje que permite reiniciar la consola.
    def emailVerificator(self, value):
        if value == "atError":
            self.title()
            print("Email incorrecto.")
            print("El email debe tener un @")
            input("Enter para continuar")
            return "error"
        elif value == "endError":
            self.title()
            print("Email incorrecto.")
            print("El email debe terminar en .algo")
            input("Enter para continuar")
            return "error"
        elif value == "providerError":
            self.title()
            print("Email incorrecto.")
            print("El proveedor de correo no puede estar vacío.")
            input("Enter para continuar")
            return "error"
        
    # Imprime la respuesta final de la aplicación.
    def emailProcessed(self, name, email):
        if email[0] == "personalized":
            self.title()
            print(f"Hola, {name}. Estoy observando que estás usando un dominio personalizado de {email[1].capitalize()}. ¡Impresionante!.")
            print()
            self.footer()
        else:
            self.title()
            print(f"Hola, {name}. Veo que tu email está registrado con {email.capitalize()}. ¡Eso es genial!.")
            print()
            self.footer()