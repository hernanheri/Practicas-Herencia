from hierba import TipoHierba
from veneno import TipoVeneno


class Bulbasaur(TipoHierba, TipoVeneno):
    def __init__(self, defensa=111, ataque=118):
        TipoHierba.__init__(self, "Bulbasaur", defensa, ataque)
        TipoVeneno.__init__(self, "Bulbasaur", defensa, ataque)