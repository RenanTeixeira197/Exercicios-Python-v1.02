#Faça um programa que leia uma palavra e imprima
#quantas vezes for o número de caracteresS


nome = str(input("Informe um nome: "))
comprimento_nome = len(nome)

for i in range(comprimento_nome):
    print(nome[i], end=' ')
    print()  
