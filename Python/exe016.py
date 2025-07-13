altura = float(input("Informe sua altura: "))
sexo = input("SEXO [M]/[F]: ").upper()

if sexo == 'F':
    pesoF = 62.1 * altura - 44.7
    print("Seu peso ideal é:", round(pesoF, 2), "Kg")
elif sexo == 'M':
    pesoM = 72.7 * altura - 58
    print("Seu peso ideal é:", round(pesoM, 2), "Kg")
else:
    print("Valor Inválido!")

