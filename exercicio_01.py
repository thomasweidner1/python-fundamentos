def exercicio_paciente():
    nome: str = input("Insira o nome do paciente: ")
    peso: float = float(input("Qual o peso do paciente? "))
    altura: float = float(input("Qual a altura do paciente?(ex: 1.80m) "))

    calculo_imc: float = peso/(altura**2)

    print("Nome: ",nome)
    print("Peso: ",peso)
    print("altura: ",altura)
    print("IMC: ",calculo_imc)

if __name__ == "__main__":
    exercicio_paciente()