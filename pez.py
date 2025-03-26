from animal import Animal

class Pez(Animal):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre,edad)
        self.tipo = tipo

    def hacer_sonido(self):
        print("Glu glu! 🫧")