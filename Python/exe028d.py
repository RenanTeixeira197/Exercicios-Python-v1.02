total_itens = 0
total_valor = 0

print("Digite 0 quando finalizar todos os itens!")

while True:
    valor_item = float(input("Preço: "))
    if valor_item == 0:
        break
    else:
        total_itens += 1
        total_valor += valor_item

print(f"Total de itens: {total_itens}")
print(f"Valor da compra: {total_valor:.2f}")

   