def media_digitos(n):
    soma = 0
    i = 0

    while n > 0:
        last_digit = n % 10

        soma += last_digit
        n //= 10
        i += 1

    return soma/i
