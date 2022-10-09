import collections.abc


# ====== Bucle for =====

# for i in range(0,5):
#     print(i)

# for i in "Python":
#     print(i)

# =====iterables=====
"""
lista = [1, 2, 3, 4]
it = iter(lista)
print(next(it))
print(next(it))

lista = [5, 6, 7]
it1 = iter(lista)
it2 = iter(lista)
print(next(it1)) 
print(next(it1)) 
print(next(it1)) 
print(next(it2))
"""

# =======for anidados======
"""
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

for i in lista:
    for j in i:
        print(j)
"""
# ======ejemplos for=====
"""
texto= "Python"
for i in texto[::-1]:
    print(i) # iterar cadenas alrevez

texto= "python"
for i in texto[::2]:
    print(i) #itera las cadenas saltandose los elementos
"""

#=====range=====

print(list(range(5,20,2)))
"""
for i in range(5, 20, 2):
    print(i) #range(inicio, fin, salto)

for i in range(5,0,-1):
    print(i) # secuencia inversa
"""


# ========== BUCLE WHILE =========
"""
x = ["Uno", "Dos", "Tres"]
while x:
    x.pop(0)
    print(x)

# Permutación a generar
i = 0
j = 0
while i < 3:
    while j < 3:
        print(i,j)
        j += 1
    i += 1
    j = 0
"""
#El primer bucle genera números del 0 al 2, lo que corresponde a la variable i. Por otro lado el segundo bucle genera también número del 0 al 2, almacenados en la variable j. Al tener un bucle dentro de otro, lo que pasa es que por cada i se generan 3 j. Muy importante no olvidar que al finalizar el bucle de la j, debemos resetear j=0
"""                 
i, j, k = 0, 0, 0
while i < 3:
    while j < 3:
        while k < 3:
            print(i,j,k)
            k += 1
            j += 1
        k = 0
    i += 1
    j = 0


z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1

a, b = 0, 1
while b < 0:
    print(b)
    a, b = b, a + b
"""


    
    

















#argumentos for

#argumento end:para ejecutar el bucle en una misma linea de codigo
#     Sintaxis: end=""