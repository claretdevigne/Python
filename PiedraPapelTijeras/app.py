from os import system
import random

# Funcion que limpia la consola e imprime el nombre de la app, centrada.
def title():
    system("clear")
    print(" PIEDRA, PAPEL O TIJERAS ".center(80, "="))
    print()

# Clase que genera el contador y los métodos para trabajar con él.
class Counter():
    
    userCounter = 0
    pcCounter = 0

    # Método que imprime el contador por consola.
    def showCounter(self):
        print(f"USUARIO: {self.userCounter} puntos. | PC: {self.pcCounter} puntos.".center(80))
        print()

    # Aumenta el contador para el usuario.
    def userWin(self):
        self.userCounter += 1

    # Aumenta el contador para la pc.
    def pcWin(self):
        self.pcCounter += 1

    # Resetea el contador.
    def reset(self):
        self.pcCounter = 0
        self.userCounter = 0

    # Envía un mensaje si la partida ha terminado, ya que alguno de los jugadores alcanzó el máximo
    # de 3 puntos. En cuyo caso envía el nombre del ganador.
    def endGame(self):
        if self.userCounter == 3:
            return "user"
        elif self.pcCounter == 3:
            return "pc"

# Imprime el menú, recibe la respuesta del jugadro, limpia la consola y retorna la jugada del usuario.
def userMoves():
    print("1) Piedra.")
    print("2) Papel.")
    print("3) Tijeras.")
    print()
    option = int(input())
    system("clear")
    return option

# Genera y retorna la jugada de la pc.
def pcMoves():
    moves = [1, 2, 3]
    move = random.choice(moves)
    return move

# Permite imprimir por consola un mensaje con las jugadas, tanto del usuario como de la pc.
def message(user, pc):
    if user == 0 and pc == 0:
        pass
    else:
        moves = {1: "PIEDRA", 2: "PAPEL", 3: "TIJERAS"}
        print(f"Escogiste {moves[user]} | La PC escogió {moves[pc]}".center(80))

# En base a la elección del usuario (1, 2, 3) permite imprimir por consola un mensaje diciendo 
# el resultado de las jugadas.
def result(user, pc):
    if user == 1:
        if pc == 1:
            print("Han empatado.".center(80))
            print()
        elif pc == 2:
            print("Has perdido.".center(80))
            print()
        elif pc == 3:
            print("Tú ganas.".center(80))
            print()
    elif user == 2:
        if pc == 1:
            print("Tú ganas.".center(80))
            print()
        elif pc == 2:
            print("Han empatado.".center(80))
            print()
        elif pc == 3:
            print("Has perdido.".center(80))
            print()
    elif user == 3:
        if pc == 1:
            print("Has perdido.".center(80))
            print()
        elif pc == 2:
            print("Tú ganas.".center(80))
            print()
        elif pc == 3:
            print("Han empatado.".center(80))
            print()

# En base a la elección del usuario (1, 2, 3) piedra, papel o tijeras, respectivamente, retorna el valor 
# 1 si ha ganado el usuario, el valor 0 si ha ganado la pc y nada si hubo un empate. 
# Este resultado se utilizará para activar desde el main el método de la clase Counter necesario
# para actualizar el contador.
def play(user, pc):

    if user == 1:
        if pc == 1:
            pass
        elif pc == 2:
            return 0
        elif pc == 3:
            return 1
    elif user == 2:
        if pc == 1:
            return 1
        elif pc == 2:
            pass
        elif pc == 3:
            return 0
    elif user == 3:
        if pc == 1:
            return 0
        elif pc == 2:
            return 1
        elif pc == 3:
            pass


