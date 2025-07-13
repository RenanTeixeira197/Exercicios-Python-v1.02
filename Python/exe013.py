nome_pessoa = str(input("Informe seu nome: "))
idade_pessoa = int(input("Informe sua Idade: "))

if idade_pessoa <= 18:
    print("Valor a pagar R$ 50,00")
elif idade_pessoa >= 19 and idade_pessoa <= 29:
    print("Valor a pagar R$: 70,00")
elif idade_pessoa >= 30 and idade_pessoa <= 45:
    print("Valor a pagar R$: 90,00")
elif idade_pessoa >= 46 and idade_pessoa <= 65:
    print("Valor a pagar R$: 130,00")
elif idade_pessoa > 65:
    print("Valor a Pagar R$: 170,00")