def num_para_seq_cod(n):
    pares = [0, 2, 4, 6, 8]
    impares = [1, 3, 5, 7, 9]
    tup = tuple()

    while n > 0:
        ld = n % 10
        if ld % 2 == 0:
            a = pares[pares.index(ld)+1] if ld != 8 else 0
        else:
            a = impares[impares.index(ld)-1] if ld != 1 else 9
        tup += (a,)
        n //= 10

    return tup[::-1]
