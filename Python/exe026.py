total_idade = 0
total_altura = 0
contador = 0

print("Digite 0 em idade para encerrar")
while True:
    idade = int(input("Informe sua idade: "))
    if idade == 0:
        break
    else:
        altura = float(input("Informe sua altura: "))
        total_idade += idade
        total_altura += altura
        contador += 1

if contador > 0:
    media_idade = total_idade / contador
    media_altura = total_altura / contador
    print(f"Média de idade das pessoas: {media_idade:.2f}")
    print(f"Média de altura das pessoas: {media_altura:.2f}")
else:
    print("Nenhum dado salvo")

