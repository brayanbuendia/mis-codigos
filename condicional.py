import math
# ======== BUCLE FOR =======

# print("programa de evaluacion de notas de alumnos")
# nota_alumno=int(input("introduce tu nota: "))
# def evaluacion(nota):
#     valoracion="aprobado"

#     if nota<5:
#        valoracion="suspendido"
#     return valoracion

# print(evaluacion(nota_alumno))

# #practica if,else y elif

# nota=int(input("introduce tu nota: "))

# if nota<5:
#    print("tu nota es insuficiente")
# elif nota==5:
#     print("tu nota es suficiente")
# elif nota==6:
#     print("tu nota es sobresaliente")
# elif nota==7:
#     print("tu nota es perfecta")
# else:
#     print("esto no es una nota")

# # #ejercisio 1

# n1=int(input("introduce un numero: "))
# n2=int(input("introduce otro numero "))

# if n1>n2:
#     print(f"{n1} es mayor que {n2}")
# elif n2>n1:
#     print(f"{n2} es mayor que {n1}")
# elif n1==n2:
#     print("estos numeros son iguales")

# #ejercisio 2

# nombre=input("introduce tu nombre: ")
# direccion=input("introduce tu direccion: ")
# telefono=float(input("intrpduce tu telefono: "))

# lista=[nombre,direccion,telefono]

# print(f"los datos personales son: {lista}")

# edad=-8

# if 0<edad<100:
#     print("edad es correcta")
# else:
#     print("edad incorrecta")

# #concadenacion de operadores de comparacion 

# presidente=10000000
# director=2000000
# jefe=5000000
# administrador=2000000

# if administrador<jefe<director<presidente:
#      print("todo funciona correctamente")
# else:
#      print("algo falla en la empresa")

# #practica and y or

# print("======== Programa de becas año 2019 ========")
# distancia_centro=int(input("introduce la distancia de tu casa al centro en km: "))
# print(distancia_centro)
# hermanos=int(input("introdcue cuantos hermanos tienes: "))
# print(hermanos)
#  salario_familiar=int(input("introdcue su salario familiar: "))
#  print(salario_familiar)

# if 0<distancia_centro>10 and 0<hermanos>2 or 0<salario_familiar<1000000:
#      print("merece una beca")
# else:
#      print("no merece una beca")
    
# #practica in

# print("======== Asignaturasoptativas Año 2017 ========")
# print("Asignaturas optativas:\n 1-Informatica grafica\n 2-Pruebas de sofware\n 3-Usabilidad y accesibilidad")
# asignatura=input("Introduce la asignatura que desees: ").lower()

# if asignatura in ("Informatica grafica", "Pruebas de sofware", "Usabilidad y accesibilidad"):
#     print(f"La asignatura escogida es {asignatura}")
# else:
#     print("esto no es una asignatura")

# print("========== Formulario de contacto ==========")
# name=input("ingrese su nombre: ")
# apellido=input("ingrese su apellido: ")

# numero=int(input("ingr"))

# valido=False

# email=input("introduce tu email: ")

# for i in range(len(email)):

#     if email[i]=="@":
#         valido=True


    
# if valido:
#     print("email es correcto")
# else:
#     print("email es incorrecto")

# ====== BUCLE WHILE ======

# i=1

# while i<=5:
#     print(f"Ejecuccion {i}")
    
#     i=i+1

    

# print("termino la ejecucion")

# edad=int(input("introduce tu edad: "))

# while edad<=0:
#     print("edad incorrecta; vuelve a intentarlo")
#     edad=int(input("introduce tu edad: "))

# print("Gracias por colaborar")
# print(f"tu edad es {edad }")

# print("programa de calculo de raiz cuadrada")
# numero=int(input("ingrese un numero porfavor: "))

# intentos=0

# while numero<0:
#     print("no se puede hallar la raiz de un numero negativo")

#     if intentos==2:
#         print("has consumido demasiados intentos. El programa ha finalizado")
#         break;
    
#     numero=int(input("ingrese un numero porfavor: "))
#     if numero<0:
#         intentos=intentos+1

# if intentos<2:
#     solucion=math.sqrt(numero)
#     print(f"la raiz cuadrada de {solucion}")

# ======= CONTINUE =======

name="pildoras informaticas"

contador=0

for i in name:

    if i==" ":
        continue
    
    contador+=1
print(contador)

# ======= PASS =======

#para dar un valor nulo, se usa para posponer un trabajo

email=input("introduce tu email: ")

for i in email:

    if i=="@":

        arroba=True

        break;

else:

    arroba:False











           


