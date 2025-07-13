lista = []

for i in range(10):
    elementos = int(input("Insira um elemento: "))
    lista.append(elementos)


print("Elementos numéricos inseridos na lista: ", lista)
print("Elemetos na ordem inversa: ", lista[::-1])