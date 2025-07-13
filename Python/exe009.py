from math import sqrt

def numero_ao_quadrado(numero):
    return numero * 2

def raiz_quadrada(numero):
    return sqrt(numero)

num1 = int(input("Digite um número: "))

resultadoRQ = raiz_quadrada(num1)
resultadoAQ = numero_ao_quadrado(num1)

print("Seu número elevado ao quadrado é: ", resultadoAQ, "e sua raiz quadrada é: ", resultadoRQ)