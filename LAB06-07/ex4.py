def filtrar_pares(tup):
    res = tuple()
    
    for i in tup:
        if not isinstance(i, int):
            raise ValueError
        res += (i,) if (i % 2 == 0) else ()

    return res
