def area_circulo(r):
    return 3.14*(r**2)

def area_coroa(r1, r2):
    if r1 > r2:
        raise ValueError # Enuncia um erro e o programa acaba
    
    return area_circulo(r2)-area_circulo(r1)
    
