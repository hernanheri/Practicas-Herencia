from animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad, vidas):
        super().__init__(nombre,edad)
        self.vidas = vidas

    def hacer_sonidos(self):
        #print(f'{self.nombre} esta maullando')
        print("Miau! 🥵🫦")