
frase = 'Todos, tu también'
frase_t=''

palabras = frase.split()

for palabra in palabras:
        if palabra[-2]=='o':
            frase_t=frase_t+ palabra[:-2] + palabra[-2:].replace('o','e') + ' '
        else:
            frase_t= frase_t + palabra +' '
            
print(frase_t)
