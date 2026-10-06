def funcion_portero(Numero_real_excepto_el_2):
    while True:
        try:
            valor = (input(Numero_real_excepto_el_2))
            if valor == "2":
                print("El valor no puedes ser 2, porfavor ingrese otro valor.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Por favor ingrese un número real.")

def main():
    n = funcion_portero("Ingrese un número real (excepto 2): ")
    print(f"El valor ingresado es: {n}")
if __name__ == "__main__":
    main()