frase = 'Todos, tu también'
palabras = frase.split()
print(palabras)
frase_t = []
for palabra in palabras:
    if palabra[-1] == 'o':
        palabra = palabra[:-1] + 'e'
    if len(palabra) > 1 and palabra[-2] == 'o' :
        palabra = palabra[:-2] + 'es'
    frase_t.append(palabra)

frase_e = ' '.join(frase_t)
print(frase_e)

# 'todes somes programadores'