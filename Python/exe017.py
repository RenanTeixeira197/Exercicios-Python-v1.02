lista = []

for numero in range(5):
    numero = int(input("Informe um número: "))
    lista.append(numero)

print("Números registrados: ", lista)
print("Maior número: ", max(lista))
print("Menor número: ", min(lista))