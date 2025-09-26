def remove_multiplos(ls, n):
    if not isinstance(ls, list) or not isinstance(n, int):
        raise ValueError(':33')
    
    res = []
    for i in ls:
        if i % n != 0:
            res.append(i)
    
    return res
