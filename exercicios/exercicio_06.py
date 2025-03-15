def formatar_nome_empresa():
    empresa = input("Digite o nome de uma empresa especificando se é LTDA ou SA: ")
    if empresa.endswith("LTDA"):
        empresa_sanitizada = empresa.replace(" LTDA", "")
        empresa_formatada = empresa_sanitizada.strip().lower()
    elif empresa.endswith("SA"):
        empresa_sanitizada = empresa.replace(" SA", "")
        empresa_formatada = empresa_sanitizada.strip().lower()
    print("Empresa formatada: ", empresa_formatada)

if __name__ == "__main__":
    formatar_nome_empresa()