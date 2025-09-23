def explode(n1):
    if not isinstance(n1, int):
        raise ValueError
    
    digits = []
    while n1 > 0:
        digits.insert(0, n1 % 10)
        n1 //= 10
  
    return tuple(digits)
    
def explode(n1):
    if not isinstance(n1, int):
        raise ValueError
    
    res = ()
    for i in str(n1):
        i = int(i)
        res += (i,)

    return res
