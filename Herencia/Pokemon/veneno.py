from pokemon import Pokemon


class TipoVeneno(Pokemon):
    def __init__(self, nombre, defensa, ataque, tipo="Veneno"):
        super().__init__(nombre, defensa, ataque, tipo)