def soma_cumulativa(ls):
    if not isinstance(ls, list):
        raise ValueError
    
    res = []
    last = 0
    for i in ls:
        res.append(i + last)
        last += i
    return res

