def media_ponderada(n1, n2, n3, p1, p2, p3):
    media = (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3)
    return media

num1 = float(input("Informe o primeiro valor: "))
num2 = float(input("Informe o segundo valor: "))
num3 = float(input("Informe o terceiro valor: "))

peso1 = float(input("Informe o Peso 1: "))
peso2 = float(input("Informe o Peso 2: "))
peso3 = float(input("Informe o Peso 3: "))

resultado = media_ponderada(num1, num2, num3, peso1, peso2, peso3)

if (peso1 + peso2 + peso3) == 0:
    print("A soma dos pesos não pode ser zero.")
else:
    resultado = media_ponderada(num1, num2, num3, peso1, peso2, peso3)
    print("A Média ponderada é:", round(resultado, 2))
