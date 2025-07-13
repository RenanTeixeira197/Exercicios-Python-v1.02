satisfatorio = 0
indiferente = 0
insatisfatorio = 0
contador = 0
total_idade = 0
soma_idade_satisfatorio = 0
cont_satisfatorio = 0

print('=' * 30)
print(" QUEREMOS SABER SUA OPINIAO  ")
print('=' * 30)

while True:
    idade = int(input("Informe sua idade: "))
    if idade == 0:
        break
    else:
        total_idade += idade
        contador += 1
    avaliacao = int(input("[1] Satisfatorio [2] Indiferente [3] Insatisfatorio: "))
    if avaliacao == 1:
        satisfatorio += 1
        soma_idade_satisfatorio += idade
        cont_satisfatorio += 1
    elif avaliacao == 2:
        indiferente += 1
    elif avaliacao == 3:
        insatisfatorio += 1
    else:
        print("Valor Invalido!")

if contador > 0:
    media_idade = total_idade / contador
else:
    media_idade = 0

if cont_satisfatorio > 0:
    media_idade_satisfatorio = soma_idade_satisfatorio / cont_satisfatorio
else:
    media_idade_satisfatorio = 0       

print('\n' + '=' * 30)
print("         RESULTADOS FINAIS         ")
print('=' * 30)
print(f"Total de avaliacoes {contador}")
print(f"Responderam Satisfatorio: {satisfatorio}")
print(f"Media de idade satisfatorio: {media_idade_satisfatorio:.2f}")
print(f"Responderam Indiferente: {indiferente}")
print(f"Responderam Insatisfatorio: {insatisfatorio}")
print(f"Media de idade: {media_idade:.2f}")