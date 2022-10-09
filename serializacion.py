import pickle

class vehiculos():

    
    #propiedades

    def __init__(self, marca , modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frenar=False

    #metodos

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frena(self):
        self.frenar=True
    
    def estado(self):
        print(f"marca: {self.marca} \nnmodelo: {self.modelo} \narrancar: {self.enmarcha} \nacelera: {self.acelera} \nfrenar: {self.frenar}")

coche1=vehiculos("forx","13")
coche2=vehiculos("cadillac","12")
coche3=vehiculos("lambo","1990")

coches=[coche1,coche2,coche3]

fichero=open("LosCoches","wb")

fichero=pickle.dump(coches,fichero)

print(fichero)












"""
fichero=open("lista_nombres","rb")

lista=pickle.load(fichero)

print(lista)
"""










#para convertir texto en codigo binario
"""
lista_nombres=["pedro","laura","victor","brayan","jose"]


fichero_binario=open("Lista_nombres","wb")

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

del (fichero_binario)
"""