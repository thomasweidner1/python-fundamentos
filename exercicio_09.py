def apresentar_empresa():
    encerrar = " "
    while encerrar.strip().lower() != "sair":
        empresa = input("Digite o nome da empresa e especifique se é LTDA ou SA: ")
        while empresa.endswith("LTDA"):
            print("A empresa é  uma Sociedade de responsabilidade limitada")
            input("Digite o nome da empresa e especifique se é LTDA ou SA: ")
        while empresa.endswith("SA"):
            print("A empresa é uma Sociedade Anônima")
            input("Digite o nome da empresa e especifique se é LTDA ou SA: ")
    encerrar = input("Para finalizar, digite sair...")

if __name__ == "__main__":
    apresentar_empresa()