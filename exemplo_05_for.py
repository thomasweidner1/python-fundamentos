import time

def exemplo_for_apresentar_numeros():
    # indice = 0
    # while indice < 5:
    #   print("")
    #   indice = indice + 1
    for indice in range(0, 5):
        print(indice)

def exemplo_for_incrementar_dois_em_dois():
    # Apresentar 0, 3, 6, 9
    for indice in range(0, 10, 3):
        print(indice)

def exemplo_solicitar_dados():
    quantidade_desejada = int(input("Digite a quantidade desejada: "))
    for i in range(0, quantidade_desejada):
        nome = input("Digite o nome: ")
        sobrenome = input("Digite o sobrenome: ")
        nome_completo = nome + " " + sobrenome
        print("Nome completo:", nome_completo)

def exemplo_apresentar_contagem_regressiva():
    for i in range(10, 0, -1):
        #if i % 2 == 0: para mostrar apenas os pares
        print(i)
        time.sleep(1) # delay de 1 segundo no código (USAR "import time")

def exemplo_relogio():
    for hora in range(0, 24):
        for minuto in range (0, 60):
            for segundo in range(0, 60):
                print(hora, minuto, segundo, sep=":")
                time.sleep(1)

if __name__ == "__main__":
    exemplo_relogio()