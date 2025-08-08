#função que receba uma string e retorne o número de consoantes

def contar_consoantes(texto):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    contador = 0
    for char in texto:
        if char in consoantes:
            contador += 1
    return contador


if __name__ == "__main__":
    texto = input("Digite uma frase: ")
    total_consoantes = contar_consoantes(texto)
    print(f"Número de consoantes na frase: {total_consoantes}")