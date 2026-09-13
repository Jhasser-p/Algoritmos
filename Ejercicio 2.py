"""
Representación de un número entero positivo n en una base b.

El programa le pide al usuario un entero positivo n y luego una base b,
donde b debe cumplir 2 <= b < 10 (si no cumple, se vuelve a pedir).
Luego calcula y muestra los dígitos de n expresado en esa base b,
usando el método de divisiones sucesivas.
"""


def pedir_entero_positivo(mensaje):
    """
    Pide al usuario un número entero positivo, validando que lo
    ingresado sea realmente un número entero y que sea mayor que 0.
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


def pedir_base():
    """
    Pide al usuario la base b, validando que sea un entero en el
    rango 2 <= b < 10. Repite la pregunta hasta recibir un valor válido.
    """
    while True:
        try:
            b = int(input("Ingrese la base b (2 <= b < 10): "))
            if b < 2 or b >= 10:
                print("La base debe estar en el rango 2 <= b < 10. Intente de nuevo.")
                continue
            return b
        except ValueError:
            print("Valor inválido. Por favor ingrese un número entero.")


def convertir_a_base(n, b):
    """
    Convierte el número entero positivo n a su representación en
    base b, usando el método de divisiones sucesivas:

    - Se divide n entre b, guardando el resto (ese resto es un dígito
      de la representación, empezando por el menos significativo).
    - Se repite el proceso con el cociente obtenido, hasta que el
      cociente sea 0.
    - Los dígitos obtenidos, leídos en orden inverso al que se
      calcularon, forman la representación de n en base b.

    Devuelve la representación como una cadena de texto (string).
    """
    if n == 0:
        return "0"

    digitos = []
    while n > 0:
        resto = n % b          # dígito menos significativo actual
        digitos.append(str(resto))
        n = n // b              # se continúa con el cociente

    # Los dígitos se calcularon del menos al más significativo,
    # por lo que se debe invertir el orden antes de unirlos.
    digitos.reverse()
    return "".join(digitos)


def main():
    """
    Función principal: pide n y b al usuario, calcula la
    representación de n en base b y la muestra en pantalla.
    """
    n = pedir_entero_positivo("Ingrese un número entero positivo n: ")
    b = pedir_base()

    representacion = convertir_a_base(n, b)
    print(f"El número {n} en base {b} se representa como: {representacion}")


if __name__ == "__main__":
    main()