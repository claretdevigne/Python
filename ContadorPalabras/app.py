def title():
    print("CONTADOR DE PALABRAS")
    print()

def question():
    print("¿En qué estás pensando hoy?")
    phrase = input()
    print()
    phraseList = phrase.split(" ")
    words = len(phraseList)
    result = print(f"¡Genial! Me has expresado tus pensamentos en {words} palabras.")
    return result

def bye():
    print()
    print("Gracias por probarnos.")
    print()