def peca_a_jogar_pessoa(pessoa, jogadores, mesa):
    
    for peças in jogadores[pessoa]:

        if len(mesa) == 0:
            return True
        
        else:

            x = mesa[len(mesa) - 1]
            y = mesa[0]
            
            if peças[0] == x[1] or peças[1] == y[0] or peças[1] == x[1] or peças[0] == y[0]:
                return True
            
    return False
            



