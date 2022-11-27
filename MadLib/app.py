# Diccionario que guarda las palabras requeridas por el juego
palabras = {"adjetivo1": "", "adjetivo2": "", "pajaro": "", "espacio": "",
            "verboPasado": "", "verbo": "", "familiar": "", "objeto": "", 
            "liquido": "", "verboProgresivo1": "", "parteDelCuerpo": "", 
            "nombrePlural": "", "verboProgresivo2": "", "nombreFemenino": ""}

# Función que crea el título, da las instrucciones del juego.
def titulo():
    print("BIENVENIDOS AL JUEGO DE MAD LIB")
    print()
    print("Se te pedirán una serie de adjetivos, verbos o nombres en masculino o femenino y con eso crearemos una LoOOcAA historia")
    print("Pisa enter para continuar o X para salir.")
    respuesta = input()

    if respuesta == "X" or respuesta == "x":
        exit()

# Función encargada de obtener las palabras del usuario desde la linea de comandos. Y luego imprimir la historia.
def recogedorDePalabras():
    palabras["adjetivo1"] = input("Ingresa un adjetivo (Masculino): ")
    palabras["adjetivo2"] = input("Ingresa otro adjetivo (Masculino): ")
    palabras["pajaro"] = input("Ingresa el nombre de un pajaro (femenino): ")
    palabras["espacio"] = input("Ingresa el nombre de un espacio de una casa: ")
    palabras["verbo"] = input("Ingresa un verbo en infinitivo: ")
    palabras["familiar"] = input("Ingresa un familiar (No madre): ")
    palabras["objeto"] = input("Ingresa un objeto (Masculino): ")
    palabras["liquido"] = input("Ingresa un liquido: ")
    palabras["verboProgresivo2"] = input("Ingresa un verbo en presente progresivo: ")
    palabras["adjetivo3"] = input("Ingresa otro adjetivo (Masculino): ")
    palabras["parteDelCuerpo"] = input("Ingresa una parte del cuerpo: ")
    palabras["nombrePlural"] = input("Ingresa un objeto, animal o cosa en plural: ")
    palabras["verboProgresivo2"] = input("Ingresa un verbo en presente progresivo: ")
    palabras["nombreFemenino"] = input("Ingresa un objeto, animal o cosa (femenino): ")
    print()
    print("La historia es: ")

    cuento = f"Era un {palabras['adjetivo1']} y frío día de Noviembre. Desperté con el {palabras['adjetivo2']} olor de {palabras['pajaro']} asada en el/la {palabras['espacio']} del piso de abajo. Yo bajé para ver si podía ayudar a {palabras['verbo']} la cena. Mi madre dijo, \"Ve si tu {palabras['familiar']} necesita un {palabras['objeto']} fresco\" Así que le llevé un montón de vasos llenos de {palabras['liquido']} a la {palabras['verboProgresivo1']} habitación. Cuando llegué allí, no podía creer a mi {palabras['parteDelCuerpo']}. Había unos {palabras['nombrePlural']} {palabras['verboProgresivo2']} en la {palabras['nombreFemenino']}."

    return print(cuento)

# Función encargada de imprimir la despedida.
    def despedida():
        print()
        print("Muchas gracias por usar nuestro programa.")
        print()
