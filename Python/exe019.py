numero_mes = int(input("Informe o número do mês: "))

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

if 1 <= numero_mes <= 12:
    print(meses[numero_mes - 1])
else:
    print("Mês Inválido!")
