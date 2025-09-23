def codifica(chars):
    left = ''
    right = ''

    for i,j in enumerate(chars):
        if i % 2 == 1:
            right += j
        else:
            left += j

    return left+right
