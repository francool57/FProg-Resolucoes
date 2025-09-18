# inserir exs 2,3,4

def algarismos_pares(n):
    to_tup = explode(n)
    pares = filtrar_pares(to_tup)
    return implode(pares)
