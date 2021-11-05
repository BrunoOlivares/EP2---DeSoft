from coreshumano import cores_mãohumana
from qualpecajogarmaquina import peca_a_jogar_maquina
from qualpecajogarpessoa import peca_a_jogar_pessoa
from coreshumano import cores_mãohumana
from cores_mesa import cores_mesa
import time

def meiota(ordem, jogadores, mesa, pecinhas):

    continuar = True

    empate = 0

    while continuar:

        for jogador in ordem:
                        
            if jogador == "jogador 1":

                pessoa = peca_a_jogar_pessoa('jogador 1', jogadores, mesa)

                #pegar do monte

                while len(pecinhas) != 0 and pessoa == False:
                    print('monte')
                    print(pecinhas[0])

                    jogadores['jogador 1'].append(pecinhas[0])
                    del pecinhas[0]
                    pessoa = peca_a_jogar_pessoa('jogador 1', jogadores, mesa)

                if pessoa == True:

                    empate = 0
                    pecas_disponiveis=peca_a_jogar(jogadores[jogador],mesa)   
                    print("Sua mão é essa:")
                    cores_mãohumana(jogadores['jogador 1'])
                    if len(mesa) != 0:
                        print("As pecas disponiveis a jogar estão nas posições: {}".format(','.join(pecas_disponiveis)))
                    else:
                        print(pecas_disponiveis)
                    escolher = int(input("Qual peça escolher? "))

                    while escolher < 0 or escolher > len(jogadores['jogador 1']):

                        print("Você não tem esse tanto de peças, tente mais uma vez")
                        escolher = int(input("Qual peça escolher?"))                        
                        
                    peca_pessoa = jogadores['jogador 1'][(escolher - 1)]
                                
                    if len(mesa) == 0:

                        mesa.append(peca_pessoa)
                        peca_del = jogadores['jogador 1'].index(peca_pessoa)
                        del jogadores['jogador 1'][peca_del]                    

                    else:

                        while peca_pessoa[0] != mesa[len(mesa) - 1][1] and peca_pessoa[1] != mesa[0][0] and peca_pessoa[1] != mesa[len(mesa) - 1][1] and peca_pessoa[0] != mesa[0][0]:
                            pecas_disponiveis=peca_a_jogar(jogadores['jogador 1'],mesa)
                            print("Essa peça não se encaixa")
                            escolher = int(input("Qual peça escolher? "))
                            peca_pessoa = jogadores['jogador 1'][escolher - 1]
                                        
                        if peca_pessoa[0] == mesa[len(mesa) - 1][1]:

                            mesa.append(peca_pessoa)
                            peca_del = jogadores['jogador 1'].index(peca_pessoa)
                            del jogadores['jogador 1'][peca_del]

                        elif peca_pessoa[1] == mesa[0][0]:

                            mesa.insert(0, peca_pessoa)
                            peca_del = jogadores['jogador 1'].index(peca_pessoa)
                            del jogadores['jogador 1'][peca_del]
                                        
                        elif peca_pessoa[1] == mesa[len(mesa) - 1][1]:

                            pecainvertida = list(reversed(peca_pessoa))
                            mesa.append(pecainvertida)
                            peca_del = jogadores['jogador 1'].index(peca_pessoa)
                            del jogadores['jogador 1'][peca_del]
                                        
                        elif peca_pessoa[0] == mesa[0][0]:

                            pecainvertida = list(reversed(peca_pessoa))
                            mesa.insert(0, pecainvertida)
                            peca_del = jogadores['jogador 1'].index(peca_pessoa)
                            del jogadores['jogador 1'][peca_del]
                else:
                     
                    empate += 1

                print("MESA: ")
                cores_mesa(mesa)
                time.sleep(2)
                    
                                
            else:

                maquina = peca_a_jogar_maquina(jogador, jogadores, mesa)

                if len(mesa) == 0:

                    mesa.append(maquina)
                    peca_del = jogadores[jogador].index(maquina)
                    del jogadores[jogador][peca_del]

                else:

                    while len(pecinhas) != 0 and maquina == False:

                        (jogadores[jogador]).append(pecinhas[0])
                        del pecinhas[0]
                        maquina = peca_a_jogar_maquina(jogador, jogadores, mesa)
                                
                    if maquina != False:

                        empate = 0

                        if maquina[0] == mesa[len(mesa) - 1][1]:

                            mesa.append(maquina)
                            peca_del = jogadores[jogador].index(maquina)
                            del jogadores[jogador][peca_del]

                        elif maquina[1] == mesa[0][0]:

                            mesa.insert(0, maquina)
                            peca_del = jogadores[jogador].index(maquina)
                            del jogadores[jogador][peca_del]
                                            
                        elif maquina[1] == mesa[len(mesa) - 1][1]:

                            pecainvertida = list(reversed(maquina))
                            mesa.append(pecainvertida)
                            peca_del = jogadores[jogador].index(maquina)                            
                            del jogadores[jogador][peca_del]
                                            
                        elif maquina[0] == mesa[0][0]:

                            pecainvertida = list(reversed(maquina))
                            mesa.insert(0, pecainvertida)
                            peca_del = jogadores[jogador].index(maquina)                           
                            del jogadores[jogador][peca_del]
                    else:

                        empate += 1

                print("MESA: ")
                cores_mesa(mesa)
                time.sleep(2)    

            if len(jogadores[jogador]) == 0:
                if jogador=='jogador 1':
                    finalizacao=('Voce venceu o jogo, Parabens!')
                else:
                    finalizacao = ("O {} venceu o jogo".format(jogador))
                return finalizacao

            if empate == len(ordem):

                texto = ('O jogo foi travado')
                return texto

def peca_a_jogar(mao,mesa):
    
    if len(mesa) != 0:
        locais_a_jogar=[]
        numero_final=mesa[len(mesa)-1][1]
        numero_inicial=mesa[0][0]
        for peca in mao:
            x=mao.index(peca)
            if (peca[1]==numero_final or peca[1]==numero_inicial) and (peca[0]!=numero_inicial and peca[0]!=numero_final):
                locais_a_jogar.append(x+1)
            if (peca[0]==numero_inicial or peca[0]==numero_final) and (peca[1]!=numero_final and peca[1]!=numero_inicial) :
                locais_a_jogar.append(x+1)
            elif (peca[1]==numero_final or peca[1]==numero_inicial) and (peca[0]==numero_inicial or peca[0]==numero_final):
                locais_a_jogar.append(x+1)
        locais=[str(i) for i in locais_a_jogar]
        return locais
    else:
        return 'Escolha a peça a começar!'

