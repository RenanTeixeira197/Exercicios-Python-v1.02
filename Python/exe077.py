

def lista():
    return [1, 2, 3, 4, 5]


def cabeçalho():
    print("-" * 30)
    print("LISTA DE NÚMEROS".center(30))
    print("-" * 30)

def exibir_lista(numeros):
    for numero in numeros:
        print(f"Número: {numero}")
    print("-" * 30)

if __name__ == "__main__":
    cabeçalho()
    numeros = lista()
    exibir_lista(numeros)
    print("Fim do programa.")