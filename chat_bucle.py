conversacion = ["hola yasir", "adios yasir"]

while True:
    chat = input("Escribe algo (o escribe 'salir' para terminar): ")

    if chat.lower() == "hola":
        print(conversacion[0])
    elif chat.lower() == "adios":
        print(conversacion[1])
    elif chat.lower() == "salir":
        print("Hasta luego. ¡Adiós!")
        break
    else:
        print("No entiendo ese mensaje. Intenta de nuevo.")
