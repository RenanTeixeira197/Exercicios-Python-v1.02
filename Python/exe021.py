codigo_estado = int(input("Informe o código do estado [1] [2] [3] [4]: "))
peso_carga = float((input("Peso da carga (T): ")))
codigo_carga = int(input("Informe o código da carga: [10 a 20] [21 a 30] [31 a 40]:"))

if codigo_estado == 1:
    taxa_imposto = 20/100
elif codigo_estado == 2:
    taxa_imposto = 15/100
elif codigo_estado == 3:
    taxa_imposto = 5/100
else:
    print("Código Inválido!")
    taxa = None

if 10 <= codigo_carga <= 20:
    preco_por_quilo = 180
elif 21 <= codigo_carga <= 30:
    preco_por_quilo = 120
elif 31 <= codigo_carga <= 40:
    preco_por_quilo = 230
else:
    print("Código Inválido!")

if taxa_imposto is not None and preco_por_quilo is not None:
    peso_em_kg = peso_carga * 1000  # converter toneladas para quilos
    valor_total_carga = peso_em_kg * preco_por_quilo
    imposto = valor_total_carga * taxa_imposto
    total_a_pagar = valor_total_carga + imposto

    print("\n--- RESUMO ---")
    print(f"Peso da carga (Kg): {peso_em_kg:.2f}")
    print(f"Preço da carga por quilo: R$ {preco_por_quilo:.2f}")
    print(f"Valor da carga: R$ {valor_total_carga:.2f}")
    print(f"Imposto: R$ {imposto:.2f}")
    print(f"Total a pagar: R$ {total_a_pagar:.2f}")
else:
    print("Não foi possível calcular devido a dados inválidos.")