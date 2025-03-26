from animal import Animal
from perro import Perro
from gato import Gato
from ave import Ave
from murcielago import Murcielago
from pez import Pez
from ornitorrinco import Ornitorrinco

def main():
    #leon = Animal("Leon", 5)
    #print(leon)
    #leon.hacer_sonido()

    perro = Perro("Churro", 3, "Salchicha")
    perro.hacer_sonido()
    print(perro.es_cachorro())

    gato = Gato("Michi", 2, 4)
    gato.hacer_sonidos()
    print("vida(s) restante(s):",gato.vidas)
    print("Atropellado 🏎️" if not gato.sobrevive() else "Vive 😸")

    print("vida(s) restante(s):",gato.vidas)
    print("Intoxicado ☢️" if not gato.sobrevive() else "Vive 😸")

    print("vida(s) restante(s):",gato.vidas)
    print("Electrocutado 🌩️" if not gato.sobrevive() else "Vive 😸")

    print("vida(s) restante(s):",gato.vidas)
    print("Conocio una gatita gotica culona ☠️" if not gato.sobrevive() else "Vive 😸")

    ave = Ave("Piolin", 8)
    ave.hacer_sonido()

    dracula = Murcielago("Dragculo", 100, "Vampiro")
    dracula.hacer_sonido()
    dracula.soy_un()

    Dory = Pez("Dory", 30, "Salada")
    Dory.hacer_sonido()

    perry = Ornitorrinco("Perry", 5)
    perry.hacer_sonido()
    print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevo(s)")
    for i in range(6):
        perry.poner_huevos()
    print(f"{perry.nombre} ha puesto {perry.NUMERO_HUEVOS} huevo(s)")
    



if __name__ == '__main__':
    main()
