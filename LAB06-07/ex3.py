def implode(tup): # Com o for
    res = 0
    for i in tup:
        if not isinstance(i, int):
            raise ValueError
        res = res * 10 + i
    return res

def implode(tup): # Com o while
    res = 0
    i = 0
    while i < len(tup):
        if not isinstance(tup[i], int):
            raise ValueError
        res = res * 10 + tup[i]
        i += 1
    return res
