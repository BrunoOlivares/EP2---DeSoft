# Aqui se introduz o jogo e traz a possibilidade de seleção de número de jogadores

print("Seja Bem vindo ao nosso JOGO DE DOMINÓ")
print("Regras:")

q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

while q_jogadores > 4 or q_jogadores < 2:
    print("Não se pode jogar com essa quantidade de jogadores. Tente inserir outro número")
    q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

    




