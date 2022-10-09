#=======ZIP=======
"""
a=[1,2]
b=["uno","Dos"]

c=zip(a,b)

for numero, texto in zip(a,b):
    print("numero",numero,"letra",texto)

#=======Zip con n argumentos===========

numero=[1,2]
español=["Uno","Dos"]
ingles=["one","two"]
frances=["un","Deux"]

argumentos= zip(numero,español,ingles,frances)

for n,e,i,f in zip(numero,español,ingles,frances):
    print(n,i,e,f)

#======zip cpn diferentes longitudes=======

numeros = [1, 2, 3, 4, 5]
espanol = ["Uno", "Dos"]

for n, e in zip(numeros, espanol):
    print(n, e)
"""
#======zip cn argumentos=======
"""
numeros = [1, 2, 3, 4, 5]
zz = zip(numeros)
print(list(zz))

# [(1,), (2,), (3,), (4,), (5,)]
"""

#=======zip con diccionarios=========
"""
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for a, b in zip(esp, eng):
    print(a, b)
"""
#para acceder a las keys y valores
"""
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}

for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)
"""
#========enumerante en python=========
"""
abc=("A","B","C")

indice=0
for l in abc:
    print(l,indice)
    indice=+1
"""
#funcion numerate
"""
lista = ["A", "B", "C"]

for indice, l in enumerate(lista):
    print(indice, l)
"""

#===== List Comprehesions========
"""
cuadrados = [i**2 for i in range(5)]
print(cuadrados)

unos = [1 for i in range(5)]
#list comprehesions con condicionales
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']

#set comprehesions 
frase = "El perro de san roque no tiene rabo"
mi_set = {i for i in frase if i == "r"}

#Dictionary comprehesions
lista1 = ['nombre', 'edad', 'región']
lista2 = ['Pelayo', 30, 'Asturias']

mi_dict = {i:j for i,j in zip(lista1, lista2)}
"""
#=======Iteradore e Iterables========
lista = [5, 4, 9, 2]
for elemento in lista:
    print(elemento)# con lista

cadena = "Hola"
for c in cadena:
    print(c) # con cadena

from collections import Iterable

cadena = "Hola"
numero = 3
print("cadena", isinstance(cadena, Iterable))
print("numero", isinstance(numero, Iterable)) # para saber si una clase es iterable o no




