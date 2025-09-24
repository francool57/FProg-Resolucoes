def apaga1(tup, n):
    res = ()
    for i in tup:
        if i != n:
            res = res + (i,)
        else:
            n = -1

    return res
