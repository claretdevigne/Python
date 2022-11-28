from app import *
from os import system

def main():
    system("clear")
    title()
    nameTmp = name()
    birthDateTmp = birthDate()
    addressTmp = address()
    goalsTmp = goals()
    system("clear")
    title()
    result(nameTmp, birthDateTmp, addressTmp, goalsTmp)
    end()

if __name__ == "__main__":
    main()