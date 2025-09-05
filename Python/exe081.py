def cabeçalho():
    print("-" * 30)
    print("CONTAGEM DE CONSOANTES".center(30))
    print("-" * 30)

def contar_consoantes():
    consoantes = "bcdfghjklmnpqrstvxz"
    total_consoantes = 0
    for i in range(1, 6):
        palavra = input(f"Digite a {i}ª palavra (ou 0 para encerrar o programa.): ").lower().strip()
        if palavra == "0":
            break
        else:
            for letra in palavra:
                if letra in consoantes:
                    total_consoantes += 1
                    print(f'{letra}', end=' ')
        print(f"\nTotal de consoantes: {total_consoantes}")

cabeçalho()
contar_consoantes()