def inverte(lista):
    lista_invertida=[]
    for i in range(len(lista)-1,-1,-1):
        lista_invertida.append(lista[i])
    return lista_invertida

def primeiro_elemento(lista,qtd):
    lista_nova=[qtd]
    for i in range(0,len(lista)):
        lista_nova.append(lista[i])
    return lista_nova
