# EJERCICIO 5
# Media de los valores pares

# ---------------------------------------------------
# PRIMERA FORMA: USANDO LISTAS
# ---------------------------------------------------

print("MEDIA DE NUMEROS PARES - USANDO LISTAS")

# Esta lista almacenara los numeros ingresados
numeros = []

# Se utiliza 0 como valor centinela.
# Cuando el usuario ingrese 0, terminara la lectura de datos.
numero = int(input("Ingrese un numero entero (0 para terminar): "))

while numero != 0:

    # Se agrega el numero ingresado a la lista
    numeros.append(numero)

    # Se solicita el siguiente numero
    numero = int(input("Ingrese otro numero entero (0 para terminar): "))


# Lista donde se guardaran solamente los numeros pares
pares = []

# Se recorren todos los numeros ingresados
for numero in numeros:

    # Un numero es par si el residuo de dividirlo entre 2 es cero
    if numero % 2 == 0:
        pares.append(numero)


# Se verifica que exista al menos un numero par
if len(pares) > 0:

    suma = 0

    # Se suman todos los numeros pares
    for numero in pares:
        suma = suma + numero

    # Se calcula la media
    media = suma / len(pares)

    print("Los numeros pares son:", pares)
    print("La media de los numeros pares es:", media)

else:
    print("No se ingreso ningun numero par.")


# ---------------------------------------------------
# SEGUNDA FORMA: SIN USAR LISTAS
# ---------------------------------------------------

print("\nMEDIA DE NUMEROS PARES - SIN USAR LISTAS")

# Variable para acumular la suma de los pares
suma_pares = 0

# Variable para contar cuantos numeros pares se ingresaron
cantidad_pares = 0

# Nuevamente se utiliza 0 como valor centinela
numero = int(input("Ingrese un numero entero (0 para terminar): "))

while numero != 0:

    # Se comprueba si el numero es par
    if numero % 2 == 0:

        # Se acumula el numero par
        suma_pares = suma_pares + numero

        # Se aumenta el contador de pares
        cantidad_pares = cantidad_pares + 1

    # Se solicita otro numero
    numero = int(input("Ingrese otro numero entero (0 para terminar): "))


# Se comprueba si se ingreso por lo menos un numero par
if cantidad_pares > 0:

    # Media = suma de los pares / cantidad de pares
    media = suma_pares / cantidad_pares

    print("La media de los numeros pares es:", media)

else:
    # Este caso evita dividir entre cero
    print("No se ingreso ningun numero par.")
