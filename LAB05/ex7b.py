def valor(q, j, n):
    if not 0 < j < 1 or q < 0 or n < 0:
        raise ValueError('Value is wrong')
    
    return(q*(1+j)**n)

def duplicar(q, j):
    i = 0
    while True:
        if valor(q, j, i) >= 2*q:
            return i
        i += 1
    
print(duplicar(100, 0.03)) #24
