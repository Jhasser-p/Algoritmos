# EJERCICIO 9
# Aproximacion de pi usando la serie de Leibniz
# con un criterio de tolerancia.

import math

# Se solicita al usuario la tolerancia epsilon.
epsilon = float(input("Ingrese el valor de la tolerancia: "))

# Variables iniciales.
suma = 0
n = 0
terminos = 0

# Se calcula inicialmente el primer termino de la serie.
termino = 1 / (2 * n + 1)

# El ciclo continua mientras el valor absoluto
# del termino sea mayor o igual que la tolerancia.
while abs(termino) >= epsilon:

    # Termino general de la serie de Leibniz:
    # (-1)^n / (2n + 1)
    termino = ((-1) ** n) / (2 * n + 1)

    # Se agrega el termino a la suma.
    suma = suma + termino

    # Se cuenta el termino utilizado.
    terminos = terminos + 1

    # Se pasa al siguiente valor de n.
    n = n + 1

# Como la serie calcula pi/4, multiplicamos la suma por 4.
pi_aproximado = 4 * suma

# Se calcula el error respecto al valor real de pi.
error = abs(math.pi - pi_aproximado)

# Se muestran los resultados.
print("\nRESULTADOS")
print("Aproximacion de pi:", pi_aproximado)
print("Numero de terminos utilizados:", terminos)
print("Valor de math.pi:", math.pi)
print("Error respecto a math.pi:", error)
