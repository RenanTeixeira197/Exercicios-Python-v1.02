total_salario = 0
total_filhos = 0
contador = 0

print("Digite -1 como salário para encerrar o programa.\n")


while True:
  salario = float(input("Informe seu salário: "))
  if salario == -1:
    break
  else:
    numero_de_filhos = int(input("Informe o número de filhos: "))
    total_salario += salario
    total_filhos  += numero_de_filhos
    contador += 1

if contador > 0:
  media_salario = total_salario / contador
  media_filhos = total_filhos / contador
  print(f"Média dos salários: {media_salario:.2f}")
  print(f"Média do número de filhos: {media_filhos:.2f}")
else:
    print("Nenhum dado informado.")

