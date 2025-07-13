#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(numeros):
    """Sorteia 5 números aleatórios e os adiciona à lista."""
    for _ in range(5):
        numeros.append(randint(1, 100))  # Sorteia números entre 1 e 100
    print(f"Números sorteados: {numeros}")


def somaPar(numeros):
    """Calcula a soma dos números pares na lista."""
    soma = sum(num for num in numeros if num % 2 == 0)
    print(f"Soma dos números pares: {soma}")


def main():
    numeros = []  # Lista para armazenar os números sorteados
    sorteia(numeros)  # Chama a função para sortear os números
    somaPar(numeros)  # Chama a função para calcular a soma dos pares
if __name__ == '__main__':
    main()  # Executa o programa principal
# Fim do programa