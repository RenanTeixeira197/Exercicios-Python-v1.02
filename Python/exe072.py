def cabeçalho():
    print("-" * 30)
    print("Nota Fiscal".center(30))
    print("-" * 30)

def aplicar_desconto(valor, percentual):
    return valor - (valor * percentual / 100)

def aplicar_acrescimo(valor, percentual):
    return valor + (valor * percentual / 100)

def validar_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            return valor
        except ValueError:
            print("Digite um número válido.")

def validar_int(mensagem, minimo=1):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < minimo:
                print(f"O número deve ser maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Digite um número inteiro válido.")

# Programa principal
cabeçalho()

preco_produto = validar_float("Valor a ser pago (R$): ")

while True:
    forma_pagamento = input(
        "\nSelecione a forma de pagamento:\n"
        "1 - [Dinheiro/Cheque]\n"
        "2 - [Crédito à vista]\n"
        "3 - [Crédito parcelado até 2x]\n"
        "4 - [Crédito parcelado 3x ou mais]\n"
        "Opção: "
    )

    if forma_pagamento == '1':
        valor_final = aplicar_desconto(preco_produto, 10)
        print("Desconto de 10% aplicado.")
    elif forma_pagamento == '2':
        valor_final = aplicar_desconto(preco_produto, 5)
        print("Desconto de 5% aplicado.")
    elif forma_pagamento == '3':
        valor_final = preco_produto
        print("Sem desconto ou acréscimo.")
    elif forma_pagamento == '4':
        qtde_parcelas = validar_int("Número total de parcelas (3 ou mais): ", minimo=3)
        valor_final = aplicar_acrescimo(preco_produto, 20)
        valor_parcela = valor_final / qtde_parcelas
        print("Acréscimo de 20% aplicado.")
        print(f"Valor de cada parcela: R$ {valor_parcela:.2f}")
    else:
        print("Opção inválida! Tente novamente.")
        continue

    print(f"\nValor total a ser pago: R$ {valor_final:.2f}")
    print("-" * 30)
    print("Compra concluída. Obrigado pela preferência!")
    break
