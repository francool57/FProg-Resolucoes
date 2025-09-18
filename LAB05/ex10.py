def inverter_num(n):
    inv = 0
    while n > 0:
        last_digit = n % 10
        inv = inv * 10 + last_digit
        n //= 10
    
    return inv

def misterio(n):
    a = n          # Definir a como n para o n continuar como numero inicial
    l = 0          # Contar a lenght do numero 
    while a > 0:   # A funcao len(n) nao e possivel com int
        l += 1
        a //= 10

    if l != 3 or abs(n//100 - n%10) < 1:
        raise ValueError('Condições não verificadas')
    
    n_inv = inverter_num(n)
    ns = abs(n - n_inv)
    ns_inv = inverter_num(ns)

    return ns + ns_inv



    
    
