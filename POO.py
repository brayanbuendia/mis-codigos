"""
class Coche():

    def __init__(self):

    #propiedades
        self.Largochasis=250
        self.anchocahsis=120
        self.__Ruedas=4
        self.enmarcha=False
        self.color="negro"

    #comportamiento o metodos

    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        if(self.enmarcha):
            chequeo=self.__chequeo_interno()


        if (self.enmarcha and chequeo):
            return "El coche esta en marcha"
        
        elif (self.enmarcha and chequeo==False):
            return "no podemos arrancar. hay un problema"

        else:

            return "El coche esta parado"
    
    def estado(self):
        print(f"el coche tiene  {self.__Ruedas} ruedas. un ancho de  {self.anchocahsis} y un largo de {self.Largochasis}")
    
    def __chequeo_interno(self):
        print("Realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            
            return True
        
        else:
            return False
   
        

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("--------------A continuacion crearemos el segundo objeto-------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))


miCoche2.estado()
"""

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


class Furgoneta(vehiculos):
    def cargar(self,carga):
        self.cargado=carga
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"
    


class Moto(vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="voy haciendo caballito"
    
    def estado(self):
        print(f"marca: {self.marca} \nnmodelo: {self.modelo} \narrancar: {self.enmarcha} \nacelera: {self.acelera} \nfrenar: {self.frenar} \n {self.hcaballito}")

class Velectricos(vehiculos):
    def __init__(self,marca,modelo):


        super().__init__(marca,modelo)
    def __init__(self):
        self.autonomia=100
    
    def cargarEnergia(self):
        self.cargando=True




mifurgoneta=Furgoneta("renault","todo terreno")
mifurgoneta.arrancar()
mifurgoneta.estado()
print(mifurgoneta.cargar(True))

miMoto=Moto("Honda", "CBR")

miMoto.caballito()

miMoto.estado()

class BicicletaElectrica(Velectricos,vehiculos):
    pass

   
    

 












    