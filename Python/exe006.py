def soma_numero(n1, n2):
    return n1 + n2

def potencia_numero(base, expoente):
    return base ** expoente

try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resultado_soma = soma_numero(num1, num2)
    resultado_potencia = potencia_numero(num1, num2)

    print("\nResultados:")
    print(f"A soma dos dois números é: {resultado_soma}")
    print(f"A potência do número 1 elevado ao número 2 é: {resultado_potencia}")

except ValueError:
    print("Por favor, digite apenas números inteiros.")