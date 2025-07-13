import csv

mulheres = {"casadas": 0, "separadas": 0, "solteiras": 0, "viúvas": 0}
homens = {"casados": 0, "separados": 0, "solteiros": 0, "viúvos": 0}
total_pessoas = 0

while True:
    idade = int(input("\nInforme sua idade (ou 0 para encerrar): "))
    if idade == 0:
        break

    peso = float(input("Informe seu peso: "))
    sexo = input("Informe seu sexo: [M]/[F] ").strip().upper()
    estado_civil = int(input("Estado civil: [1] Casado(a), [2] Separado(a), [3] Solteiro(a), [4] Viúvo(a): "))

    if sexo not in ["M", "F"]:
        print("Sexo inválido.")
        continue

    if estado_civil not in [1, 2, 3, 4]:
        print("Estado civil inválido.")
        continue

    total_pessoas += 1
    
    with open("dados.csv", "a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([idade, peso, sexo, estado_civil])

    # Registro por sexo e estado civil
    if sexo == "F":
        if estado_civil == 1:
            mulheres["casadas"] += 1
        elif estado_civil == 2:
            mulheres["separadas"] += 1
        elif estado_civil == 3:
            mulheres["solteiras"] += 1
        elif estado_civil == 4:
            mulheres["viúvas"] += 1
    elif sexo == "M":
        if estado_civil == 1:
            homens["casados"] += 1
        elif estado_civil == 2:
            homens["separados"] += 1
        elif estado_civil == 3:
            homens["solteiros"] += 1
        elif estado_civil == 4:
            homens["viúvos"] += 1

# Função para exibir o relatório
def relatorio():
    print("\n" + "=" * 40)
    print(f"RELATÓRIO FINAL - Total de Pessoas: {total_pessoas}")
    print("=" * 40)

    print("\n👩 MULHERES:")
    for status, qtd in mulheres.items():
        print(f"{status.capitalize()}: {qtd}")

    print("\n👨 HOMENS:")
    for status, qtd in homens.items():
        print(f"{status.capitalize()}: {qtd}")

relatorio()
