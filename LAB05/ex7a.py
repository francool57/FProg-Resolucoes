def valor(q, j, n):
    if not 0 < j < 1 or q < 0 or n < 0:
        raise ValueError('Value is wrong')
    
    return(q*(1+j)**n)

print(valor(100, 0.03, 4))
