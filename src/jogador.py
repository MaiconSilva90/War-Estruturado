class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.territorios = []
        self.exercitos = 0

    def adicionar_territorio(self, territorio):
        self.territorios.append(territorio)

    def __str__(self):
        return f"{self.nome} - Territórios: {len(self.territorios)}, Exércitos: {self.exercitos}"
