def codifica(chars):
    left = ''
    right = ''

    for i,j in enumerate(chars):
        if i % 2 == 1:
            right += j
        else:
            left += j

    return left+right

def descodifica(cod):
    left = cod[0:len(cod)//2]
    right = cod[len(cod)//2:]
    res = ''
    
    if len(left) == len(right):
        for n,m in zip(left,right):
            res += n + m
    else:
        for n,m in zip(left, right[1:]):
            res += n + m
        res += right[0]

    return res
