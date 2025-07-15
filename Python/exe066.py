def LetrasNaPosicaoPar(nome):
    nome = input("Informe um nome: ")
    letras = []
    for i in range(len(nome)):
        if nome % 2 == 0:
            letras.append(nome)
    return nome

informar_nome = input("Informe um nome: ")

resultado = LetrasNaPosicaoPar(informar_nome)

print(f'As letras pares no nome {informar_nome} são: {resultado}')