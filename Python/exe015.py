opcao_prato = int(input("Informe o prato desejado: [1] Italiano [2] Japonês [3] Salvadorenho: "))
opcao_bebida = int(input("Informe a Bebida desejada: [1] Chá [2] Suco de Laranja [3] Refrigerante:"))


if opcao_prato == 1:
    calorias_prato = 750
elif opcao_prato == 2:
    calorias_prato = 324
elif opcao_prato == 3:
    calorias_prato = 545
else:
    print("Informe um valor válido!")
    calorias_prato = 0

if opcao_bebida == 1:
    calorias_bebida = 30
elif opcao_bebida == 2:
    calorias_bebida = 80
elif opcao_bebida == 3:
    calorias_bebida = 90
else:
    print("Informe um valor válido!")
    calorias_bebida = 0

total_calorias = calorias_bebida + calorias_prato

print("Total de calorias: ", total_calorias)
