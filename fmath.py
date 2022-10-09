# ======= Semana 1 ======



#actividad 1

#  numero = int(input("Digite un numero: "))

#  print(f"El numero es: {numero}")

#  #actividad 2

#  nombre = input("Ingresa tu nombre: ")
#  apellido = input("ingresa tu apellido: ")
#  edad=int(input("ingresa tu edad: "))
#  pais=input("De que pais y ciudad de procedencia eres?: ")
#  cedula=int(input("ingresa tu cedula: "))
#  fechanacimiento=input("ingresa tu fecha de nacimiento: ")
#  gustos=input("Cuales son tus gustos?: ")

#  print(F"Holaa Buenas tardes, mi nombre es {nombre} {apellido}, tengo {edad} años, naci el {fechanacimiento}, Soy de {pais}, Estoy identificado con la cedula de ciudadania {cedula}, y me gusta {gustos} es muy entretenido ")


# # ======= Semana 2 =======

# #actividad 1

# edad2 = int(input("Ingrese su edad: "))

# if edad2 <18 and edad2 >0:
#     print(f"Usted no es mayor de edad tiene {edad2}")

# elif edad2 <0:
#     print("esta edad no existe porfavor responda correctamente")
# elif edad2 > 105:
#     print("Esta edad no existe porfavor responda correctamente")
# else:
#     print(f"Usted es mayor de edad tiene {edad2}")



# # actividad 2 


# aliensRojos=int(input("Ingrese la cantidad de rojos derribados: "))
# aliensVerdes=int(input("Ingrese la cantidad de verdes derribados: "))
# aliensAzules=int(input("Ingrese la cantidad de rojos derribados: "))
# cantidad= aliensAzules + aliensRojos+ aliensVerdes

# puntosRojos= aliensRojos*10
# puntosVerdes= aliensVerdes*5
# puntosAzules= aliensAzules*2


# sumaPuntos = puntosRojos+ puntosVerdes+ puntosAzules
# totalpuntos= sumaPuntos

# adiccionalRojos=0
# adiccionalverdes=0
# adiccionalazules=0


# if aliensRojos > 10:
#     adiccionalRojos = sumaPuntos*0.1
# if aliensVerdes > 5:
#     adiccionalverdes = sumaPuntos*0.05
# if aliensAzules > 2:
#     adiccionalazules = sumaPuntos*0.02

# sumaPuntos= adiccionalRojos +adiccionalverdes +adiccionalazules
# totalpuntos += sumaPuntos

# totalpuntos = int(totalpuntos)



# print("El total de puntos son: ", totalpuntos)
# print("La cantidad total de enemigos derrotados son: ", cantidad)

#======= semana 3 =======


numero=int(input("Ingrese un numero entero: "))

if numero < 10 :
    print(f"numero:{numero}\nunidad")
elif numero <100:
    print(f"numero:{numero}\ndecena")
elif numero <1000:
    print(f"numero:{numero}\ncentena")
elif numero <10000:
    print(f"numero:{numero}\nmilesima")
elif numero <100000:
    print(f"numero:{numero}\ndecena de mil")
elif numero < 1000000:
    print(f"numero:{numero}\ncentena de mil")




    
    
   





