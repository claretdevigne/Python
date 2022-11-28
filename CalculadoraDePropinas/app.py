from os import system

# Imprime el nombre de la aplicación.
def title():
    system("clear")
    print(" Calculadora de Propinas ".center(80, "="))
    print()

# Pide el importe de la factura y verifica que sea un monto válido.
# Devuelve una lista con una confirmación y el importe.
def amount():
    while(True):
        print("Por favor ingrese el importe de la factura:")
        value = input()
        try:
            amount = int(value)
            if amount < 0.1:
                print("El monto introducido es muy bajo.")
                input("Presione enter")
                return "restart"
            else:
                print(f"El monto del importe es: ${value}.")
                print("Enter para confirmar | N para ingresar de nuevo")
                option = input()

                if option == "N" or option == "n":
                    return "restart"
                else:
                    return ["ok", amount]
        except:
            print(f"Usted ingresó: {value}.")
            print("Por favor ingrese un monto válido")
            input("Presione enter")
            return "restart"

# Recibe el importe, pregunta por el porcentaje a utilizar y lo aplica.
# Devuelve una lista con una confirmación, el valor del porcentaje y el resultado al aplicarlo.
def definePercertages(amount):

    percetages = [0.18, 0.2, 0.25]
    print("¿Qué porcentage quiere dar como propina?")
    print("1) 18%")
    print("2) 20%")
    print("3) 25%")
    option = input()

    if option == "1":
        tip = amount * percetages[0]
        return ["ok", 18, tip]
    if option == "2":
        tip = amount * percetages[1]
        return ["ok", 20, tip]
    if option == "3":
        tip = amount * percetages[2]
        return ["ok", 25, tip]
    else:
        print("Ingrese una opción válida.")
        input("Presione enter para continuar")
        return ["error"]

# Recibe el importe y la el porcentaje aplicado y realiza la suma.
# Devuelve una lista con el total (importe + iva), el porcentaje y el mismo aplicado.
def total(amount, tip):
    total = amount + tip[2]
    return [total, tip[1], tip[2]]

# Imprime la información por consola.
def showInfo(info):
    print(f"La propina aplicada al {info[1]}% es ${info[2]}, lo que da un total de ${info[0]}.")
    print()

# Pide el número de comensales, gestiona los errores y devuelve la cantidad a pagar por cada comensal.
def totalPerDiner(total):
    while(True):
        print("¿Cuántos comensales hay en la mesa?")
        value = input()
        try:
            diners = int(value)
        except:
            print("Ingrese un número válido")
            input("Presione enter para continuar")
            return ["error"]

        if diners < 1:
            print("Debe haber al menos 1 comensal.")
            input("Presione enter para continuar")
            return ["error"]
        else:
            totalPerDinner = total / diners
            return ["ok", totalPerDinner]

# Imprime la cantidad a pagar por cada comensal.
def message(totalPerDinner):
    print(f"Cada comensal debe pagar ${totalPerDinner[1]}.")
    print()

# Imprime un menú para reiniciar o terminar la ejecución del programa.
# Al terminarlo imprime un mensaje de despedida.
def restart():
    print("S para salir | Enter para reiniciar.")
    option = input()
    if option == "s" or option == "S":
        system("clear")
        title()
        print("Gracias por usar nuestro programa.".center(80))
        print()
        exit()