from os import system

# Clase principal
class Screen():

    # Imprime el titulo de la aplicación.
    def title(self):
        system("clear")
        print(" Letras de canciones ".center(80, "="))
        print()

    # Imprime un mensaje de despedida y cierra la aplicación.
    def exitFunction(self):
        self.title()
        print("Gracias por usar este programa.".center(80))
        print()
        exit()

    # Imprime un mensaje preguntando si cerrar la aplicación o continuar.
    def resetMenu(self):
        print("Enter para hacer una nueva selección | S para salir")
        option = input()
        if option == "s" or option == "S":
            self.exitFunction()
        else:
            return "reset"

    # Imprime el mensajes de error.
    def errorManager(self, list):
        print()
        print(f"Error: debe ingresar una opción válida entre el 1 y el {len(list)}")
        input("Presione enter para continuar")

    # Imprime un menu de opciones con los artistas agregados.
    # Recibe una opción y gestiona la respuesta.
    def artistMenu(self):
        self.title()
        artistList = ["null", "Sam Smith", "Bruno Mars", "Michael Jackson"]

        for i in range(len(artistList)-1):
            print(f"{i + 1}) {artistList[i + 1]}")
        
        print()
        print("Ingrese una opción:")
        try:
            artist = int(input())
            if artist < 1 or artist > len(artistList):
                self.errorManager(artistList)
                return "error"
            else:
                return artistList[artist]
        except:
            self.errorManager(artistList)
            return "error"

    # Imprime un menu de opciones con las canciones agregadas.
    # Recibe una opción y gestiona la respuesta.
    def songMenu(self, artist):
        self.title()
        songs = {
            "Sam Smith": ["null", "I'm not the only one", "Dancing with a stranger", "Love is a losing game"],
            "Bruno Mars": ["null", "When I was your man", "Just the way you are", "24K Magic"],
            "Michael Jackson": ["null", "Billie Jean", "Smooth Criminal", "Beat It"]
        }
        songList = songs[artist]
        for i in range(len(songList) - 1):
            print(f"{i + 1}) {songList[i + 1]}")
        print()
        try:
            song = int(input())

            if song < 1 or song > len(songs):
                self.errorManager(songs)
                return "error"
            else:
                return songList[song]
        except:
            self.errorManager(songs)
            return "error"


    # Recibe el nombre de una canción e imprime la letra correspondiente.
    def lyrics(self, song):
        lyricsList = {
            "I'm not the only one": 
            """You and me we made a vow
For better or for worse
I can't believe you let me down
But the proof is in the way it hurts
For months on end I've had my doubts
Denying every tear
I wish this would be over now
But I know that I still need you here...""",

            "Dancing with a stranger":
            """I don't wanna be alone tonight (alone tonight)
It's pretty clear that I'm not over you (over you, over you)
I'm still thinking 'bout the things you do (things you do)
So I don't wanna be alone tonight, alone tonight, alone tonight
Can you light the fire? (light the fire, light the fire)
I need somebody who can take control (take control)
I know exactly what I need to do
'Cause I don't wanna be alone tonight, alone tonight, alone tonight...""",

            "Love is a losing game":
            """For you, I was a flame
Love is a losing game
Five story fire as you came
Love is a losing game
One I wished I never played
Oh, what a mess we made
And now, the final frame
Love is a losing game...""",

            "When I was your man":
            """Same bed but it feels just a little bit bigger now
Our song on the radio but it don't sound the same
When our friends talk about you, all it does is just tear me down
\'Cause my heart breaks a little when I hear your name...""",

            "Just the way you are":
            """Oh, her eyes, her eyes
Make the stars look like they're not shinin'
Her hair, her hair
Falls perfectly without her tryin'
She's so beautiful and I tell her everyday
Yeah, I know, I know
When I compliment her, she won't believe me
And it's so, it's so
Sad to think that she don't see what I see
But every time she asks me, "Do I look okay?"
I say...""",

            "24K Magic":
            """Tonight
I just want to take you higher
Throw your hands up in the sky
Let's set this party off right
Players, put yo' pinky rings up to the moon
Girls, what y'all trying to do?
Twenty four karat magic in the air
Head to toe so player
Look out uh...""",

            "Billie Jean":
            """She was more like a beauty queen from a movie scene
I said don't mind, but what do you mean, I am the one
Who will dance on the floor in the round?
She said I am the one, who will dance on the floor in the round...""",

            "Smooth Criminal":
            """As he came into the window was a sound of a crescendo
He came into her apartment, he left the bloodstains on the carpet
She ran underneath the table, he could see she was unable
So she ran into the bedroom, she was struck down
It was her doom...""",

            "Beat It":
            """They told him, \"Don't you ever come around here\"
\"Don't wanna see your face, you better disappear\"
The fire's in their eyes and their words are really clear
So beat it, just beat it..."""
        }
        self.title()
        print(lyricsList[song])
        print()
        option = self.resetMenu()
        return option