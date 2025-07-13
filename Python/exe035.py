numero_inteiro = 0
total_numeros = 0
contador = 0
lista_numeros = []

def cabeçalho():
    print("=" * 20)
    print("APERTE 0 PARA ENCERRAR O PROGRAMA")
    print("=" * 20)

cabeçalho()

while True:
    numero_inteiro = int(input("Informe um número:"))
    if numero_inteiro == 0:
        break
    else:
        total_numeros += numero_inteiro
        contador += 1
        lista_numeros.append(numero_inteiro)

media_numeros = total_numeros / contador
lista_numeros.sort()

print("Números informados: ", lista_numeros)
print("Média dos valores: ", media_numeros)
print("Maior número: ", max(lista_numeros))
print("Menor número: ", min(lista_numeros))