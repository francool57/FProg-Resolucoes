def escreve_matriz(ls):
    for i in ls:
        for k in i:
            print(k, end= ' '*(4-len(str(k))))
        print('')

def soma_mat(m1, m2):
    if len(m1) != len(m2):
        raise ValueError('Soma impossivel')
    
    res = []
    for l1, l2 in zip(m1, m2):
        lsoma = []
        for i, j in zip(l1, l2):
            lsoma.append(i+j)

        res.append(lsoma)
            
    return(res)
