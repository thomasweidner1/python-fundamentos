def apresentar_caracter_nome_animal():
    animal = input("Digite o nome de um animal: ")
    animal_sanitizado = animal.strip()
    quantidade_caracter = len(animal_sanitizado)
    print("Animal: ", animal_sanitizado.lower())
    print("Caracteres: ", quantidade_caracter)

if __name__ == "__main__":
    apresentar_caracter_nome_animal()