print(f'{"":>4}', end="")

# Encabezado superior
for i in range(10):
    print(f'{i:>4}', end="")
print()

print("-" * 44)

# Cuerpo de la tabla
for base in range(10):
    print(f'{base:>2} :', end="")

    resultado = 0
    for i in range(10):
        print(f'{resultado:>4}', end="")
        resultado += base   # solo suma

    print()