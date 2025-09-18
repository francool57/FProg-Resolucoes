def media_digitos(n):
    soma = 0

    a = n          # Definir a como n para o n continuar como numero inicial
    l = 0          # Contar a lenght do numero 
    while a > 0:   # A funcao len(n) nao e possivel com int
        l += 1
        a //= 10

    while n > 0:
        last_digit = n % 10

        soma += last_digit
        n //= 10

    return soma/l

