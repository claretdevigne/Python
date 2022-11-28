from os import system

# Lista en donde se guardaran las letras de las palabras para poder manipularla y compararla
wordList = []

# Limpia la consola e imprime el nombre de la aplicación.
def header():
    system("clear")
    print(" ¿Es un Palíndromo? ".center(80, "="))
    print()

# Imprime un menú en el footer para poder salir de la aplicación.
def footer():
    print("S para salir | enter para introducir una nueva palabra.")
    option = input()
    
    if option == "s" or option == "S":
        exit()
        print()

# Pide una palabra al usuario, la convierte en minusculas y la retorna.
def receiveWord():
    word = input("Por favor introduzca una palabra.\n")
    word = word.lower()
    return word



# Recibe una palabra y calcula si es un palindromo.
def calculator(word):
    # Anexa cada letra de la palabra a la lista "wordList".
    for i in range(len(word)):
        wordList.append(word[i])

    # Crea una copia de la lista "wordList" e invierte la copia.
    wordListCopy = wordList.copy()
    wordListCopy.reverse()

    # Compara la lista "wordList" con su copia invertida "wordListCopy"
    if wordListCopy == wordList:
        return True
    else:
        return False

# Recibe el resultado de los calculos e imprime un mensaje por consola en base a ellos.
def results(result):
    if result == True:
        print("¡Genial! Has encontrado un palíndromo.")
    else:
        print("Los siento, la palabra ingresada no es un palíndromo.")
