def soma_de_cada_mao(dicionario):

    dic = dicionario

    for item, valor in dicionario.items():

        total = 0

        for pecas in valor:

            for numero in pecas:

                total += numero

            dic[item] = valor,total 

    return dic

def percorrer_min_dicionario(dicionario):

    lista = []

    for item, valor in dicionario.items():

        total = 0

        if len(valor[0]) != 0:

            for pecas in valor[0]:

                for numero in pecas:

                    total += numero

            lista.append(total)

    l = []

    minimo = min(lista)

    for item, valor in dicionario.items():

        if minimo == valor[1]:

            vencedor = item
            l.append(vencedor)

    if len(l) > 1:

        return ('empate entre jogadores')

    else:

        return ('o vencedor do jogo foi {}'.format(vencedor))