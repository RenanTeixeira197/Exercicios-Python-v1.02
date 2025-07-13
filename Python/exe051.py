# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
# Seu programa tem que realizar três contagens através da função criada:                                                                                                                                                                           
#  a) de 1 até 10, de 1 em 1                                                                                                                                             
#  b) de 10 até 0, de 2 em 2                                                                                                                                            
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1  # Evita divisão por zero
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ', flush=True)
            sleep(0.5)
    print()  # Nova linha ao final da contagem


# Programa principal
print('Contagem de 1 até 10 de 1 em 1:')
contador(1, 10, 1)
print('Contagem de 1 até 10 de 1 em 1:')
contador(10, 0, 2)


print('Contagem personalizada:')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
# Fim do programa