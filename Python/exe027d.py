total_positivos = 0
total_negativos = 0
total_zeros = 0

for numeros in range(10):
    numero = int(input("Informe um número: "))
    if numero > 0:
        total_positivos += 1
    elif numero < 0:
        total_negativos += 1
    elif numero == 0:
        total_zeros += 1
    
print(f"Total Positivos: {total_positivos}")
print(f"Total Negativos: {total_negativos}")
print(f"Total Zeros: {total_zeros}")