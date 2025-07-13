total_salario = 0
total_filhos = 0
maior_salario = 0
salario_ate_mil = 0
contador = 0

print("Digite -1 como salário para encerrar o programa.\n")

while True:
    salario = float(input("Informe seu salário: "))
    if salario == -1:
        break

    numero_de_filhos = int(input("Informe o número de filhos: "))

    
    if salario > maior_salario:
        maior_salario = salario

   
    if salario <= 1000:
        salario_ate_mil += 1

   
    total_salario += salario
    total_filhos += numero_de_filhos
    contador += 1


if contador > 0:
    media_salario = total_salario / contador
    media_filhos = total_filhos / contador
    porcentagem_ate_mil = (salario_ate_mil / contador) * 100

    print(f"\nMédia dos salários: R$ {media_salario:.2f}")
    print(f"Média do número de filhos: {media_filhos:.2f}")
    print(f"Maior salário informado: R$ {maior_salario:.2f}")
    print(f"Quantidade de pessoas que ganham até R$ 1.000: {salario_ate_mil}")
    print(f"Porcentagem que ganha até R$ 1.000: {porcentagem_ate_mil:.2f}%")
else:
    print("Nenhum dado informado.")


