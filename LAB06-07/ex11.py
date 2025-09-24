def posicoes_maximo(tup):
    maxi = 0

    for j,i in enumerate(tup):
        if i > maxi:
            pos = (j,)
            maxi = i
        elif i == maxi:
            pos += (j,)

    return pos
