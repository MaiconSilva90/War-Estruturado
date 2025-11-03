from jogador import Jogador
from mapa import Mapa
from batalha import atacar

def main():
    # Criando jogadores
    jogador1 = Jogador("Maicon")
    jogador2 = Jogador("Oponente")

    # Exércitos iniciais
    jogador1.exercitos = 5
    jogador2.exercitos = 5

    # Criando mapa
    mapa = Mapa()
    mapa.mostrar_mapa()

    # Exemplo de batalha
    atacar(jogador1, jogador2)

    # Mostrar status
    print(jogador1)
    print(jogador2)

if __name__ == "__main__":
    main()
