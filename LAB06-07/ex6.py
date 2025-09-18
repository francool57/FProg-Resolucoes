def num_para_seq_cod(n):
    cod = {0:2, 2:4, 4:6, 6:8, 8:0, 1:9, 3:1, 5:3, 7:5, 9:7}
    tup = tuple()
    
    while n > 0:
        tup = (cod[n % 10],) + tup
        n //= 10
    return tup
