from time import sleep

def cabecalho():
    print("=-" * 30)
    print("CALCULADORA DE ÁREA EM M²")
    print("Digite 'FIM' para encerrar a entrada de cômodos.")
    print("=-" * 30)

def calculo_area_comodo(larg, comp):
    return larg * comp

def solicitar_comodos():
    area_total = 0
    while True:
        comodo = input("Informe o nome do cômodo: ").strip()
        if comodo.upper() == "FIM":
            break

        try:
            largura = float(input(f"Largura de {comodo} (m): "))
            comprimento = float(input(f"Comprimento de {comodo} (m): "))
        except ValueError:
            print("⚠️ Valores inválidos! Tente novamente.")
            continue

        area = calculo_area_comodo(largura, comprimento)
        print(f"➡ A área do cômodo '{comodo.title()}' é: {area:.2f} m²\n")
        area_total += area

    return area_total

# Execução principal
cabecalho()
area_total = solicitar_comodos()

print("\nCalculando total...")
sleep(1)
print(f"\n✅ Área total do imóvel: {area_total:.2f} m²")
