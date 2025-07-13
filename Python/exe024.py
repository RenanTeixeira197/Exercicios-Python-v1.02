numero = int(input("Informe um número: "))

if numero > 1 and numero % 3 == 0 and numero % 7 ==0:
    print("Esse número é primo!")
else:
    print("Esse número não é primo!")