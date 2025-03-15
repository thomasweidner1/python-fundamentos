def exercicio_carro():
    modelo: str = input("Insira o modelo do carro: ")
    parcelas: int = int(input("Insira a quantidade de parcelas: "))
    valor_da_parcela: float = float(input("Insira o valor da parcela: "))
    valor_fipe: float = float(input("Insira o valor da FIPE: "))

    valor_com_juros: float = valor_da_parcela * parcelas
    juros: float = valor_com_juros - valor_fipe

    print("Modelo: ",modelo)
    print("Quantidade de Parcelas: ",parcelas)
    print("Valor da parcela: R$",valor_da_parcela)
    print("Valor total: ",valor_com_juros)
    print("Juros pagos: ", juros)
    print("FIPE: ", valor_fipe)

if __name__ == "__main__":
    exercicio_carro()