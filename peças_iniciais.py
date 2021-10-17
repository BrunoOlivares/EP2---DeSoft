import random
from iniciojogo import inicio_de_jogo

q_jogadores = int(input("Serão quantos jogadores na partida? "))

os_jogadores = inicio_de_jogo(q_jogadores)

for jogadores in os_jogadores:
    for peças in range(0, 6):
        jogadores.append([str(random.randint(1 , 6)) + "|" + str(random.randint(1,6))])

print (os_jogadores)