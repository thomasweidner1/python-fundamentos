def definir_idade():
    idade: int = int(input("Insira sua idade: "))
    if idade < 12:
        print("Você é uma criança")
    elif idade < 18:
        print("Você é um adolescente")
    elif idade < 60:
        print("Você é um adulto")
    else:
        print("Você é um idoso")

if __name__ == "__main__":
    definir_idade()