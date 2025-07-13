listaA = []
listaB = []

for i in range(10):
    num = int(input(f"Digite o {i+1}º número da lista A: "))
    listaA.append(num)

for i in range(10):
    num = int(input(f"Digite o {i+1}º número da lista B: "))
    listaB.append(num)

listaC = []
for i in range(10):
    if listaA[i] > listaB[i]:
        listaC.append(listaA[i])
    else:
        listaC.append(listaB[i])


print("Soma das listas A e B:", sum(listaA) + sum(listaB))
print("Lista C em ordem crescente:", sorted(listaC))
print("Lista A:", listaA)
print("Lista B:", listaB)
print("Lista C:", listaC)

