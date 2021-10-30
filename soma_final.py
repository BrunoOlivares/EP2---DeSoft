def soma_de_cada_mao(dicionario):
    dic=dicionario
    for item,valor in dicionario.items():
        total=0
        for pecas in valor:
            for numero in pecas:
                total += numero
            dic[item]=valor,total 
    return dic
def percorrer_max_dicionario(dicionario):
    lista=[]
    for item,valor in dicionario.items():
        total=0
        if len(valor) !=0 :
            for pecas in valor:
                for numero in pecas:
                    total += numero
                lista.append(total)
    l=[]
    maximo=max(lista)
    for item,valor in dicionario.items():
        if maximo in valor:
            vencedor=item
            l.append(vencedor)
    if len(l)>1:
        return ('empate entre os jogadores')
    else:
        return ('o vencedor do jogo foi {}'.format(vencedor))