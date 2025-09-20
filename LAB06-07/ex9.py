def reconhece(chars):
    letras = ['A', 'B', 'C', 'D']
    num = ['1', '2', '3', '4']

    numeros = False
    for i in chars:
        if i not in num or i not in letras:
            return False

        if not numeros and i in letras:
            pass
        elif not numeros and i in num:
            numeros = True
        elif numeros and i in letras:
            return False

    return True

