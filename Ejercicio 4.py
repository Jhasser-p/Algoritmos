#Ejercicio 4: Intercalar ceros entre las cifras de un número entero positivo

def pedir_entero_positivo(mensaje):
    """
    Pide el número entero positivo, valida que sea realmente un número entero 
    y que sea mayor que 0.
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
    """
    cifras = []
    while n > 0:
        cifra = n % 10       # cifra menos significativa actual
        cifras.append(str(cifra))
        n = n // 10
    resultado = []
    for i in range(len(cifras)):
        resultado.append(cifras[i])
        if i != len(cifras) - 1:   
            resultado.append("0")

    # Se invierte para obtener el orden correcto del número original.
    resultado.reverse()
    return "".join(resultado)


def main():
    """
    Función principal: pide el número, calcula el número
    resultante con los ceros intercalados.
    """
    n = pedir_entero_positivo("Ingrese un número entero positivo: ")
    resultado = intercalar_ceros(n)
    print(f"El número {n} con ceros intercalados es: {resultado}")


if __name__ == "__main__":
    main()