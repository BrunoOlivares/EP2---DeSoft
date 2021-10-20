import random

def as_pecas(x):
    
    pecas = []

    i1 = 0
    i2 = 0
    i3 = 0
    
    while i3 < x:
        
        if [i1, i2] in pecas or i2 > 6:
            i1 += 1
            i2 = 0

        else:

            if [i2, i1] in pecas:
                i2 += 1

            else:    
                pecas.append([i1, i2])
                i2 += 1
                i3 += 1

    random.shuffle(pecas)    
    
    return (pecas)

print(as_pecas(28))
