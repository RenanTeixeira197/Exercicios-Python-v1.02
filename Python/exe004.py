def media_aritmetica(nota1, nota2, nota3, nota4):
    return (nota1 + nota2 + nota3 + nota4) / 4

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media_notas = media_aritmetica(n1, n2, n3, n4)

print("A média aritmética é: ", media_notas)