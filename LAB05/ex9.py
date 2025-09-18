dias = {
    0: 'sabado',
    1: 'domingo', 
    2: 'segunda',
    3: 'terca',
    4: 'quarta',
    5: 'quinta',
    6: 'sexta'
}

def dia_da_semana(dia, mes, ano):
    if mes < 3:       # A congruência de Zeller vai ate ao mes 14
        mes += 12
        ano -= 1
    
    K = ano % 100 # Ultimos 2 digitos
    J = ano // 100 # Primeiros 2 digitos
    
    h = (dia + ((13 * (mes + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7
    
    return dias[h]
