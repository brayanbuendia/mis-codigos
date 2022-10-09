import random

def jugar():

    print("\t\t\t====== Bienvenido al Juego de piedra, papel y tijera ======\n")
    nombre=input("Porfavor Introduzca su nombre para empezar el juego: ")



    usuario = input("escoge una opcion: 'pi' para piedra, 'pa' para papel y 'ti' para tijera.\n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])

    if usuario == computadora:
        print(f"\t {usuario} vs {computadora}")
        print('\t\t¡empate!') 
    elif usuario == 'pi' and computadora == 'ti':
        print(f"\t{usuario} vs {computadora}")
        print("\t\t====== has vencido a la computadora ======")
    elif usuario == 'pa' and computadora == 'pi':
        print(f"\t{usuario} vs {computadora}")
        print("\t\t====== has vencido a la computadora ======")
    elif usuario == 'ti' and computadora == 'pa':
        print(f"\t{usuario} vs {computadora}")
        print("\t\t====== Has vencido a la computadora ======")
    elif computadora == 'pi' and usuario == 'ti':
        print(f"\t{usuario} vs {computadora}")
        print("\t\t====== la computadora te ha vencido ======")
    elif computadora == 'pa' and usuario == 'pi':
        print(f"\t{usuario} vs {computadora}")
        print("\t\t====== La computadora te ha vencido ======")
    elif computadora == 'ti' and usuario == 'pa':
        print(f"\t{usuario} vs {computadora}")
        print("\t\t====== La computadora te ha vencido ======")
    
    
        
    
        

jugar()


        
        
        
     

   