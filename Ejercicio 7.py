# EJERCICIO 7
# Moda de un conjunto de enteros

# El usuario ingresa los numeros separados por espacios
entrada = input("Ingrese los numeros enteros separados por espacios: ")

# split() separa los valores ingresados
datos = entrada.split()

# Lista donde se guardaran los numeros como enteros
numeros = []

# Se convierten los datos de texto a numeros enteros
for dato in datos:
    numeros.append(int(dato))


# Lista donde se guardaran las modas encontradas
modas = []

# Guarda la mayor cantidad de repeticiones encontrada
frecuencia_maxima = 0


# Recorremos cada numero de la lista
for numero in numeros:

    # count() indica cuantas veces aparece el numero
    frecuencia = numeros.count(numero)

    # Si encontramos una frecuencia mayor,
    # actualizamos la frecuencia maxima
    if frecuencia > frecuencia_maxima:

        frecuencia_maxima = frecuencia

        # Se borra la moda anterior y se guarda la nueva
        modas = [numero]

    # Si tiene la misma frecuencia maxima,
    # puede existir mas de una moda
    elif frecuencia == frecuencia_maxima:

        # Evitamos guardar el mismo numero varias veces
        if numero not in modas:
            modas.append(numero)


# Si la frecuencia maxima es 1,
# significa que ningun numero se repitio
if frecuencia_maxima == 1:

    print("Ningun valor se repite, por lo tanto no hay moda.")


# Si solamente existe una moda
elif len(modas) == 1:

    print("La moda es:", modas[0])
    print("Se repite", frecuencia_maxima, "veces.")


# Si existen varias modas, el conjunto es multimodal
else:

    print("El conjunto es multimodal.")
    print("Las modas son:", modas)
    print("Cada una se repite", frecuencia_maxima, "veces.")
