#Entre funções colocar duas linhas
#Nome de função (def) deve ser no padrão snake_case
def exemplo_tipos_primitivos():
    # Nome de variáveis deve ser no padrão snake_case (nome_completo_funcionario)
    # Nome de variáveis não pode começar com números, n pode conter caracteres especiais (~,`...)
    nome: str = "PS5 Pro" #str é string
    preco: float = 7000.99 #float número real
    quantidade: int = 2 #int é inteiro
    compra_realizada: bool = True # bool é operador lógico (True: verdadeiro, False: falso)

    #calcular o total da compra
    total_compra: float = preco * quantidade
    
    print("Nome:", nome)
    print("Preço:", preco)
    print("Quantidade:", quantidade)
    print("Compra realizada:", compra_realizada)
    print("Total da compra:", total_compra)

def exemplo_entrada_dados():
    # input é utilizado para questionar para o usuário uma entrada de dados, tudo o
    # que o usuário digitar virá como string
    nome: str = input("Digite o nome: ")
    sobrenome: str = input("Digite o sobrenome: ")
    # Convertendo o que o usuário digitou para inteiro
    idade: int = int(input("Digite a idade: "))
    
    # + neste cenário está concatenando o nome, espaço e o sobrenome
    nome_completo: str = nome + " " + sobrenome
    # str(idade) => convertendo de int para string
    texto: str = "Nome completo: " + nome_completo + " tem " + str(idade) + " anos"
    print(texto)

#ex.1: Criar a função exercicio_paciente
#   - Solicitar os campos: nome, peso, altura e e-mail
#   - calcular o imc do paciente
#   - apresentar o IMC e seus dados
#ex.2: Criar a função exercicio_carro
#   - Solicitar os campos: modelo do carro, quantidade parcelas, valor de cada parcela, valor da fipe.
#   - Calcular o valor total pago no carro
#   - Calcular o valor total pago de juros (total pago - valor da fipe)
#   - Apresentar todos os dados para o usuário

# esse trecho é chamado quando o arquivo é executado, main é
# o ponto de entrada (execução) de uma aplicação
if __name__ == "__main__":
    #executa a função abaixo, ou seja, executará o código que está dentro da função
    exemplo_entrada_dados()
# Como executar:
# Abrir o terminal(Ctrl + J)
# executar o comando "py exemplo_00_variaveis.py"