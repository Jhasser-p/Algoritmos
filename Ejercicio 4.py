"""
Intercalado de ceros entre las cifras de un número.

El programa lee un entero positivo y construye un nuevo número que
tiene las mismas cifras, pero con un "0" intercalado entre cada
cifra consecutiva.

Ejemplo: 4567 -> 4050607
(entre el 4 y el 5 se agrega un 0, entre el 5 y el 6 se agrega un 0,
y entre el 6 y el 7 se agrega un 0).
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


def intercalar_ceros(n):
    """
    Recibe un entero positivo n y devuelve un nuevo entero que resulta
    de intercalar un "0" entre cada cifra de n.

    Estrategia:
    - Se extraen las cifras de n una por una usando el resto (%) y la
      división entera (//) por 10, igual que en el ejercicio de bases,
      obteniendo primero la cifra menos significativa.
    - Cada cifra extraída se agrega a una lista, junto con un "0"
      después de ella (salvo la última cifra procesada, que en
      realidad es la primera del número original, para no dejar un
      0 sobrando al final).
    - Como las cifras se extraen en orden inverso, al final se
      invierte la lista de caracteres para reconstruir el número
      con el orden correcto.
    """
    cifras = []
    while n > 0:
        cifra = n % 10       # cifra menos significativa actual
        cifras.append(str(cifra))
        n = n // 10

    # 'cifras' quedó en orden inverso (de la última cifra a la primera).
    # Se arma el resultado insertando un "0" entre cifras consecutivas.
    resultado = []
    for i in range(len(cifras)):
        resultado.append(cifras[i])
        if i != len(cifras) - 1:   # no agregar 0 después de la última agregada
            resultado.append("0")

    # Se invierte para obtener el orden correcto del número original.
    resultado.reverse()
    return "".join(resultado)


def main():
    """
    Función principal: pide el número al usuario, calcula el número
    resultante con los ceros intercalados y lo muestra en pantalla.
    """
    n = pedir_entero_positivo("Ingrese un número entero positivo: ")
    resultado = intercalar_ceros(n)
    print(f"El número {n} con ceros intercalados es: {resultado}")


if __name__ == "__main__":
    main()