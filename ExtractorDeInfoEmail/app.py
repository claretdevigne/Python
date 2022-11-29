# Pide el correo al usuario y retorna el valor ingresado.
def emailCatcher():
    email = input()
    return email

# Recibe el correo ingresado por el usuario y verifica que cumpla con los criterios 
# que componen un correo electrónico.
def emailVerificator(email):
    # Verifica que el correo incluya un @, sino retorna un error.
    if "@" in email:
        emailFiltered = email.split("@")
    else:
        return "atError"

    # Verifica que luego del @ haya un proveedor de correo electrónico, sino retorna un error.   
    if emailFiltered[1] == "" or emailFiltered[1][0] == ".":
        return "providerError"

    # Utiliza un try para evitar que haya un error.
    # Verifica que exista un punto en el correo ingresado, sino devuelve un error.
    try:
        if emailFiltered[1][-4] == "." or emailFiltered[1][-3] == ".":
            return emailFiltered
    except:
        return "endError"

# Elimina el .algo del correo y verifica si el proveedor es genérico o es de dominio personalizado.
def providerVerificator(email):
    providers = ["google", "gmail", "hotmail", "outlook", "zoho", "icloud", "yahoo", "proton", "mailbox", "hubspot"]

    if email[1][-4] == ".":
        emailProcessed = email[1][:-4]
    elif email[1][-3] == ".":
        emailProcessed = email[1][:-3]

    if emailProcessed in providers:
        index = providers.index(emailProcessed)
        return providers[index].capitalize()
    else:
        return ["personalized", emailProcessed]

# Verifica el nombre del usuario.
def nameVerificator(name):
    try:
        nameSplitted = name.split(".")
        return nameSplitted[0].capitalize()
    except:
        return name.capitalize()