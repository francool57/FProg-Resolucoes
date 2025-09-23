def explode(n1):
    if not isinstance(n1, int):
        raise ValueError
    
    digits = tuple()
    while n1 > 0:
        digits = (n1 % 10,) + digits
        n1 //= 10
  
    return digits
    
def explode(n1):
    if not isinstance(n1, int):
        raise ValueError
    
    res = ()
    for i in str(n1):
        i = int(i)
        res += (i,)

    return res
