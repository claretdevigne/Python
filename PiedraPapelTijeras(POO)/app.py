from os import system
from random import randint

class Main():

    # Contador [usuario, pc]
    counter = [0, 0]
    name = ""
    userMove = 0
    pcMove = 0

    # Imprime el título de la aplicación.
    def title(self):
        system("clear")
        print(" Piedra, Papel o Tijeras ".center(80, "="))
        print()

    # Imprime un menú que permite cerrar la app o continuar.
    def exitApp(self):
        print("Enter para continuar o S para salir ".center(80))
        option = input()
        if option == "s" or option == "S":
            self.title()
            print("Gracias por jugar con nosotros".center(80))
            print()
            exit()

    # Pide el nombre del jugador.
    def userNameScreen(self):
        self.title()
        print("Ingresa tu nombre:")
        self.name = input()

    # Imprime un contador de puntos.
    def showCounter(self):
        message = f"| { self.name.upper() }: { self.counter[0] } | PC: { self.counter[1] } |"
        spaces = len(message)
        line = "-" * spaces
        print(line.center(80))
        print(f"| { self.name.upper() }: { self.counter[0] } | PC: { self.counter[1] } |".center(80))
        print(line.center(80))
        print()

    # Aumenta el contador del usuario.
    def userWin(self):
        self.counter[0] += 1
    
    # Aumenta el contador de la pc.
    def pcWin(self):
        self.counter[1] += 1

    # Hace un reset al contador.
    def reset(self):
        self.counter = [0, 0]

    # Verifica que alguno de los jugadores haya alcanzado los 3 puntos.
    def verificateCounter(self):
        if self.counter[0] == 3:
            return "win"
        elif self.counter[1] == 3:
            return "game over"

    # Pide y gestiona la jugada del usuario.
    def userMoveScreen(self):
        self.title()
        self.showCounter()
        moves = ["Piedra", "Papel", "Tijeras"]
        for i in range(len(moves)):
            print(f"{ i + 1 }) { moves[i] }.")
        print()
        print("Ingresa una opción:")
        try:
            option = int(input())

            if option < 1 or option > 3:
                print("Debe escoger una opción válida.")
                input("Enter para continuar")
                return "error"    
            else:
                self.userMove = option

        except:
            print("Debe escoger una opción válida.")
            input("Enter para continuar")
            return "error"

    # Genera la jugada de la pc.
    def pcMoveScreen(self):        
        self.pcMove = randint(1, 3)

    # Calcula el resultado de la partida.
    def gameCalculation(self):
        if self.userMove == self.pcMove:    
            return "match"
        elif self.userMove == 1:
            if self.pcMove == 2:
                self.pcWin()
                return "pc"
            else:
                self.userWin()
                return "user"
        elif self.userMove == 2:
            if self.pcMove == 1:
                self.userWin()
                return "user"
            else:
                self.pcWin()
                return "pc"
        elif self.userMove == 3:
            if self.pcMove == 1:
                self.pcWin()
                return "pc"
            else:
                self.userWin()
                return "user"

    # Imprime un mensaje con el resultado de la partida.
    def messages(self, value):
        if value == "pc":
            print("Has perdido.".center(80))
            print()
        elif value == "user":
            print("Has ganado. !Felicitaciones¡".center(80))
            print()
        elif value == "match":
            print("Han empatado.".center(80))
            print()

    # Imprime la pantalla final del juego.
    def endGame(self, value):
        self.title()
        if value == "win":
            print("¡HAS GANADO!".center(80))
            print()
            self.exitApp()
            self.reset()
        elif value == "game over":
            print("¡GAME OVER!".center(80))
            print()
            self.exitApp()
            self.reset()

    # Imprime la pantalla principal del juego.
    def gameScreen(self):
        moves = ["Piedra", "Papel", "Tijeras"]
        self.title()
        self.showCounter()
        print(f"Escogiste: { moves[self.userMove - 1] } | la pc escogió: { moves[self.pcMove - 1] }".center(80))
        result = self.gameCalculation()
        end = self.verificateCounter()
        if end == "win" or end == "game over":
            self.endGame(end)
        else:
            self.messages(result)
            print()
            self.exitApp()

        