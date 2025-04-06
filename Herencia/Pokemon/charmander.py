from fuego import TipoFuego

class Charmander(TipoFuego):
    def __init__(self, defensa=70, ataque=80):
        super().__init__("Charmander", defensa, ataque)