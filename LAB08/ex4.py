def elemento_matriz(ls, l, c):
    if not isinstance(l, int) or not isinstance(c, int) or not isinstance(ls, list):
        raise ValueError('Argumentos errados')
    
    if len(ls)-1 < l: 
        raise ValueError(f'indice invalido, linha {l}')
    
    for i in ls:
        if ls[l] == i:
            if len(ls[l])-1 < c:
                raise ValueError(f'indice invalido, coluna {c}')
            return ls[l][c]
