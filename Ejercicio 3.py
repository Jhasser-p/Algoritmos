# EJERCICIO 3
# Inversion de una frase

# Se solicita al usuario que ingrese una frase
frase = input("Ingrese una frase: ")

# split() separa la frase y guarda cada palabra
# como un elemento de una lista
palabras = frase.split()

# Se invierte el orden de las palabras
palabras_invertidas = palabras[::-1]

# join() vuelve a unir las palabras separándolas por espacios
frase_palabras_invertidas = " ".join(palabras_invertidas)

# Se invierte toda la frase caracter por caracter
frase_letras_invertidas = frase[::-1]

# Se muestran los resultados
print("Frase original:")
print(frase)

print("Invertida palabra por palabra:")
print(frase_palabras_invertidas)

print("Invertida letra por letra:")
print(frase_letras_invertidas)
