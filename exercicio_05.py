def remover_espaco_texto():
    texto = input("Digite um texto, vamos formatá-lo: ")
    texto_sanitizado = texto.lstrip()
    print("Texto formatado: ", texto_sanitizado.lower())

if __name__ == "__main__":
    remover_espaco_texto()