# EJERCICIO 1
# Calculadora de funciones trigonométricas por series

import math


# Esta función calcula el seno de x utilizando la serie dada
def calcular_seno(x, n_terminos):
    resultado = 0

    # La serie comienza en n = 0 y se calculan n_terminos
    for n in range(n_terminos):

        termino = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)

        # Se suma cada término al resultado anterior
        resultado = resultado + termino

    return resultado


# Esta función calcula el coseno de x utilizando la serie dada
def calcular_coseno(x, n_terminos):
    resultado = 0

    # La serie comienza en n = 0 y se calculan n_terminos
    for n in range(n_terminos):

        termino = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)

        # Se suma cada término al resultado anterior
        resultado = resultado + termino

    return resultado


# Se coloca un valor inicial diferente de 4
# para poder entrar al ciclo while
opcion = 0


# El menú se repetirá mientras el usuario no seleccione 4
while opcion != 4:

    print("\nCALCULADORA TRIGONOMETRICA")
    print("1. Seno")
    print("2. Coseno")
    print("3. Tangente")
    print("4. Salir")

    opcion = int(input("Seleccione una opcion: "))


    # OPCIÓN 1: SENO
    if opcion == 1:

        grados = float(input("Ingrese el valor de x en grados: "))
        n_terminos = int(input("Ingrese el numero de terminos de la serie: "))

        # Convertimos los grados a radianes antes de evaluar la serie
        x = grados * math.pi / 180

        seno = calcular_seno(x, n_terminos)

        print("El seno aproximado es:", seno)


    # OPCIÓN 2: COSENO
    elif opcion == 2:

        grados = float(input("Ingrese el valor de x en grados: "))
        n_terminos = int(input("Ingrese el numero de terminos de la serie: "))

        # Convertimos los grados a radianes
        x = grados * math.pi / 180

        coseno = calcular_coseno(x, n_terminos)

        print("El coseno aproximado es:", coseno)


    # OPCIÓN 3: TANGENTE
    elif opcion == 3:

        print("Con esta opcion se podria calcular la tangente,")
        print("pero aun no ha sido implementada.")


    # OPCIÓN 4: SALIR
    elif opcion == 4:

        print("Saliendo del programa...")


    # Si el usuario introduce una opción diferente de 1, 2, 3 o 4
    else:

        print("Opcion invalida. Intente nuevamente.")


print("Programa terminado.")
