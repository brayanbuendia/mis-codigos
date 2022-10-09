from io import open

archivo_de_texto=open("archivo de texto.txt","r")

print(archivo_de_texto.read())
archivo_de_texto.seek(0)
print(archivo_de_texto.read())



#para añadir una nueva linea de texto
"""
archivo_de_texto.write("Hola")

archivo_de_texto.close()
"""





#para leer linea por linea
"""
lector_lineas=archivo_de_texto.readlines()
archivo_de_texto.close()

print(lector_lineas[1])
"""











#para leer texto
"""
texto=archivo_de_texto.read()

archivo_de_texto.close()

print(texto)
"""




#modo escritura
"""
frase="estupendo dia para estudiar python \n un sabado"

archivo_de_texto.write(frase)
#para cerrar el archivo
archivo_de_texto.close()
"""