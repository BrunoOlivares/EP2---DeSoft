from qualpecajogarmaquina import peca_a_jogar_maquina
from qualpecajogarpessoa import peca_a_jogar_pessoa

def meiota(ordem, jogadores, mesa, pecinhas):

    continuar = True

    empate = 0

    while continuar:

        for jogador in ordem:
                        
            if jogador == "jogador 1":

                pessoa = peca_a_jogar_pessoa('jogador 1', jogadores, mesa)

                while len(pecinhas) != 0 and pessoa == False:
                    print('monte')
                    print(pecinhas[0])

                    jogadores['jogador 1'].append(pecinhas[0])
                    del pecinhas[0]
                    pessoa = peca_a_jogar_pessoa('jogador 1', jogadores, mesa)

                if pessoa == True:

                    empate = 0
                                
                    print("Sua mão é essa:")
                    print(jogadores['jogador 1'])
                    escolher = int(input("Qual peça escolher? "))

                    while escolher < 0 or escolher > len(jogadores['jogador 1']):

                        escolher = int(input("Qual peça escolher"))                        
                        
                    peca_pessoa = jogadores['jogador 1'][(escolher - 1)]
                                
                    if len(mesa) == 0:

                        mesa.append(peca_pessoa)
                        peca_del = jogadores['jogador 1'].index(peca_pessoa)
                        del jogadores['jogador 1'][peca_del]                    

                    else:

                        while peca_pessoa[0] != mesa[len(mesa) - 1][1] and peca_pessoa[1] != mesa[0][0] and peca_pessoa[1] != mesa[len(mesa) - 1][1] and peca_pessoa[0] != mesa[0][0]:

                            print ("A peça está disponível, mas não é essa, tente escolher outra")
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
                            
                print(mesa)
                    
                                
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

                print(mesa)    

            if len(jogadores[jogador]) == 0:

                finalizacao = ("O {} venceu o jogo".format(jogador))
                return finalizacao

            if empate == len(ordem):

                texto = ('O jogo foi travado')
                return texto