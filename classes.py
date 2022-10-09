#creando una clase vacia

class Perro:
    #atributo de clase
    especie = "mamifero"
    #el metodo __init__ es llamado al crear el objeto
    def __init__(self,nombre, raza):
        print(f"Creando perro {nombre},{raza}")

        #atributos de instancia
        self.nombre= nombre
        self.raza = raza
    
    #metodos de funcionalidad

    def Ladra(self):
        print("Guau")
    
    def Caminar(self,pasos):
        print(f"caminando {pasos} pasos")































    

#creamos un objeto de la clase perro
mi_perro= Perro("Toby","Bulldog")
print(type(mi_perro))
#creando perro toby, bulldog
#class '__main__.Perro'

