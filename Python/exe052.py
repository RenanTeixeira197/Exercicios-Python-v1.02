#Faça um programa que tenha uma função chamada maior(), 
# que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*args):
    if len(args) == 0:
        return None  # Retorna None se não houver argumentos

    maior_valor = args[0]  # Assume o primeiro valor como o maior
    for num in args:
        if num > maior_valor:
            maior_valor = num  # Atualiza o maior valor se encontrar um maior

    return maior_valor  # Retorna o maior valor encontrado


def main():
    print("Analisando os valores: 3, 5, 7, 2, 8")
    resultado = maior(3, 5, 7, 2, 8)
    print(f"O maior valor é: {resultado}")

    print("Analisando os valores: 10, 20, 30")
    resultado = maior(10, 20, 30)
    print(f"O maior valor é: {resultado}")

    print("Analisando os valores: -1, -5, -3")
    resultado = maior(-1, -5, -3)
    print(f"O maior valor é: {resultado}")

    print("Analisando sem valores")
    resultado = maior()
    if resultado is None:
        print("Nenhum valor foi fornecido.")
    else:
        print(f"O maior valor é: {resultado}")
if __name__ == '__main__':
    main()
# Fim do programa