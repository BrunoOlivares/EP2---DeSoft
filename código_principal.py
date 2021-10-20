from iniciojogo import inicio_de_jogo
import random
import peças_iniciais

print("Seja Bem vindo ao nosso JOGO DE DOMINÓ")
print("----------------------------------------------------------------------------------------------------------")
print("Regras:")
print("----------------------------------------------------------------------------------------------------------")

q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

while q_jogadores > 4 or q_jogadores < 2:
    print("Não se pode jogar com essa quantidade de jogadores. Tente inserir outro número")
    q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

começo = inicio_de_jogo(q_jogadores)

peças = []

i1 = 0
i2 = 0
i3 = 0

while i3 < 28:
    if (str(i1) + "|" + str(i2)) in peças or i2 > 6:
        i1 += 1
        i2 = 0
    else:
        if (str(i2) + "|" + str(i1)) in peças:
            i2 += 1
        else:    
            peças.append((str(i1) + "|" + str(i2)))
            i2 += 1
            i3 += 1












