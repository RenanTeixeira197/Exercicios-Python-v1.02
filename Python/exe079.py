def pos_ou_neg(num):
    if num >=0:
        return "Positivo"
    else:
        return "Negativo"
    
numero = int(input("Informe um número: "))

resultado = pos_ou_neg(numero)

print(f'O número {numero} é {resultado}.')