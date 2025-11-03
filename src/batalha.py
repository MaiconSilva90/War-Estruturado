import random

def atacar(atacante, defensor):
    dado_atacante = random.randint(1, 6)
    dado_defensor = random.randint(1, 6)
    print(f"{atacante.nome} atacando {defensor.nome}")
    print(f"Dado atacante: {dado_atacante}, Dado defensor: {dado_defensor}")

    if dado_atacante > dado_defensor:
        print(f"{atacante.nome} venceu a batalha!")
        defensor.exercitos -= 1
    else:
        print(f"{defensor.nome} defendeu com sucesso!")
        atacante.exercitos -= 1
