#Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável

def escreva(texto):
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)

def main():
    escreva('Olá, Mundo!')
    escreva('Python é uma linguagem de programação incrível!')
    escreva('Exercício 050 concluído!')

if __name__ == '__main__':
    main()

