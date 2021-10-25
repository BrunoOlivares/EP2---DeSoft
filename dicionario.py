def dicionario_jogadores(lista,quantidade):
    jogadores={}
    i=0
    for i in range (0,quantidade):
        jogadores['jogador {}'.format(i+1)]=lista[i]