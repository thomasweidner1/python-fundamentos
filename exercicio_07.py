def curso_inicia_com():
    curso = input("Insira o nome do curso: ")
    if curso.startswith("SuperDev"):
        print("Melhor curso do mundo")
    else:
        print("Pode abandonar")

if __name__ == "__main__":
    curso_inicia_com()