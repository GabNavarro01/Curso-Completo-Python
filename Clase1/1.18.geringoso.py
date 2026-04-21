cadena = "Geringoso"
capadepenapa = ''

for c in cadena:
    if c in ['a','e','i','o','u']:
        capadepenapa = capadepenapa + c + 'p' + c
    else:
        capadepenapa = capadepenapa + c
    
print(capadepenapa)