"""
Cálculo de la desviación estándar (poblacional) de un conjunto de
números ingresados por el usuario.

Este programa muestra DOS formas de calcularla:

  1) calcular_con_lista(): guardando todos los valores en una lista.
  2) calcular_sin_lista(): sin guardar los valores, acumulando solo
     algunos totales a medida que se van leyendo.

Se calcula la desviación estándar POBLACIONAL (se divide entre n).
Ver el análisis de a) y b) al final del archivo, en los comentarios.
"""


def pedir_entero_positivo(mensaje):
    """
    Pide un número entero positivo, validando la entrada.
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


def pedir_flotante(mensaje):
    """
    Pide un número decimal, validando la entrada.
    """
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Valor inválido. Por favor ingrese un número.")


def calcular_con_lista(n):
    """
    Versión CON lista.

    - Se leen los n valores y se guardan todos en una lista.
    - Se calcula la media (promedio) recorriendo la lista.
    - Se recorre la lista una segunda vez para sumar (x_i - media)^2.
    - La desviación estándar poblacional es la raíz cuadrada de esa
      suma dividida entre n.

    Esta versión es directa porque, al tener todos los valores
    guardados, se puede recorrer la lista tantas veces como se
    necesite (una vez para la media, otra para las diferencias).
    """
    datos = []
    for i in range(n):
        x = pedir_flotante(f"Ingrese el valor #{i + 1}: ")
        datos.append(x)

    # Primera pasada: calcular la media
    suma = 0
    for x in datos:
        suma += x
    media = suma / n

    # Segunda pasada: sumar los cuadrados de las diferencias con la media
    suma_diferencias_cuadrado = 0
    for x in datos:
        suma_diferencias_cuadrado += (x - media) ** 2

    varianza = suma_diferencias_cuadrado / n
    desviacion = varianza ** 0.5
    return desviacion


def calcular_sin_lista(n):
    """
    Versión SIN lista (no se guardan los valores en ninguna estructura).

    La dificultad de esta versión es que la fórmula original de la
    desviación estándar necesita primero conocer la media de TODOS
    los valores para luego calcular (x_i - media)^2 de cada uno; pero
    si no se guardan los valores, no se puede volver a recorrerlos
    una segunda vez para hacer esa resta.

    La solución es usar una fórmula algebraicamente equivalente, que
    solo necesita UNA pasada sobre los datos:

        varianza = (suma de x_i^2)/n - media^2

    Esta fórmula se obtiene expandiendo (x_i - media)^2 y usando que
    la suma de (x_i - media) es 0. Así, basta con ir acumulando, a
    medida que se leen los datos, dos totales: la suma de los valores
    y la suma de los valores al cuadrado. No hace falta guardarlos.
    """
    suma = 0
    suma_cuadrados = 0
    for i in range(n):
        x = pedir_flotante(f"Ingrese el valor #{i + 1}: ")
        suma += x
        suma_cuadrados += x ** 2

    media = suma / n
    varianza = (suma_cuadrados / n) - (media ** 2)
    desviacion = varianza ** 0.5
    return desviacion


def main():
    """
    Función principal: pide la cantidad de datos, permite elegir
    qué versión usar y muestra el resultado.
    """
    print("Cálculo de la desviación estándar")
    print("1. Calcular usando una lista")
    print("2. Calcular sin usar una lista")
    opcion = input("Seleccione una opción (1 o 2): ")

    n = pedir_entero_positivo("¿Cuántos datos va a ingresar?: ")

    if opcion == "1":
        resultado = calcular_con_lista(n)
    elif opcion == "2":
        resultado = calcular_sin_lista(n)
    else:
        print("Opción inválida.")
        return

    print(f"La desviación estándar (poblacional) es: {resultado}")


if __name__ == "__main__":
    main()


# ---------------------------------------------------------------------
# a) ¿Poblacional o muestral, y en qué se diferencian?
# ---------------------------------------------------------------------
# Este programa calcula la desviación estándar POBLACIONAL: la
# varianza se obtiene dividiendo la suma de las diferencias al
# cuadrado entre n (la cantidad total de datos).
#
# La desviación estándar MUESTRAL se usa cuando los datos son solo
# una MUESTRA tomada de una población más grande (no todos los
# datos posibles). En ese caso, la varianza se divide entre (n - 1)
# en lugar de n. Esto se conoce como "corrección de Bessel" y hace
# que el resultado sea un poco más grande que el poblacional. Se usa
# porque, al no tener todos los datos de la población, dividir entre
# n tiende a subestimar la variabilidad real; dividir entre (n - 1)
# corrige ese sesgo.
#
# Para obtener la versión muestral en este programa, bastaría con
# cambiar la línea "varianza = suma_diferencias_cuadrado / n" (o su
# equivalente en la versión sin lista) por "... / (n - 1)".
#
# ---------------------------------------------------------------------
# b) Dificultad adicional en la versión sin listas y cómo se resuelve
# ---------------------------------------------------------------------
# La fórmula original de la desviación estándar requiere conocer la
# media ANTES de poder calcular cada diferencia (x_i - media)^2, y
# luego habría que recorrer los datos una SEGUNDA vez para sumar esas
# diferencias. Sin una lista, los valores ya leídos no se pueden
# recuperar para una segunda pasada.
#
# La solución implementada (calcular_sin_lista) usa la fórmula
# algebraica equivalente:
#
#       varianza = (suma de x_i^2)/n - media^2
#
# la cual solo necesita ir acumulando, en una única pasada, la suma
# de los valores y la suma de sus cuadrados. Con esos dos totales
# (y n) alcanza para calcular la varianza y la desviación estándar,
# sin necesidad de guardar ni volver a recorrer los datos originales.