import inverte_lista
def rodada(pessoa,mesa,dicionario):
    controle=True
    lista_a_jogar=[]
    for jogador,pecas in dicionario.items():
            if jogador==pessoa:
                lista_a_jogar=dicionario[pessoa]
                if len(mesa)==0:
                    mesa.append(lista_a_jogar[0])
                    del dicionario[jogador][0]
                    del lista_a_jogar[0]
                print(jogador)
                i=0
                while controle:
                        peca=lista_a_jogar[i]
                    #primeira peça do domino
                        peca_inicial_mesa=mesa[0]
                        numero_inicial=peca_inicial_mesa[0]
                        #ultima peça do domino
                        peca_final_mesa=mesa[len(mesa)-1]
                        numero_final=peca_final_mesa[1]
                        local_peca_na_lista=lista_a_jogar.index(peca)
                        if numero_final in peca and numero_inicial not in peca:
                            local_peca_jogador=peca.index(numero_final)
                            if local_peca_jogador==0:
                                mesa.append(peca)
                                del dicionario[jogador][local_peca_na_lista]
                                print(jogador)
                                print(f'local mesa igual a 1 e local jogador igual a 0, tem {mesa} e {peca}')
                                            
                            else:
                                peca_inv=inverte_lista.inverte(peca)
                                mesa.append(peca_inv)
                                del dicionario[jogador][local_peca_na_lista]
                                print(jogador)
                                print(f'local mesa igual a 1 e local jogador igual a 1, tem {mesa} e {peca}')     
                            controle=False
                        if numero_inicial in peca and numero_final not in peca:
                            local_peca_jogador=peca.index(numero_inicial)
                            if local_peca_jogador==0:
                                peca_inv=inverte_lista.inverte(peca)
                                mesa=inverte_lista.primeiro_elemento(mesa,peca_inv)
                                del dicionario[jogador][local_peca_na_lista]
                                print(jogador)
                                print(f'local mesa igual a 0 e local jogador igual a 0, tem {mesa} e {peca}')
                                        
                                            
                            else:
                                mesa=inverte_lista.primeiro_elemento(mesa,peca)
                                del dicionario[jogador][local_peca_na_lista]
                                print(jogador)
                                print(f'local mesa igual a 0 e local jogador igual a 1, tem {mesa} e {peca}')

                            controle=False                
                        if numero_inicial in peca and numero_final in peca:
                                mesa.append(peca)
                                del dicionario[jogador][local_peca_na_lista]
                                controle=False
                        i+=1
                        if i==len(lista_a_jogar):
                            controle=False
    return mesa