def tratar_erro_na_conversao_string_nao_inteira():
    # Tentar executar um trecho de código que sabemos que poderá acontecer algum erro
    try: # tente
        # convertendo o que o usuário digitou de str apra int e sabemos que pode acontecer algum erro
        numero = int(input("Digite o número: "))
    except Exception as erro: # quando ocorrer algum erro executa o código daqui de dentro do except
        print ("Deu erro na conversão do número")
        # Caso desejar apresentar a mensagem do erro
        print ("Mensagem do erro: ", erro)

    # Apresnetar essa mensagem dando erro ou não
    print("Programa finzalidao com sucesso")

if __name__ = "__main__":
    tratar_erro_na_conversao_string_nao_inteira()