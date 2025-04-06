class Pokemon:
    tipo_emojis = {
        "Fuego": "🔥",
        "Agua": "🌊",
        "Hierba": "🌱",
        "Eléctrico": "⚡",
        "Hielo": "❄️",
        "Lucha": "🥊",
        "Veneno": "☠️",
        "Tierra": "🌬️",
        "Volador": "💸",
        "Psíquico": "🔮",
        "Bicho": "🐛",
        "Roca": "🪨",
        "Fantasma": "👻",
        "Dragón": "🐉",
        "Siniestro": "💀",
        "Acero": "🪦",
        "Hada": "🌸"
    }

    def __init__(self, nombre, defensa, ataque, tipo="N/A"):
        self.nombre = nombre
        self.defensa = defensa
        self.ataque = ataque
        self.tipo = tipo

    def __str__(self):
        emoji = self.tipo_emojis.get(self.tipo, "❓")
        return f"{self.nombre} ({self.tipo} {emoji})"

# Ejemplo de uso
charizard = Pokemon("Charizard", 78, 84, "Fuego")
blastoise = Pokemon("Blastoise", 100, 83, "Agua")
venusaur = Pokemon("Venusaur", 83, 82, "Planta")

print(charizard)
print(blastoise)
print(venusaur)
