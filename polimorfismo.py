class coche():
    def desplazamiento(self):
        print("me desplazo en 4 ruedas")

class moto():
    def desplazamiento(self):
        print("me desplazo en 2 ruedas")

class camion():
    def desplazamiento(self):
        print("me desplazo en seis ruedas")

def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

mivehiculo=camion()

mivehiculo.desplazamiento()






