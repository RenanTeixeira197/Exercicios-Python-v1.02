casadas = 0
separadas = 0
solteiras = 0
viuvas = 0
total_pessoas = 0

while True:
    idade = int(input("Informe sua idade (ou 0 para encerrar): "))
    if idade == 0:
        break
    else:
        peso = float(input("Informe seu peso: "))
        sexo = input("Informe seu sexo: [M]/[F] ").strip().upper()
        estado_civil = int(input("Informe seu estado civil: [1] Casado, [2] Separado, [3] Solteiro, [4] Viúvo: "))
        
        if estado_civil == 1:
            casadas += 1
        elif estado_civil == 2:
            separadas += 1
        elif estado_civil == 3:
            solteiras += 1
        elif estado_civil == 4:
            viuvas += 1
        else:
            print("Número Inválido!")
            continue
        
        total_pessoas += 1

def cabecalho():
    print('=' * 30)
    print("TOTAL DE PESSOAS:")
    print('=' * 30)

cabecalho()
print("Total: ", total_pessoas)
print("Casadas: ", casadas)
print("Separadas:", separadas)
print("Solteiras: ", solteiras)
print("Viúvas: ", viuvas)

    