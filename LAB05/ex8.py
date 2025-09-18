def serie_geom(r, n):
    if n < 0: 
        raise ValueError

    res = 0
    for i in range(n+1):
        res += r**i
    return res

print(serie_geom(2, 4)) #31
