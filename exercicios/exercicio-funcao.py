from typing import Tuple

def calcular_produto() -> Tuple [str, int, float]:
    modelo = solicitar_modelo()
    quantidade = solicitar_quantidade()
    preco = solicitar_preco()
    total = quantidade * preco


def apresentar_produto():
    modelo, quantidade, preco, total = calcular_produto()
    print("Modelo: ", modelo, "\nQuantidade: ", quantidade, "\nPreço: ", preco, "\nValor total do produto: ", total)


def solicitar_modelo() -> str:
    modelo_solicitado = input("Informe o modelo:").strip()
    while len(modelo_solicitado) < 4:
        print("Nome inválido! Deve possuir no mínimo 4 caracter")
        modelo_solicitado = input("Informe o modelo: ").strip()
    return modelo_solicitado

def solicitar_quantidade() -> int:
    quantidade_solicitada: int = int(input("Informe a quantidade: "))
    while quantidade_solicitada < 1 or quantidade_solicitada > 5:
        print("Quantidade inválida! máximo 5 e mínimo 1")
        quantidade_solicitada: int = int(input("Informe a quantidade: "))
    return quantidade_solicitada

def solicitar_preco() -> float:
    preco_solicitado: float = float(input("Informe o preço: "))
    while preco_solicitado < 100 or preco_solicitado > 500:
        print("Preço inválido! mínimo 100 e máximo 500")
        preco_solicitado: float = float(input("Informe o preço: "))
    return preco_solicitado

if __name__ == "__main__":
    calcular_produto()

# Exercicio:
# Criar uma função solicitar_modelo min: 4, retornando o modelo
# Criar uma função solicitar_quantidade min: 1 max: 5, retornando a quantidade
# Criar uma função solicitar_preco min: 100, max: 500, retornando o preco
# Criar uma função solicitar_calcular_produto, chamando as funções e armazenar as variáveis
# Apresentar o total e as variáveis