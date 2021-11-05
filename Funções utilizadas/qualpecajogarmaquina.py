def peca_a_jogar_maquina(maquina, jogadores, mesa):

    for pecas_maquina in jogadores[maquina]:

        if len(mesa) == 0:

            return pecas_maquina

        else:

            x = mesa[len(mesa) - 1]
            y = mesa[0]

            if pecas_maquina[0] == x[1] or pecas_maquina[1] == y[0] or pecas_maquina[1] == x[1] or pecas_maquina[0] == y[0]:
                
                return pecas_maquina

    return False
            

