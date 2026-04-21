frase ='Todos somos programadores'
frase_t = ''

palabras = frase.split()

for palabra in palabras:
    if palabra.rfind('o'):
        frase_t = frase_t + palabra[:-2] + palabra[-2:].replace('o', 'e') + ' '
    elif palabra.rfind('a'):
        frase_t = frase_t + palabra[:-2] + palabra[-2:].replace('a', 'e') + ' '
    else:
        frase_t = frase_t + palabra
    
print(frase_t)