from iniciojogo import inicio_de_jogo
import pecas_iniciais

print("Seja Bem vindo ao nosso JOGO DE DOMINÓ")
print("----------------------------------------------------------------------------------------------------------")
print("Regras:")
print("----------------------------------------------------------------------------------------------------------")

q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

while q_jogadores > 4 or q_jogadores < 2:
    print("Não se pode jogar com essa quantidade de jogadores. Tente inserir outro número")
    q_jogadores = int(input("Entre quantos jogadores se dará este duelo (2 - 4)? "))

começo = inicio_de_jogo(q_jogadores)
print(começo)

pecinhas = pecas_iniciais.as_pecas(28)
print(pecinhas)
















