def cores_mesa(pecas):

    dicionario_de_cores = {

    0: ('\033[37m' + '0'),
    1: ('\033[31m' + '1'),
    2: ('\033[32m' + '2'),
    3: ('\033[34m' + '3'),
    4: ('\033[36m' + '4'),
    5: ('\033[33m' + '5'),
    6: ('\033[35m' + '6'),

    }

    for peca in pecas:
        if peca == pecas[len(pecas) - 1]:
             print('\033[37m' + "[" + dicionario_de_cores[peca[0]] + '\033[37m' + "|" + dicionario_de_cores[peca[1]] + '\033[37m' + "]")
        else:
            print(('\033[37m' + "[" + dicionario_de_cores[peca[0]] + '\033[37m' + "|" + dicionario_de_cores[peca[1]] + '\033[37m' + "]"), end="")


