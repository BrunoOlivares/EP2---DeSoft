from iniciojogo import inicio_de_jogo
import pecas_iniciais
from quem_comeca import quem_comeca
from Apecainicial import aprimeirapeça
from qualpecajogarpessoa import peca_a_jogar_pessoa
from qualpecajogarmaquina import peca_a_jogar_maquina
from o_meio import meiota
from soma_final import soma_de_cada_mao
from soma_final import vencedor


print("Seja Bem vindo ao nosso JOGO DE DOMINÓ")
pergunta = input("Vamos jogar??")

while pergunta != 'nao':

    q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

    while q_jogadores > 4 or q_jogadores < 2:
        print("Não se pode jogar com essa quantidade de jogadores. Tente inserir outro número")
        q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

    começo = inicio_de_jogo(q_jogadores)

    pecinhas = pecas_iniciais.as_pecas(28)

    for jogador in começo:
        for numero in range(0, 7):
            jogador.append(pecinhas[numero])
        for i in range(0, 7):
            del pecinhas[0]

    jogadores={}

    i=0

    for i in range (0,q_jogadores):
        jogadores['jogador {}'.format(i+1)]=começo[i]

    ordem = quem_comeca(jogadores)

    mesa = []

    durante_jogo = meiota(ordem, jogadores, mesa, pecinhas)
    jogadores=soma_de_cada_mao(jogadores)
    if durante_jogo=='O jogo foi travado':
        ganhador=vencedor(jogadores)
        print(jogadores)
        print(ganhador)
    else:
        print(durante_jogo)
        print(jogadores)
        print(durante_jogo)












    pergunta=input("Voce ainda quer jogar?")
print('Até a proxima!')
                
                
                    



                        


                

            



