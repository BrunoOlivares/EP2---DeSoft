from iniciojogo import inicio_de_jogo
import pecas_iniciais
from quem_comeca import quem_comeca
from BemVindo import q_jogadores
import dicionario

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

ordem=quem_comeca(jogadores)
















