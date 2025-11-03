class Mapa:
    def __init__(self):
        # Exemplo de mapa simplificado
        self.territorios = {
            "Brasil": ["Argentina", "Peru"],
            "Argentina": ["Brasil", "Chile"],
            "Peru": ["Brasil", "Colombia"],
            "Chile": ["Argentina"]
        }

    def mostrar_mapa(self):
        for t, vizinhos in self.territorios.items():
            print(f"{t}: vizinhos -> {', '.join(vizinhos)}")
