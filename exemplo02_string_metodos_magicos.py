

def subsitituir_parte_string():
    texto = "EU tenho um gato."
    # Substituir o EU para Eu
    texto = texto.replace("EU", "Eu")
    # Substituir o ponto final por nada
    texto = texto.replace(".", "")
    print("Texto: "+ texto)

def Substituir_valor():
    valor_entrada: str = "R$ 2.395,33" # Alterar a string para "2395.33"
    valor_entrada_sanitizada: str = valor_entrada.replace(".", "") # "R$ 2.395,33" => "R$ 2395,33"
    valor_entrada_sanitizada = valor_entrada_sanitizada.replace("R$", "") # "R$ 2395.33" => " 2395.33"
    valor_entrada_sanitizada = valor_entrada_sanitizada.strip() #" 2395.33" => "2395.33"

    valor: float = float(valor_entrada_sanitizada)
    print("Valor: ", valor)

def verificar_comeca_com_enzo():
    texto = "Enzo da Silva"
    if texto.startswith("Enzo"): # Começa com 'Enzo'
        print("Geração alpha")
    else:
        print("Outra geração")

def verificar_termina_com_silva_ou_souza():
    texto = "Enzo da Souza"
    if texto.endswith("Silva") or texto.endswith("Souza"): # termina "Silva" ou "Souza"
        print("Brasileiro")
    else:
        print("Estrangeiro")

def verificar_se_contem():
    produto = "Toddy com pão e linguiça blumenau"
    produto = "Pão de queijo e Toddy"
    produto = "Pizza, Toddy e Açaí"
    if "Toddy" in produto:
        print("Viva o toddy")
    elif "Nescau" in produto:
        print("Trocar por Toddy, o vveridadeiro achocolotado")
    else:
        print("Sei lá")

def vericiar_se_nao_contem():
    produto = "Aipim com frango"
    produto = "Toddy"
    if "Toddy" not in produto: # se "Toddy" não está no texto
        print("Ta errado, deixa o toddy de lado")
    else:
        print("Ta errado, sem toddy")

if __name__ == "__main__":
    verificar_se_contem()
    