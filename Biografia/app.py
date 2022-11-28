def title():
    print(" BIOGRAFÍA ".center(80, "="))
    print()

def name():
    while(True):
        print("Por favor ingrese su primer nombre y primer apellido: ")
        name = input()
        print()
        fullName = name.split(" ")
        
        if len(fullName) < 2:
            continue
        elif len(fullName[0]) < 2:
            print("Error: Nombre muy corto.")
            print("Presione enter para continuar.")
            input()
            continue
        elif len(fullName[1]) < 2:
            print("Error: Apellido muy corto.")
            print("Presione enter para continuar.")
            input()
            continue
        else:
            name = f"{fullName[0].capitalize()} {fullName[1].capitalize()}"
            return name

def birthDate():
    while(True):
        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        print("Introduzca su fecha de nacimiento:")
        print("\"(DD/MM/YYYY\")")
        birthDate = input()
        
        if len(birthDate.split("/")) < 2:
            continue
        else:
            date = birthDate.split("/")
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])
            if day < 1 or day > 31:
                print("Error: Ingrese un día válido.")
            elif month < 1 or month > 12:
                print("Error: Ingrese un mes válido.")
            elif year > 2022:
                print("Oops viajero del futuro. Ese año aún no existe.")
            else:
                month = months[month - 1]
                date = f"{day} de {month} de {year}"
            print()    
            return date 

def address():
    print("Introduzca su dirección:")
    address = input()
    print()
    return address

def goals():
    print("Introduzca su meta personal:")
    goals = input()
    print()
    return goals

def result(name, birthDay, address, goals):
    print(f"Nombre: {name}.")
    print(f"Fecha de nacimiento: {birthDay}.")
    print(f"Direccón: {address}.")
    print(f"Metas personales: {goals}")
    print()

def end():
    print("Gracias por probarnos.")
    print()