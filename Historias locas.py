#concatenar cadenas de caracteres
#supongamos que queremos crear una cadena que diga:
#aprende a programar con ______________.

#organizacion = "freeCodeCamp"

#print(f"aprende a programar con {organizacion}")

adj = input("Adjetivo: ")
verbo1 = input("verbo: ")
verbo2 = input("verbo2: ")
sustantivo_plural = input("sustantivo (plurarl): ")


madlib = f"¡programar es tan {adj}! siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}"

print(madlib)