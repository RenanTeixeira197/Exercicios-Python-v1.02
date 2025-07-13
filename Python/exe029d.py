precos = []
total_valor = 0

print("Digite 0 quando finalizar todos os itens!")

while True:
    valor_item = float(input("Preço do item: R$ "))
    if valor_item == 0:
        break
    precos.append(valor_item)
    total_valor += valor_item

# Desconto se valor total passar de 100
desconto = 0
if total_valor > 100:
    desconto = total_valor * 0.1  # 10%
    print(f"Desconto aplicado: R$ {desconto:.2f}")

total_com_desconto = total_valor - desconto

# Mostra todos os itens comprados
print("\n--- NOTA FISCAL ---")
for i, valor in enumerate(precos, start=1):
    print(f"Item {i}: R$ {valor:.2f}")

print(f"\nTotal de itens: {len(precos)}")
print(f"Total da compra: R$ {total_valor:.2f}")
print(f"Total com desconto: R$ {total_com_desconto:.2f}")

# Valor pago e troco
valor_pago = float(input("Valor pago pelo cliente: R$ "))

if valor_pago >= total_com_desconto:
    troco = valor_pago - total_com_desconto
    print(f"Troco: R$ {troco:.2f}")
else:
    falta = total_com_desconto - valor_pago
    print(f"Falta pagar: R$ {falta:.2f}")
