lista_demo = [1, 2, "hello", 2.6,["hola 2"]]

print(lista_demo)
colores = ["red", "green", "blue"]

numeros_lista = list((1, 2, 3, 4))

print(type(numeros_lista))

# de donde hasta donde quiero q llege mis numeros
#r = list(range(1, 100))

#print(r)

#print(dir(colores))

print(len(colores))
print(len(lista_demo))
print(colores[1])

print("green" in colores)
print("pink" in colores)
print(2 in numeros_lista)

print(colores)

colores[2] = "black"

print(colores)

colores[0] = "yellow" 

print(colores)
colores[1] = "blue"
colores[2] = "red"

print(colores)

#append para agregar un nuevo elemento
colores.append("white")

print(colores)

#extend añade nuevos elementos en tuplas o listas

colores.extend(("violet", "pink", "black"))
print(colores)

colores.insert(0, "blue")
print(colores)

colores.insert(8, "green")

print(colores)
# len tambien sirve  para añadir otro elemento al final de la lista
print(len(colores))
colores.insert(len(colores), "amarillo")
print(colores)

colores.pop()
print(colores)
colores.pop()
print(colores)
colores.pop()
print(colores)
colores.pop()
print(colores)
colores.pop(1)
print(colores)
colores.pop(0)
print(colores)

colores.insert(len(colores), "black")
print(colores)
colores.pop(3)
print(colores)
# REMOVE PARA REMOVER STRING Y POP REMOVER STRINGS MEDIANTE SU INDICE
colores.remove("red")
print(colores)
#clear para limpiar la lista
print(colores)

#sort para ordenarlo alfabeticamente
colores.sort()
print(colores)

#sort mas reverse para odenarlo alreves del alfabeto
colores.sort(reverse=True)
print(colores)

#append: añadir un elemento a una lista 
#insert: añadir un elemento a una lista y escoger la posicion
#index: para saber si un elemento se encuentra dentro de dicha lista
#extend: para añadir 1 o mas elementos a una lista
#in: para saber si dicho nombre de un elemento esta dentro de una lista
#*: para repetir la lista por el numero asignado
