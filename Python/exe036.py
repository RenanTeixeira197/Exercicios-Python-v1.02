def cabeçalho():
    print('-' * 30)
    print("TABUADA")
    print('-' * 30)

cabeçalho()

def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

num = int(input("Digite um número para ver a tabuada: "))
tabuada(num)