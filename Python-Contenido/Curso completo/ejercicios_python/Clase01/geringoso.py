cadena = 'Geringoso'
capadepenapa = ''

for c in cadena:
    if c == 'a' or c == 'A':
        capadepenapa = capadepenapa + 'apa'
    elif c == 'e' or c == 'E':
        capadepenapa = capadepenapa + 'epe'
    elif c == 'i' or c == 'I':
        capadepenapa = capadepenapa + 'ipi'
    elif c == 'o' or c == 'O':
        capadepenapa = capadepenapa + 'opo'
    elif c == 'u' or c == 'U':
        capadepenapa = capadepenapa + 'upu'
    else:
        capadepenapa = capadepenapa + c

print(capadepenapa)

#%% Código de clase

# La versión de código anterior es larga y puede ser reemplazada por:

cadena = 'Geringoso'
capadepenapa = ''

for c in cadena:
    capadepenapa += c
    if c in 'aeiouáéíóú':
        capadepenapa += 'p' + c
    elif c in 'AEIOUÁÉÍÓÚ':
        capadepenapa += 'P' + c

print(capadepenapa)
