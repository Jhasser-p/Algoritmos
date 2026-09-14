# Ejercicio 2: Conversión de un número entero positivo a otra base (2 <= b < 10)

def pedir_entero_positivo(mensaje):
    """
    Define una funcion que valida que lo
    ingresado sea realmente un número entero y que sea mayor que 0.
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
    Se define otra funcion base b, esta valida que sea un entero en el
    rango 2 <= b < 10.
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
    Funcion que convierte el número entero positivo n a su representación en
    base b, usando el método de divisiones sucesivas.
    """
    if n == 0:
        return "0"

    digitos = []
    while n > 0:
        resto = n % b          # dígito menos significativo actual
        digitos.append(str(resto))
        n = n // b              # se continúa con el cociente
    digitos.reverse()
    return "".join(digitos)


def main():
    """
    Función que recopila todo: pide n y b, calcula la
    representación de n en base b
    """
    n = pedir_entero_positivo("Ingrese un número entero positivo n: ")
    b = pedir_base()

    representacion = convertir_a_base(n, b)
    print(f"El número {n} en base {b} se representa como: {representacion}")


if __name__ == "__main__":
    main()