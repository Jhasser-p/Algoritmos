"""
Clasificación de triángulos.

El programa lee las longitudes de los tres lados de un triángulo y:

  1) Verifica que las longitudes sean válidas (mayores que 0).
  2) Verifica que con esas tres longitudes se pueda formar un
     triángulo real, usando la desigualdad triangular (la suma de
     dos lados cualquiera debe ser mayor que el tercero).
  3) Si es un triángulo válido, lo clasifica:
       a) Por sus lados: equilátero, isósceles o escaleno.
       b) Por sus ángulos: rectángulo, acutángulo u obtusángulo,
          comparando el cuadrado del lado mayor con la suma de los
          cuadrados de los otros dos (relación basada en el Teorema
          de Pitágoras).

El proceso se repite pidiendo un nuevo triángulo, hasta que el
usuario ingresa 0 como PRIMERA longitud (valor centinela para salir).
"""


def pedir_lado(mensaje, permitir_centinela=False):
    """
    Pide una longitud de lado y valida que sea un número.

    - Si permitir_centinela es True (solo se usa para el primer lado),
      un valor de 0 es aceptado y se devuelve tal cual, para que
      main() lo use como señal de salida del programa.
    - En cualquier otro caso, se rechazan los valores negativos o
      nulos (0), pidiendo el dato nuevamente.
    """
    while True:
        try:
            valor = float(input(mensaje))
        except ValueError:
            print("Valor inválido. Por favor ingrese un número.")
            continue

        if permitir_centinela and valor == 0:
            return valor  # 0 aceptado únicamente como centinela de salida

        if valor <= 0:
            print("La longitud debe ser mayor que 0. Intente de nuevo.")
            continue

        return valor


def es_triangulo_valido(a, b, c):
    """
    Aplica la desigualdad triangular: para que a, b y c formen un
    triángulo real, la suma de cualquier par de lados debe ser
    estrictamente mayor que el lado restante.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)


def clasificar_por_lados(a, b, c):
    """
    Clasifica el triángulo según sus lados:
      - Equilátero: los tres lados son iguales.
      - Isósceles: exactamente dos lados son iguales.
      - Escaleno: los tres lados son diferentes.
    """
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"


def clasificar_por_angulos(a, b, c):
    """
    Clasifica el triángulo según sus ángulos, comparando el cuadrado
    del lado mayor con la suma de los cuadrados de los otros dos
    (generalización del Teorema de Pitágoras):

      - Si lado_mayor^2 == suma de los otros dos al cuadrado:
            el ángulo opuesto al lado mayor mide 90°  -> Rectángulo
      - Si lado_mayor^2 <  suma de los otros dos al cuadrado:
            ese ángulo es menor a 90° (y por lo tanto los demás
            también) -> Acutángulo
      - Si lado_mayor^2 >  suma de los otros dos al cuadrado:
            ese ángulo es mayor a 90°  -> Obtusángulo

    Se ordenan los lados de menor a mayor para identificar con
    facilidad cuál es el lado mayor.
    """
    lados = sorted([a, b, c])
    menor1, menor2, mayor = lados[0], lados[1], lados[2]

    cuadrado_mayor = mayor ** 2
    suma_cuadrados_menores = menor1 ** 2 + menor2 ** 2

    if cuadrado_mayor == suma_cuadrados_menores:
        return "Rectángulo"
    elif cuadrado_mayor < suma_cuadrados_menores:
        return "Acutángulo"
    else:
        return "Obtusángulo"


def main():
    """
    Función principal: repite el proceso de leer un triángulo,
    validarlo y clasificarlo, hasta que el usuario ingresa 0 como
    primera longitud (valor centinela).
    """
    print("--- Clasificación de triángulos ---")
    print("(Ingrese 0 como primera longitud para salir)\n")

    while True:
        a = pedir_lado("Ingrese la longitud del lado 1: ", permitir_centinela=True)
        if a == 0:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        b = pedir_lado("Ingrese la longitud del lado 2: ")
        c = pedir_lado("Ingrese la longitud del lado 3: ")

        if not es_triangulo_valido(a, b, c):
            print("Esos valores no pueden formar un triángulo (no cumplen la desigualdad triangular).\n")
            continue

        tipo_lados = clasificar_por_lados(a, b, c)
        tipo_angulos = clasificar_por_angulos(a, b, c)

        print(f"El triángulo es {tipo_lados} (por sus lados) y {tipo_angulos} (por sus ángulos).\n")


if __name__ == "__main__":
    main()