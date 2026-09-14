"""
Números primos menores o iguales que n.

El programa lee un entero positivo n y muestra todos los números
primos menores o iguales que n, determinando la primalidad "por
tanteo" (probando divisores uno por uno), sin usar ninguna
biblioteca externa (ni siquiera math). Solo se usan estructuras de
decisión (if) y de repetición (while/for).

Al terminar, se informa cuántos primos se encontraron y cuál es el
mayor de ellos.

Optimización aplicada: al buscar divisores de un número k, la
búsqueda se detiene cuando el divisor supera la raíz cuadrada de k
(sin calcular la raíz con ninguna función; ver justificación en
es_primo()).
"""


def pedir_entero_positivo(mensaje):
    """
    Pide un número entero positivo, validando la entrada.
    Repite la pregunta hasta recibir un valor válido.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("El valor debe ser un entero positivo (mayor que 0).")
                continue
            return valor
        except ValueError:
            print("Valor inválido. Por favor ingrese un número entero.")


def es_primo(k):
    """
    Determina si k es primo probando divisores por tanteo, desde 2
    en adelante.

    Optimización (detenerse en la raíz cuadrada de k):
    Si k = d1 * d2 con d1 <= d2 (una descomposición cualquiera de k
    en dos factores), entonces necesariamente d1 <= raíz(k) <= d2.
    Esto es así porque si ambos factores fueran mayores que raíz(k),
    su producto sería mayor que k, y si ambos fueran menores, su
    producto sería menor que k.

    Por lo tanto, si k tiene algún divisor, SIEMPRE existe uno menor
    o igual a raíz(k) (el más pequeño de cada pareja de factores).
    Esto significa que, si se recorren los posibles divisores desde
    2 hasta raíz(k) y no se encuentra ninguno, entonces k no tiene
    divisores propios en ningún rango y es primo: no hace falta
    seguir probando divisores más grandes, porque cualquier divisor
    mayor que raíz(k) tendría obligatoriamente una pareja (el
    cociente k // divisor) menor que raíz(k), que ya habría sido
    detectada.

    Para no calcular la raíz cuadrada con ninguna función, se evita
    despejarla y en su lugar se compara divisor * divisor con k, lo
    cual es equivalente a comparar divisor con raíz(k), pero usando
    solo multiplicación.
    """
    if k < 2:
        return False  # 0 y 1 no son primos

    divisor = 2
    while divisor * divisor <= k:
        if k % divisor == 0:
            return False  # se encontró un divisor propio: no es primo
        divisor += 1

    return True  # no se encontró ningún divisor hasta raíz(k): es primo


def main():
    """
    Función principal: pide n, recorre todos los números de 2 a n
    verificando cuáles son primos, los muestra, y al final informa
    cuántos se encontraron y cuál es el mayor.
    """
    n = pedir_entero_positivo("Ingrese un número entero positivo n: ")

    cantidad_primos = 0
    mayor_primo = None  # todavía no se ha encontrado ningún primo

    print(f"\nNúmeros primos menores o iguales que {n}:")
    for numero in range(2, n + 1):
        if es_primo(numero):
            print(numero, end=" ")
            cantidad_primos += 1
            mayor_primo = numero  # como se recorre en orden creciente,
                                   # el último primo encontrado es el mayor

    print()  # salto de línea después de la lista de primos

    if cantidad_primos == 0:
        print(f"No hay números primos menores o iguales que {n}.")
    else:
        print(f"Se encontraron {cantidad_primos} números primos.")
        print(f"El mayor de ellos es: {mayor_primo}")


if __name__ == "__main__":
    main()