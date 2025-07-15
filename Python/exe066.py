def LetrasNaPosicaoPar(nome):
    letras_pares = []
    for i in range(len(nome)):
        if i % 2 == 0:  # Verifica se o índice é par
            letras_pares.append(nome[i])
    return letras_pares

# Exemplo de uso
nome = str(input("Digite um nome: "))
resultado = LetrasNaPosicaoPar(nome)
print("Letras nas posições pares:", resultado)