# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    return largura * comprimento

def main():
    print('Controle de Terrenos')
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento (m): '))
    a = area(largura, comprimento)
    print(f'A área do terreno {largura} x {comprimento} é de {a:.2f} m²')

if __name__ == '__main__':
    main()