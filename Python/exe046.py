lista_pedidos = []
valor_pedidos = 0
preço_unitario = 0
total_quantidade = 0

while True:
    numero_pedido = int(input("Número do pedido:"))
    if numero_pedido == 0:
        break
    else:
        dia = int(input("Dia:"))
        mes = int(input("Mês"))
        if mes > 12:
            print("MÊS INVÁLIDO!")
        else:
            ano = int(input("Ano: "))
            nome_pedido = str(input("Produto: "))
            preço_unitario = float(input("Preço"))
            quantidade = int(input("Quantidade:"))
            
            valor_pedidos += preço_unitario * quantidade
            total_quantidade += quantidade
            lista_pedidos.append(nome_pedido)

        
print("Valor total dos pedidos: ", valor_pedidos)
print("Quantidade de itens: ", total_quantidade)
print("Lista de pedidos: ", lista_pedidos)

       