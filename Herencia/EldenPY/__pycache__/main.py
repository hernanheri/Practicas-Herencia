from personaje import Personaje
from guerrero import Guerrero

def main():
    
    guts = Guerrero("Guts", 20,5,20,100,1)
    #guts.atributos()

    doxter = Personaje("Doxter",10,5,10,100)
    #doxter.atributos()

    doctormalvadin = Personaje("Doctor Malvadin", 30,50,10,300)
    doctormalvadin.atributos()

    ataque_serie = int(input("Cuantas veces ataca:"))
    for i in range (ataque_serie):
        if doctormalvadin.vida == 0:
            doctormalvadin.morir()
            break
        else:
            print(guts.atacar(doctormalvadin))
    
    
        
    


if __name__ == '__main__':
    main()