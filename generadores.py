#==========yield======
"""
def generapares(limite):
    num=1

    while num<limite:
        
        yield num*2

        num=num+1
devuelvepares=generapares(10)


print(next(devuelvepares))

print("aqui podria ir mas codigo....")

print(next(devuelvepares))

print("aqui podria ir mas codigo....")

print(next(devuelvepares))
"""

#=========== yield from =========

def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        
        yield from elemento

            

ciudades_devuelve=devuelve_ciudades("Bogota","medellin","monteria", "cucuta")
print(next(ciudades_devuelve))

print(next(ciudades_devuelve))


