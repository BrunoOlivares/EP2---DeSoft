def aprimeirapeça(ordem, jogadores):

    mesa=[]

    if ordem[0] == "jogador 1":
        print(jogadores["jogador 1"])
        print(mesa)
        x = int(input("Que peça?"))
        
        while x < 1 or x > 7:
            print("Não há essa quantidade de peças na sua mão, tente outro número")
            x = int(input("Que peça?"))

        y = x - 1            
        mesa.append(jogadores["jogador 1"][y])
        del (jogadores["jogador 1"][y])
                
    else:
        lista_a_jogar= []
        lista_a_jogar = jogadores[ordem[0]]
        mesa.append(lista_a_jogar[0])
        del jogadores[ordem[0]][0]
                
    return (mesa)

