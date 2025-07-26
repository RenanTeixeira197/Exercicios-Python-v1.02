def cabeçalho():
    print("-" * 30)
    print("Nota Fiscal")
    print("-" * 30)

cabeçalho()

preco_produto = float(input("Valor a ser pago (R$): "))

while True:
    forma_pagamento = input(
        "Selecione a forma de pagamento:\n"
        "1-[Dinheiro/Cheque]\n"
        "2-[Crédito à vista]\n"
        "3-[Crédito parcelado até 2x]\n"
        "4-[Crédito parcelado 3x ou mais]\n"
        "Opção: "
    )

    try:
        if forma_pagamento == '1':
            valor_final = preco_produto - (preco_produto * 0.10)
            print("Desconto de 10% aplicado.")
        elif forma_pagamento == '2':
            valor_final = preco_produto - (preco_produto * 0.05)
            print("Desconto de 5% aplicado.")
        elif forma_pagamento == '3':
            valor_final = preco_produto
            print("Sem desconto ou acréscimo.")
        elif forma_pagamento == '4':
            qtde_parcelas = int(input("Número total de parcelas (3 ou mais): "))
            if qtde_parcelas < 3:
                print("Para essa opção, o número de parcelas deve ser 3 ou mais.")
                continue
            valor_final = preco_produto + (preco_produto * 0.20)
            print("Acréscimo de 20% aplicado.")
            print(f"Valor de cada parcela: {valor_final / qtde_parcelas:.2f}")
        else:
            print("Dados Inválidos!")
            continue
    except Exception as e:
        print("ERRO! Tente novamente")
        continue
    else:
        if forma_pagamento in ['1', '2', '3', '4']:
            print(f'Valor total a ser pago: {valor_final:.2f}')
            break
        else:
            print("Dados Inválidos!")