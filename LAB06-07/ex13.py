def permutacao(tup1, tup2):
    if len(tup1) != len(tup2):
        return False
    
    for i in tup1:
        if i not in tup2:
            return False
    
    return True
