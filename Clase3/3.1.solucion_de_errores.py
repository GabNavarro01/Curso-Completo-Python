def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False