import random


def adivina_el_numero_computadora(z):

    print("=====================================")
    print("  Bienvenida computadora al juego  ")
    print("=====================================")
    print(f"Selecciona un numero entre 1 y {z} para que la computadora intente adivinarlo...")

    limite_inferior = 1
    limite_superior = z

    respuesta = ""

    while respuesta != "c":
         #generar una prediccion
        if limite_inferior != limite_superior:
             prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior # pero tambien puede ser el limite superior
        #obtener respuesta del usuario
        respuesta = input(f"mi prediccion es {prediccion}. si es muy alta ingresa, (A). si es muy baja ingresa, (B). si es correcta ingresa, (C).").lower()

        if limite_superior == "a":
            limite_inferior = prediccion - 1
        elif limite_inferior == "b":
            limite_superior = + 1

    print(f"!SIIII¡La computadora adivino el numero {prediccion} correctamente")

    


      




    


