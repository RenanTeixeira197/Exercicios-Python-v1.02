#Faça um programa que leia um nome 
# e apresente as letras que estão na posição par


nome = input("Digite um nome: ")
letras_pares = [letra for i, letra in enumerate(nome) if i % 2 == 0]
print("Letras nas posições pares:", letras_pares)