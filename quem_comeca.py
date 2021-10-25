import random

def quem_comeca(jogadores):
    ordem=[]
    for jogador in jogadores.keys():
        ordem.append(jogador)
    random.shuffle(ordem)
    return ordem

