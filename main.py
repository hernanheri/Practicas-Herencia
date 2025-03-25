from animal import Animal
from perro import Perro
from gato import Gato
from ave import Ave
from murcielago import Murcielago

def main():
    leon = Animal("Leon", 5)
    print(leon)
    leon.hacer_sonido()

    perro = Perro("Churro", 3, "Salchicha")
    perro.hacer_sonido()

    gato = Gato("Michi", 2, 7)
    gato.hacer_sonidos()

    ave = Ave("Piolin", 8)
    ave.hacer_sonido()

    dracula = Murcielago("Draculo", 100, "Vampiro")
    dracula.hacer_sonido()
    dracula.soy_un()


if __name__ == '__main__':
    main()
