

def suma(nume1, nume2):
    return nume1+nume2

def resta(nume1, nume2):
    return nume1-nume2

def multiplicar(nume1,nume2):
    return nume1*nume2

def dividir(nume1,nume2):
    try:
        return nume1/nume2

    except ZeroDivisionError:
        print("no se puede dividir por cero. Idiota.")
        return "operacion no valida"

while True:
    try:
        op1 = int(input("escriba el primero numero: "))
        op2 = int(input("escriba el segundo numero: "))
        break
    except ValueError:
        print("no se puede escribir texto manco como yair17 xd, intentalo de nuevo maco")
        
    
 

operacion= input("¿que operacion quiere realizar de las siguientes (suma,resta,multiplicar,dividir)? : ")

if operacion == "suma":
   print(suma(op1,op2))
elif operacion == "resta":
    print(resta(op1,op2))
elif operacion =="multiplicar":
    print(multiplicar(op1,op2))
elif operacion == "dividir":
    print(dividir(op1,op2))
else:
    print("Esta opcion no esta asignada.")
"""
#========exepciones multiples en def=========
"""
def divide():
    try:

        num1=int(input("Introduce un numero para dividir: "))
        num2=int(input("Introduce otro numero para dividir: "))

        division=num1/num2
        print(division)
    except ValueError:
        print("no se puede introducir texto pndj")
    except ZeroDivisionError:
        print("no se puede dividir por 0")

    finally:

        print("Division completada")

divide()
"""
#========prueba exepciones3 =========
"""
def evaluaEdad():
    edad=(int(input("introduce tu edad: ")))
    if edad<0:
        raise NameError("no se puede introducir numeros negativos kapo")
    if edad<20:
        print("eres muy joven")
    elif edad<40:
        print( "eres joven")
    elif edad<60:
        print("eres maduro")
    elif edad<100:
        print("Cuidate...")
   
    
    print("el programa ha finalizado")
evaluaEdad()
"""
#========prueba exepcion=======
def calculaRaiz(num1):
    if num1<0:
        raise ValueError("no se puede sacar la raiz cuadrada de un numero negativo")
    else:
        return math.sqrt(num1)

op1=int(input("Introduce un numero: "))    

print(calculaRaiz(op1))