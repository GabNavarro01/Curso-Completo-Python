cadena = 'Ejemplo con for'

for c in cadena:
    print('caracter:', c)

cuenta = 0
for c in cadena:
    if c == 'o':
        cuenta = cuenta + 1
print(cuenta)
