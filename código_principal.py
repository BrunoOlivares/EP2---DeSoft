from iniciojogo import inicio_de_jogo
import random

print("Seja Bem vindo ao nosso JOGO DE DOMINÓ")
print("----------------------------------------------------------------------------------------------------------")
print("Regras:")
print("----------------------------------------------------------------------------------------------------------")

q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

while q_jogadores > 4 or q_jogadores < 2:
    print("Não se pode jogar com essa quantidade de jogadores. Tente inserir outro número")
    q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

começo = inicio_de_jogo(q_jogadores)
for jogadores in começo:
    for peças in range(0, 7):
        jogadores.append([str(random.randint(1 , 6)) + "|" + str(random.randint(1,6))])
print(começo[0])

o_bolinho = []
contador = 1

if q_jogadores == 2:
    while contador <= 14:
        o_bolinho.append([str(random.randint(1,6)) + "|" + str(random.randint(1,6))])
        contador += 1
    
elif q_jogadores == 3:
    while contador <= 7:
        o_bolinho.append([str(random.randint(1,6)) + "|" + str(random.randint(1,6))])
        contador += 1 

else:
    o_bolinho = []

print(o_bolinho)








