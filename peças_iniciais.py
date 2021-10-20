peças = []

i1 = 0
i2 = 0
i3 = 0

while i3 < 28:
    if (str(i1) + "|" + str(i2)) in peças or i2 > 6:
        i1 += 1
        i2 = 0
    else:
        if (str(i2) + "|" + str(i1)) in peças:
            i2 += 1
        else:    
            peças.append((str(i1) + "|" + str(i2)))
            i2 += 1
            i3 += 1

  

