#1
"""
print("====== Mayores que el primero ========")

valores=int(input("¿Cuantos valores va a introducir?: "))

if valores <= 0:
    print("imposible")
num1=int(input("Escriba un numero: "))
print(num1)


for i in range(valores):
    
    num2=int(input(f"Escribe un numero mayor que {num1}: "))
    print(num2)

    if num2 < num1:
        print(f"{num2} no es mayor que {num1}")
    
print("Gracias por su colaboracion")
"""
"""
2#
    print("MAYORES QUE EL ANTERIOR")
    valores = int(input("¿Cuántos valores va a introducir? "))
    if valores < 1:
        print("¡Imposible!")
    else:
        anterior = int(input("Escriba un número: "))
        for i in range(valores - 1):
            numero = int(input(f"Escriba un número más grande que {anterior}: "))
            if numero <= anterior:
                print(f"¡{numero} no es mayor que {anterior}!")
            anterior = numero
        print("Gracias por su colaboración.")
"""

#===== Bucle While =======
#1
"""
programa=input("Desea continuar con el programa?: ")

while programa:
    if programa == "si":
        programa=input("Desea continuar con el programa?: ")
    else:
        print("hasta la vista beibi")
        break
"""       
#2
"""
programa2=input("Desea continuar con el programa?: ")

while programa2:
    if programa2 == "SI":
        print("hasta la vista beibi")
        break

    else:
        programa2=input("Desea continuar con el programa?: ")
"""
#3
"""
contraseña=input("Ingrese una contraseña: ")
verfificar=input("vuelva a introducirla para confirmar: ")

while contraseña:
    if contraseña == verfificar:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta vuelva a intentarlo.")
        contraseña=input("Ingrese una contraseña: ")
        verfificar=input("vuelva a introducirla para confirmar: ")     
"""

#4
"""
print("HUCHA")
ahorrado = 0.0

while objetivo > ahorrado:
    if objetivo <0:
        print("no se admiten numeros negativos")
        objetivo = float(input("¿Cuántos euros quiere ahorrar?: "))


    ahorrado += float(input("¿Cuántos euros quiere meter en la hucha?: "))
    
    if ahorrado >0:
        
        print(f"¡Objetivo conseguido! Ha ahorrado usted {ahorrado} euros.")
    else:
        print("no se admiten numeros negativos")
"""
#5
"""
pasworld=input("introduce tu contraseña: ")
verifyk=input("verifique su contraseña: ")
limite=3
contador=0

while pasworld:
    contador+=1
    if contador == limite:
        print("lo siento demasiados intentos :C")
        
        break
    if pasworld == verifyk:
        print("contraseña correcta")
        break

    else:
        print("contraseña incorrecta intentelo de nuevo")
        pasworld=input("introduce tu contraseña: ")
        verifyk=input("verifique su contraseña: ")
"""

tupla=(1, 2, "Hola", 3.3, "hello", 5, 4.3)

Datos_de_tipo_int=[1, 2, 5]

Datos_de_tipo_float=[3.3, 4.3]

Datos_de_tipo_str=["Hola", "hello"]

print(f"Datos de tipo int\n{Datos_de_tipo_int}")
print(f"Datos de tipo float\n{Datos_de_tipo_float}")
print(f"Datos de tipo str\n{Datos_de_tipo_str}")








    

