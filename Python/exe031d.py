pessoas = []
dados = []

while True:
    pessoas.append(str(input("informe seu nome: ")))
    pessoas.append(float(input("Informe seu peso: ")))
    dados.append(pessoas[:])
    dados.clear()
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()
    if continuar == 'N':
        break
    elif continuar != 'S':
        print("Opção inválida. Tente novamente.")
        continue
    pessoas.clear()

print(f"Ao todo você cadastrou {len(dados)} pessoas.")
if len(dados) > 0:
    pesos = [p[1] for p in dados]
    print(f"O maior peso foi de {max(pesos)} kg. Peso de ", end="")
    for p in dados:
        if p[1] == max(pesos):
            print(f"{p[0]} ", end="")
    print()
    
    print(f"O menor peso foi de {min(pesos)} kg. Peso de ", end="")
    for p in dados:
        if p[1] == min(pesos):
            print(f"{p[0]} ", end="")
    print()

else:
    print("Nenhuma pessoa foi cadastrada.")
print("Programa encerrado.")