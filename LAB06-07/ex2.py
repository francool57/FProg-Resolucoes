def explode(n1):
    if not isinstance(n1, int):
        raise ValueError
    
    digits = []
    while n1 > 0:
        digits.insert(0, n1 % 10)
        n1 //= 10
  
    return tuple(digits)
