idade = int(input("Informe sua idade: "))

if idade < 16:
    print("Não Eleitor")
elif idade >= 18 and idade <= 65:
    print("Eleitor Obrigatório!")
elif (16 <= idade < 18) or idade > 65:
    print("Eleitor Facultativo!")
