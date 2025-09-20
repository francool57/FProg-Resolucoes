def amigas(word1, word2):
    word1, word2 = tuple(word1), tuple(word2)
    if len(word1) != len(word2):
        return False

    iguais = 0
    for i,j in zip(word1, word2):
        if i == j:
            iguais += 1
    
    return (iguais/len(word1))*100 > 90
    
