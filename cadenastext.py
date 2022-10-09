mystr = "brayan buendia"

 # print(dir(mystr))


# upper = mayuscula
print(mystr.upper())
#title = titulo
print(mystr.title())
# lower = minuscula
print(mystr.lower())
#minuscula y mayuscula
print(mystr.swapcase())
# primera letra de cada palabra en mayuscula
print(mystr.capitalize())
#replace para remplazar un string
print(mystr.replace("buendia","brayan").upper())
print(mystr.replace("david","acosta").title())
#count para contar cuantas veces se repite una letra 
print(mystr.count("a"))
print(mystr.count("i"))
# con q palabra empieza la variable
print(mystr.startswith("buendia"))
print(mystr.startswith("david"))
print(mystr.startswith("b"))
#con q palabra termina la variable
print(mystr.endswith("Buendia"))
print(mystr.endswith("Buendia"))
#separa los string
print(mystr.split())
print(mystr.split(" "))
#posicion de los caracteres o letras
print(mystr.find("B"))
#longitud del string
print(len(mystr))
#para saber en q posicion esta cada caracter
print(mystr.index("a"))
#si es alfanumerico o numerico
print(mystr.isnumeric())
print(mystr.isalpha())
#PARA SABER la ubicacion de cada caracter
print(mystr[6])

# + para concadenar string o unir string
print("hola mi nombre es "+ mystr)
# metodo diferente para concadenar string
print(f"mi nombre es {mystr}")
#otro metodo poco utilizado
print("mi nombre es {0}".format(mystr))

print(mystr.upper())

[::-1] para invertir una frase