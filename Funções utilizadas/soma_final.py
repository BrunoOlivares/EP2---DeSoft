def soma_de_cada_mao(dicionario):

    dic = dicionario

    for item, valor in dicionario.items():

        total = 0

        for pecas in valor:

            for numero in pecas:

                total += numero

            dic[item] = valor,total 

    return dic
def vencedor(di):
    min=3000000
    l=[]
    contador=0
    vencedor=''
    for item in di:
        valor=di[item][1]
        l.append(valor)
        if valor<min:
            min=valor
            vencedor=item
    for v in l:
        if v==min:
            contador+=1
    if contador>1:
        return ('Empate entre os jogadores')
    else:
        return ('o vencedor do jogo foi {} com a soma de suas peças sendo em torno de {} pontos'.format(vencedor,min))

