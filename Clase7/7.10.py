def valor_absoluto(n):
    """
    Calcula el valor absoluto de un número entero.

    Contrato:
    - Entrada: n (int)
    - Salida: int
    - Devuelve |n|, es decir, el número sin signo.

    """
    
    # Si n es positivo o cero, su valor absoluto es el mismo número
    if n >= 0:
        return n
    else:
        # Si n es negativo, el valor absoluto es su opuesto
        return -n


def suma_pares(l):
    """
    Suma todos los números pares de una lista.

    Contrato:
    - Entrada: l (list[int]) lista de números enteros
    - Salida: int
    - Devuelve la suma de todos los elementos pares de la lista.

    """

    res = 0

    for e in l:
        # Si el número es par se suma al resultado
        if e % 2 == 0:
            res += e
        else:
            # Si no es par no afecta la suma
            res += 0

    return res

    # Invariante de ciclo:
    # En cada iteración, res es la suma de todos los números pares
    # procesados hasta el momento en la lista.


def veces(a, b):
    """
    Multiplica dos números usando sumas repetidas.

    Contrato:
    - Entrada: a (int), b (int >= 0)
    - Salida: int
    - Devuelve a * b.
    """

    res = 0
    nb = b

    while nb != 0:
        # En cada paso sumamos 'a' una vez
        # print(nb * a + res)  # línea usada para observar el proceso
        res += a
        nb -= 1

    return res

    # Invariante de ciclo:
    # res + nb * a = a * b
    # res representa la suma acumulada de 'a' las veces ya procesadas.


def collatz(n):
    """
    Calcula la cantidad de pasos de la secuencia de Collatz
    hasta llegar a 1.

    Contrato:
    - Entrada: n (int, n > 0)
    - Salida: int
    - Devuelve la cantidad de valores en la secuencia de Collatz
      comenzando en n hasta llegar a 1 (incluyendo el 1).

    Reglas de Collatz:
    - Si n es par: n = n / 2
    - Si n es impar: n = 3n + 1
    """

    res = 1

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1

        # Se cuenta cada transformación realizada
        res += 1

    return res

    # Invariante de ciclo:
    # res cuenta la cantidad de pasos aplicados a la secuencia
    # desde el valor inicial hasta el valor actual de n.