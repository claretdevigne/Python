from app import *

# Punto de entrada de la aplicación.
def main():
    screen = Screen()
    while(True):
        artist = screen.artistMenu()
        if artist == "error":
            continue
        while(True):
            song = screen.songMenu(artist)
            if song == "error":
                continue
            lyrics = screen.lyrics(song)
            if lyrics == "reset":
                break

if __name__ == "__main__":
    main()