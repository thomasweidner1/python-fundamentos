def apresentar_numero():
    numero: float = float(input("Digite um número qualquer: "))

    if numero < 15:
        print("Numero é menor que 15")
    else:
        print("Número é maior que 15")

if __name__ == "__main__":
    apresentar_numero()