def bissexto(ano):
    if ano % 4 == 0 and not ano % 100 == 0 or ano % 100 == 0 and ano % 400 == 0:
        return True
    else:
        return False
    
def dias_mes(mes, ano):
    if mes in ['abr', 'set', 'nov', 'jun']:
        day = 31
    elif mes == 'fev':
        if bissexto(ano):
            day = 29
        else:
            day = 28
    else: 
        day = 31

    return day
