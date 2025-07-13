pares = []
impares = []
valores = []

for lista in range(7):
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
    valores.append(numero)

print(f"Você digitou os valores: {valores}")
print(f"Os valores pares foram: {pares}")
print(f"Os valores ímpares foram: {impares}")
print(f"A lista completa é: {valores}")