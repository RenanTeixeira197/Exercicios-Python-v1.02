#Faça um programa que leia uma palavra e imprima quantas vezes forem o número de caracteres:
def repetir_palavra(palavra):
    return [palavra for _ in range(len(palavra))]

palavra = input("Digite uma palavra: ")

resultado = repetir_palavra(palavra)

for item in resultado:
    print(item)
